import os
from datetime import datetime

from .base_cfg import Node
from .definition_chains import build_def_use_chain, build_use_def_chain
from .lattice import Lattice


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
    with Output('use-def_chain.pyt') as fd:
            for i, cfg in enumerate(cfg_list):
                fd.write('##### Use-def chain for CFG {} #####{}'
                         .format(i, os.linesep))
                def_use = build_use_def_chain(cfg.nodes)
                for k, v in def_use.items():
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


def lattice_to_file(cfg_list, analysis_type):
    with Output('lattice.pyt') as fd:
        for i, cfg in enumerate(cfg_list):
            fd.write('##### Lattice for CFG {} #####{}'.format(i, os.linesep))
            l = Lattice(cfg.nodes, analysis_type)

            fd.write('# Elements to bitvector #{}'.format(os.linesep))
            for k, v in l.el2bv.items():
                fd.write('{} -> {}{}'.format(str(k), bin(v), os.linesep))

            fd.write('# Bitvector to elements #{}'.format(os.linesep))
            for k, v in l.el2bv.items():
                fd.write('{} -> {}{}'.format(bin(v), str(k), os.linesep))


def write_vlog_to_file(fd, vulnerability_log):
    for i, vulnerability in enumerate(vulnerability_log.vulnerabilities,
                                      start=1):
        fd.write('Vulnerability {}:\n{}{}{}'
                 .format(i, vulnerability, os.linesep, os.linesep))


def vulnerabilities_to_file(vulnerability_log):
    with Output('vulnerabilities.pyt') as fd:
        number_of_vulnerabilities = len(vulnerability_log.vulnerabilities)
        if number_of_vulnerabilities == 1:
            fd.write('{} vulnerability found:{}'
                     .format(number_of_vulnerabilities, os.linesep))
        else:
            fd.write('{} vulnerabilities found:{}'
                     .format(number_of_vulnerabilities, os.linesep))
        write_vlog_to_file(fd, vulnerability_log)


def save_repo_scan(repo, entry_path, vulnerability_log, error=None):
    with open('scan.pyt', 'a') as fd:
        fd.write('{}{}'.format(repo.name, os.linesep))
        fd.write('{}{}'.format(repo.url, os.linesep))
        fd.write('Entry file: {}{}'.format(entry_path, os.linesep))
        fd.write('Scanned: {}{}'.format(datetime.now(), os.linesep))
        if vulnerability_log:
            write_vlog_to_file(fd, vulnerability_log)
        else:
            fd.write('No vulnerabilities found.{}'.format(os.linesep))
        if error:
            fd.write('An Error occurred while scanning the repo: {}'
                     .format(str(error)))
        fd.write(os.linesep)
        fd.write(os.linesep)
