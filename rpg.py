import os
import time
import random

personagem = {}
inimigo = {}
conseguencia = False

Armas_Gue = {
    "Berserk": {
        "Classe": "Espadas Grandes",
        "Nome": "Berserk Sword",
        "Dano": 10,
    },
    "Katana": {
        "Classe": "Espadas Longas",
        "Nome": "Katana de aço",
        "Dano": 6,
    },
    "Moonlight": {
        "Classe": "Espadas Grandes",
        "Nome": "Lamina da Lua",
        "Dano": 33,
    },
    "Rapieira": {
        "Classe": "Espadas Longas",
        "Nome": "Rapieira",
        "Dano": 5,
    },
    "Espada normal": {
        "Classe": "Espadas Normais",
        "Nome": "Espada de ferro",    
        "Dano": 6,
    },
    "Adaga": {
        "Classe": "Adagas",
        "Nome": "Adagas de ferro",
        "Dano": 3,
    }
}

Armas_Mago = {
    "Cajado Comum": {
        "Classe": "Cajado",
        "Nome": "Cajado Magico",
        "Dano": 4,
    },
    "Cajado raro": {
        "Classe": "Cajado raro",
        "Nome": "Cajado de Fogo",
        "Dano": 6,
    },
    "Cajado épico": {
        "Classe": "Cajado épico",
        "Nome": "Cajado Pedrilhante",
        "Dano": 26,
    },
    "Cajado Comum2": {
        "Classe": "Cajado",
        "Nome": "Cajado brilhante",
        "Dano": 3,
    },
    "Cajado raro2": {
        "Classe": "Cajado raro",
        "Nome": "Cajado de Gelo",
        "Dano": 6,
    },
    "Cajado épico2": {
        "Classe": "Cajado épico",
        "Nome": "Cajado lunar",
        "dano": 33,
    },
}

Armas_Arq = {
    "Arco basico": {
        "Classe": "Arco comum",
        "Nome": "Arco basico",
        "Dano": 3,
    },
    "Crossbow": {
        "Classe": "Crossbow",
        "Nome": "Crossbow",
        "Dano": 6,
    },
    "Crossbow Automatica": {
        "Classe": "Crossbow",
        "Nome": "Crossbow Automatica",
        "Dano": 12,
    },
    "Arco basico": {
        "Classe": "Arco comum",
        "Nome": "Arco de Madeira",
        "Dano": 4,
    },
    "Arco épico": {
        "Classe": "Arco épico",
        "Nome": "Artemis",
        "Dano": 23,
    },
    "Arco épico": {
        "Classe": "Arco épico",
        "Nome": "Arco lunar",
        "Dano": 33,
    },
}

monstros = {
    "Goblin": {
        "Classe": "Goblin",
        "Nome": "🧌ﾠﾠGoblin",
        "Vida": 15,
        "VidaInicial": 15,
        "Dano": 4,
        "Sorte": 3,
    },
    "Esqueleto": {
        "Classe": "Esqueleto",
        "Nome": "💀ﾠEsqueleto",
        "Vida": 15,
        "VidaInicial": 15,
        "Dano": 8,
        "Sorte": 2,
    },
    "Fadas": {
        "Classe": "Fada",
        "Nome": "🧚ﾠFada",
        "Vida": 10,
        "VidaInicial": 10,
        "Dano": 3,
        "Sorte": 6,
    },
    "Elfos":  {
        "Classe": "Elfo",
        "Nome": "🧝ﾠElfo",
        "Vida": 20,
        "VidaInicial": 20,
        "Dano": 9,
        "Sorte": 3,
    },
    "Reptiliano": {
        "Classe": "Reptiliano",
        "Nome": "🦎ﾠReptiliano",
        "Vida": 18,
        "VidaInicial": 18,
        "Dano": 8,
        "Sorte": 2,
    },
    "ArmaduraﾠViva": {
        "Classe": "Fantasma",
        "Nome": "🛡ﾠﾠArmaduraﾠViva",
        "Vida": 40,
        "VidaInicial": 40,
        "Dano": 16,
        "Sorte": 1,
    },
    "AlmaﾠPerdida": {
        "Classe": "AlmaﾠPerdida",
        "Nome": "🔥ﾠAlmaﾠPerdida",
        "Vida": 15,
        "VidaInicial": 15,
        "Dano": 8,
        "Sorte": 2,
    },
    "Ogro": {
        "Classe": "Ogro",
        "Nome": "👹ﾠOgro",
        "Vida": 50,
        "VidaInicial": 50,
        "Dano": 12,
        "Sorte": 2,
    },
    "LoboﾠFantasma": {
        "Classe": "Fantasma",
        "Nome": "🐺ﾠLoboﾠFantasma",
        "Vida": 20,
        "VidaInicial": 20,
        "Dano": 6,
        "Sorte": 2,
    },
    "Pessoaﾠdesconhecida": {
        "Classe": "Estranho",
        "Nome": "Estranho",
        "Vida": 25,
        "VidaInicial": 25,
        "Dano": 7,
        "Sorte": 7,
    }
}

