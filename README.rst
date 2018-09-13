.. initialize RKM codes

    >>> from rkm_codes import set_prefs
    >>> set_prefs(rkm_maps=None, units_to_rkm_base_code=None, map_sf=None)

RKM codes
=========

| Version: 0.1.0
| Released: 2018-09-12
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

Install with::

    pip3 install --user rkm_codes

Requires Python3.4 or better.

The following is a simple example of how to convert back and forth between RKM 
codes and Quantities::

    >>> from rkm_codes import from_rkm, to_rkm
    >>> r = from_rkm('6K8')
    >>> r
    Quantity('6.8k')

    >>> to_rkm(r)
    '6K8'

You Note that in this case the quantity does not include units. That is because 
by default *rkm_codes* assumes unitless numbers. You can change this behavior. 
Out of the box *rkm_codes* supports two kinds of numbers, unitless and those 
that follow the IEC60062 standard. You can switch between those two kinds of 
numbers using something like this::

    >>> from rkm_codes import set_prefs, IEC60062_MAPS, UNITLESS_MAPS
    >>> r = from_rkm('6k8')
    >>> r
    Quantity('6.8k')

    >>> set_prefs(rkm_maps=IEC60062_MAPS)
    >>> from_rkm('6k8')
    Quantity('6.8 kΩ')

    >>> set_prefs(rkm_maps=UNITLESS_MAPS)
    >>> from_rkm('6k8')
    Quantity('6.8k')

In either case, *rkm_codes* allows you to explicitly specify the units, which 
always overrides any implied units::

    >>> set_prefs(rkm_maps=UNITLESS_MAPS)
    >>> from_rkm('6k8Ω')
    Quantity('6.8 kΩ')

    >>> i = from_rkm('2u5A')
    >>> i
    Quantity('2.5 uA')

When converting to an RKM code, you can instruct that the units be included::

    >>> to_rkm(i, show_units=True)
    '2μ5A'

You can also indicate how many digits should be included::

    >>> to_rkm(i.add(1e-9), prec=5, show_units=True)
    '2μ501A'

Normally, any excess zeros are removed, but you can change that too::

    >>> to_rkm(i.add(1e-9), prec=5, show_units=True, strip_zeros=False)
    '2μ50100A'

You can create your own maps by passing in a dictionary that maps a RKM base 
code character into a scale factor and units. For example, you could create 
a map that uses 'd' or 'D' to represent the decimal point in numbers without 
scale factors rather than 'r', 'c', etc.  For example::

    >>> set_prefs(rkm_maps=dict(d=('', ''), D=('', '')))
    >>> from_rkm('6d8Ω')
    Quantity('6.8 Ω')

    >>> from_rkm('2d5V')
    Quantity('2.5 V')

Passing *None* for the value of a map returns it to its default value.

If *rkm_codes* encounters a RKM base code character that is not in the map, it 
simply uses that character. In this way, scale factors are handled::

    >>> from_rkm('6k8Ω')
    Quantity('6.8 kΩ')

When converting from Quantities to RKM codes, you can override the default 
mappings from units to RKM base code characters. The default mapping maps 'Ω' 
and 'Ohm' to 'r', 'F' to 'c', 'H' to 'l', 'V' to 'v', and 'A' to 'i'.  However, 
you may prefer uppercase base characters, which is more in alignment with the 
original standard. To get that, you can use something like this::

    >>> rkm_base_code_mappings = {
    ...     'Ω': 'R',
    ...     'Ohm': 'R',
    ...     'F': 'C',
    ...     'H': 'L',
    ...     'V': 'V',
    ...     'A': 'I',
    ... }
    >>> set_prefs(rkm_maps=IEC60062_MAPS, units_to_rkm_base_code=rkm_base_code_mappings)
    >>> r = from_rkm('k0012')
    >>> to_rkm(r)
    '1R2'

You can control the scale factors used by to_rkm() by setting *map_sf* using 
*set_prefs*. The default maps 'u' to 'μ' and 'k' to 'K'. You might wish to 
prevent the use of 'μ' while retaining the use of 'K', which you can do with:

    >>> set_prefs(map_sf=dict(k='K'))
    >>> c = from_rkm('5u')
    >>> to_rkm(c)
    '5u'




