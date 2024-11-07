import os
import time
import random

personagem = {}
conseguencia = False

# Estrutura dos monstros
monstros = {
    "monstroInicial": {
        "Nome": "Globin",
        "Classe": "🧌ﾠﾠGlobin:",
        "Vida": 10,
        "Dano": 4,
        "Sorte": 2,
    },
    "Esqueleto": {
        "Nome": "Esquelo",
        "Vida": 25,
        "Dano": 7,
        "Sorte": 5,
    },
}

def coletar_item(item, valor): 
    personagem["Mochila"][item] = valor
    print(f"Você coletou um(a) {item}. Seu inventário agora: {personagem['Mochila']}")

def clear():
    if os.name == 'nt': 
        os.system('cls')
    else: 
        os.system('clear')

def recompensa(): 
    global personagem
    
    ganhoMoeda = random.randint(1, 8)
    ganhoXP = random.randint(1, 4)
    
    personagem['Atributos']['Moeda'] += ganhoMoeda
    personagem['Atributos']['XP'] += ganhoXP
    
def iniciarJogo():
    clear()
    
    print("Terra do Bug")
    opcao = int(input("\n1- Novo jogo \n2- Instruções \n3- Sair \nOpção: "))
    
    match opcao:
        case 1:
            return novoJogo()
        case 2:
            return instrucoes()
        case 3:
            return
        case _:
            print("Opção Invalida!")
            time.sleep(1) 
            iniciarJogo()
            
def instrucoes():
    clear()
    
    print("----------Instruções----------")
    print("Os comandos do jogo são simples!")
    print("Digite o numero da opção no terminal para continuar o jogo.")
    print("O jogo será baseado em turnos. Durante um turno, você atacará e no outro seu inimigo atacará.")
    print("Cada classe virá com níveis de atributos diferentes.")
    print("Escolha com cuidado!!")
   
    opcao = int(input("\n1- Sair \nOpção: "))
    
    match opcao:
        case 1:
            return iniciarJogo()
        case _:
            print("Opção Invalida!")
            time.sleep(1) 
            instrucoes()
            
def novoJogo():
    global personagem
    
    clear()
    
    print("Bem-vindo a Terra do Bug!") 
    print("Se você está procurando uma aventura perigosa, com desafios difíceis, você está no lugar certo!\n")
    time.sleep(1) 
    print("Dê vida ao seu herói: ")
    nome = str(input("Digite o nome do seu herói: "))
    idade = int(input("Digite a idade do seu herói: "))
    
    print("\nEscolha uma classe:")
    
    opcao = int(input("1- ⚔️ﾠﾠGuerreiro \n2- 🧙ﾠMago \n3- 🏹ﾠArqueiro \n4- Voltar \nOpção: "))
    
    match opcao:
        case 1: 
            clear()
            personagem = {
                "Nome": nome,
                "Idade": idade,
                "Classe": "⚔️ﾠﾠGuerreiro",
                "Atributos": {
                    "Vida": 100,
                    "Dano": 7,
                    "Sorte": 3,
                    "XP": 0,
                    "Moeda": 0,
                },
                "Mochila": {
                    "Cura": 2,
                    "Mana": 1,
                    "Sorte": 0,
                },
                "Habilidades": ["Ataque Brutal", "Escudo de Ferro"]
            }
            escolha()
        
        case 2:
            clear()
            personagem = {
                "Nome": nome,
                "Idade": idade,
                "Classe": "🧙ﾠMago",
                "Atributos": {
                    "Vida": 100,
                    "Dano": 4,
                    "Sorte": 4,
                    "XP": 0,
                    "Moeda": 0,
                },
                "Mochila": {
                    "Cura": 2,      
                    "Mana": 3,   
                    "Sorte": 0,     
                },
                "Habilidades": ["Bola de Fogo", "Relâmpago em Cadeia"]
            }
            escolha()
            
        case 3:
            clear()
            personagem = {
                "Nome": nome,
                "Idade": idade,
                "Classe": "🏹ﾠArqueiro",
                "Atributos": {
                    "Vida": 125,
                    "Dano": 2,
                    "Sorte": 7,
                    "XP": 0,
                    "Moeda": 0,
                },
                "Mochila": {
                    "Cura": 2,
                    "Mana": 1,
                    "Sorte": 0,
                },
                "Habilidades": ["Tiro Preciso", "Camuflagem"]
            }
            escolha()
            
        case 4:
            iniciarJogo() 
        case _:
            print("Opção Inválida!")
            time.sleep(1) 
            clear()
            novoJogo()
            