def itens():
    clear()
    global personagem
    print("Após derrotar todos os monstros da caverna você")
    
    if personagem["Identificador"] == "Guerreiro":
        armasRandom = random.choice(list(Armas_Gue.keys()))
        print(f"Sua arma atual: {personagem['Mochila']['Armas_Gue']}\n")
        print(f"{personagem['Nome']} encontrou uma {Armas_Gue[armasRandom]['Classe']} \nNome: {Armas_Gue[armasRandom]['Nome']} \nDano: {Armas_Gue[armasRandom]['Dano']}")
        opcao = int(input("Você deseja coletar o item? \n1- Coletar \n2- Não Pegar \nOpção: "))

        match opcao:
            case 1:
                personagem['Mochila']['Armas_Gue'] = {armasRandom: Armas_Gue[armasRandom]}
                print(f"{personagem['Nome']} pegou a {Armas_Gue[armasRandom]} e colocou na mochila.")
            case 2:
                print("Você deixou o item no chão, talvez algum outro aventureiro faça um melhor uso...")
            case _:
                print("Opção Inválida!")
                time.sleep(1)
                itens()
    
    elif personagem["Identificador"] == "Mago":
        armasRandom = random.choice(list(Armas_Mago.keys()))
        print(f"Sua arma atual: {personagem['Mochila']['Armas_Mago']}\n")
        print(f"{personagem['Nome']} encontrou uma {Armas_Mago[armasRandom]['Classe']} \nNome: {Armas_Mago[armasRandom]['Nome']} \nDano: {Armas_Mago[armasRandom]['Dano']}")
        
        opcao = int(input("Você deseja coletar o item? \n1- Coletar \n2- Não Pegar \nOpção: "))

        match opcao:
            case 1:
                personagem['Mochila']['Armas_Mago'] = {armasRandom: Armas_Mago[armasRandom]}
                print(f"{personagem['Nome']} pegou a {Armas_Mago[armasRandom]} e colocou na mochila.")
            case 2:
                print("Você deixou o item no chão, talvez algum outro aventureiro faça um melhor uso...")
            case _:
                print("Opção Inválida!")
                time.sleep(1)
                itens()

    elif personagem["Identificador"] == "Arqueiro":
        armasRandom = random.choice(list(Armas_Arq.keys()))
        print(f"Sua arma atual: {personagem['Mochila']['Armas_Arq']}\n")
        print(f"{personagem['Nome']} encontrou uma {Armas_Arq[armasRandom]['Classe']} \nNome: {Armas_Arq[armasRandom]['Nome']} \nDano: {Armas_Arq[armasRandom]['Dano']}")
        
        opcao = int(input("Você deseja coletar o item? \n1- Coletar \n2- Não Pegar \nOpção: "))

        match opcao:
            case 1:
                personagem['Mochila']['Armas_Arq'] = {armasRandom: Armas_Arq[armasRandom]}
                print(f"{personagem['Nome']} pegou a {Armas_Arq[armasRandom]} e colocou na mochila.")
            case 2:
                print("Você deixou o item no chão, talvez algum outro aventureiro faça um melhor uso...")
            case _:
                print("Opção Inválida!")
                time.sleep(1)
                itens()

def clear():
    if os.name == 'nt': 
        os.system('cls')
    else: 
        os.system('clear')
        
