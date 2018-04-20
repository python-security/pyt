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
#### :mortar_board: Walkthrough / Help
#### :telescope: Precision
#### :bug: Bugfixes
#### :snake: Miscellaneous

[#xxxx]: https://github.com/python-security/pyt/pull/xxxx
[@xxxx]: https://github.com/xxxx
-->

# Unreleased
##### April 18, 2018

#### :tada: New Features

* Baseline support ([#106], thanks [@omergunal])

[#106]: https://github.com/python-security/pyt/pull/106
[@omergunal]: https://github.com/omergunal

#### :sparkles: Usability
* Combined all source/sink information files and made it the default ([#116])

#### :telescope: Precision
* Fixed a bug where `Post.query.paginate` propagated taint ([#115])
* Fixed a false-positive where `self` was marked as taint ([#119], thanks [@lFatty])

#### :bug: Bugfixes
* Fixed a bug where `visit_Raise` raised a `TypeError`  ([#117], thanks [@lFatty])
* Fixed an infinite loop bug that was caused while handling certain loops ([#118])

#### :snake: Miscellaneous

* Moved out a bunch of historical files to the [ReadTheDocs repo](https://github.com/KevinHock/rtdpyt) ([#110], [#111])

[#116]: https://github.com/python-security/pyt/pull/116
[#115]: https://github.com/python-security/pyt/pull/115
[#119]: https://github.com/python-security/pyt/pull/119
[#117]: https://github.com/python-security/pyt/pull/117
[#118]: https://github.com/python-security/pyt/pull/118
[#111]: https://github.com/python-security/pyt/pull/111
[#110]: https://github.com/python-security/pyt/pull/110
[@lfatty]: https://github.com/lfatty