def escolha():
    global personagem
    
    print(f"\nVocê escolheu a classe: {personagem['Classe']}")
    print(f"Atributos: {personagem['Atributos']}")
    print(f"Habilidades: {personagem['Habilidades']}")
    
    opcao = int(input("\nVocê tem certeza? \n1- Sim \n2- Voltar \nOpção: "))
    match opcao:
        case 1:
            partida()
        case 2:
            novoJogo()
        case _:
            print("Opção Inválida!")
            time.sleep(1) 
            clear()
            escolha()

def partida():
    global personagem
    global conseguencia
    
    clear()
    
    print(f"{personagem['Nome']} sai em sua primeira jornada para se tornar um grande herói!")
    print(f"Durante sua caminhada, {personagem['Nome']} escuta gritos dentro da floresta")
    time.sleep(2) 
    
    opcao = int(input("Você deseja: \n1- Investigar \n2- Ir embora \nOpção: "))
    clear()
    
    match opcao:
        case 1:
            tutorial()
        case 2: 
            print("Você fugiu. Consequências virão no futuro.")
            personagem['Atributos']['Sorte'] -= 2
            conseguencia = True
            time.sleep(2) 
            clear()
            exploracao()
        case _:
            print("Opção Inválida!")
            time.sleep(1) 
            clear()
            partida()
    
def tutorial():
    global personagem
    global monstros
    
    clear()
    
    print(f"Voce ve um {monstros['monstroInicial']['Nome']} atancando pessoas dentro da floresta")
    print("Se prepare pela primeira batalha!")
    while personagem['Atributos']['Vida'] > 0 and monstros['monstroInicial']['Vida'] > 0:
        print(f"\n{monstros['monstroInicial']['Classe']} \n❤️ﾠﾠVida: {monstros['monstroInicial']['Vida']} \n⚔️ﾠﾠDano: {monstros['monstroInicial']['Dano']}\n")
        opcao = int(input("Deseja: \n1- Atacar \n2- Usar Mochila \nOpção: "))
        
        match opcao:
            case 1:
                clear()
                
                chance = random.randint(1, 3)
                ganhoMoeda = random.randint(1, 8)
                ganhoXP = random.randint(1, 4)
                
                if personagem['Atributos']['Sorte'] >= chance:
                    monstros['monstroInicial']['Vida'] -= personagem['Atributos']["Dano"]
                    print(f"{monstros['monstroInicial']['Nome']} está com {monstros['monstroInicial']['Vida']} de vida.")
                    
                    if personagem['Atributos']['Vida'] <= 0 or monstros['monstroInicial']['Vida'] <= 0:
                        personagem['Atributos']['Moeda'] += ganhoMoeda
                        personagem['Atributos']['XP'] += ganhoXP
                        
                        print(f"Você derrotou o {monstros['monstroInicial']['Nome']}! \nRecompensas: \n💰ﾠR$: {ganhoMoeda} \n✨ﾠXP: {ganhoXP}")
                        break
                    else:
                        print(f"Agora é o turno de {monstros['monstroInicial']['Nome']}.")
                        
                        if monstros['monstroInicial']['Sorte'] >= chance:
                            personagem['Atributos']['Vida'] -= monstros['monstroInicial']['Dano']
                            print(f"Você está com {personagem['Atributos']['Vida']} de vida.")
                        else:
                            print(f"{monstros['monstroInicial']['Nome']} errou o ataque.")
                else:
                    print("Você errou o ataque.")
                    
                    print(f"Agora é o turno de {monstros['monstroInicial']['Nome']}.")
                        
                    if monstros['monstroInicial']['Sorte'] >= chance:
                        personagem['Atributos']['Vida'] -= monstros['monstroInicial']['Dano']
                        print(f"Você está com {personagem['Atributos']['Vida']} de vida.")
                    else:
                        print(f"{monstros['monstroInicial']['Nome']} errou o ataque.")
                continue
            case 2:
                clear()
                chance = random.randint(1, 3)
                ganhoMoeda = random.randint(1, 10)
                ganhoXP = random.randint(1, 5)
                
                print(personagem['Mochila'])
                
                print("Digite o nome do item que deseja usar")
                opcao = str(input("Deseja usar algum item? \nOpção: "))
                
                if opcao in personagem['Mochila']:
                    if personagem['Mochila'][opcao] == 0:
                        print("Vc n tem mais esse item")
                    else:
                        personagem['Mochila'][opcao] -= 1
                        print(f"Agora é o turno de {monstros['monstroInicial']['Nome']}.")
                        
                        if monstros['monstroInicial']['Sorte'] >= chance:
                            personagem['Atributos']['Vida'] -= monstros['monstroInicial']['Dano']
                            print(f"Você está com {personagem['Atributos']['Vida']} de vida.")
                        else:
                            print(f"{monstros['monstroInicial']['Nome']} errou o ataque.")
                else:
                    print("Item não encontrado")
    print(f"\nObrigado por salvar nossas vidas, pegue esse Moeda como recompensa")
    personagem['Atributos']['Moeda'] += ganhoMoeda + 2
    print(f"💰ﾠR$: {personagem['Atributos']['Moeda']}")
    time.sleep(5) 
    exploracao()
    
