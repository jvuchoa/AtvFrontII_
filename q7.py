fibonacci = []

n = int(input("Insira o valor máximo da sequência de Fibonacci: "))

if n > 0:
 fibonacci.append(0)
if n > 1:
 fibonacci.append(1)

while True:
 ultimo_elemento = fibonacci[-1]
 penultimo_elemento = fibonacci[-2]
 proximo_elemento = ultimo_elemento + penultimo_elemento
 if proximo_elemento <= n:
    fibonacci.append(proximo_elemento)
 else:
    break
print(fibonacci)