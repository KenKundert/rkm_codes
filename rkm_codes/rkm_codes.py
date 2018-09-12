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

# globals {{{1
# version {{{2
__version__ = '0.0.1'
__released__ = '11 September 2018'

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

# units to rkm base code {{{2
UNITS_TO_RKM_BASE_CODE = {
    'Ω': 'r',
    'Ohm': 'r',
    'F': 'c',
    'H': 'l',
    'V': 'v',
    'A': 'a',
}

# utilities {{{1
# cull {{{2
def cull(collection):
    return (v for v in collection if v)

# set_maps {{{1
RKM_MAPS = UNITLESS_MAPS
def set_maps(maps):
    global RKM_MAPS
    RKM_MAPS = maps

# read_rkm_code {{{1
# RKM code patterns
# regex1 matches rkm codes that start with a digit.
# regex2 matches rkm codes that end with a digit.
# Both allow optional trailing units that consist only of letters selected 
# symbols (no digits).
regex1 = re.compile(r'([0-9]+)([a-z]+)(?:([0-9]+)([a-zΩ℧]*))?', re.I)
regex2 = re.compile(r'([0-9]*)([a-z]+)([0-9]+)([a-zΩ℧]*)', re.I)

def read_rkm_code(code):
    for regex in [regex1, regex2]:
        match = regex.match(code)
        if match:
            ld, base, td, units = match.groups()
            sf, implied_units = RKM_MAPS.get(base, (base, ''))
            units = units if units else implied_units
            return Quantity(''.join(cull([ld,  '.',  td,  sf, units])))

# write_rkm_code {{{1
def write_rkm_code(q, prec=1, show_units=False):
    value = q.render(
        form='si', show_units=False, strip_zeros=False, strip_radix=False, 
        prec=prec
    )
    sf = value[-1]
    if sf in q.output_sf:
        value = value[:-1]
    else:
        sf = UNITS_TO_RKM_BASE_CODE.get(q.units, q.units)
    if '.' not in value:
        value += '.'
    return value.replace('.', sf) + (q.units if show_units else '')
