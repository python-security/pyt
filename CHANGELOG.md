# What's New

Thanks to all our contributors, users, and the many people that make PyT possible! :heart:

If you love PyT, please star our project on GitHub to show your support! :star:

<!--
# A.B.C
##### MMM DD, YYYY

#### :newspaper: News
#### :mega: Release Highlights
#### :boom: Breaking Changes
#### :tada: New Features
#### :sparkles: Usability
#### :telescope: Precision
#### :bug: Bugfixes
#### :snake: Miscellaneous

[#xxxx]: https://github.com/python-security/pyt/pull/xxxx
[@xxxx]: https://github.com/xxxx
-->

# Unreleased
##### April 18, 2018

#### :tada: New Features

* Baseline support by  in ([#106], thanks [@omergunal])

[#106]: https://github.com/python-security/pyt/pull/106
[@omergunal]: https://github.com/omergunal

#### :sparkles: Usability
* Combined all source/sink files and made it the default (#116)

#### :telescope: Precision
* Fixed a bug where "Post.query.paginate" progated taint (#115)
* Fixed a false-positive where `self` was marked as taint (#119)

#### :bug: Bugfixes
* Fixed a bug where `visit_Raise` raised a `TypeError`  (#117)
* Fixed an infinite loop bug that was caused while handling certain loops (#118)

#### :snake: Miscellaneous

* Moved out a bunch of historical files to the [ReadTheDocs repo](https://github.com/KevinHock/rtdpyt) (#110, #111)

[#106]: https://github.com/python-security/pyt/pull/116
[#106]: https://github.com/python-security/pyt/pull/115
[#106]: https://github.com/python-security/pyt/pull/119
[#106]: https://github.com/python-security/pyt/pull/117
[#106]: https://github.com/python-security/pyt/pull/118
[#106]: https://github.com/python-security/pyt/pull/111
[#106]: https://github.com/python-security/pyt/pull/110
