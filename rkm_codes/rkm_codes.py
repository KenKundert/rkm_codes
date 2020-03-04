# RKM codes
# encoding: utf8

# description {{{1
"""
RKM codes are used to represent electrical quantities in labels, particularly on
schematics and on the components themselves.  They are standardized in various
national and international standards, including: IEC 60062 (1952) (formerly IEC 62),
DIN 40825 (1973), BS 1852 (1974), IS 8186 (1976) and EN 60062 (1993).
IEC-60062 was significantly updated in 2016.

RKM codes were originally meant also as part marking code.  This shorthand
notation is widely used in electrical engineering to denote the values of
resistors and capacitors in circuit diagrams and in the production of electronic
circuits (for example in bills of material and in silk screens). This method
avoids overlooking the decimal separator, which may not be rendered reliably on
components or when duplicating documents.  They also provide the benefit that
the characters within a RKM code are either letters or digits, and so can be
embedded within identifiers without introducing invalid characters.

IEC 60062 is described in https://en.wikipedia.org/wiki/RKM_code.

Essentially an RKM version of a number is the number with a scale factor where
the decimal point replaced by the scale factor. For example, a resistance of
4.7kΩ becomes 4k7. If there is no scale factor, the decimal point is replaced by
a letter that signifies the type of the component.  For example, a resistance of
4.7Ω becomes 4r7.

In the standard, large values are assumed to be resistances and small values are
assumed to be capacitances.  So 4k7 is a resistance and 2n5 is a capacitance.
However, this package also supports a version of RKM codes where the units are
not implied by the value, making RKM codes suitable for a wider variety of value
types, such as voltage, current, and inductance.
"""

# license {{{1
# Copyright (C) 2018-2020 Kenneth S. Kundert
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].


# imports {{{1
import re
from quantiphy import Quantity

# constants {{{1
# version {{{2
__version__ = '0.5.0'
__released__ = '2020-03-03'

# IEC60062 maps {{{2
IEC60062_MAPS = {
    # These maps conform to the latest recommended mappings as defined in the 
    # IEC-60062 standard. They apply assume only resistors and capacitors. Small 
    # values are associated with capacitors and large values with resistors. The 
    # units can be inferred by the scale factors and so it is unnecessary to 
    # specify the units with the number. For example, 4k7 is a resistance (k 
    # implies resistance) and 2p5 is a capacitance (p implies capacitance)
    #
    # These maps map a RKM code into a scale factor and the implied units (the 
    # implied units can be overwritten by explicitly specified units)

    # Resistors
    'r': ('', 'Ω'),
    'R': ('', 'Ω'),
    'Ω': ('', 'Ω'),
    'L': ('m', 'Ω'),
    'l': ('m', 'Ω'),
    'k': ('k', 'Ω'),
    'K': ('k', 'Ω'),
    'M': ('M', 'Ω'),
    'G': ('G', 'Ω'),
    'T': ('T', 'Ω'),

    # Capacitors
    'c': ('', 'F'),
    'C': ('', 'F'),
    'F': ('', 'F'),
    'm': ('m', 'F'),
    'm': ('m', 'F'),
    'u': ('µ', 'F'),
    'μ': ('µ', 'F'),
    'µ': ('µ', 'F'),
    'n': ('n', 'F'),
    'p': ('p', 'F'),
}

# unitless maps {{{2
UNITLESS_MAPS = {
    # These maps do not conform to the IEC-60062 standard, but can be applied to 
    # values other than resistance and capacitance. In this case, adding 
    # optional units is helpful because, while it would be possible to infer the 
    # units for some values (such as 4r7), it is not possible for most values 
    # (such as 4m7) and so implied units are not specified for any value.
    #
    # These maps map a RKM code into a scale factor and the implied units (the 
    # implied units can be overwritten by explicitly specified units)

    'r': ('', ''),  # resistors
    'R': ('', ''),
    'v': ('', 'V'),  # voltages
    'i': ('', ''),  # currents
    'I': ('', ''),
    'c': ('', ''),  # capacitors
    'f': ('', ''),
    'l': ('', ''),  # inductors
    'h': ('', ''),
}

# map units to rkm base code {{{2
# Controls the base code produced by to_rkm().
UNITS_TO_RKM_BASE_CODE = {
    'Ω': 'r',
    'Ohm': 'r',
    'F': 'c',
    'H': 'l',
    'V': 'v',
    'A': 'i',
}

