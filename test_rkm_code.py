# encoding: utf8

from rkm_codes import (
    set_prefs, from_rkm, to_rkm, find_rkm, IEC60062_MAPS, UNITLESS_MAPS
)
from quantiphy import Quantity

testcases = [
    dict(maps=UNITLESS_MAPS, name='dampen', icode='R47', q='470m', ocode='470m', ocodeu='470m'),
    dict(maps=UNITLESS_MAPS, name='monopoly', icode='Ω47', q='470 mΩ', ocode='470m', ocodeu='470mΩ'),
    dict(maps=UNITLESS_MAPS, name='tappet', icode='4R7', q='4.7', ocode='4d7', ocodeu='4d7'),
    dict(maps=UNITLESS_MAPS, name='requite', icode='4Ω7', q='4.7 Ω', ocode='4r7', ocodeu='4Ω7'),
    dict(maps=UNITLESS_MAPS, name='revamp', icode='470R', q='470', ocode='470d', ocodeu='470d'),
    dict(maps=UNITLESS_MAPS, name='caterer', icode='470Ω', q='470 Ω', ocode='470r', ocodeu='470Ω'),
    dict(maps=UNITLESS_MAPS, name='strap', icode='4K7', q='4.7k', ocode='4K7', ocodeu='4K7'),
    dict(maps=UNITLESS_MAPS, name='front', icode='4KΩ7', q='4.7 kΩ', ocode='4K7', ocodeu='4KΩ7'),
    dict(maps=UNITLESS_MAPS, name='ensue', icode='47K', q='47k', ocode='47K', ocodeu='47K'),
    dict(maps=UNITLESS_MAPS, name='spooky', icode='47K3', q='47.3k', ocode='47K', ocodeu='47K'),
    dict(maps=UNITLESS_MAPS, name='surface', icode='470K', q='470k', ocode='470K', ocodeu='470K'),
    dict(maps=UNITLESS_MAPS, name='remover', icode='4M7', q='4.7M', ocode='4M7', ocodeu='4M7'),
    dict(maps=UNITLESS_MAPS, name='borrowing', icode='150nA', q='150 nA', ocode='150n', ocodeu='150nA'),
    dict(maps=UNITLESS_MAPS, name='loofah', icode='2v5', q='2.5 V', ocode='2v5', ocodeu='2V5'),
    dict(maps=UNITLESS_MAPS, name='scree', icode='2nA5A', q='2.5 nA', ocode='2n5', ocodeu='2nA5'),
    dict(maps=UNITLESS_MAPS, name='socialite', icode='f220', q='220m', ocode='220m', ocodeu='220m'),
    dict(maps=UNITLESS_MAPS, name='rehearsal', icode='2c', q='2', ocode='2d', ocodeu='2d'),
    dict(maps=UNITLESS_MAPS, name='kilogram', icode='2c5', q='2.5', ocode='2d5', ocodeu='2d5'),
    dict(maps=UNITLESS_MAPS, name='misinform', icode='2f', q='2', ocode='2d', ocodeu='2d'),
    dict(maps=UNITLESS_MAPS, name='whetstone', icode='2f5', q='2.5', ocode='2d5', ocodeu='2d5'),
    dict(maps=UNITLESS_MAPS, name='funny', icode='2pF5', q='2.5 pF', ocode='2p5', ocodeu='2pF5'),
    dict(maps=UNITLESS_MAPS, name='shallot', icode='h220', q='220m', ocode='220m', ocodeu='220m'),
    dict(maps=UNITLESS_MAPS, name='sniper', icode='2l', q='2', ocode='2d', ocodeu='2d'),
    dict(maps=UNITLESS_MAPS, name='pajama', icode='2l5', q='2.5', ocode='2d5', ocodeu='2d5'),
    dict(maps=UNITLESS_MAPS, name='prose', icode='2pH5', q='2.5 pH', ocode='2p5', ocodeu='2pH5'),
    dict(maps=UNITLESS_MAPS, name='gaffe', icode='p2pH5', q='2.5 pH', ocode='2p5', ocodeu='2pH5'),
    dict(maps=UNITLESS_MAPS, name='object', icode='n2pH5', q='-2.5 pH', ocode='n2p5', ocodeu='n2pH5'),
    dict(maps=UNITLESS_MAPS, name='shuffle', icode='m2pH5', q='-2.5 pH', ocode='n2p5', ocodeu='n2pH5'),

    dict(maps=IEC60062_MAPS, name='tilde', icode='R47', q='470 mΩ', ocode='470m', ocodeu='470mΩ'),
    dict(maps=IEC60062_MAPS, name='circlet', icode='R47', q='470 mΩ', ocode='470m', ocodeu='470mΩ'),
    dict(maps=IEC60062_MAPS, name='polygon', icode='4R7', q='4.7 Ω', ocode='4r7', ocodeu='4Ω7'),
    dict(maps=IEC60062_MAPS, name='hacksaw', icode='470R', q='470 Ω', ocode='470r', ocodeu='470Ω'),
    dict(maps=IEC60062_MAPS, name='spurt', icode='4K7', q='4.7 kΩ', ocode='4K7', ocodeu='4KΩ7'),
    dict(maps=IEC60062_MAPS, name='corkscrew', icode='4K7Ω', q='4.7 kΩ', ocode='4K7', ocodeu='4KΩ7'),
    dict(maps=IEC60062_MAPS, name='cemetery', icode='47K', q='47 kΩ', ocode='47K', ocodeu='47KΩ'),
    dict(maps=IEC60062_MAPS, name='quintet', icode='47K3', q='47.3 kΩ', ocode='47K', ocodeu='47KΩ'),
    dict(maps=IEC60062_MAPS, name='farthing', icode='470K', q='470 kΩ', ocode='470K', ocodeu='470KΩ'),
    dict(maps=IEC60062_MAPS, name='rudder', icode='4M7', q='4.7 MΩ', ocode='4M7', ocodeu='4MΩ7'),
    dict(maps=IEC60062_MAPS, name='clinch', icode='150nA', q='150 nA', ocode='150n', ocodeu='150nA'),
    dict(maps=IEC60062_MAPS, name='pioneer', icode='2v5', q='2.5 v', ocode='2v5', ocodeu='2v5'),
    dict(maps=IEC60062_MAPS, name='pretense', icode='2nA5', q='2.5 nA', ocode='2n5', ocodeu='2nA5'),
    dict(maps=IEC60062_MAPS, name='caress', icode='f220', q='220a', ocode='220a', ocodeu='220a'),
    dict(maps=IEC60062_MAPS, name='tassel', icode='2c', q='2 F', ocode='2c', ocodeu='2F'),
    dict(maps=IEC60062_MAPS, name='hundred', icode='2c5', q='2.5 F', ocode='2c5', ocodeu='2F5'),
    dict(maps=IEC60062_MAPS, name='speckle', icode='2f', q='2f', ocode='2f', ocodeu='2f'),
    dict(maps=IEC60062_MAPS, name='pachyderm', icode='2f5', q='2.5f', ocode='2f5', ocodeu='2f5'),
    dict(maps=IEC60062_MAPS, name='tight', icode='2pF5', q='2.5 pF', ocode='2p5', ocodeu='2pF5'),
    dict(maps=IEC60062_MAPS, name='entree', icode='h220', q='220 mh', ocode='220m', ocodeu='220mh'),
    dict(maps=IEC60062_MAPS, name='mannerism', icode='2l', q='2 mΩ', ocode='2m', ocodeu='2mΩ'),
    dict(maps=IEC60062_MAPS, name='story', icode='2l5', q='2.5 mΩ', ocode='2m5', ocodeu='2mΩ5'),
    dict(maps=IEC60062_MAPS, name='vexation', icode='2pH5', q='2.5 pH', ocode='2p5', ocodeu='2pH5'),

    dict(maps=IEC60062_MAPS, name='grandpa', icode='l047', q='47 uΩ', ocode='47μ', ocodeu='47μΩ'),  # using invalid sf
    dict(maps=IEC60062_MAPS, name='stock', icode='l47', q='470 uΩ', ocode='470μ', ocodeu='470μΩ'), # using invalid sf
    dict(maps=IEC60062_MAPS, name='speedwell', icode='4l7', q='4.7 mΩ', ocode='4m7', ocodeu='4mΩ7'),
    dict(maps=IEC60062_MAPS, name='instinct', icode='47l', q='47 mΩ', ocode='47m', ocodeu='47mΩ'),
    dict(maps=IEC60062_MAPS, name='discord', icode='470l', q='470 mΩ', ocode='470m', ocodeu='470mΩ'),
    dict(maps=IEC60062_MAPS, name='eunuch', icode='r47', q='470 mΩ', ocode='470m', ocodeu='470mΩ'),
    dict(maps=IEC60062_MAPS, name='jewel', icode='4r7', q='4.7 Ω', ocode='4r7', ocodeu='4Ω7'),
    dict(maps=IEC60062_MAPS, name='mudguard', icode='47r', q='47 Ω', ocode='47r', ocodeu='47Ω'),
    dict(maps=IEC60062_MAPS, name='kebab', icode='470r', q='470 Ω', ocode='470r', ocodeu='470Ω'),
    dict(maps=IEC60062_MAPS, name='chomp', icode='k47', q='470 Ω', ocode='470r', ocodeu='470Ω'),
    dict(maps=IEC60062_MAPS, name='gambol', icode='K47', q='470 Ω', ocode='470r', ocodeu='470Ω'),
    dict(maps=IEC60062_MAPS, name='interject', icode='4k7', q='4.7 kΩ', ocode='4K7', ocodeu='4KΩ7'),
    dict(maps=IEC60062_MAPS, name='thank', icode='4K7', q='4.7 kΩ', ocode='4K7', ocodeu='4KΩ7'),
    dict(maps=IEC60062_MAPS, name='edify', icode='47k', q='47 kΩ', ocode='47K', ocodeu='47KΩ'),
    dict(maps=IEC60062_MAPS, name='assistant', icode='47K', q='47 kΩ', ocode='47K', ocodeu='47KΩ'),
    dict(maps=IEC60062_MAPS, name='voter', icode='470k', q='470 kΩ', ocode='470K', ocodeu='470KΩ'),
    dict(maps=IEC60062_MAPS, name='brief', icode='470K', q='470 kΩ', ocode='470K', ocodeu='470KΩ'),
    dict(maps=IEC60062_MAPS, name='gaiter', icode='M470', q='470 kΩ', ocode='470K', ocodeu='470KΩ'),
    dict(maps=IEC60062_MAPS, name='plank', icode='4M70', q='4.7 MΩ', ocode='4M7', ocodeu='4MΩ7'),
    dict(maps=IEC60062_MAPS, name='statesman', icode='47M', q='47 MΩ', ocode='47M', ocodeu='47MΩ'),
    dict(maps=IEC60062_MAPS, name='suffuse', icode='470M', q='470 MΩ', ocode='470M', ocodeu='470MΩ'),
    dict(maps=IEC60062_MAPS, name='trait', icode='G470', q='470 MΩ', ocode='470M', ocodeu='470MΩ'),
    dict(maps=IEC60062_MAPS, name='daiquiri', icode='4G7', q='4.7 GΩ', ocode='4G7', ocodeu='4GΩ7'),
    dict(maps=IEC60062_MAPS, name='reunion', icode='47G', q='47 GΩ', ocode='47G', ocodeu='47GΩ'),
    dict(maps=IEC60062_MAPS, name='diatribe', icode='470G', q='470 GΩ', ocode='470G', ocodeu='470GΩ'),
    dict(maps=IEC60062_MAPS, name='emerge', icode='4700G', q='4.7 TΩ', ocode='4T7', ocodeu='4TΩ7'),  # uses invalid sf
    dict(maps=IEC60062_MAPS, name='guardsman', icode='4MHz70', q='4.7 MHz', ocode='4M7', ocodeu='4MHz7'),
]
more_testcases = '''
    470e-9Ω    0           0R          0Ω          R0000
    4.7e-6Ω    0           0R          0Ω          R0000
    47e-6Ω     0           0R          0Ω          R0000
    470e-6Ω    R0005       R0005       Ω0005       R0005
    4.7e-3Ω    R0047       R0047       Ω0047       R0047
    47e-3Ω     R047        R047        Ω047        R0470
    470e-3Ω    R47         R47         Ω47         R4700
    4.7Ω       4R7         4R7         4Ω7         4R7000
    47Ω        47          47R         47Ω         47R000
    470Ω       470         470R        470Ω        470R00
    4.7kΩ      4K7         4K7         4KΩ7        4K7000
    47kΩ       47K         47K         47KΩ        47K000
    470kΩ      470K        470K        470KΩ       470K00
'''


