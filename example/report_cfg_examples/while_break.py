while x < threshold:
    if invalid_value(x):
        break
    x += 1
else:
    handle_value()