def caverna():
    global personagem
    clear()
    
    print("Caverna foda")
    inimigo = random.choice(list(monstros.keys()))
    print(f"Você encontrou um {monstros[inimigo]['Nome']}!")
    time.sleep(5) 
    exploracao()  
    
def mercador():
    global personagem
    clear()
    
    while True:
        print("Bem vindo ao mercado!")
        print("Oque gostaria de comprar?")
        opcao = int(input("1- Poção de cura \n2-Poção de mana \n3- Poção de sorte \n4- Sair: "))
        
        match opcao:
            case 1:
                print()
            case 2:
                print()
            case 3:
                print()
            case 4:
                vila()
            case _:
                print("Opção Inválida!")
                time.sleep(1)
                clear()   

def motel():
    global personagem
    clear()
    
    print("Bem vindo ao motel!")
    print("Gostaria de passar uma noite?")
    print("Uma noite custa R$ 10 moeda")
    opcao = int(input("1- Sim \n2- Sair \n3- Opção: "))
    
    match opcao:
        case 1:
            if personagem['Atributos']['Moeda'] < 10:
                clear()
                print("Voce não tem moeda suficiente")
                print("Caia fora do meu motel!")
                time.sleep(3)
                vila()
            else:
                clear()
                personagem['Atributos']['Moeda'] -= 10 
                personagem['Atributos']['Vida'] + 200
                print(f"Vc ainda tem R$: {personagem['Atributos']['Moeda']}")
                print(f"Sua vida esta recuperada {personagem['Atributos']['Vida']}")
                time.sleep(5)
        case 2:
            vila()
        case _:
            print("Opção Inválida!")
            time.sleep(1)
            motel()

def vila():
    clear()
    print("Você chegou a vila")
    print("Voce pode visitar lugares pra recuperar vida e mercadores pra comprar poções")
    opcao = int(input("1- Motel \n2- Mercador \n3- Opção: "))
    
    match opcao:
        case 1:
            motel()
        case 2:
            mercador()
        case _:
            print("Opção Inválida!")
            time.sleep(1)
            vila()

def exploracao():
    global personagem
    
    while True:
        clear()
        caminho = random.randint(1, 25)
        if caminho <= 13:
            
            print("Qual caminho devo seguir: ")
            opcao = int(input("1- Seguir estrada \nOpção: "))
            match opcao:
                case 1:
                    pass  
                case _:
                    print("Opção Inválida!")
                    time.sleep(1)
                    
        elif caminho >= 14 and caminho < 17:
            
            print("Qual caminho devo seguir: ")
            opcao = int(input("1- Seguir estrada \n2- Seguir caverna \nOpção: "))
            match opcao:
                case 1:
                    pass  
                case 2:
                    caverna()  
                case _:
                    print("Opção Inválida!")
                    time.sleep(1)
                    
        elif caminho >= 17 and caminho < 22:
            
            print("Qual caminho devo seguir: ")
            opcao = int(input("1- Seguir estrada \n2- Seguir vila \nOpção: "))
            match opcao:
                case 1:
                    pass
                case 2:
                    vila() 
                case _:
                    print("Opção Inválida!")
                    time.sleep(1)
                    
        elif caminho >= 23:
            print("Você encontrou um item no chão!")
            time.sleep(5)
            
            
print(iniciarJogo())