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
# Copyright (C) 2018 Kenneth S. Kundert
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
__version__ = '0.0.2'
__released__ = '2018-09-12'

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
    'u': ('μ', 'F'),
    'μ': ('μ', 'F'),
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
    'Ω': ('', ''),
    'v': ('', ''),  # voltages
    'V': ('', ''),
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
MAP_SF = dict(u='μ', k='K')

# utilities {{{1
# cull {{{2
def cull(collection):
    return (v for v in collection if v)

# set_prefs {{{1
_rkm_maps = UNITLESS_MAPS
_units_to_rkm_base_code = UNITS_TO_RKM_BASE_CODE
_map_sf = MAP_SF
def set_prefs(rkm_maps=False, units_to_rkm_base_code=False, map_sf=False):
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
    '''
    global _rkm_maps, _units_to_rkm_base_code, _map_sf
    if rkm_maps:
        _rkm_maps = rkm_maps
    elif rkm_maps is None:
        _rkm_maps = UNITLESS_MAPS

    if units_to_rkm_base_code:
        _units_to_rkm_base_code = units_to_rkm_base_code
    elif units_to_rkm_base_code is None:
        _units_to_rkm_base_code = UNITS_TO_RKM_BASE_CODE

    if map_sf:
        _map_sf = map_sf
    elif map_sf is None:
        _map_sf = MAP_SF

# from_rkm {{{1
# RKM code patterns
# regex1 matches rkm codes that start with a digit.
# regex2 matches rkm codes that end with a digit.
# Both allow optional trailing units that consist only of letters selected 
# symbols (no digits).
regex1 = re.compile(r'([0-9]+)([a-z]+)(?:([0-9]+)([a-zΩ℧]*))?', re.I)
regex2 = re.compile(r'([0-9]*)([a-z]+)([0-9]+)([a-zΩ℧]*)', re.I)

def from_rkm(code):
    '''From RKM

    Convert a RKM code string to a quantiphy.Quantity.

    Args:
        code (str of tuples):
            An RKM code that may include explicitly specified. Examples of
            acceptable RKM codes for resistance include:   R47 (0.47 Ω), 4R7
            (4.7 Ω), 470R (470 Ω), 4K7 (4.7 kΩ), 47K (47 kΩ), 47K3 (47.3 kΩ),
            470K (470 kΩ), and 4M7 (4.7 MΩ).  Units may be added by appending
            the units to the end: 47K3Ω ((47.3 kΩ).
    Returns:
        A quantiphy.Quantity if a valid RKM code was found, otherwise *None* is
        returned.
    '''
    for regex in [regex1, regex2]:
        match = regex.match(code)
        if match:
            ld, base, td, units = match.groups()
            sf, implied_units = _rkm_maps.get(base, (base, ''))
            units = units if units else implied_units
            return Quantity(''.join(cull([ld,  '.',  td,  sf, units])))

# to_rkm {{{1
def to_rkm(q, prec=1, show_units=False, strip_zeros=True):
    '''To RKM

    Convert a quantiphy.Quantity to an RKM string.

    Args:
        q (quantiphy.Quantity):
            The value to be converted to an RKM code.
        prec (int):
            The precision. The number of digits is the precision + 1 (default is
            1).
        show_units (bool):
            Whether the units should be appended to the RKM code (default is
            False).
        strip_zeros (bool):
            Whether excess zeros should be removed (default is True).
    Returns:
        A quantiphy.Quantity if a valid RKM code was found, otherwise *None* is
        returned.
    '''
    value = q.render(
        form='si', show_units=False, strip_zeros=False, strip_radix=False, 
        prec=prec
    )
    sf = SF = value[-1]
    if sf in q.output_sf:
        value = value[:-1]
    else:
        sf = _units_to_rkm_base_code.get(q.units, q.units)
    if '.' not in value:
        value += '.'
    if strip_zeros:
        value = value.rstrip('0')
    units = q.units if show_units else ''
    if not sf and value[-1] != '.':
        sf = units if units else 'd'
        units = ''
    if SF != sf:
        value = value.rstrip('.')
    return value.replace('.', _map_sf.get(sf, sf)) + units
