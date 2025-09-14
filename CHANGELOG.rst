Change Log
==========

Latest Development Version
--------------------------

| Version: 0.6
| Released: 2023-04-14


1.0 (2025-09-14)
----------------
- Change to MIT license


0.6 (2023-04-14)
----------------
- Suppress *rkm_code*’s use of the new SI scale factors in `QuantiPhy 
    <https://quantiphy.readthedocs.io>`_ so that ``R`` is no longer treated as 
    a scale factor when using the latest version of *QuantiPhy*.


0.5 (2020-02-01)
----------------
- Allow argument to *to_rkm()* to be a string or simple number
- Added *strip_code* preference
- With small numbers show 0 rather than exponent


0.4 (2019-08-29)
----------------
- added *find_rkm()*


0.3 (2019-08-23)
----------------
- move the units to the middle of the number with the scale factor
- added support for signed numbers
- added *show_units*, *strip_zeros*, *minus_sign*, and *prec* to preferences
- this release is not backward compatible; units at the end of the number
    are no longer supported


0.2 (2018-09-14)
----------------
- fixed issue in *set_prefs()*


0.1 (2018-09-12)
----------------
- initial release
