import decimal


name = 'Fred'
greeting = f"Hello {name}"
width = 10
precision = 4
value = decimal.Decimal("12.34567")
result = f"result: {value:{width}.{precision}}"
print (result)