def batalha():
    global personagem
    global monstros

    while personagem['Atributos']['Vida'] > 0 and monstros[inimigo]['Vida'] > 0:
        opcao = int(input("Deseja: \n1- Atacar \n2- Usar Mochila \n3- Fugir \nOpção: "))
        
        match opcao:
            case 1:
                clear()
                
                chance = random.randint(1, 10)
                
                if personagem['Atributos']['Sorte'] >= chance:
                    monstros[inimigo]['Vida'] -= personagem['Atributos']["Dano"]
                    print(f"Você deu -{personagem['Atributos']['Dano']} de dano")
                    print(f"{monstros[inimigo]['Nome']} \n❤ﾠﾠVida: {monstros[inimigo]['Vida']} \n⚔ﾠﾠDano: {monstros[inimigo]['Dano']}\n")
                    
                    if monstros[inimigo]['Vida'] <= 0:
                        recompensa()
                        break
                    else:
                        print(f"\nTurno de {monstros[inimigo]['Classe']}")
                        
                        if monstros[inimigo]['Sorte'] >= chance:
                            personagem['Atributos']['Vida'] -= monstros[inimigo]['Dano']
                            print(f"{monstros[inimigo]['Classe']} deu -{monstros[inimigo]['Dano']} de dano")
                            print(f"{personagem['Classe']} \n❤ﾠﾠ{personagem['Atributos']['Vida']} \n⚔ﾠﾠDano: {personagem['Atributos']['Dano']}\n")
                            
                            if personagem['Atributos']['Vida'] <= 0:
                                playerMorto()
                                break
                        else:
                            print(f"{monstros[inimigo]['Classe']} errou o ataque\n")
                else:
                    chance = random.randint(1, 10)
                    print("Você errou o ataque")\
                    
                    print(f"\nTurno de {monstros[inimigo]['Classe']}")
                        
                    if monstros[inimigo]['Sorte'] >= chance:
                        personagem['Atributos']['Vida'] -= monstros[inimigo]['Dano']
                        print(f"{monstros[inimigo]['Classe']} deu - {monstros[inimigo]['Dano']} de dano")
                        print(f"{personagem['Classe']} \n❤ﾠﾠ{personagem['Atributos']['Vida']} \n⚔ﾠﾠDano: {personagem['Atributos']['Dano']} \n")
                        
                        if personagem['Atributos']['Vida'] <= 0:
                            playerMorto()
                            break
                    else:
                        print(f"{monstros[inimigo]['Classe']} errou o ataque\n")
                continue
            case 2:
                clear()
                chance = random.randint(1, 3)

                print(personagem['Mochila'])
                
                print("Digite o nome do item que deseja usar")
                print("Digite sair caso queira voltar pra batalha")
                opcao = str(input("Deseja usar algum item? \nOpção: ")).capitalize()
                
                if opcao in personagem['Mochila']:
                    if personagem['Mochila'][opcao]['Quantidade'] == 0:
                        print("Vc n tem mais esse item")
                    else:
                        if personagem['Mochila'][opcao] == personagem['Mochila']['Cura']:
                            if personagem['Atributos']['Vida'] <= personagem['VidaInicial']:
                                personagem['Atributos']['Vida'] += personagem['Mochila']['Cura']['Porcentagem']
                                personagem['Mochila'][opcao]['Quantidade'] -= 1
                                if personagem['Atributos']['Vida'] > personagem['VidaInicial']:
                                    personagem['Atributos']['Vida'] == personagem['VidaInicial']
                                    print(f"Vida: {personagem['Atributos']['Vida']} + Cura: {personagem['Mochila']['Cura']['Porcentagem']}")
                                else: 
                                    print(f"Voce usou cura: {personagem['Mochila']['Cura']['Porcentagem']}")
                                    print(f"Vida: {personagem['Atributos']['Vida']}")
                                    
                        elif personagem['Mochila'][opcao] == personagem['Mochila']['Dano']:
                            personagem['Atributos']['Dano'] += personagem['Mochila']['Dano']['Porcentagem']
                            print(f"Voce aumento seu dano para mais: {personagem['Mochila']['Dano']['Porcentagem']}")
                            print(f"Dano: {personagem['Atributos']['Dano']}")
                            
                        elif personagem['Mochila'][opcao] == personagem['Mochila']['Sorte']:
                            personagem['Atributos']['Sorte'] += personagem['Mochila']['Sorte']['Porcentagem']
                            print(f"Voce aumento seu sorte para mais: {personagem['Mochila']['Sorte']['Porcentagem']}")
                            print(f"Sorte: {personagem['Atributos']['Sorte']}")
                        else:
                            print(f"Agora é o turno de {monstros[inimigo]['Nome']}")
                        
                        if monstros[inimigo]['Sorte'] >= chance:
                            personagem['Atributos']['Vida'] -= monstros[inimigo]['Dano']
                            print(f"Você está com {personagem['Atributos']['Vida']} de vida")
                        else:
                            print(f"{monstros[inimigo]['Classe']} errou o ataque")
                elif opcao.capitalize() == "Sair":
                    clear()
                    batalha()
                else:
                    print("Item não encontrado")
            case 3:
                fugir = random.randint(1, 7)
                if 3 >= fugir:
                    print("Voce conseguiu fugir da batalha!")
                    time.sleep(1)
                    clear()
                    exploracao()
                else:
                    chance = random.randint(1, 10)
                    print("Você Não conseguiu fugir")
                    
                    print(f"\nTurno de {monstros[inimigo]['Classe']}")
                        
                    if monstros[inimigo]['Sorte'] >= chance:
                        personagem['Atributos']['Vida'] -= monstros[inimigo]['Dano']
                        print(f"Você está com {personagem['Atributos']['Vida']} de vida")
                        
                        if personagem['Atributos']['Vida'] <= 0:
                            playerMorto()
                            break
                    else:
                        print(f"{monstros[inimigo]['Classe']} errou o ataque")
            case _:
                print("Opção Inválida!")
                time.sleep(1)
                clear()
          
