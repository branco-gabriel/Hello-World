def soma():
    a = int(input('Digite um número: '))
    b = int(input('Digite um número: '))
    print(a + b)


def subtracao():
    a = int(input('Digite um número: '))
    b = int(input('Digite um número: '))
    print(a - b)


def multiplicacao(a, b):
    a = int(input('Digite um número: '))
    b = int(input('Digite um número: '))
    print(a * b)


def divisao():
    try:
        a = int(input('Digite um número: '))
        b = int(input('Digite um número: '))
        print(a / b)
    except:
        print('divisao impossivel')


def menu():
    print("""
    [1] Soma
    [2] Subtração
    [3] Multiplicação
    [4] Divisão 
    """)
    op = int(input('Digite uma opcão: '))

    if op == 1:
        soma()

    elif op == 2:
        subtracao()

    elif op == 3:
        multiplicacao()

    elif op == 4:
        divisao()


menu()
