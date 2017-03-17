"""This module handles module definitions which basically is a list of module definition."""

project_definitions = dict()  # Contains all project definitions for a program run


class ModuleDefinition():
    """Handling of a definition."""

    name = None
    node = None
    path = None
    module_definitions = None

    def __init__(self, local_module_definitions, name, parent_module_name, path):
        if parent_module_name:
            self.name = parent_module_name + '.' + name
        else:
            self.name = name
        self.path = path

        self.module_definitions = local_module_definitions

    def __str__(self):
        name = 'NoName'
        node = 'NoNode'
        if self.name:
            name = self.name
        if self.node:
            node = str(self.node)
        return self.__class__.__name__ + ': ' + ';'.join((name, node))


class LocalModuleDefinition(ModuleDefinition):
    """A local definition."""
    pass


class ModuleDefinitions():
    """A collection of module definition.

    Adds to the project definitions list.
    """

    def __init__(self, import_names=None, module_name=None):
        """Optionally set import names and module name.

        Module name should only be set when it is a normal import statement.
        """
        self.definitions = list()
        self.module_name = module_name
        self.classes = list()
        self.import_names = import_names

    def append(self, definition):
        """Add definition to list.

        Handles localdefinitions and adds to project_definitions.
        """
        if isinstance(definition, LocalModuleDefinition):
            self.definitions.append(definition)
        elif self.import_names and definition.name in self.import_names:
            self.definitions.append(definition)

        if not definition.node in project_definitions:
            project_definitions[definition.node] = definition

    def is_import(self):
        """Return whether it is a normal import statement and not a from import.

        This can be checked by checking the module name as it is only set when it is a normal import.
        """
        return self.module_name

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

        return 'Definitions: ' + ' '.join([str(definition) for definition in self.definitions]) + '\nmodule_name: ' + module + '\n'


