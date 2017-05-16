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

def handle_aliases_in_calls(name, import_alias_mapping):
    """Returns either None or the handled alias.
    Used in add_module.
    """
    for key, val in import_alias_mapping.items():
        # e.g. Foo == Foo
        # e.g. Foo.Bar startswith Foo.
        if name == key or \
                name.startswith(key + '.'):

            # Replace key with val in name
            # e.g. StarbucksVisitor.Tea -> Eataly.Tea because
            #   "from .nested_folder import StarbucksVisitor as Eataly"
            return name.replace(key, val)
    return None

def handle_aliases_in_init_files(name, import_alias_mapping):
    """Returns either None or the handled alias.
    Used in add_module.
    """
    for key, val in import_alias_mapping.items():
        # e.g. Foo == Foo
        # e.g. Foo.Bar startswith Foo.
        if name == val or \
                name.startswith(val + '.'):

            # Replace val with key in name
            # e.g. StarbucksVisitor.Tea -> Eataly.Tea because
            #   "from .nested_folder import StarbucksVisitor as Eataly"
            return name.replace(val, key)
    return None

def handle_fdid_aliases(module_or_package_name, import_alias_mapping):
    """Returns either None or the handled alias.
    Used in add_module.
    fdid means from directory import directory.
    """
    for key, val in import_alias_mapping.items():
        if module_or_package_name == val:
            return key
    return None

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
