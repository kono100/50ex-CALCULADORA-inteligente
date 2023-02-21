


#50. Criar uma calculadora inteligente que realize as 4 operações básica (+, -, /, *). No programa
#principal:
#a) leia um número (float)
#b) leia uma operação (+, -, /, *)
#c) leia um número (float)
#Na função:

#a) receba os parâmetros
#b) calcule apenas a operação solicitada
#c) imprima na tela o valor

print()
num1 = float(input('Primeiro n°: '))
num2 = float(input('Segundo n°: '))
operacao = input('\nEscolha sua operação (+, -, *, /): ')

if operacao =='+':
        soma = num1 + num2
        print(f'\nO Resultado da Soma é: {soma}\n')
elif operacao =='-':
        sub = num1 - num2
        print(f"\nO Resultado da Subtração é: {sub}\n")
elif operacao == '*':
        mult = num1 * num2
        print(f"\nO Resultado da Multiplicação é: {mult}\n")
elif operacao == '/':
        div = num1 / num2
        print(f"\nO Resultado da Divisão é: {div}\n")
else:
        print('Burro pra caralho, escolhe certo ai zé')