"""This module handles module definitions
 which basically is a list of module definition."""

import ast


# Contains all project definitions for a program run
# Only used in framework_adaptor.py, but modified here
project_definitions = dict()


class ModuleDefinition():
    """Handling of a definition."""
    module_definitions = None
    name = None
    node = None
    path = None

    def __init__(
        self,
        local_module_definitions,
        name,
        parent_module_name,
        path
    ):
        self.module_definitions = local_module_definitions
        self.parent_module_name = parent_module_name
        self.path = path

        if parent_module_name:
            if isinstance(parent_module_name, ast.alias):
                self.name = parent_module_name.name + '.' + name
            else:
                self.name = parent_module_name + '.' + name
        else:
            self.name = name

    def __str__(self):
        name = 'NoName'
        node = 'NoNode'
        if self.name:
            name = self.name
        if self.node:
            node = str(self.node)
        return "Path:" + self.path + " " + self.__class__.__name__ + ': ' + ';'.join((name, node))


class LocalModuleDefinition(ModuleDefinition):
    """A local definition."""
    pass


class ModuleDefinitions():
    """A collection of module definition.

    Adds to the project definitions list.
    """

    def __init__(
        self,
        import_names=None,
        module_name=None,
        is_init=False,
        filename=None
    ):
        """Optionally set import names and module name.

        Module name should only be set when it is a normal import statement.
        """
        self.import_names = import_names
        # module_name is sometimes ast.alias or a string
        self.module_name = module_name
        self.is_init = is_init
        self.filename = filename
        self.definitions = list()
        self.classes = list()
        self.import_alias_mapping = dict()

    def append_if_local_or_in_imports(self, definition):
        """Add definition to list.

        Handles local definitions and adds to project_definitions.
        """
        if isinstance(definition, LocalModuleDefinition):
            self.definitions.append(definition)
        elif self.import_names == ["*"]:
            self.definitions.append(definition)
        elif self.import_names and definition.name in self.import_names:
            self.definitions.append(definition)
        elif (self.import_alias_mapping and definition.name in
              self.import_alias_mapping.values()):
            self.definitions.append(definition)

        if definition.parent_module_name:
            self.definitions.append(definition)

        if definition.node not in project_definitions:
            project_definitions[definition.node] = definition

    def get_definition(self, name):
        """Get definitions by name."""
        for definition in self.definitions:
            if definition.name == name:
                return definition

    def set_definition_node(self, node, name):
        """Set definition by name."""
        definition = self.get_definition(name)
        if definition:
            definition.node = node

    def __str__(self):
        module = 'NoModuleName'
        if self.module_name:
            module = self.module_name

        if self.definitions:
            if isinstance(module, ast.alias):
                return (
                    'Definitions: "' + '", "'
                    .join([str(definition) for definition in self.definitions]) +
                    '" and module_name: ' + module.name +
                    ' and filename: ' + str(self.filename) +
                    ' and is_init: ' + str(self.is_init) + '\n')
            return (
                'Definitions: "' + '", "'
                .join([str(definition) for definition in self.definitions]) +
                '" and module_name: ' + module +
                ' and filename: ' + str(self.filename) +
                ' and is_init: ' + str(self.is_init) + '\n')
        else:
            if isinstance(module, ast.alias):
                return (
                    'import_names is ' + str(self.import_names) +
                    ' No Definitions, module_name: ' + str(module.name) +
                    ' and filename: ' + str(self.filename) +
                    ' and is_init: ' + str(self.is_init) + '\n')
            return (
                'import_names is ' + str(self.import_names) +
                ' No Definitions, module_name: ' + str(module) +
                ' and filename: ' + str(self.filename) +
                ' and is_init: ' + str(self.is_init) + '\n')
