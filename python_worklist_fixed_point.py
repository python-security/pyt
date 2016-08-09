def dep(node):
    r = list()
    for n in cfg.nodes:
        if node in n.new_constraint:
            r.append(n)
    return n


q = cfg.nodes
while q != []:
    y = fix()
    q = q[1:]
    if y != x_1:
        for v in dep(q[0]):
            q.append(v)
        q.new_constraint = y


