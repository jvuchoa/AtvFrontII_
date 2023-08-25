def calcular_media_pares(lista):       #FUNÇAO PARA CALCULAR A MEDIA DOS NUMEROS PARES
    numeros_pares = [num for num in lista if num % 2 == 0]
    
    if not numeros_pares:  
        return 0
    
    soma_pares = sum(numeros_pares)   #FUNÇÃO PARA SOMAR OS NUMEROS DA LISTA
    media_pares = soma_pares / len(numeros_pares) #DIVIDINDO O VALOR DA SOMA PELA QUANT DE NUM PARES 
    return media_pares

# Lê a lista de números do usuário
entrada = input("Digite a lista de números separados por espaços: ")
numeros = [int(num) for num in entrada.split()]  #SPLIT VAI SERVIR PARA SEPARAR UMA STRING 

media = calcular_media_pares(numeros)  

print(f"A média dos números pares é: {media:.2f}")  