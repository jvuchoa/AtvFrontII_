numero = int(input("Informe um número inteiro positivo: "))

# Verifica se o número é positivo
if numero < 0:
    print("Número inválido! O número deve ser positivo.")
else:
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i

    print("O fatorial de", numero, "é", fatorial)