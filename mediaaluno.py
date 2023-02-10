alunos = []

mediaf = 0


ap = 0


rp = 0


mediat = 0

for i in range(1, 7):
    nome = input('Digite o nome do Aluno:')
    n1 = int(input('Nota da 1ª Prova:'))
    n2 = int(input('Nota da 2ªProva:'))
    media = (n1+n2)/2
    alunos.append([nome, [n1],[n2], media])
    if media >= 6:
            ap += 1
            print("A media é: ", media)
            alunos.append('aprovado')
            mediaf += media
    else:
            rp += 1
            print("A media é: ", media)
            alunos.append('reprovado')
            mediaf += media


print(alunos)

mediat = mediaf / 6

alrp = (rp * 100) / 6

alap = (ap * 100) / 6

alunost = 6 // 6 * 100

print("**RELATÓRIO**")

print("A media da classe é: ", round(mediat, 2))

print("Percentual de: ", round(alap, 2), "% aprovados!")

print("Percentual de: ", alunost," % alunos de exame")

print("Percentual de: ", round(alrp, 2), "% reprovados!")