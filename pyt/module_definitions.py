project_definitions = dict()

class ModuleDefinition():
    name = None
    node = None
    path = None
    module_definitions = None

    def __init__(self, local_module_definitions, name, parent_module_name):
        if parent_module_name:
            self.name = parent_module_name + '.' + name
        else:
            self.name = name

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
    pass


class ModuleDefinitions():
    def __init__(self, import_names=None, module_name=None):
        self.definitions = list()
        self.module_name = module_name
        self.classes = list()
        self.import_names = import_names

    def append(self, definition):
        if isinstance(definition, LocalModuleDefinition):
            self.definitions.append(definition)
        elif definition.name in self.import_names:
            self.definitions.append(definition)

        if not definition.node in project_definitions:
            project_definitions[definition.node] = definition

    def is_import(self):
        return self.module_name

    def get_definition(self, name):
        for definition in self.definitions:
            if definition.name == name:
                return definition
            
    def set_defintion_node(self, node, name):
        definition = self.get_definition(name)
        if definition:
            definition.node = node

    def __str__(self):
        module = 'NoModuleName'
        if self.module_name:
            module = self.module_name
            
        return 'Definitions: ' + ' '.join([str(definition) for definition in self.definitions]) + '\nmodule_name: ' + module + '\n'

            
