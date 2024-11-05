# Escrevendo um programa que calcule o fatorial de um numero dado.
# O fatorial (!) de um numero n, representado por n!, é a multiplicação de n por seus antecessores maiores ou iguais a 1.
# Resumindo, o fatorial de 3 é 3 x 2 x 1, ou seja, 6.

# Etapas do programa
# 1. Perguntar qual o número em que devemos calcular o fatoral?
# 2. Armazenas a resposta do usuario em uma variavel.
# 3. Criar um loop para multiplicar o número fornecido pelo usuário por todos os seus antecessores, até que o numero multiplicado chegue a 1.

num_fatorial = int(input("Qual o numero devemos calcular o fatorial?"))

fatorial = 1
for num in range(num_fatorial, 1 , -1):
    # fatorial = fatorial * num
    fatorial *= num

    print(fatorial)
    