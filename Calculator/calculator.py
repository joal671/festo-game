import math

def show_menu():
    print('*****************\nInput voltage 220')
    print('1.- Get C value')
    print('2.- Get L value')
    print('3.- Get Ql')
    print('4.- Get Qc')
    print('5.- Power triangle')
    print('6.- Exit\n')

def pwr_lst():
    print('1.- P - fp ')
    print('2.- Q - fp ')
    print('3.- S - fp ')


def get_option():
    op = input()
    return int(op)

def frec():
    f = input('Frecuency on Hz: ')
    return int(f)

def volt():
    v = input('Input Voltage: ')
    return int(v)

def read(str):
    val = input(str + ': ')
    return int(val)

def get_c():
    qc = input('Qc on var: ')
    qc = int(qc)
    f = frec()
    v = volt()
    c = qc / (2*3.1416*f*(v**2))
    print(c / (10**6), 'uF')


def get_l():
    ql = input('Ql on var: ')
    ql = int(ql)
    f = frec()
    v = volt()
    l = (v**2) / (2*3.1416*f*ql)
    print(l, 'H')

def get_ql():
    l = input('L on H: ')
    l = int(l)
    f = frec()
    v = volt()
    ql = (v**2) / (2*3.1416*f*l)
    print(ql, 'Var')


def get_qc():
    c = input('C on uF: ')
    c = int(c)
    f = frec()
    v = volt()
    qc = (v**2) * (2*3.1416*f*c*(10**-6))
    print(qc, 'Var')

def pw_trng():
    pwr_lst()
    option = get_option()
    
    if option == 1:
        p = read('Active Power')
        fp = read('Power factor')
        angle = math.acos(fp)
        print(type(angle))
        q = p * math.tan(angle)
        s = math.hypot(p, q)
        print('Angule: {}\nActive Pwr: {}\nReactive Pwr: {}\nAparent Pwr: {}'.format(math.degrees(angle), p, q, s))
    elif option == 2:
        q = read('Reactive Power')
        fp = read('Power factor')
        angle = math.acos(fp)
        p = q / math.tan(angle)
        s = math.hypot(p, q)
        print('Angule: {}\nActive Pwr: {}\nReactive Pwr: {}\nAparent Pwr: {}'.format(math.degrees(angle), p, q, s))
    elif option == 3:
        s = read('Aparent Power')
        fp = read('Power factor')
        angle = math.acos(fp)
        p = s * math.cos(angle)
        q = s * math.sin(angle)
        print('Angule: {}\nActive Pwr: {}\nReactive Pwr: {}\nAparent Pwr: {}'.format(math.degrees(angle), p, q, s))


while True:
    show_menu()
    op = get_option()
    if op == 1:
        get_c()
    elif op == 2:
        get_l()
    elif op == 3:
        get_ql()
    elif op == 4:
        get_qc()
    elif op == 5:
        pw_trng()
    elif op == 6:
        break
