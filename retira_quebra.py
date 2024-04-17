def retira_quebra_linha(original, sem_quebra):
    with open(original, 'r', encoding='utf8') as arquivo:
        conteudo = arquivo.read().replace('\n\n', ' ')
    
    with open(sem_quebra, 'w', encoding='utf8') as arquivo:
        arquivo.write(conteudo)

retira_quebra_linha('2_Sessao_Extraordinaria.txt', '2_sessao_ordinaria_sem_quebra.txt')

