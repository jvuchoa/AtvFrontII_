def encontre_maior_menor(lista):
 maior = lista[0]
 menor = lista[0]

 for num in lista:
    if num > maior:
        maior = num
    if num < menor:
        menor = num
 return (maior, menor)

numeros = input("Digite uma lista de números separados por vírgula: ")
numeros = [int(num) for num in numeros.split(",")]
maior, menor = encontre_maior_menor(numeros)
print(f"O maior número da lista é: {maior}")
print(f"O menor número da lista é: {menor}")