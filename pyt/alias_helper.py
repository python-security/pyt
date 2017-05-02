"""This module contains helper functions for the interprocedural_cfg module."""

def as_alias_handler(alias_list):
    """Returns a list of all the names that will be called."""
    list_ = list()
    for alias in alias_list:
        if alias.asname:
            list_.append(alias.asname)
        else:
            list_.append(alias.name)
    return list_

def not_as_alias_handler(names_list):
    """Returns a list of names ignoring any aliases."""
    list_ = list()
    for alias in names_list:
        list_.append(alias.name)
    return list_

def retrieve_import_alias_mapping(names_list):
    """Creates a dictionary mapping aliases to their respective name.
    import_alias_names is used in module_definitions.py and visit_Call"""
    import_alias_names = {}

    for alias in names_list:
        if alias.asname:
            import_alias_names[alias.asname] = alias.name
    return import_alias_names
