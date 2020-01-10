def linquad(x, form = 'lin'):
    if form == 'lin':
        return 4*x+5
    elif form == 'quad':
        return 4*x**2+5*x+6
    else:
        return 'Falsche Eingabe!'

print(linquad(10))
print(linquad(10, 'quad'))


def linquad_dic(x, form = 'lin'):
    dic = {'lin': 4*x+5, 'quad': 4*x**2+5*x+6}
    return dic[form]

print(linquad_dic(10))
print(linquad_dic(10, 'quad'))
