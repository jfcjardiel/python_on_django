List = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom']
#Essa será a lista com todas as combinações de dias de semana
combinacao = []
combinacao_for = []

for dia in List:
    combinacao.append(dia)
    combinacao_for = []
    combinacao_for.extend(combinacao)
    for comb in combinacao_for:
        if comb != dia:
            combinacao.append(comb+dia)

combinacao_for = sorted(combinacao, key=len)
combinacao = combinacao_for

print(combinacao)
print(len(combinacao))