def test_rkm_codes():
    # set maps to their default behavior
    set_prefs(
        rkm_maps=None, units_to_rkm_base_code=None, map_sf=None,
        show_units=None, strip_zeros=None, minus_sign=None, prec=None,
        strip_code=False
    )

    # run tests
    known_cases = set()
    for case in testcases:
        assert case['name'] not in known_cases, 'duplicate case {}'.format(case['name'])
        known_cases.add(case['name'])

        set_prefs(case['maps'])
        maps = 'unitless' if case['maps'] == UNITLESS_MAPS else 'IEC60062'
        q = from_rkm(case['icode'])
        print(
            maps,
            case['icode'],
            q,
            to_rkm(q),
            to_rkm(q, show_units=True),
            sep=', '
        )
        assert str(q) == case['q'], case['name']
        assert to_rkm(q) == case['ocode'], case['name']
        assert to_rkm(q, show_units=True) == case['ocodeu'], case['name']

    # return maps to their default behavior
    set_prefs(rkm_maps=None, units_to_rkm_base_code=None, map_sf=None)


def test_misc():
    # set maps to their default behavior
    set_prefs(
        rkm_maps=None, units_to_rkm_base_code=None, map_sf=None,
        show_units=None, strip_zeros=None, minus_sign=None, prec=None,
        strip_code=True
    )

    c = Quantity(2)
    assert to_rkm(c) == '2'
    assert to_rkm(c, strip_zeros=False) == '2d0'
    assert to_rkm(c, strip_zeros=False, prec=5) == '2d00000'

    c = Quantity(20)
    assert to_rkm(c) == '20'
    assert to_rkm(c, strip_zeros=False) == '20'
    assert to_rkm(c, strip_zeros=False, prec=5) == '20d0000'

    c = 20
    assert to_rkm(c) == '20'
    assert to_rkm(c, strip_zeros=False) == '20'
    assert to_rkm(c, strip_zeros=False, prec=5) == '20d0000'

    c = 20.0
    assert to_rkm(c) == '20'
    assert to_rkm(c, strip_zeros=False) == '20'
    assert to_rkm(c, strip_zeros=False, prec=5) == '20d0000'

    c = Quantity(2, units='Ω')
    assert to_rkm(c) == '2'
    assert to_rkm(c, strip_zeros=False) == '2r0'
    assert to_rkm(c, strip_zeros=False, prec=5) == '2r00000'

    c = Quantity(20, units='Ω')
    assert to_rkm(c) == '20'
    assert to_rkm(c, strip_zeros=False) == '20'
    assert to_rkm(c, strip_zeros=False, prec=5) == '20r0000'

    c = '20Ω'
    assert to_rkm(c) == '20'
    assert to_rkm(c, strip_zeros=False) == '20'
    assert to_rkm(c, strip_zeros=False, prec=5) == '20r0000'

    found = ', '.join(str(e) for e in find_rkm('sink200nA', 'ld'))
    assert found == '200 nA'

    found = ', '.join(str(e) for e in find_rkm('sink200nA', 'td'))
    assert found == '200 msink'

    found = ', '.join(str(e) for e in find_rkm('ib_n2nA5_vco', 'ld'))
    assert found == '-2.5 nA'

    found = ', '.join(str(e) for e in find_rkm('''
        An RKM code that may include explicitly specified. Examples of
        acceptable RKM codes for resistance include:   R47 (0.47 Ω), 4R7
        (4.7 Ω), 470R (470 Ω), 4K7 (4.7 kΩ), 47K (47 kΩ), 47K3 (47.3 kΩ),
        470K (470 kΩ), and 4M7 (4.7 MΩ).  Units may be added by appending
        the units to the scale factor: 47KΩ3 (47.3 kΩ).
    '''))
    assert found == '470m, 4.7, 470, 4.7k, 47k, 47.3k, 470k, 4.7M, 47.3 kΩ'

    # return maps to their default behavior
    set_prefs(rkm_maps=None, units_to_rkm_base_code=None, map_sf=None)


def test_more_rkm_codes():
    set_prefs(
        rkm_maps=IEC60062_MAPS, units_to_rkm_base_code={'Ω': 'R'}, map_sf=None,
        show_units=None, strip_zeros=None, strip_code=True, minus_sign=None,
        prec=4
    )

    for line in more_testcases.splitlines():
        if not line:
            continue
        q, a, b, c, d = line.split()
        q = Quantity(q)
        q.output_sf = 'TGMk'
        assert a == to_rkm(q), 'sarong {}'.format(q)
        assert b == to_rkm(q, strip_code=False), 'wader {}'.format(q)
        assert c == to_rkm(q, show_units=True), 'footprint {}'.format(q)
        assert d == to_rkm(q, strip_zeros=False), 'scabby {}'.format(q)
