def verifica_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Solicita ao usuário um número
numero = int(input("Digite um número: "))

# Verifica se o número é primo ou não
if verifica_primo(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")