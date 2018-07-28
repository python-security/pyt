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
#### :performing_arts: Performance
#### :telescope: Precision
#### :bug: Bugfixes
#### :snake: Miscellaneous

[#xxxx]: https://github.com/python-security/pyt/pull/xxxx
[@xxxx]: https://github.com/xxxx
-->

# Unreleased

#### :tada: New Features

* Ability to analyze directories, `-r` Recursive option ([#129], thanks [@omergunal])
* Added `--dont-prepend-root` option, makes it so that we don't require imports start with `project_root.*` ([#151], thanks [@bcaller])
* Added `--no-local-imports` option, to require absolute imports be relative to the project root ([#151], thanks [@bcaller])
* [PEP 498] support, formatted string literals ([#142], thanks [@bcaller])
* [PEP 526] support, syntax for variable annotations ([#143], thanks [@bcaller])
* Whitelist lines of sources and sinks ending in `# nosec` ([#121], thanks [@omergunal])

[@bcaller]: https://github.com/bcaller
[PEP 498]: https://www.python.org/dev/peps/pep-0498/
[PEP 526]: https://www.python.org/dev/peps/pep-0526/
[#121]: https://github.com/python-security/pyt/pull/121
[#129]: https://github.com/python-security/pyt/pull/129
[#142]: https://github.com/python-security/pyt/pull/142
[#143]: https://github.com/python-security/pyt/pull/143
[#151]: https://github.com/python-security/pyt/pull/151

#### :telescope: Precision

* Added per-arg taint, for sink functions ([#147], thanks [@bcaller])
* Improved tuple assingment to be more precise and support starargs ([#150], thanks [@bcaller])

[#147]: https://github.com/python-security/pyt/pull/147
[#150]: https://github.com/python-security/pyt/pull/150

#### :bug: Bugfixes
* Fixed a bug where `get_call_names` only handled ast.Attribute nodes ([#148], thanks [@bcaller])
* Fixed a bug where `vars_visitor.py` crashed on Python 3.5 dict syntax ([#144], thanks [@bcaller])

[#144]: https://github.com/python-security/pyt/pull/144
[#148]: https://github.com/python-security/pyt/pull/148

#### :performing_arts: Performance

* Added an `lru_cache` to the `generate_ast` function ([#153], thanks [@bcaller])

[#153]: https://github.com/python-security/pyt/pull/153

#### :mortar_board: Walkthrough / Help

* Added README.rst files to almost every directory. (Partially [#126])

#### :snake: Miscellaneous

* Added tests for `vars_visitor.py`, making our overall coverage 91% ([#139], thanks [@stannum-l])
* Cleaned and organized requirements, `setup.py`, `tox.ini` and `.travis.yml` ([#152], thanks [@bcaller])
* Cleaned up the new pyt/core/ folder ([#132]) 
* Fixed all flake8 errors ([#114] & [#130], thanks [@cclauss])
* Re-organized the entire codebase into different directories ([#126])
* Return exit code 1 if any non-sanitised vulnerabilities are found ([#156], thanks [@bcaller])

[@cclauss]: https://github.com/cclauss
[@stannum-l]: https://github.com/stannum-l
[#114]: https://github.com/python-security/pyt/pull/114
[#126]: https://github.com/python-security/pyt/pull/126
[#130]: https://github.com/python-security/pyt/pull/130
[#132]: https://github.com/python-security/pyt/pull/132
[#139]: https://github.com/python-security/pyt/pull/139
[#152]: https://github.com/python-security/pyt/pull/152
[#156]: https://github.com/python-security/pyt/pull/156

# 0.34
##### April 24, 2018

#### :tada: New Features

* Baseline support ([#106], thanks [@omergunal])

[@omergunal]: https://github.com/omergunal
[#106]: https://github.com/python-security/pyt/pull/106

#### :sparkles: Usability
* Combined all source/sink information files and made it the default ([#116])

#### :telescope: Precision
* Fixed a bug where `Post.query.paginate` propagated taint ([#115])
* Fixed a false-positive where `self` was marked as taint ([#119], thanks [@lFatty])

#### :bug: Bugfixes
* Fixed a bug where `visit_Raise` raised a `TypeError`  ([#117], thanks [@lFatty])
* Fixed a bug where we were not including `pyt/vulnerability_definitions` files ([#122], thanks [@Ekultek])
* Fixed an infinite loop bug that was caused while handling certain loops ([#118])

#### :snake: Miscellaneous

* Moved out a bunch of historical files to the [ReadTheDocs repo](https://github.com/KevinHock/rtdpyt) ([#110], [#111])

[@Ekultek]: https://github.com/Ekultek
[@lfatty]: https://github.com/lfatty
[#110]: https://github.com/python-security/pyt/pull/110
[#111]: https://github.com/python-security/pyt/pull/111
[#115]: https://github.com/python-security/pyt/pull/115
[#116]: https://github.com/python-security/pyt/pull/116
[#119]: https://github.com/python-security/pyt/pull/119
[#117]: https://github.com/python-security/pyt/pull/117
[#118]: https://github.com/python-security/pyt/pull/118
[#122]: https://github.com/python-security/pyt/issues/122