def playerMorto():
    global personagem
    global monstros
    global inimigo
    
    clear()
    
    print("Voce morreu!")
    print(f"Inimigos Mortos: {personagem['Kills']}")
    print(f"Você completou: {personagem['CavernaExplorada']} cavernas. ")
    time.sleep(1)
    print("Deseja reniciar?")
    opcao = int(input("1- Sim \n2- Não \nOpção: "))
    match opcao:
        case 1:
            iniciarJogo()
        case 2:
            clear()
            print("Jogo finalizado!")
            exit()
        case _:
            print("Opção Inválida!")
            time.sleep(1)
            clear()
            playerMorto()

def recompensa(): 
    global personagem
    global monstros
    global inimigo
    
    ganhoMoeda = random.randint(1, 10)
    ganhoXP = random.randint(1, 5)
    
    personagem['Kills'] += 1
    personagem['Moeda'] += ganhoMoeda
    personagem['XP'] += ganhoXP
    
    monstros[inimigo]['Vida'] = monstros[inimigo]['VidaInicial']
    
    print(f"Você derrotou \nRecompensas: \n💰ﾠR$: {ganhoMoeda} \n✨ﾠXP: {ganhoXP} \n☠️ﾠﾠKills: {personagem['Kills']}")
      
def iniciarJogo():
    clear()
    
    print("\033[1mTerra do Bug\033[0m")
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
    
    print("\033[1m----------Instruções----------\033[0m")
    print("Os comandos do jogo são simples!")
    print("Digite um \033[1mnumero\033[0m da opção no terminal para continuar o jogo")
    print("O jogo será baseado em \033[1mturnos\033[0m, durante um turno, você atacará e no outro seu inimigo atacará")
    print("Seu objetivo é explorar \033[1mcavernas\033[0m e \033[1mderrotar 25 inimigos\033[0m para encontrar a \033[1mcaverna final\033[0m, onde vc encontrara seu \033[1mfinal\033[0m")
    print("Cada classe virá com níveis de atributos \033[1mdiferentes\033[0m")
   
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
    
    print("Bem-vindo a \033[1mTerra do Bug\033[0m!") 
    print("Se você está procurando uma aventura perigosa, com desafios difíceis, você está no lugar certo!\n")
    print("Dê \033[1mvida\033[0m ao seu herói: ")
    nome = str(input("Digite o \033[1mnome\033[0m do seu herói: "))
    idade = int(input("Digite a \033[1midade\033[0m do seu herói: "))
    
    print("\nEscolha uma \033[1mclasse\033[0m:")
    
    opcao = int(input("1- ⚔ﾠﾠGuerreiro \n2- 🧙ﾠMago \n3- 🏹ﾠArqueiro \n4- Voltar \nOpção: "))
    
    match opcao:
        case 1: 
            clear()
            personagem = {
                "Nome": nome,
                "Idade": idade,
                "Classe": "⚔ﾠﾠGuerreiro",
                "Identificador": "Guerreiro",
                "Kills": 0,
                "CavernaExplorada": 0,
                "Estamina": 60,
                "XP": 0,
                "Moeda": 0, 
                "VidaInicial": 120,
                "EstaminaInicial": 60,
                "Atributos": {
                    "Vida": 120,
                    "Dano": 6,
                    "Sorte": 4,
                },
                "Mochila": {
                    'Armas_Gue': {
                    },
                    "Cura": {
                        "Quantidade": 3,
                        "Porcentagem": 10,
                    },
                    "Dano": {
                        "Quantidade": 1,
                        "Porcentagem": 1,
                    },
                    "Sorte": {
                        "Quantidade": 0,
                        "Porcentagem": 1,
                    },
                },
                "Habilidades": ["Ataque Brutal", "Escudo de Ferro"]
            }
            escolhaPersonagem()
        
        case 2:
            clear()
            personagem = {
                "Nome": nome,
                "Idade": idade,
                "Classe": "🧙ﾠMago",
                "Identificador": "Mago",
                "Kills": 0,
                "CavernaExplorada": 0,
                "Estamina": 40,
                "XP": 0,
                "Moeda": 0, 
                "VidaInicial": 80,
                "EstaminaInicial": 40,
                "Atributos": {
                    "Vida": 80,
                    "Dano": 12,
                    "Sorte": 5,
                },
                "Mochila": {
                    "Armas_Mago": {
                        
                    },
                    "Cura": {
                        "Quantidade": 2,
                        "Porcentagem": 25,
                    },
                    "Dano": {
                        "Quantidade": 4,
                        "Porcentagem": 1,
                    },
                    "Sorte": {
                        "Quantidade": 1,
                        "Porcentagem": 1,
                    },    
                },
                "Habilidades": ["Bola de Fogo", "Relâmpago em Cadeia"]
            }
            escolhaPersonagem()
            
        case 3:
            clear()
            personagem = {
                "Nome": nome,
                "Idade": idade,
                "Classe": "🏹ﾠArqueiro",
                "Identificador": "Arqueiro",
                "Kills": 0,
                "CavernaExplorada": 0,
                "Estamina": 50,
                "XP": 0,
                "Moeda": 0, 
                "VidaInicial": 100,
                "EstaminaInicial": 50,
                "Atributos": {
                    "Vida": 100,
                    "Dano": 8,
                    "Sorte": 7,
                },
                "Mochila": {           
                    'Armas_Arq': {
                    },
                  "Cura": {
                        "Quantidade": 3,
                        "Porcentagem": 25,
                    },
                    "Dano": {
                        "Quantidade": 2,
                        "Porcentagem": 1,
                    },
                    "Sorte": {
                        "Quantidade": 1,
                        "Porcentagem": 1,
                    },    
                },
                "Habilidades": ["Tiro Preciso", "Camuflagem"]
            }
            escolhaPersonagem()
            
        case 4:
            iniciarJogo() 
        case _:
            print("Opção Inválida!")
            time.sleep(1) 
            clear()
            novoJogo()
            
