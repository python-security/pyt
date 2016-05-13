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

class ModuleDefinitions():
    def __init__(self, module_name=None):
        self.definitions = []
        self.module_name = module_name

    def append(self, definition):
        self.definitions.append(definition)

    def is_import(self):
        return self.module_name

    def get_definition(self, name):
        for definition in self.definitions:
            if definition.name == name:
                return definition
            
    def set_defintion_node(self, node, name):
        definition = self.get_definition(name)
        if definition:
            self.node = node

            