# map scale factors {{{2
# Controls the scale factors produced by to_rkm().
#MAP_SF = dict(u='μ', k='K')  # this is mu
MAP_SF = dict(u='µ', k='K')  # this is micro

# others {{{2
MINUS_SIGN = 'n'
SHOW_UNITS = False
STRIP_ZEROS = True
STRIP_CODE = True
PREC = 1

# utilities {{{1
# cull {{{2
def cull(collection):
    return (v for v in collection if v)

# set_prefs {{{1
_rkm_maps = UNITLESS_MAPS
_units_to_rkm_base_code = UNITS_TO_RKM_BASE_CODE
_map_sf = MAP_SF
_minus_sign = MINUS_SIGN
_show_units = SHOW_UNITS
_prec = PREC
_strip_zeros = STRIP_ZEROS
_strip_code = STRIP_CODE

def set_prefs(
    rkm_maps=False, units_to_rkm_base_code=False, map_sf=False,
    show_units='', strip_zeros='', strip_code='', minus_sign=False, prec=False
):
    '''Set Preferences

    Use to set values that control the behavior of the RKM code.
    Any values not passed in a left alone.
    Pass in *None* to reset a preference to its default value.

    Args:
        rkm_maps (dictionary of tuples):
            A dictionary that maps a base code or scale factor into a scale
            factor and units. Used to affect the behavior or *from_rkm()*.
            Generally set to rkm_codes.IEC60062_MAPS, which encourages
            conformance to the standard, or to rkm_codes.UNITLESSs_MAPS, which
            supports a wider range of quantities than resistances and
            capacitances. You can also pass in a custom mapping to get a
            particular result.

        units_to_rkm_base_code (dictionary of strings):
            A dictionary that maps a units to a base code. Used to affect the
            behavior of *to_rkm()*.

        map_sf (dictionary of strings):
            A dictionary that maps the scale factors used by QuantiPhy to the
            ones found in a RKM code. Used to affect the
            behavior of *to_rkm()*.
        show_units (bool):
            Whether the units should be included in the RKM code.
        strip_zeros (bool):
            Whether the units should be included in the RKM code.
        strip_code (bool):
            Whether the base code should be removed from the end of the RKM code
            (eg: 470 → 470 if true and 470r otherwise).
        minus_sign (str):
            Character to use to indicate a negative value. The default is 'n',
            but 'm' is also common.
        prec (int):
            Precision. Number of digits shown in 1 plus this number.
    '''
    global _rkm_maps, _units_to_rkm_base_code, _map_sf
    global _show_units, _strip_zeros, _strip_code, _minus_sign, _prec

    if rkm_maps is None:
        _rkm_maps = UNITLESS_MAPS
    elif rkm_maps is not False:
        _rkm_maps = rkm_maps

    if units_to_rkm_base_code is None:
        _units_to_rkm_base_code = UNITS_TO_RKM_BASE_CODE
    elif units_to_rkm_base_code is not False:
        _units_to_rkm_base_code = units_to_rkm_base_code

    if map_sf is None:
        _map_sf = MAP_SF
    elif map_sf is not False:
        _map_sf = map_sf

    if show_units is None:
        _show_units = SHOW_UNITS
    elif show_units != '':
        _show_units = show_units

    if strip_zeros is None:
        _strip_zeros = STRIP_ZEROS
    elif strip_zeros != '':
        _strip_zeros = strip_zeros

    if strip_code is None:
        _strip_code = STRIP_ZEROS
    elif strip_code != '':
        _strip_code = strip_code

    if minus_sign is None:
        _minus_sign = MINUS_SIGN
    elif minus_sign is not False:
        _minus_sign = minus_sign

    if prec is None:
        _prec = PREC
    elif prec is not False:
        _prec = prec

# RKM code patterns {{{1
# regex1 matches rkm codes that start with a digit.
# regex2 matches rkm codes that end with a digit.
ld_regex = r'([pmn]?)([0-9]+)([a-zµμΩ℧]+)([0-9]*)'
td_regex = r'([pmn]?)([0-9]*)([a-zµμΩ℧]+)([0-9]+)'
combined_regex = '(?:{})|(?:{})'.format(ld_regex, td_regex)
ld_matcher = re.compile(ld_regex, re.I)
td_matcher = re.compile(td_regex, re.I)
combined_matcher = re.compile(combined_regex, re.I)

