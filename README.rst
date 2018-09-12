RKM codes
=========

| Version: 0.0.1
| Released: 2018-09-11
|

.. image:: https://img.shields.io/travis/KenKundert/rkm_codes/master.svg
    :target: https://travis-ci.org/KenKundert/rkm_codes

.. image:: https://img.shields.io/coveralls/KenKundert/rkm_codes.svg
    :target: https://coveralls.io/r/KenKundert/rkm_codes

.. image:: https://img.shields.io/pypi/v/rkm_codes.svg
    :target: https://pypi.python.org/pypi/rkm_codes

.. image:: https://img.shields.io/pypi/pyversions/rkm_codes.svg
    :target: https://pypi.python.org/pypi/rkm_codes/

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

Resistance examples:

    | R47 → 0.47 Ω
    | 4R7 → 4.7 Ω
    | 470R → 470 Ω
    | 4K7 → 4.7 kΩ
    | 47K → 47 kΩ
    | 47K3 → 47.3 kΩ
    | 470K → 470 kΩ
    | 4M7 → 4.7 MΩ

In the standard, large values are assumed to be resistances and small values are
assumed to be capacitances.  So 4k7 is a resistance and 2n5 is a capacitance.
However, this package also supports a version of RKM codes where the units are
not implied by the value, making RKM codes suitable for a wider variety of value
types, such as voltage, current, and inductance.

This package is used to convert RKM codes to `QuantiPhy Quantities 
<https://quantiphy.readthedocs.io>`_ and Quantities to RKM codes.

For example::

    >>> from rkm_codes import read_rkm_code, write_rkm_code
    >>> r = read_rkm_code('6k8')
    >>> r
    Quantity('6.8k')

    >>> write_rkm_code(r)
    '6k8'

Note that in this case the quantity does not include units. That is because by 
default *rkm_codes* assumes unitless numbers. You can change this behavior. Out 
of the box *rkm_codes* supports two kinds of numbers, unitless and those that 
follow the IEC60062 standard. You can switch between those two kinds of numbers 
using something like this::

    >>> from rkm_codes import set_maps, IEC60062_MAPS, UNITLESS_MAPS
    >>> r = read_rkm_code('6k8')
    >>> r
    Quantity('6.8k')

    >>> set_maps(IEC60062_MAPS)
    >>> read_rkm_code('6k8')
    Quantity('6.8 kΩ')

    >>> set_maps(UNITLESS_MAPS)
    >>> read_rkm_code('6k8')
    Quantity('6.8k')

In either case, *rkm_codes* allows you to explicitly specify the units, which 
always overrides any implied units::

    >>> set_maps(UNITLESS_MAPS)
    >>> read_rkm_code('6k8Ω')
    Quantity('6.8 kΩ')

    >>> read_rkm_code('2u5A')
    Quantity('2.5 uA')

You can create your own maps by passing in a dictionary that maps a RKM code 
character into a scale factor and units. For example, you could create a map 
that uses 'd' or 'D' to represent the decimal point in numbers without scale 
factors rather than 'r', 'c', etc.  For example::

    >>> set_maps({'d': (''. ''), 'D': (''. '')})
    >>> read_rkm_code('6d8Ω')
    Quantity('6.8 Ω')

    >>> read_rkm_code('2d5V')
    Quantity('2.5 V')

If *rkm_codes* encounters a RKM code character that is not in the map, it simply 
uses that character. In this way, scale factors are handled::

    >>> read_rkm_code('6k8Ω')
    Quantity('6.8 kΩ')
