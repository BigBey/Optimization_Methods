def writeRow(data, a, b, prev_length, x1, x2, f1, f2):
    data['a'].append(a)
    data['b'].append(b)
    data['Отношение длин'].append(abs(b - a) / prev_length if prev_length != None else 'None')
    data['x1'].append(x1)
    data['x2'].append(x2)
    data['f(x1)'].append(f1)
    data['f(x2)'].append(f2)