from .expr_visitor import ExprVisitor


class CFG():
    def __init__(
        self,
        nodes,
        blackbox_assignments,
        filename
    ):
        self.nodes = nodes
        self.blackbox_assignments = blackbox_assignments
        self.filename = filename

    def __repr__(self):
        output = ''
        for x, n in enumerate(self.nodes):
            output = ''.join((output, 'Node: ' + str(x) + ' ' + repr(n), '\n\n'))
        return output

    def __str__(self):
        output = ''
        for x, n in enumerate(self.nodes):
            output = ''.join((output, 'Node: ' + str(x) + ' ' + str(n), '\n\n'))
        return output


def make_cfg(
    tree,
    project_modules,
    local_modules,
    filename,
    module_definitions=None,
    allow_local_directory_imports=True
):
    visitor = ExprVisitor(
        tree,
        project_modules,
        local_modules,
        filename,
        module_definitions,
        allow_local_directory_imports
    )
    return CFG(
        visitor.nodes,
        visitor.blackbox_assignments,
        filename
    )
