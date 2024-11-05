def iniciar_jogo():
    print("Terra do Bug")
    opcao = int(input("\n1- Novo jogo \n2- Instruções \n3- Sair \nOpção: "))
    
    match opcao:
        case 1:
            return novojogo()
        case 2:
            return instrucoes()
        case 3:
            return
        case _:
            print("Opção Invalida!")
            iniciar_jogo()
            
def instrucoes():
    print("-a---------Instruções----------")
    print("O jogo funcionara com os seguintes comando")
    print("O jogo tera escolha por numeros")
    
    opcao = int(input("\n1- Sair \nOpção: "))
    
    match opcao:
        case 1:
            return iniciar_jogo()
        case _:
            print("Opção Invalida!")
            instrucoes()
            
def novojogo():
    print("Bem vindo a Terra do Bug!") 
    print("Voce é uma pessoa que procura por uma aventura pelo mundo sendo um heroi, vc pega suas coisas e vai pelo mundo a fora, oque o destino escolhera ao seu personagem?\n")
    
    print("Escolha um personagem: ")
    print("Cada personagem seu atributos unicos \nCombate, Armas, Habilidade, \nForça, Agilidade, Inteligência\n")
    opcao = str(input("1- ⚔️ㅤGuerreiro \n2- 🧙 Mago \n3- 🏹 Arqueiro \n4- Voltar \nOpção:"))
    
    if opcao == 1:
        nome = str(input("Digite o nome do seu personagem: "))
        idade = int(input("Digite a idade do seu personagem:"))
    elif opcao == 2:
        nome = str(input("Digite o nome do seu personagem: "))
        idade = int(input("Digite a idade do seu personagem:"))
    elif opcao == 3:
        nome = str(input("Digite o nome do seu personagem: "))
        idade = int(input("Digite a idade do seu personagem:"))
    elif opcao == 4:
        iniciar_jogo() 
    else:
        print("Opção Invalida!")
        novojogo()
            
print(iniciar_jogo())