def escolhaPersonagem():
    global personagem
    
    print(f"\nVocê escolheu a classe: {personagem['Classe']}")
    print(f"Atributos: {personagem['Atributos']}")
    print(f"Habilidades: {personagem['Habilidades']}")
    
    opcao = int(input("\nVocê tem certeza? \n1- Sim \n2- Voltar \nOpção: "))
    match opcao:
        case 1:
            tutorial()
        case 2:
            novoJogo()
        case _:
            print("Opção Inválida!")
            time.sleep(1) 
            clear()
            escolhaPersonagem()

def tutorial():
    global personagem
    global monstros
    global inimigo
    global conseguencia
    
    clear()
    
    print(f"{personagem['Nome']} sai em sua primeira jornada para se tornar um grande herói!")
    print(f"Durante sua caminhada, {personagem['Nome']} escuta \033[1mgritos dentro da floresta\033[0m")
    time.sleep(1) 
    
    opcao = int(input("Você deseja: \n1- Investigar \n2- Ir embora \nOpção: "))
    
    match opcao:
        case 1:
            pass
        case 2: 
            print("Você fugiu, \033[1mconsequências\033[0m virão no futuro")
            personagem['Atributos']['Sorte'] -= 2
            conseguencia = True
            time.sleep(1) 
            clear()
            exploracao()
        case _:
            print("Opção Inválida!")
            time.sleep(1) 
            clear()
            tutorial()
    
    clear()
    print(f"Voce ve um {monstros['Goblin']['Classe']} atancando pessoas dentro da floresta")
    print("Se prepare pela primeira batalha!")
    inimigo = 'Goblin'
    batalha()
    
    print(f"\nObrigado por salvar nossas vidas, pegue esse Moeda como recompensa")
    ganhoMoeda = random.randint(1, 10)
    personagem['Moeda'] += ganhoMoeda + 2
    print(f"💰ﾠR$: {personagem['Moeda']}")
    time.sleep(1) 
    exploracao()

