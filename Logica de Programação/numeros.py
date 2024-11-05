#Criando um programa que verifique se um numero dado é primo ou não.
#Um numero primo é um numero natural maior que 1 que não pode ser dormado pela multiplicação de outros dois naturais menores.
#Por exemplo, 5 é primo porque as unicas maneiras de escreve-lo como um produto, 1 x 5 ou 5 x 1, envolvem o próprio 5. Oque significa, que 6 não é primo, porque 6 pode ser escrito como 3 * 2.


# Etapas
# 1. perguntar para o usuario qual o numero?
# 2. armazenar o numero em uma variavel
# 3. inicializar uma lista vazia com os divisores do numero
# 4. se esse numero for 1, automaticamente descartar
# 5. se o numero for 2, automaticamente classificar como primo
# 6. gerar uma lista com todos os numeros de 2 até o numero digitado
# 7. se o numero digitado for divisivel por algum dos numeros da lista (que não seja ele), adicionar esse numero na,lista de divisores
# 8. ao final, ver o tamanho da lista de divisores. se não tiver nenhum divisor, é primo

check_num = int(input("Qual numero devo verificar se é primo? "))

lista_divisores = []

if check_num == 1:
    print("Não é um numero primo.")
elif check_num == 2:
    print("É um numero primo.")
else:
    for num in range(2, check_num, 1):
        if check_num % num == 0:
            lista_divisores.append(num)

    if len(lista_divisores) == 0:
        print("É um numero primo")
    else:
        print("Não é um numero primo")