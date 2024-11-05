# Escrevendo um programa que calcule a área de um quadrado

# Etapas do programa
# 1. Perguntar qual o comprimento da base do quadrado?
# 2. Armazennar o comprimento da base em uma variável
# 3. Perguntar qual a altura do quadrado?
# 4. Armazenar a altura do quadrado em uma variavel
# 5. Cacular a área do quadrado multiplicando base * altura
# 6. Armazenar o resultado do calculo em uma variavel
# 7. Printar o resultado

base = int(input("Qual o comprimento da base do quadrado? "))
altura = int(input("Qual a altura do quadrado? "))

area_quadrado = base * altura

print("A area do quadrado com base de", base, "e altura de", altura, "é igual a", area_quadrado)