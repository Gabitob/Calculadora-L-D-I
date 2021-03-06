import sympy as np
print('-=' * 40)
print('          CALCULADORA DE LIMITES, DERIVADAS E INTEGRAIS')
print('-=' * 40)
escolha = input('Digite l para limites, d para derivadas e i para integrais:')
if escolha == 'l':
    equa = input('Digite a equação do limite:')
    tend = input('Tendendo:')
    x = np.Symbol('x')
    valor = np.limit(equa, x, tend)
    print('O resultado é:')
    print(' ')
    print(valor)
    print(' ')
    print('Estamos juntos?')
    np.plot(equa)
elif escolha == 'd':
    equa1 = input('Digite a equação da derivada:')
    valor1 = np.diff(equa1)
    print('O resultado é:')
    print('')
    print(valor1)
    print(' ')
    print('Estamos juntos?')
else:
    equa2 = input('Digite a equação da integral:')
    valor2 = np.integrate(equa2)
    print('O resultado é:')
    print('')
    print(valor2)
    print(' ')
    print('Estamos juntos?')
