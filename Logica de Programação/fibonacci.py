#Desenvolvendo um algoritmo que escreve uma lista con todos os nuneros da sequencia de fibonacci ate 100
#Na matematica, a sucesseção de fibonnaci, é uma sequencia de numeros inteiros, comceçando normalmente por 0 e 1, na qual cada termo subsequente corresponde a soma dos dois anteriores.

#Exemplo : 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...

# Etapas
# 1. Inicializar uma lista com 0 e 1
# 2. Somar os dois ultimos numeros da lista
# 3. Armazenar esses dois ultimos numeros em uma variavel
# 4. Adicionar essa nova variavel a lista
# 5. Inteirar até chegar a 100

fibonacci = [0,1]

qtd_valores = int(input("Quantos elementos da lista Fibonacci você quer gerar?"))

for num in range(2, qtd_valores, 1):
    ultimo_numero = fibonacci[-1]
    penultimo_numero = fibonacci [-2]
#somo os dois ultimos numeros
    proximo_numero = ultimo_numero + penultimo_numero
#adiciono o valor de proximo_numero ao final da lista
    fibonacci.append(proximo_numero)

#uma colaçãp de itens ordenados
    print("A lista Fibonacci com",qtd_valores, "elementos, é a seguinte", fibonacci)