def exploracao():
    global personagem
    global monstros
    global inimigo
    mudarValor = True
    caminhoSalvo = 0

    while True:

        # Se não estiver mais estamina volta pra vila
        if personagem["Estamina"] <= 0:
            print("Voce não consegue andar mais!")
            print("Volte para vila descançar")
            time.sleep(1)
            vila()
       
       # Se não, ele anda
        else:
            clear()
            if mudarValor:
                caminho = random.randint(1, 34)
            else:
                caminho = caminhoSalvo
                mudarValor = True

        # Caminho só de estrada
        if caminho <= 10:
            print("Qual caminho devo seguir: ")
            opcao = int(input("1- Seguir estrada \nOpção: "))   
            match opcao:
                case 1:
                    personagem["Estamina"] -= 2
                    pass
                case _:
                    print("Opção Inválida!")
                    caminhoSalvo = caminho
                    mudarValor = False
                    time.sleep(1)

        # Caminho de estrada e vila
        elif caminho > 10 and caminho <= 15:
            print("Qual caminho devo seguir: ")
            opcao = int(input("1- Seguir estrada \n2- Vila \nOpção: "))   
            match opcao:
                case 1:
                    personagem["Estamina"] -= 2
                    pass  
                case 2:
                    vila()
                case _:
                    print("Opção Inválida!")
                    caminhoSalvo = caminho
                    mudarValor = False
                    time.sleep(1)
        
        # Caminho de estrada e caverna pequena, media e grande
        elif caminho > 10 and caminho <= 20:
            chancecaverna = random.randint(1, 25)
        
        # Caminho de estrada e caverna pequena,    
            if chancecaverna <= 10:
                
                print("Qual caminho devo seguir: ")
                opcao = int(input("1- Seguir estrada \n2- Seguir caverna \nOpção: "))
                match opcao:
                    case 1:
                        personagem["Estamina"] -= 2
                        pass 
                    case 2:
                        personagem["Estamina"] -= 2
                        cavernaPequena()
                    case _:
                        print("Opção Inválida!")
                        caminhoSalvo = caminho
                        mudarValor = False
                        time.sleep(1)
        
        # Caminho de estrada e caverna media,         
        elif chancecaverna > 20 and chancecaverna <= 25:
                print("Qual caminho devo seguir: ")
                opcao = int(input("1- Seguir estrada \n2- Seguir caverna media \nOpção: "))
                match opcao:
                    case 1:
                        personagem["Estamina"] -= 2
                        pass 
                    case 2:
                        personagem["Estamina"] -= 2
                        cavernaMed()
                    case _:
                        print("Opção Inválida!")
                        caminhoSalvo = caminho
                        mudarValor = False
                        time.sleep(1)
        
        # Caminho de estrada e caverna grande,
        elif chancecaverna > 25 and chancecaverna <= 30:
            if personagem["CavernaExplorada"] == 15:
                    print("Qual caminho devo seguir: ")
                    opcao = int(input("1- Seguir estrada \n2- Seguir Caverna misteriosa \nOpção: "))
                    match opcao:
                        case 1:
                            personagem["Estamina"] -= 2
                            pass 
                        case 2:
                            personagem["Estamina"] -= 2
                            cavernaGrande()
                        case _:
                            print("Opção Inválida!")
                            caminhoSalvo = caminho
                            mudarValor = False
                            time.sleep(1)
            else: 
                print("Qual caminho devo seguir: ")
                opcao = int(input("1- Seguir estrada \nOpção: "))   
                match opcao:
                    case 1:
                        personagem["Estamina"] -= 2
                        pass
                    case _:
                        print("Opção Inválida!")
                        caminhoSalvo = caminho
                        mudarValor = False
                        time.sleep(1)
        
        # Lugares Abandonados
        elif caminho > 30 and caminho <= 32:
            chance = random.randint(1, 5)
            chanceMoeda = random.randint(1, 8)
            
            if chance == 1:
                print("Voce encontrou uma casa abandonada")
                print("👜ﾠVasculhando..")
                time.sleep(1)
                personagem["Moeda"] += chanceMoeda
                
                print("Itens encontrados:")
                print(f"Moeda: {chanceMoeda}")
                time.sleep(1)
            elif chance == 2:
                print("Voce encontrou uma vila abandonada")
                print("👜ﾠVasculhando..")
                time.sleep(1)
                personagem["Moeda"] += chanceMoeda
                
                print("Itens encontrados:")
                print(f"Moeda: {chanceMoeda}")
                time.sleep(1)
            elif chance == 3:
                print("Voce encontrou uma campo de batalha destruido")
                print("👜ﾠVasculhando..")
                time.sleep(1)
                personagem["Moeda"] += chanceMoeda
                
                print("Itens encontrados:")
                print(f"Moeda: {chanceMoeda}")
                time.sleep(1)
            elif chance == 4:
                print("Voce encontrou uma arvore estranha")
                print("👜ﾠVasculhando..")
                time.sleep(1)
                personagem["Moeda"] += chanceMoeda
                
                print("Itens encontrados:")
                print(f"Moeda: {chanceMoeda}")
                time.sleep(1)
            elif chance == 5:
                print("Voce encontrou uma torre destruida")
                print("👜ﾠVasculhando..")
                time.sleep(1)
                personagem["Moeda"] += chanceMoeda
                
                print("Itens encontrados:")
                print(f"Moeda: {chanceMoeda}")
                time.sleep(1)
        
        # Bolsa no chão    
        elif caminho > 32:
            personagem["Estamina"] -= 2
            bolsa = random.randint(1, 5)
            personagem['Moeda'] += bolsa
            print("Você encontrou uma sacola no chão!")
            print("👜ﾠVasculhando..")
            time.sleep(1)
           
            print("Itens encontrados:")
            print(f"Moeda: {bolsa}")
            
            time.sleep(1)
          
