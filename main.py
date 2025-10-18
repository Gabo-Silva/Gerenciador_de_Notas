# Importando minhas funções
import notas
# Loop infinito
while True:
    # Dicionário com as informações do aluno.
    aluno = {}
    # Lista menor que guardará as informações do aluno.
    lista_menor = []
    # Lista com as quatro notas do aluno.
    aluno_notas = []
    # Menu
    print('-' * 50)
    print('GERENCIADOR DE NOTAS'.center(50))
    print('-' * 50)
    usu_res = notas.menu('Adicionar aluno', 'Exibir Alunos',
                         'Excluir aluno', 'Sair')
    print('-' * 50)
    # Dependedo da escolha do usuário um bloco de comando será ativado.
    if usu_res == 1:
        # Aqui será recolhido as informações do aluno.
        aluno['Nome'] = notas.leiaStr('Nome do aluno: ')
        aluno_notas.append(notas.leiaFloat('Primeira'))
        aluno_notas.append(notas.leiaFloat('Segunda'))
        aluno_notas.append(notas.leiaFloat('Terceira'))
        aluno_notas.append(notas.leiaFloat('Quarta'))
        aluno['Notas'] = aluno_notas
        aluno['Média'] = round(sum(aluno_notas) / 4, 1)
        aluno['Situação'] = notas.validacao(aluno['Média'])
        lista_menor.append(aluno)
        notas.arquivo(lista_menor)
    if usu_res == 2:
        notas.exibir()
    elif usu_res == 3:
        notas.excluir()
    elif usu_res == 4:
        # Para o loop infinito.
        break
    # Limpa as duas listas, para que não fique acumulando informações.
    lista_menor.clear()
    aluno_notas.clear()
# Fim
print('OBRIGADO POR USAR O MEU GERENCIADOR DE NOTAS'.center(50))
print('-' * 50)