# from_rkm {{{1
def from_rkm(code):
    '''From RKM

    Convert a RKM code string to a quantiphy.Quantity.

    Args:
        code (str):
            An RKM code that may include explicitly specified. Examples of
            acceptable RKM codes for resistance include:   R47 (0.47 Ω), 4R7
            (4.7 Ω), 470R (470 Ω), 4K7 (4.7 kΩ), 47K (47 kΩ), 47K3 (47.3 kΩ),
            470K (470 kΩ), and 4M7 (4.7 MΩ).  Units may be added by appending
            the units to the scale factor, as in 47KΩ3 (47.3 kΩ).
    Returns:
        A quantiphy.Quantity if a valid RKM code was found, otherwise *None* is
        returned.
    '''
    for matcher in [ld_matcher, td_matcher]:
        match = matcher.match(code)
        if match:
            sign, ld, base, td = match.groups()
            sf, units = _rkm_maps.get(base, (base, ''))
            if sign and sign in 'mn':
                sign = '-'
            else:
                sign = ''
            return Quantity(''.join(cull([sign, ld,  '.',  td,  sf, units])))

# to_rkm {{{1
def to_rkm(q, prec=None, show_units=None, strip_zeros=None, strip_code=None):
    '''To RKM

    Convert a quantiphy.Quantity to an RKM string.

    Args:
        q (quantiphy.Quantity, str, or float):
            The value to be converted to an RKM code.
        prec (int):
            The precision. The number of digits is the precision + 1.
        show_units (bool):
            Whether and where the units should be included in the RKM code
            (default is False).
        strip_zeros (bool):
            Whether excess zeros should be removed (default is True).
        strip_code (bool):
            Whether the base code should be removed from the end of the RKM code
            (eg: 470 → 470 if true and 470r otherwise).
    Returns:
        A quantiphy.Quantity if a valid RKM code was found, otherwise *None* is
        returned.
    '''
    if show_units is None:
        show_units = _show_units
    if strip_zeros is None:
        strip_zeros = _strip_zeros
    if strip_code is None:
        strip_code = _strip_code
    if prec is None:
        prec = _prec
    try:
        units = q.units
    except AttributeError:
        q = Quantity(q)
        units = q.units
    rkm_base_code = _units_to_rkm_base_code.get(units, units)
    if not rkm_base_code:
        rkm_base_code = 'd'
    if not show_units:
        units = ''

    with q.prefs(
        map_sf={},
        show_units=False,
        strip_zeros=False,
        strip_radix=False,
        prec=prec
    ):
        value = q.render(form='si')
        if 'e-' in value:
            value = q.render(form='fixed')
    is_negative = value.startswith('-')
    if is_negative:
        value = value[1:]

    sf = value[-1]
    if sf and sf in q.output_sf:
        value = value[:-1]
    elif units:
        sf = ''
    else:
        sf = rkm_base_code
    if '.' not in value:
        value += '.'
    if strip_zeros:
        value = value.rstrip('0')
    if value.startswith('0.') and value[-1] != '.':
        value = value[1:]
    if not sf:
        if units:
            sf = units
            units = ''
        else:
            sf = rkm_base_code
    if strip_code and sf == rkm_base_code:
        value = value.rstrip('.')
    if is_negative:
        value = '-' + value
    value = value.replace('-', _minus_sign)
    return value.replace('.', _map_sf.get(sf, sf)+units)

# find_rkm {{{1
def find_rkm(text, kind=None):
    '''Find RKM codes

    Iterate through RKM codes found in a text string.

    Args:
        text (str):
            The text string that is to be searched for RKM codes.
        kind (str):
            Specify:
                'ld': match only RKMs with leading digits
                'td': match only RKMs with trailing digits
                anything else: match either type of RKMs
    Yields:
        Succession of quantities.
    '''
    if kind == 'ld':
        matcher = ld_matcher
    elif kind == 'td':
        matcher = td_matcher
    else:
        matcher = combined_matcher

    for match in matcher.finditer(text):
        yield from_rkm(match.expand(r'\g<0>'))
