# Desenvolvendo um algoritmo que calcule a soma dos numeros de 1 a N, onde é fornecido pelo usuario.

# Etapas do meu programa
# 1. Perguntar qual o valor maximo?
# 2. Armazenar esse valor em uma variavel
# 3. Criar um loop para somar todos os numeros de 1 até o numero que o usuario forneceu
# 4. Armazenar a soma desse loop em uma variavel
# 5. Printar o resultado

valor_maximo = int(input("Até qual valor eu devo somar? "))

total = valor_maximo
for num in range(1, valor_maximo, 1):
    #valor_maximo = valor_maximo + num
    total += num

    print("A soma de todos os valores até o numero", valor_maximo, "é igual a", total)