def cavernaPequena():
    global monstros
    global inimigo
    chance = random.randint(1, 10)
    clear()
    
    print(f"Durante sua jornada {personagem['Nome']} encontra uma pequena caverna e decide que")
    print("é um bom lugar para treinar derrotando monstros...")
    inimigo = random.choice(list(monstros.keys()))
    print(f"Você encontrou um {monstros[inimigo]['Nome']}!")
    time.sleep(1)
    batalha()
    time.sleep(1)
    print(f"Parabéns, {personagem['Nome']} você derrotou todos os monstros da Caverna!!! ")
    
    
    personagem['CavernaExplorada']  =+ 1
    if chance >= 1:
        itens()
    else:
        pass
    print("Continue explorando para conquistar mais itens e moedas...")

def cavernaMed():
    global monstros
    global inimigo
    chance = random.randint(1, 10)
    clear()
    
    print(f"Enquanto andava pela floresta a procura de novos desafios {personagem['Nome']}")
    print("acaba encontrando uma caverna, que lhe chamou muita a atenção")
    time.sleep(1)
    print(f"{personagem['Nome']} entra na caverna e percebe que não estava tão inabitada quanto parecia...")
    inimigo = random.choice(list(monstros.keys()))
    print(f"Você encontrou um {monstros[inimigo]['Nome']}!")

    time.sleep(1)

    batalha()

    time.sleep(1)

    print(f"Após derrotar o monstro {personagem['Nome']} continua a")
    print("caminhar mais afundo na caverna....")

    time.sleep(1)

    print(f"Você encontrou um {monstros[inimigo]['Nome']}!")

    time.sleep(1)

    batalha()

    time.sleep(1)
    print(f"Parabéns, {personagem['Nome']} você derrotou todos os monstros da Caverna!!! ")
    time.sleep(1)
    
    personagem['CavernaExplorada']  =+ 2
    if chance >= 5:
        itens()
    else:
        pass
    print("Continue explorando para conquistar mais itens e moedas...")

def cavernaGrande():
    global monstros
    global inimigo

    inimigo  = {
    "MoonGuard": {
        "Classe": "Boss",
        "Nome": "Moonlord",
        "Vida": 200,
        "VidaInicial": 200,
        "Dano": 20,
        "Sorte": 8,
    },
} 
    
    clear()
    print("Você encontrou uma caverna misteriosa durante sua caminhada")
    print("Dela emanava uma forte aura maligna e estranhamente familiar....")
    print("Você entrou na caverna final.....")
    print("")
    inimigo = random.choice(list(monstros.keys()))
    print("Você agora esta nos dominios do Lorde Lunar...")
    print(f"Você encontrou o Boss {monstros[inimigo]}['Nome']")
    print("Prepare-se para MORRER!!!!!")
    batalha()
    time.sleep(1)
    
def vila():
    global personagem
    global conseguencia
    
    clear()
    chance = random.randint(1, 10)
    print("Você chegou a vila")
    print("Voce pode visitar lugares pra recuperar vida e mercadores pra comprar poções\n")
    if chance >= 7:
        NPC()
    else:
        opcaoVila()
        
def opcaoVila():
    clear()
    print("Você chegou a vila")
    print("Voce pode visitar lugares pra recuperar vida e mercadores pra comprar poções")
    
    opcao = int(input("\n1- Motel \n2- Mercador \n3- Sair \n4- Opção: "))
    
    match opcao:
        case 1:
            motel()
        case 2:
            mercador()
        case 3:
            exploracao()
        case _:
            print("Opção Inválida!")
            time.sleep(1)
            opcaoVila()   

