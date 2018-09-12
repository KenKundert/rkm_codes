# encoding: utf8

from rkm_codes import (
    set_maps, read_rkm_code, write_rkm_code, IEC60062_MAPS, UNITLESS_MAPS
)

testcases = [
    dict(maps=UNITLESS_MAPS, icode='R47', q='470m', ocode='470m', ocodeu='470m'),
    dict(maps=UNITLESS_MAPS, icode='R47Ω', q='470 mΩ', ocode='470m', ocodeu='470mΩ'),
    dict(maps=UNITLESS_MAPS, icode='4R7', q='4.7', ocode='47', ocodeu='47'),
    dict(maps=UNITLESS_MAPS, icode='470R', q='470', ocode='470', ocodeu='470'),
    dict(maps=UNITLESS_MAPS, icode='4K7', q='4.7k', ocode='4k7', ocodeu='4k7'),
    dict(maps=UNITLESS_MAPS, icode='4K7Ω', q='4.7 kΩ', ocode='4k7', ocodeu='4k7Ω'),
    dict(maps=UNITLESS_MAPS, icode='47K', q='47k', ocode='47k', ocodeu='47k'),
    dict(maps=UNITLESS_MAPS, icode='47K3', q='47.3k', ocode='47k', ocodeu='47k'),
    dict(maps=UNITLESS_MAPS, icode='470K', q='470k', ocode='470k', ocodeu='470k'),
    dict(maps=UNITLESS_MAPS, icode='4M7', q='4.7M', ocode='4M7', ocodeu='4M7'),
    dict(maps=UNITLESS_MAPS, icode='150nA', q='150 nA', ocode='150n', ocodeu='150nA'),
    dict(maps=UNITLESS_MAPS, icode='2v5', q='2.5', ocode='25', ocodeu='25'),
    dict(maps=UNITLESS_MAPS, icode='2n5A', q='2.5 nA', ocode='2n5', ocodeu='2n5A'),
    dict(maps=UNITLESS_MAPS, icode='f220', q='220m', ocode='220m', ocodeu='220m'),
    dict(maps=UNITLESS_MAPS, icode='2c', q='2', ocode='20', ocodeu='20'),
    dict(maps=UNITLESS_MAPS, icode='2c5', q='2.5', ocode='25', ocodeu='25'),
    dict(maps=UNITLESS_MAPS, icode='2f', q='2', ocode='20', ocodeu='20'),
    dict(maps=UNITLESS_MAPS, icode='2f5', q='2.5', ocode='25', ocodeu='25'),
    dict(maps=UNITLESS_MAPS, icode='2p5F', q='2.5 pF', ocode='2p5', ocodeu='2p5F'),
    dict(maps=UNITLESS_MAPS, icode='h220', q='220m', ocode='220m', ocodeu='220m'),
    dict(maps=UNITLESS_MAPS, icode='2h', q='2', ocode='20', ocodeu='20'),
    dict(maps=UNITLESS_MAPS, icode='2h5', q='2.5', ocode='25', ocodeu='25'),
    dict(maps=UNITLESS_MAPS, icode='2p5H', q='2.5 pH', ocode='2p5', ocodeu='2p5H'),

    dict(maps=IEC60062_MAPS, icode='R47', q='470 mΩ', ocode='470m', ocodeu='470mΩ'),
    dict(maps=IEC60062_MAPS, icode='R47Ω', q='470 mΩ', ocode='470m', ocodeu='470mΩ'),
    dict(maps=IEC60062_MAPS, icode='4R7', q='4.7 Ω', ocode='4r7', ocodeu='4r7Ω'),
    dict(maps=IEC60062_MAPS, icode='470R', q='470 Ω', ocode='470r', ocodeu='470rΩ'),
    dict(maps=IEC60062_MAPS, icode='4K7', q='4.7 kΩ', ocode='4k7', ocodeu='4k7Ω'),
    dict(maps=IEC60062_MAPS, icode='4K7Ω', q='4.7 kΩ', ocode='4k7', ocodeu='4k7Ω'),
    dict(maps=IEC60062_MAPS, icode='47K', q='47 kΩ', ocode='47k', ocodeu='47kΩ'),
    dict(maps=IEC60062_MAPS, icode='47K3', q='47.3 kΩ', ocode='47k', ocodeu='47kΩ'),
    dict(maps=IEC60062_MAPS, icode='470K', q='470 kΩ', ocode='470k', ocodeu='470kΩ'),
    dict(maps=IEC60062_MAPS, icode='4M7', q='4.7 MΩ', ocode='4M7', ocodeu='4M7Ω'),
    dict(maps=IEC60062_MAPS, icode='150nA', q='150 nA', ocode='150n', ocodeu='150nA'),
    dict(maps=IEC60062_MAPS, icode='2v5', q='2.5 v', ocode='2v5', ocodeu='2v5v'),
    dict(maps=IEC60062_MAPS, icode='2n5A', q='2.5 nA', ocode='2n5', ocodeu='2n5A'),
    dict(maps=IEC60062_MAPS, icode='f220', q='220a', ocode='220a', ocodeu='220a'),
    dict(maps=IEC60062_MAPS, icode='2c', q='2 F', ocode='2c0', ocodeu='2c0F'),
    dict(maps=IEC60062_MAPS, icode='2c5', q='2.5 F', ocode='2c5', ocodeu='2c5F'),
    dict(maps=IEC60062_MAPS, icode='2f', q='2f', ocode='2f0', ocodeu='2f0'),
    dict(maps=IEC60062_MAPS, icode='2f5', q='2.5f', ocode='2f5', ocodeu='2f5'),
    dict(maps=IEC60062_MAPS, icode='2p5F', q='2.5 pF', ocode='2p5', ocodeu='2p5F'),
    dict(maps=IEC60062_MAPS, icode='h220', q='220 mh', ocode='220m', ocodeu='220mh'),
    dict(maps=IEC60062_MAPS, icode='2h', q='2 h', ocode='2h0', ocodeu='2h0h'),
    dict(maps=IEC60062_MAPS, icode='2h5', q='2.5 h', ocode='2h5', ocodeu='2h5h'),
    dict(maps=IEC60062_MAPS, icode='2p5H', q='2.5 pH', ocode='2p5', ocodeu='2p5H'),

    dict(maps=IEC60062_MAPS, icode='l047', q='47 uΩ', ocode='47u', ocodeu='47uΩ'),  # using invalid sf
    dict(maps=IEC60062_MAPS, icode='l47', q='470 uΩ', ocode='470u', ocodeu='470uΩ'), # using invalid sf
    dict(maps=IEC60062_MAPS, icode='4l7', q='4.7 mΩ', ocode='4m7', ocodeu='4m7Ω'),
    dict(maps=IEC60062_MAPS, icode='47l', q='47 mΩ', ocode='47m', ocodeu='47mΩ'),
    dict(maps=IEC60062_MAPS, icode='470l', q='470 mΩ', ocode='470m', ocodeu='470mΩ'),
    dict(maps=IEC60062_MAPS, icode='r47', q='470 mΩ', ocode='470m', ocodeu='470mΩ'),
    dict(maps=IEC60062_MAPS, icode='4r7', q='4.7 Ω', ocode='4r7', ocodeu='4r7Ω'),
    dict(maps=IEC60062_MAPS, icode='47r', q='47 Ω', ocode='47r', ocodeu='47rΩ'),   # 47rΩ is weird
    dict(maps=IEC60062_MAPS, icode='470r', q='470 Ω', ocode='470r', ocodeu='470rΩ'),   # 470rΩ is weird
    dict(maps=IEC60062_MAPS, icode='k47', q='470 Ω', ocode='470r', ocodeu='470rΩ'),   # 470rΩ is weird
    dict(maps=IEC60062_MAPS, icode='K47', q='470 Ω', ocode='470r', ocodeu='470rΩ'),   # 470rΩ is weird
    dict(maps=IEC60062_MAPS, icode='4k7', q='4.7 kΩ', ocode='4k7', ocodeu='4k7Ω'),   # should be K
    dict(maps=IEC60062_MAPS, icode='4K7', q='4.7 kΩ', ocode='4k7', ocodeu='4k7Ω'),   # should be K
    dict(maps=IEC60062_MAPS, icode='47k', q='47 kΩ', ocode='47k', ocodeu='47kΩ'),   # should be K
    dict(maps=IEC60062_MAPS, icode='47K', q='47 kΩ', ocode='47k', ocodeu='47kΩ'),   # should be K
    dict(maps=IEC60062_MAPS, icode='470k', q='470 kΩ', ocode='470k', ocodeu='470kΩ'),   # should be K
    dict(maps=IEC60062_MAPS, icode='470K', q='470 kΩ', ocode='470k', ocodeu='470kΩ'),   # should be K
    dict(maps=IEC60062_MAPS, icode='M470', q='470 kΩ', ocode='470k', ocodeu='470kΩ'),   # should be K
    dict(maps=IEC60062_MAPS, icode='4M70', q='4.7 MΩ', ocode='4M7', ocodeu='4M7Ω'),
    dict(maps=IEC60062_MAPS, icode='47M', q='47 MΩ', ocode='47M', ocodeu='47MΩ'),
    dict(maps=IEC60062_MAPS, icode='470M', q='470 MΩ', ocode='470M', ocodeu='470MΩ'),
    dict(maps=IEC60062_MAPS, icode='G470', q='470 MΩ', ocode='470M', ocodeu='470MΩ'),
    dict(maps=IEC60062_MAPS, icode='4G7', q='4.7 GΩ', ocode='4G7', ocodeu='4G7Ω'),
    dict(maps=IEC60062_MAPS, icode='47G', q='47 GΩ', ocode='47G', ocodeu='47GΩ'),
    dict(maps=IEC60062_MAPS, icode='470G', q='470 GΩ', ocode='470G', ocodeu='470GΩ'),
    dict(maps=IEC60062_MAPS, icode='4700G', q='4.7 TΩ', ocode='4T7', ocodeu='4T7Ω'),  # uses invalid sf
]

def test_rkm_codes():
    for case in testcases:
        set_maps(case['maps'])
        maps = 'unitless' if case['maps'] == UNITLESS_MAPS else 'IEC60062'
        q = read_rkm_code(case['icode'])
        print(
            maps,
            case['icode'],
            q,
            write_rkm_code(q),
            write_rkm_code(q, show_units=True),
            sep=', '
        )
        assert str(q) == case['q']
        assert write_rkm_code(q) == case['ocode']
        assert write_rkm_code(q, show_units=True) == case['ocodeu']
