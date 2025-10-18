def menu(* opcoes):
    # Exibir as opções de escolha.
    for i, o in enumerate(opcoes):
        print(f'{i + 1}. {o}')
    print('-' * 50)
    # Usúario irá escolher a opção que deseja. Caso seja um valor menor que 1 ou maior que 4, será exibido uma mensagem de erro. Caso tudo ocorra de maneira correta, o valor será retornado.
    while True:
        esc = leiaInt('Digite uma opção: ')
        if esc < 1 or esc > 4:
            print('ERRO! Opção Inválida')
            print('-' * 50)
        else:
            return esc


def leiaInt(msg):
    # Ler um número inteiro. Caso não seja, será exibido uma mensagem de erro, caso seja, ele será retornado.
    # Loop infinito.
    while True:
        try:
            n = int(input(msg))
        except:
            print('ERRO! Opção Inválida')
            print('-' * 50)
        else:
            if n < 1:
                print('ERRO! Opção Inválida')
                print('-' * 50)
            else:
                return n


def leiaFloat(msg):
    # Ler um número de ponto flutuante. Será usado para as notas.
    # Loop infinito.
    while True:
        try:
            num = float(input(f'{msg} nota: '))
        except:
            # Caso não seja um valor de ponto flutuante, será exibido uma mensagem de erro.
            print('ERRO! Por favor digite um valor válido')
            print('-' * 50)
        else:
            # Caso seja um valor diferente de 10, será feito uma verificação.
            if num != 10:
                # Verifica se o valor digitado possui mais de 2 caracteres ou se ele é menor que 0 ou maior que 10. Caso algumas dessas alternativas ocorra, uma mensagem de erro será exibida.
                if len(str(f'{num}').replace('.', '')) > 2 or num < 0 or num > 10:
                    print('ERRO! Por favor digite um valor válido')
                    print('-' * 50)
                else:
                    # Caso nenhumas das alternativas ocorra, será exibido uma mensagem que o cadastro foi concluido.
                    print(f'{msg} nota cadastrada!!!'.upper())
                    print('-' * 50)
                    # O valor será retornado com apenas uma casa decimal
                    return float(f'{num:.1f}')
            else:
                # Caso seja o número 10, será exibido uma mensagem que o cadastro foi concluido.
                print(f'{msg} nota cadastrada!!!'.upper())
                print('-' * 50)
                # O valor será retornado com apenas uma casa decimal
                return float(f'{num:.1f}')


def leiaStr(msg):
    # Loop infinito
    while True:
        # Aqui irá ler uma string. Caso todos os valores não sejam uma letra do alfabeto, será exibido uma mensagem de erro, caso todos sejam, será exibido uma mensagem que o cadastro foi concluido e o valor digitado será retornado.
        nome = str(input(msg).strip())
        if ''.join(nome.split()).isalpha():
            print(f'AlUNO CADASTRADO!!!')
            print('-' * 50)
            return nome
        else:
            print('ERRO! Nome do aluno inválido.')
            print('-' * 50)


def validacao(media):
    # Irá verificar a média do aluno e depois irá retornar a situação dele.
    if media >= 7:
        return 'APROVADO'
    elif media >= 5 and media < 7:
        return 'RECUPERAÇÃO'
    else:
        return 'REPROVADO'


