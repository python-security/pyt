result = (
    "abc"
    if t.u == v.w else
    "def"
    if x else
    y  # This is the only RHS variable which taints result
    if func(z if 1 + 1 == 2 else z) else
    "ghi"
)
