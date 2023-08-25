executar="S"
while(executar=='S'):
    num=int(input("Digite um numero: "))
    if num%2==0:
        print("PAR")
    else:
        print("IMPAR")
executar=str.lower("Deseja digitar outro numero? \nS \n N")