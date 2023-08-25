def filtrar_nomes_a(lista_nomes):
    nomes_com_a = [nome for nome in lista_nomes if nome.startswith('A') or nome.startswith('a')]
    return nomes_com_a


entrada = input("Digite a lista de nomes separados por espaços: ")
nomes = entrada.split()

nomes_iniciados_com_a = filtrar_nomes_a(nomes)

print("Nomes que começam com a letra 'A':", nomes_iniciados_com_a)