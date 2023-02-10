produtos = []


nomesp = []


superior = 0


inferior = 0


sp = 0


mp = 0


media = 0


for i in range(1,6):
    nome = (str(input('Digite o nome do Produto -> ')))
    valor = (float(input('Valor R$:')))
    produtos.append([nome,valor])
    if valor <= 50.00:
        inferior += 1
    elif valor >= 50.00 and valor <= 100:
        superior += 1
        nomesp.append(nome)

    else:
        sp += 1
        mp += valor
        media = mp // sp



print("**RELATORIO**")
print(produtos)
print("Quantidades de produto preço inferior a R$50,00: ", inferior)
print("Nome dos produtos com preço entre 50 e 100 reais: ", nomesp)
print("A media dos preços dos produtos superior a 100 reais: ", media)

