def resumo():
    mensagem = (
        "Grace Hopper foi uma cientista da computação e contra-almirante da Marinha dos Estados Unidos. "
        "Ela é famosa por seu trabalho pioneiro na criação do primeiro compilador de computador, "
        "além de ajudar a popularizar o conceito de linguagens de programação de alto nível. "
        "Grace Hopper também foi uma das primeiras a desenvolver a linguagem de programação COBOL, "
        "que foi amplamente utilizada em sistemas administrativos e financeiros."
    )
    return mensagem


def doutorado():
    mensagem = (
        "Grace Hopper obteve seu doutorado em matemática pela Universidade de Yale em 1934. "
        "Ela foi uma das poucas mulheres da época a alcançar esse nível de educação em um campo dominado por homens. "
        "Sua tese focou em geometria, e sua formação sólida em matemática foi fundamental para sua futura carreira na computação."
    )
    return mensagem


def contribuicoes():
    mensagem = (
        "Grace Hopper foi uma das pioneiras na ciência da computação. Suas principais contribuições incluem:\n"
        "- Desenvolvimento do primeiro compilador, que traduzia código simbólico para linguagem de máquina.\n"
        "- Criação da linguagem de programação COBOL, uma das primeiras linguagens voltadas para negócios.\n"
        "- Popularização do conceito de linguagens de programação de alto nível, tornando a computação mais acessível.\n"
        "- Introdução da ideia de que computadores devem entender comandos próximos à linguagem humana.\n"
        "- Sua frase 'É mais fácil pedir perdão do que permissão' tornou-se um marco no pensamento inovador."
    )
    return mensagem


def artigos():
    mensagem = (
        "Principais trabalhos de Grace Hopper:\n"
        "- Desenvolvimento do compilador A-0 em 1952, um marco no avanço da programação.\n"
        "- Projeto e padronização da linguagem COBOL, amplamente usada em sistemas administrativos.\n"
        "- Trabalhos publicados sobre linguagens de programação de alto nível e sua aplicabilidade na indústria.\n"
        "- Palestras e artigos sobre a importância de educar e inspirar novas gerações na área de tecnologia."
    )
    return mensagem


def citacoes():
    mensagem = (
        "Citações famosas de Grace Hopper:\n"
        "- 'A coisa mais perigosa é acreditar que você já sabe tudo.'\n"
        "- 'O futuro não é um lugar para o qual estamos indo, é um lugar que estamos criando.'\n"
        "- 'É mais fácil pedir perdão do que permissão.'\n"
        "- 'Os computadores são incríveis, mas precisam ser ensinados.'"
    )
    return mensagem



def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Allan Turing.\n")

continuar = True
while continuar == True:

    opcao = int(
        input(
"""
\nDigite o número correspondente ao menu que você deseja acessar:
1 - Resumo
2 - Doutorado
3 - Contribuições
4 - Principais Artigos
5 - Citações
6 - Sair\n
"""
        )
    )

    if opcao == 1:
        print("1 - Resumo")
        mensagem = resumo()

    elif opcao == 2:
        print("2 - Doutorado")
        mensagem = doutorado()

    elif opcao == 3:
        print("3 - Contribuições")
        mensagem = contribuicoes()

    elif opcao == 4:
        print("4 - Principais Artigos")
        mensagem = artigos()

    elif opcao == 5:
        print("5 - Citações")
        mensagem = citacoes()

    elif opcao == 6:
        mensagem = sair()
        continuar = False

    else:
        mensagem = erro()

    print(mensagem)