def NPC():
    clear()
    npc = random.randint(1, 25)
    print("Você chegou a vila")
    print("Voce pode visitar lugares pra recuperar vida e mercadores pra comprar poções")
    
    if npc >= 24:
        moeda = random.randint(1, 10)
        print("NPC: Isso é um assalto!")
        print("NPC: Passe a moeda ou morra!")
        personagem["Moeda"] -= moeda
        print(f"Você perdeu R$: {moeda} moedas")
        print(f"Dinheiro total: {personagem['Moeda']}")
        time.sleep(1)
        opcaoVila()
        

    elif npc >= 1 and npc <= 5:
        quantidade = random.randint(1, 25)
        print("NPC: Olá, sou um caçador!")
        print(f"NPC: Traga {quantidade} cabeças de monstros")
        time.sleep(1)
        opcaoVila()
        
        if personagem["Kills"] >= quantidade:
            moeda = random.randint(1, 10)
            print(f"NPC: Muito bem, tome R$: {moeda} como recompensa")
            personagem["Moeda"] += moeda
            print(f"Dinheiro total: {personagem['Moeda']}")
            time.sleep(1)
            opcaoVila()

    elif npc > 5 and npc  <= 23:
        fala = random.randint(1, 20)

        if fala <= 5:
            print("NPC: Cuidado! Ouvi rumores que na caverna final há um chefe muito resistente")
            time.sleep(1)
            opcaoVila()
        elif fala <= 10:
            print(f"NPC: Olá, {personagem['Nome']}! Bem-vindo ha vila")
            time.sleep(1)
            opcaoVila()
        elif fala <= 15:
            print("NPC: Ei, ei, ei...")
            time.sleep(1)
            if conseguencia:
                print("NPC: Sinto uma presença maligna ao seu redor, um sentimento de culpa")
                time.sleep(1)
                opcaoVila()
            else:
                print("NPC: Sinto uma presença boa ao seu redor, um sentimento de paz")
                time.sleep(1)
                opcaoVila()
        elif fala <= 19:
            print("NPC Mudo: ...")
            time.sleep(1)
            opcaoVila()
        elif fala == 20:
            print("Gato: Miau, Miau, Miau")
            personagem["Atributos"]['Sorte'] += 1
            time.sleep(1)
            opcaoVila()
    
def motel():
    global personagem
    clear()
    
    print("Bem vindo ao motel!")
    print("Gostaria de passar uma noite?")
    print("Uma noite custa R$ 10 moeda")
    print(f"Suas moedas: {personagem['Moeda']}")
    opcao = int(input("1- Sim \n2- Sair \n3- Opção: "))


    
    match opcao:
        case 1:
            if personagem['Moeda'] < 10:
                clear()
                print("Voce não tem moeda suficiente")
                print("Caia fora do meu motel!")
                time.sleep(1)
                vila()
            else:
                clear()
                personagem['Moeda'] -= 10 
                personagem['Atributos']['Vida'] = personagem['VidaInicial']
                personagem['Estamina'] = personagem['EstaminaInicial']
                print(f"Vc ainda tem R$: {personagem['Moeda']}")
                print(f"Sua vida esta recuperado \nVida: {personagem['Atributos']['Vida']} \nEstamina: {personagem['Estamina']}")
                time.sleep(1)
                clear()
                motel()
        case 2:
            opcaoVila()
        case _:
            print("Opção Inválida!")
            time.sleep(1)
            motel()
  
def mercador():
    global personagem
    clear()
    
    while True:
        print("Bem vindo ao mercado!")
        print("Oque gostaria de comprar?")
        print(f"Suas moedas: {personagem['Moeda']}")
        opcao = int(input("1- R$: 25 Poção de cura \n2- Poção de Dano R$: 50 \n3- R$: 75 Poção de sorte \n4- Sair \nOpção: "))
        
        match opcao:
            case 1:
                if personagem["Moeda"] >= 25:
                    personagem["Moeda"] -= 25
                    personagem["Mochila"]['Cura']['Quantidade'] += 1
                    print(f"Voce esta agora com {personagem["Mochila"]['Cura']['Quantidade']}")
                    print(f"Moeda: {personagem["Moeda"]}")
                else:
                    print("Voce não tem moeda suficiente!")
                    time.sleep(1)
                    clear()   
            case 2:
                if personagem["Moeda"] >= 50:
                    personagem["Moeda"] -= 50
                    personagem["Mochila"]['Dano']['Quantidade'] += 1
                    print(f"Voce esta agora com {personagem["Mochila"]['Dano']['Quantidade']}")
                    print(f"Moeda: {personagem["Moeda"]}")
                else:
                    print("Voce não tem moeda suficiente!")
                    time.sleep(1)
                    clear()   
            case 3:
                if personagem["Moeda"] >= 75:
                    personagem["Moeda"] -= 75
                    personagem["Mochila"]['Sorte']['Quantidade'] += 1
                    print(f"Voce esta agora com {personagem["Mochila"]['Sorte']['Quantidade']}")
                    print(f"Moeda: {personagem["Moeda"]}")
                else:
                    print("Voce não tem moeda suficiente!")
                    time.sleep(1)
                    clear()  
            case 4:
                opcaoVila()
            case _:
                print("Opção Inválida!")
                time.sleep(1)
                clear()   

print(iniciarJogo())
