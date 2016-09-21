import os

from base_cfg import Node


database_file_name = 'db.sql'
nodes_table_name = 'nodes'
vulnerabilities_table_name = 'vulnerabilities'

def create_nodes_table():
    with open(database_file_name, 'a') as fd:
        fd.write('DROP TABLE IF EXISTS ' + nodes_table_name + '\n')
        fd.write('CREATE TABLE ' + nodes_table_name +  '(id int,label varchar(255),line_number int, path varchar(255));')

def create_vulnerabilities_table():
    with open(database_file_name, 'a') as fd:
        fd.write('DROP TABLE IF EXISTS ' + vulnerabilities_table_name + '\n')
        fd.write('CREATE TABLE ' + vulnerabilities_table_name + '(id int, source varchar(255), source_word varchar(255), sink varchar(255), sink_word varchar(255));')

def quote(item):
    if isinstance(item, Node):
        item = item.label
    return "'" + item.replace("'", "''") + "'"

def insert_vulnerability(vulnerability):
    with open(database_file_name, 'a') as fd:
        fd.write('\nINSERT INTO ' + vulnerabilities_table_name + '\n')
        fd.write('VALUES (')
        fd.write(quote(vulnerability.__dict__['source']) + ',')
        fd.write(quote(vulnerability.__dict__['source_trigger_word']) + ',')
        fd.write(quote(vulnerability.__dict__['sink']) + ',')
        fd.write(quote(vulnerability.__dict__['sink_trigger_word']))
        fd.write(');')

def insert_node(node):
    with open(database_file_name, 'a') as fd:
        fd.write('\nINSERT INTO ' + nodes_table_name + '\n')
        fd.write('VALUES (')
        fd.write("'" + node.__dict__['label'].replace("'", "''") + "'" + ',')
        line_number = node.__dict__['line_number']
        if line_number:
            fd.write(str(line_number) + ',')
        else:
            fd.write('NULL,')
        path = node.__dict__['path']
        if path:
            fd.write("'" + path.replace("'", "''") + "'")
        else:
            fd.write('NULL')
        fd.write(');')

def create_database(cfg_list, vulnerability_log):
    create_nodes_table()
    for cfg in cfg_list:
        for node in cfg.nodes:
            insert_node(node)
    create_vulnerabilities_table()
    for vulnerability in vulnerability_log.vulnerabilities:
        insert_vulnerability(vulnerability)


class Output():
    filename_prefix = None

    def __init__(self, title):
        if Output.filename_prefix:
            self.title = Output.filename_prefix + '_' + title
        else:
            self.title = title

    def __enter__(self):
        self.fd = open(self.title, 'w')
        return self.fd

    def __exit__(self, type, value, traceback):
        self.fd.close()


def def_use_chain_to_file(cfg_list):
    from definition_chains import build_def_use_chain
    with Output('def-use_chain.pyt') as fd:
            for i, cfg in enumerate(cfg_list):
                fd.write('##### Def-use chain for CFG {} #####{}'
                         .format(i, os.linesep))
                def_use = build_def_use_chain(cfg.nodes)
                for k, v in def_use.items():
                    fd.write('Def: {} -> Use: [{}]{}'
                             .format(k.label,
                                     ', '.join([n.label for n in v]),
                                     os.linesep))


def use_def_chain_to_file(cfg_list):
    from definition_chains import build_use_def_chain
    with Output('use-def_chain.pyt') as fd:
            for i, cfg in enumerate(cfg_list):
                fd.write('##### Use-def chain for CFG {} #####{}'
                         .format(i, os.linesep))
                def_use = build_use_def_chain(cfg.nodes)
                for k, v in def_use.items():
                    print(type(v))
                    fd.write('Use: {} -> Def: [{}]{}'
                             .format(k.label,
                                     ', '.join([n[1].label for n in v]),
                                     os.linesep))


def cfg_to_file(cfg_list):
    with Output('control_flow_graph.pyt') as fd:
        for i, cfg in enumerate(cfg_list):
            fd.write('##### CFG {} #####{}'.format(i, os.linesep))
            for i, node in enumerate(cfg.nodes):
                fd.write('Node {}: {}{}'.format(i, node.label, os.linesep))


def verbose_cfg_to_file(cfg_list):
    with Output('verbose_control_flow_graph.pyt') as fd:
        for i, cfg in enumerate(cfg_list):
            fd.write('##### CFG {} #####{}'.format(i, os.linesep))
            for i, node in enumerate(cfg.nodes):
                fd.write('Node {}: {}{}'.format(i, repr(node), os.linesep))