def arquivo(info):
    # Aqui será criado e escrito o arquivo que iremos usar pra tudo no código.
    import json
    # Salva as informações em uma lista maior, para que no futuro possamos usar os indices.
    lista_maior = []
    lista_maior.append(info)
    # Criar o arquivo, caso ele não exista ainda. E coloca a PRIMEIRA informação dentro do arquivo json.
    try:
        with open('alunos.json', 'x', encoding='utf-8') as arquivo:
            json.dump(lista_maior, arquivo, indent=4, ensure_ascii=False)
    # Caso o arquivo já exista, esse bloco de comando será acionado.
    except:
        # Ler o arquivo json e depois transformar ele em um objeto python.
        with open('alunos.json', 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            # Pegamos o objeto e colamos a nova informação dentro dele.
            dados.append(info)
            # Aqui reescrevermos o arquivo inteiro com as novas informações.
        with open('alunos.json', 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
    print('CADASTRO CONCLUÍDO!!!'.center(50))


def exibir():
    # Biblioteca json.
    import json
    # Loop infinito.
    while True:
        aluno_esc = 0
        res = ''
        i = 0
        # O arquivo json já precisa existir. Irá ler o arquivo json e depois transformar ele em um objeto python.
        try:
            with open('alunos.json', 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)
        # Caso não exista o arquivo json esse bloco de comando será acionado.
        except:
            print('NENHUM ALUNO CADASTRADO!!!'.center(50))
        else:
            # Caso não exista nenhum registro esse bloco de comando será acionado.
            if len(dados) == 0:
                print('NENHUM ALUNO CADASTRADO!!!'.center(50))
                break
            # Será exibido todos os cadastros feitos.
            print('ALUNOS CADASTRADOS'.center(50))
            print('-' * 50)
            for dados_alunos in dados:
                for alunos in dados_alunos:
                    for k, v in alunos.items():
                        if k in 'Nome':
                            i += 1
                            print(f'{i} - {v}')
            print('-' * 50)
            # Loop que só termina caso seja um número menor que 0 ou maior que a quantidade de pessoas cadastradas.
            while aluno_esc < 1 or aluno_esc > len(dados):
                # Irá ser perguntado de qual aluno o usúario deseja ver as informações.
                aluno_esc = leiaInt(
                    'Qual aluno você deseja ver as informações: ')
                # Caso seja um número menor que 0 ou maior que a quantidade de pessoas cadastradas, será exibido uma mensagem de erro.
                if aluno_esc < 1 or aluno_esc > len(dados):
                    print('ERRO! Opção Inválida')
                    print('-' * 50)
            else:
                # Exibirá as informações do aluno selecionado.
                print('-' * 50)
                for indice_aluno, aluno in enumerate(dados):
                    if indice_aluno == aluno_esc - 1:
                        for alu in aluno:
                            for c, a in alu.items():
                                if c in 'Notas':
                                    for s, n in enumerate(a):
                                        print(f'{s + 1}° bimestre: {n}')
                                else:
                                    print(f'{c}: {a}')
                # Pergunta se o usúario quer continuar, se sim, o programa continuar, se não, ele terminá.
            while res not in ('S', 'N'):
                print('-' * 50)
                res = str(input('Quer continuar (S/N)? ').strip().upper())
                if res not in ('S', 'N'):
                    print('ERRO! Opção Inválida')
            if res in 'N':
                break
            else:
                print('-' * 50)


def excluir():
    # Biblioteca json.
    import json
    # Loop infinito.
    while True:
        excluir_aluno = 0
        res = ''
        i = 0
        # O arquivo json já precisa existir. Irá ler o arquivo json e depois transformar ele em um objeto python.
        try:
            with open('alunos.json', 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)
        # Caso não exista o arquivo json esse bloco de comando será acionado.
        except:
            print('NENHUM ALUNO CADASTRADO!!!'.center(50))
            break
        else:
            # Caso não exista nenhum registro esse bloco de comando será acionado.
            if len(dados) == 0:
                print('NENHUM ALUNO CADASTRADO!!!'.center(50))
                break
            # Será exibido todos os cadastros feitos.
            print('ALUNOS CADASTRADOS'.center(50))
            print('-' * 50)
            for dados_alunos in dados:
                for alunos in dados_alunos:
                    for k, v in alunos.items():
                        if k in 'Nome':
                            i += 1
                            print(f'{i} - {v}')
            print('-' * 50)
            # Loop que só termina caso seja um número menor que 0 ou maior que a quantidade de pessoas cadastradas.
            while excluir_aluno < 1 or excluir_aluno > len(dados):
                # Irá ser perguntado de qual aluno o usúario deseja remover.
                excluir_aluno = leiaInt('Qual aluno você deseja excluir: ')
                # Caso seja um número menor que 0 ou maior que a quantidade de pessoas cadastradas, será exibido uma mensagem de erro.
                if excluir_aluno < 1 or excluir_aluno > len(dados):
                    print('ERRO! Opção Inválida')
                    print('-' * 50)
            else:
                # Irá percorrer todos os indices e deletar o escolhido pelo usuário.
                for i, alunos in enumerate(dados):
                    if i == excluir_aluno - 1:
                        for nome_do_aluno in alunos:
                            # Exibe o nome do aluno apagado.
                            print(
                                f'ALUNO "{nome_do_aluno['Nome']}" EXCLUÍDO.'.upper())
                        # O aluno é removido, e depois o arquivo é reescrito já sem o aluno que foi apagado anteriormente.
                        del dados[i]
                        with open('alunos.json', 'w', encoding='utf-8') as arquivo:
                            json.dump(dados, arquivo, indent=4,
                                      ensure_ascii=False)
                # Pergunta se o usúario quer continuar, se sim, o programa continuar, se não, ele terminá.
                while res not in ('S', 'N'):
                    print('-' * 50)
                    res = str(input('Quer continuar (S/N)? ').strip().upper())
                    if res not in ('S', 'N'):
                        print('ERRO! Opção Inválida')
                if res in 'N':
                    break
                else:
                    print('-' * 50)
