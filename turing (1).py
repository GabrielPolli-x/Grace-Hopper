def resumo():
    mensagem = ""Grace Hopper foi uma cientista da computação e contra-almirante da Marinha dos Estados Unidos. 
    Ela é famosa por seu trabalho pioneiro na criação do primeiro compilador de computador, 
    além de ajudar a popularizar o conceito de linguagens de programação de alto nível.

    Grace Hopper também foi uma das primeiras a desenvolver a linguagem de programação COBOL, 
    que foi amplamente utilizada em sistemas administrativos e financeiros.

    Ela recebeu diversos prêmios ao longo de sua carreira, incluindo a Medalha Nacional de Tecnologia 
    e Inovação, e foi uma das primeiras mulheres a alcançar o posto de contra-almirante na Marinha dos EUA.
    ""
    return mensagem


def doutorado():
    mensagem = ""
    return mensagem


def contribuicoes():
    mensagem = "As contribuições de Grace Hopper para a Ciência da Computação incluem:

    1. Criou o primeiro compilador de computador em 1952, o A-0 System, 
       permitindo que os programadores escrevessem código mais facilmente.
    2. Trabalhou na popularização das linguagens de programação de alto nível, 
       contribuindo diretamente para a criação da linguagem COBOL, uma das primeiras linguagens voltadas para negócios.
    3. Defendeu a ideia de que os computadores devem ser capazes de entender comandos em uma linguagem próxima à humana.
    4. Sua famosa citação: 'É melhor pedir desculpas do que pedir permissão' inspirou muitas gerações de inovadores.
   "
    return mensagem


def artigos():
    mensagem = ""
    return mensagem


def citacoes():
    mensagem = "Algumas citações famosas de Grace Hopper incluem:
    
    - 'A coisa mais perigosa é acreditar que você já sabe tudo.'
    - 'O futuro não é um lugar para o qual estamos indo, é um lugar que estamos criando.'
    - 'É melhor pedir desculpas do que pedir permissão.'"
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\Boa noite! Você está aprendendo sobre Allan Turing.\n")

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
