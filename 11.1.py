def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('symbol must be a single character string.')
    if width < 2:
        raise Exception('width must be greater than 2.')
    if height < 2:
        raise Exception('height must be greater than 2.')
    
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

for sym, w, h in (('*', 4, 4), ('t', 8, 3), ('zw', 3, 5), ('x', 1, 2), ('cc', 1, 1)):
    try:
        boxPrint(sym, w, h)
        print('================')
    except Exception as err:
        print(err)
        print('================')
