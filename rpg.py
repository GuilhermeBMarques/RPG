import os
import time
import random

personagem = {}
inimigo = {}
conseguencia = False

# Armas das classes dos personagens
ArmasGuerreiro = {
    "Berserk": {
        "Nome": "Berserk Sword",
        "Raridade": 2,
        "Dano": 8,
    },
    "Katana": {
        "Nome": "Katana de aço",
        "Raridade": 3,
        "Dano": 13,
    },
    "Moonlight": {
        "Nome": "Lamina da Lua",
        "Raridade": 5,
        "Dano": 20,
    },
    "Rapieira": {
        "Nome": "Rapieira",
        "Raridade": 4,
        "Dano": 19,
    },
    "Espada normal": {
        "Nome": "Espada de ferro",    
        "Raridade": 3,
        "Dano": 11,
    },
    "Adaga": {
        "Nome": "Adagas de ferro",
        "Raridade": 1,
        "Dano": 2,
    },
    "Machado": {
        "Nome": "Machado de guerra",
        "Raridade": 4,
        "Dano": 17,
    },
    "Lança": {
        "Nome": "Lança de batalha",
        "Raridade": 2,
        "Dano": 6,
    },
    "Espada longa": {
        "Nome": "Espada longa",
        "Raridade": 4,
        "Dano": 15,
    },
}

ArmasMago = {
    "Cajado da Terra": {
        "Nome": "Cajado da Terra",
        "Raridade": 4,
        "Dano": 17,
    },
    "Cajado do Raio das Sombras": {
        "Nome": "Cajado do Raio das Sombras",
        "Raridade": 2,
        "Dano": 7,
    },
    "Cajado do estranho": {
        "Nome": "Cajado do estranho",
        "Raridade": 3,
        "Dano": 14,
    },
    "Cajado de Gelo": {
        "Nome": "Cajado de Gelo",
        "Raridade": 1,
        "Dano": 3,
    },
    "Cajado Venenoso": {
        "Nome": "Cajado Venenoso",
        "Raridade": 3,
        "Dano": 10,
    },
    "Vara de gelo": {
        "Nome": "Vara de gelo",
        "Raridade": 2,
        "Dano": 5,
    },
    "Adaga mágica": {
        "Nome": "Adaga mágica",
        "Raridade": 3,
        "Dano": 12,
    },
    "Cabeça de Medusa": {
        "Nome": "Cabeça de Medusa",
        "Raridade": 2,
        "Dano": 9,
    },
    "Último Prisma": {
        "Nome": "Último Prisma",
        "Raridade": 5,
        "Dano": 20,
    },
}

ArmasArqueiro = {
    "Arco basico": {
        "Nome": "Arco basico",
        "Raridade": 2,
        "Dano": 6,
    },
    "Crossbow": {
        "Nome": "Crossbow",
        "Raridade": 3,
        "Dano": 13,
    },
    "Crossbow Automatica": {
        "Nome": "Crossbow Automatica",
        "Raridade": 4,
        "Dano": 15,
    },
    "Arco de Madeira": {
        "Nome": "Arco de Madeira",
        "Raridade": 1,
        "Dano": 4,
    },
    "Arco Artemis": {
        "Nome": "Artemis",
        "Raridade": 3,
        "Dano": 11,
    },
    "Arco Lunar": {
        "Nome": "Arco lunar",
        "Raridade": 4,
        "Dano": 18,
    },
    "Arco de Ferro": {
        "Nome": "Arco de Ferro",
        "Raridade": 1,
        "Dano": 2,
    },
    "Arco Longo": {
        "Nome": "Arco Longo",
        "Raridade": 4,
        "Dano": 15,
    },
    "Arco Exótico": {
        "Nome": "Arco Exótico",
        "Raridade": 5,
        "Dano": 20,
    }
}

ArmasInvocador = {
    "Chicote de Couro": {
        "Nome": "Chicote de Couro",
        "Raridade": 2,
        "Dano": 8,
    },
    "Chicotespinho": {
        "Nome": "Chicotespinho",
        "Raridade": 1,
        "Dano": 1,
    },
    "Punção Lombar": {
        "Nome": "Punção Lombar",
        "Raridade": 2,
        "Dano": 7,
    },
    "Estalinho": {
        "Nome": "Estalinho",
        "Raridade": 3,
        "Dano": 14,
    },
    "Chicote Gelado": {
        "Nome": "Chicote Gelado",
        "Raridade": 2,
        "Dano": 5,
    },
    "Durindana": {
        "Nome": "Durindana",
        "Raridade": 3,
        "Dano": 12,
    },
    "Colheita Maldita": {
        "Nome": "Colheita Maldita",
        "Raridade": 1,
        "Dano": 3,
    },   
    "Mangual": {
        "Nome": "Mangual",
        "Raridade": 4,
        "Dano": 17,
    },   
    "Caleidoscópio": {
        "Nome": "Caleidoscópio",
        "Raridade": 5,
        "Dano": 20,
    },   
}

# Monstros
monstros = {
    "Goblin": {
        "Classe": "Goblin",
        "Nome": "🧌ﾠﾠGoblin",
        "Sexo": "Masculino",
        "Vida": 25,
        "VidaInicial": 25,
        "Dano": 6,
        "Sorte": 4,
    },
    "Esqueleto": {
        "Classe": "Esqueleto",
        "Nome": "💀ﾠEsqueleto",
        "Sexo": "Masculino",
        "Vida": 25,
        "VidaInicial": 25,
        "Dano": 10,
        "Sorte": 3,
    },
    "Fadas": {
        "Classe": "Fada",
        "Nome": "🧚ﾠFada",
        "Sexo": "Femenino",
        "Vida": 20,
        "VidaInicial": 20,
        "Dano": 5,
        "Sorte": 7,
    },
    "Elfos":  {
        "Classe": "Elfo",
        "Nome": "🧝ﾠElfo",
        "Sexo": "Masculino",
        "Vida": 30,
        "VidaInicial": 30,
        "Dano": 11,
        "Sorte": 4,
    },
    "Reptiliano": {
        "Classe": "Reptiliano",
        "Nome": "🦎ﾠReptiliano",
        "Sexo": "Masculino",
        "Vida": 28,
        "VidaInicial": 28,
        "Dano": 10,
        "Sorte": 3,
    },
    "ArmaduraﾠViva": {
        "Classe": "Fantasma",
        "Nome": "🛡ﾠﾠArmaduraﾠViva",
        "Sexo": "Masculino",
        "Vida": 50,
        "VidaInicial": 50,
        "Dano": 19,
        "Sorte": 2,
    },
    "AlmaﾠPerdida": {
        "Classe": "AlmaﾠPerdida",
        "Nome": "🔥ﾠAlmaﾠPerdida",
        "Sexo": "Masculino",
        "Vida": 25,
        "VidaInicial": 25,
        "Dano": 10,
        "Sorte": 3,
    },
    "Ogro": {
        "Classe": "Ogro",
        "Nome": "👹ﾠOgro",
        "Sexo": "Masculino",
        "Vida": 50,
        "VidaInicial": 50,
        "Dano": 14,
        "Sorte": 3,
    },
    "LoboﾠFantasma": {
        "Classe": "Fantasma",
        "Nome": "🐺ﾠLoboﾠFantasma",
        "Sexo": "Masculino",
        "Vida": 30,
        "VidaInicial": 3,
        "Dano": 8,
        "Sorte": 3,
    },
    "Pessoaﾠdesconhecida": {
        "Classe": "Estranho",
        "Sexo": "Masculino",
        "Nome": "Estranho",
        "Vida": 30,
        "VidaInicial": 30,
        "Dano": 10,
        "Sorte": 8,
    },
    "MoonLord": {
        "Classe": "Boss",
        "Nome": "Moonlord",
        "Sexo": "Masculino",
        "Vida": 200,
        "VidaInicial": 200,
        "Dano": 20,
        "Sorte": 9,
    },
}

# Sistema de itens encontrados
def itens():
    clear()
    global personagem
    print("Após derrotar todos os monstros da caverna você encontrou uma")
   
    if personagem["Identificador"] == "Guerreiro":
        armasRandom = random.choice(list(ArmasGuerreiro.keys()))
        print(f"{ArmasGuerreiro[armasRandom]['Nome']} \n⚔ﾠﾠDano: {ArmasGuerreiro[armasRandom]['Dano']} \n✨ﾠRaridade: {ArmasGuerreiro[armasRandom]['Raridade']}")
        print(f"\nSua arma atual: {personagem['Mochila']['ArmasGuerreiro']}\n")
        
        opcao = int(input("Você deseja coletar o item? \n1- Coletar \n2- Não Pegar \nOpção: "))

        match opcao:
            case 1:
                personagem['Mochila']['ArmasGuerreiro'] = {armasRandom: ArmasGuerreiro[armasRandom]}
                print(f"{personagem['Nome']} pegou a {ArmasGuerreiro[armasRandom]} e colocou na mochila...")
            case 2:
                print("Você deixou o item no chão...")
            case _:
                print("Opção Inválida!")
                time.sleep(1)
                itens()
    
    elif personagem["Identificador"] == "Mago":
        armasRandom = random.choice(list(ArmasMago.keys()))
        print(f"{ArmasMago[armasRandom]['Nome']} \n⚔ﾠﾠDano: {ArmasMago[armasRandom]['Dano']} \n✨ﾠRaridade: {ArmasMago[armasRandom]['Raridade']} ")
        print(f"\nSua arma atual: {personagem['Mochila']['ArmasMago']}\n")
        
        opcao = int(input("Você deseja coletar o item? \n1- Coletar \n2- Não Pegar \nOpção: "))

        match opcao:
            case 1:
                personagem['Mochila']['ArmasMago'] = {armasRandom: ArmasMago[armasRandom]}
                print(f"{personagem['Nome']} pegou a {ArmasMago[armasRandom]} e colocou na mochila...")
            case 2:
                print("Você deixou o item no chão...")
            case _:
                print("Opção Inválida!")
                time.sleep(1)
                itens()

    elif personagem["Identificador"] == "Arqueiro":
        armasRandom = random.choice(list(ArmasArqueiro.keys()))
        print(f"{ArmasArqueiro[armasRandom]['Nome']} \n⚔ﾠﾠDano: {ArmasArqueiro[armasRandom]['Dano']} \n✨ﾠRaridade: {ArmasArqueiro[armasRandom]['Raridade']} ")
        print(f"\nSua arma atual: {personagem['Mochila']['ArmasArqueiro']}\n")
        opcao = int(input("Você deseja coletar o item? \n1- Coletar \n2- Não Pegar \nOpção: "))

        match opcao:
            case 1:
                personagem['Mochila']['ArmasArqueiro'] = {armasRandom: ArmasArqueiro[armasRandom]}
                print(f"{personagem['Nome']} pegou a {ArmasArqueiro[armasRandom]} e colocou na mochila...")
            case 2:
                print("Você deixou o item no chão...")
            case _:
                print("Opção Inválida!")
                time.sleep(1)
                itens()

    elif personagem["Identificador"] == "Invocador":
        armasRandom = random.choice(list(ArmasInvocador.keys()))
        print(f"{ArmasInvocador[armasRandom]['Nome']} \n⚔ﾠﾠDano: {ArmasInvocador[armasRandom]['Dano']} \n✨ﾠRaridade: {ArmasInvocador[armasRandom]['Raridade']}")
        print(f"\nSua arma atual: {personagem['Mochila']['ArmasInvocador']}\n")
        opcao = int(input("Você deseja coletar o item? \n1- Coletar \n2- Não Pegar \nOpção: "))

        match opcao:
            case 1:
                personagem['Mochila']['ArmasInvocador'] = {armasRandom: ArmasInvocador[armasRandom]}
                print(f"{personagem['Nome']} pegou a {ArmasInvocador[armasRandom]} e colocou na mochila...")
            case 2:
                print("Você deixou o item no chão...")
            case _:
                print("Opção Inválida!")
                time.sleep(1)
                itens()

# Limpar a tela
def clear():
    if os.name == 'nt': 
        os.system('cls')
    else: 
        os.system('clear')
        
# Sistema de batalha
def batalha():
    global personagem
    global monstros

    while personagem['Atributos']['Vida'] > 0 and monstros[inimigo]['Vida'] > 0:
        opcao = int(input("Deseja: \n1- Atacar \n2- Usar Mochila \n3- Fugir \nOpção: "))
        
        match opcao:
            case 1:
                clear()
                
                chance = random.randint(1, 10)
                dano_arma = 0 
                
                if personagem['Identificador'] == 'Guerreiro':
                    if 'ArmasGuerreiro' in personagem['Mochila'] and personagem['Mochila']['ArmasGuerreiro']:
                        arma = random.choice(list(personagem['Mochila']['ArmasGuerreiro'].values()))
                        if 'Dano' in arma:
                            dano_arma = arma['Dano']
                elif personagem['Identificador'] == 'Mago':
                    if 'ArmasMago' in personagem['Mochila'] and personagem['Mochila']['ArmasMago']:  
                        arma = random.choice(list(personagem['Mochila']['ArmasMago'].values()))
                        if 'Dano' in arma:
                            dano_arma = arma['Dano']
                elif personagem['Identificador'] == 'Arqueiro':
                    if 'ArmasArqueiro' in personagem['Mochila'] and personagem['Mochila']['ArmasArqueiro']:
                        arma = random.choice(list(personagem['Mochila']['ArmasArqueiro'].values()))
                        if 'Dano' in arma:
                            dano_arma = arma['Dano']
                elif personagem['Identificador'] == 'Invocador':
                    if 'ArmasInvocador' in personagem['Mochila'] and personagem['Mochila']['ArmasInvocador']:
                        arma = random.choice(list(personagem['Mochila']['ArmasInvocador'].values()))
                        if 'Dano' in arma:
                            dano_arma = arma['Dano']
                
                dano_total = personagem['Atributos']['Dano'] + dano_arma
                monstros[inimigo]['Vida'] -= dano_total
                
                print(f"Você deu -{dano_total} de dano")
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
            case 2:
                clear()
                chance = random.randint(1, 3)

                print(f"Cura: \nQuantidade: {personagem['Mochila']['Cura']['Quantidade']} \nPorcentagem: {personagem['Mochila']['Cura']['Porcentagem']}\n")
                print(f"Dano: \nQuantidade: {personagem['Mochila']['Dano']['Quantidade']} \nPorcentagem: {personagem['Mochila']['Dano']['Porcentagem']}\n")
                print(f"Sorte: \nQuantidade: {personagem['Mochila']['Sorte']['Quantidade']} \nPorcentagem: {personagem['Mochila']['Sorte']['Porcentagem']}\n")
                
                print("Digite o nome do item que deseja usar")
                print("Digite sair caso queira voltar pra batalha")
                opcao = str(input("Deseja usar algum item? \nOpção: ")).capitalize()
                clear()
                if opcao in personagem['Mochila']:
                    if personagem['Mochila'][opcao]['Quantidade'] == 0:
                        print("Você não tem mais desse item")
                    else:
                        if personagem['Mochila'][opcao] == personagem['Mochila']['Cura']:
                            if personagem['Atributos']['Vida'] <= personagem['VidaInicial']:
                                personagem['Atributos']['Vida'] += personagem['Mochila']['Cura']['Porcentagem']
                                personagem['Mochila'][opcao]['Quantidade'] -= 1
                                if personagem['Atributos']['Vida'] > personagem['VidaInicial']:
                                    personagem['Atributos']['Vida'] = personagem['VidaInicial']
                                    print(f"Vida: {personagem['Atributos']['Vida']}")
                                else: 
                                    print(f"Vida: {personagem['Atributos']['Vida']}")
                                    
                        elif personagem['Mochila'][opcao] == personagem['Mochila']['Dano']:
                            personagem['Atributos']['Dano'] += personagem['Mochila']['Dano']['Porcentagem']
                            personagem['Mochila'][opcao]['Quantidade'] -= 1
                            print(f"Você aumento seu dano para mais: {personagem['Mochila']['Dano']['Porcentagem']}")
                            print(f"Dano: {personagem['Atributos']['Dano']}")
                            
                        elif personagem['Mochila'][opcao] == personagem['Mochila']['Sorte']:
                            personagem['Atributos']['Sorte'] += personagem['Mochila']['Sorte']['Porcentagem']
                            personagem['Mochila'][opcao]['Quantidade'] -= 1
                            print(f"Você aumento seu sorte para mais: {personagem['Mochila']['Sorte']['Porcentagem']}")
                            print(f"Sorte: {personagem['Atributos']['Sorte']}")
                        else:
                            pass
                elif opcao.capitalize() == "Sair":
                    clear()
                    batalha()
                else:
                    print("Item não encontrado")
            case 3:
                fugir = random.randint(1, 7)
                if 2 >= fugir:
                    print("Você conseguiu fugir da batalha!")
                    time.sleep(1)
                    clear()
                    exploracao()
                else:
                    chance = random.randint(1, 10)
                    print("Você não conseguiu fugir")
                    
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
     
# Morte do player 
def playerMorto():
    global personagem
    global monstros
    global inimigo
    
    clear()
    
    print(f"Você morreu para {'um' if monstros[inimigo]['Sexo'] == "Masculino" else 'uma'} {monstros[inimigo]['Nome']}!")
    print(f"Inimigos Mortos: {personagem['Kills']}")
    print(f"Cavernas Exploradas: {personagem['CavernaExplorada']}")
    time.sleep(2)
    print("Deseja reniciar?")
    opcao = int(input("1- Sim \n2- Não \nOpção: "))
    match opcao:
        case 1:
            clear()
            novoJogo()
        case 2:
            clear()
            iniciarJogo()
        case _:
            print("Opção Inválida!")
            time.sleep(1)
            clear()
            playerMorto()

# Recompensa por matar um mostro
def recompensa(): 
    global personagem
    global monstros
    global inimigo
    
    ganhoMoeda = random.randint(1, 10)
    
    personagem['Kills'] += 1
    personagem['Moeda'] += ganhoMoeda
    
    monstros[inimigo]['Vida'] = monstros[inimigo]['VidaInicial']
    
    print(f"Você derrotou {'um' if monstros[inimigo]['Sexo'] == "Masculino" else 'uma'} {monstros[inimigo]['Classe']} \nRecompensas: \n💰ﾠR$: {ganhoMoeda} \n☠️ﾠﾠKills: {personagem['Kills']}")
    time.sleep(2)
    clear()
      
# Sessão do jogador
def iniciarJogo():
    clear()
    
    print("\033[1mCivilização Zero\033[0m")
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
  
# Instruções de como que joga      
def instrucoes():
    clear()
    
    print("\033[1m----------Instruções----------\033[0m")
    print("Os comandos do jogo são simples!")
    print("Digite um \033[1mnumero\033[0m da opção no terminal para continuar o jogo")
    print("Digite o \033[1mnome\033[0m da opcçao na mochila")
    print("O jogo será baseado em \033[1mturnos\033[0m, durante um turno, você atacará e no outro seu inimigo atacará")
    print("Seu objetivo é explorar \033[1mcavernas\033[0m e \033[1mderrotar 25 inimigos\033[0m para encontrar a \033[1mcaverna final\033[0m, onde você encontrara seu \033[1mfinal\033[0m")
    print("Cada classe virá com níveis de atributos \033[1mdiferentes\033[0m")
   
    opcao = int(input("\n1- Sair \nOpção: "))
    
    match opcao:
        case 1:
            return iniciarJogo()
        case _:
            print("Opção Invalida!")
            time.sleep(1) 
            instrucoes()
    
# Partida pra ver os persomagens               
def novoJogo():
    global personagem
    
    clear()
    print("Em um tempo já quase esquecido, a humanidade conseguira alcançar um nivel tecnologico o suficiente")
    print("para se sustentar e popular outros planetas e sua Lua...")
    time.sleep(4)
    print("Os reinos da terra e da lua criados pela tecnologia humana prosperavam, e cada dia mais avançavam para seu objetivo.")
    print("Mas as coisas nao sairam como o esperado, cientistas encontraram algo que poderia destruir a humanidade escondido")
    print("dentro da Lua...")
    time.sleep(5)
    print("Algo que fez com que os cientistas enlouquecessem...")
    time.sleep
    print("Mas por pura ganancia, o Lorde que comandava a civilização da Lua continuou as pesquisas com o que haviam encontrado")
    time.sleep(5)
    print("A Lua se rompeu...")
    time.sleep(5)
    print("O rei ganancioso enlouqueceu e obrigou que criassem uma arma contra a civilização da terra")
    print("Armas essas que levariam monstros para terra, cavernas criadas para destruir e preparar a terra para a sua chegada ")
    print("durante um tempo não mais descrito nos livros de historia, a humaninade lutou incansavelmente contra a força do Lorde")
    time.sleep(5)
    print("a guerra fez com que a terra mudasse com a exposição da ''coisa'' encontrada na lua.")
    print("O mundo mudou, os humanos se adaptaram")
    time.sleep(5)
    print("Bem-vindo a \033[1mCivilização Zero\033[0m!") 
    print("Encare novos desafios!!\n")
    print("Dê \033[1mvida\033[0m ao seu herói ")
    nome = str(input("Digite o \033[1mnome\033[0m do seu herói: "))
    idade = int(input("Digite a \033[1midade\033[0m do seu herói: "))
    
    print("\nEscolha uma \033[1mclasse\033[0m:")
    
    opcao = int(input("1- ⚔ﾠﾠGuerreiro \n2- 🧙ﾠMago \n3- 🏹ﾠArqueiro \n4- 🐉ﾠInvocador \n5- Voltar \nOpção: "))
    
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
                "Moeda": 0, 
                "VidaInicial": 120,
                "EstaminaInicial": 60,
                "Atributos": {
                    "Vida": 120,
                    "Dano": 8,
                    "Sorte": 4,
                },
                "Mochila": {
                    'ArmasGuerreiro': {
                    },
                    "Cura": {
                        "Quantidade": 3,
                        "Porcentagem": 25,
                    },
                    "Dano": {
                        "Quantidade": 1,
                        "Porcentagem": 1
                    },
                    "Sorte": {
                        "Quantidade": 0,
                        "Porcentagem": 1
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
                "Moeda": 0, 
                "VidaInicial": 80,
                "EstaminaInicial": 40,
                "Atributos": {
                    "Vida": 80,
                    "Dano": 7,
                    "Sorte": 4,
                },
                "Mochila": {
                    "ArmasMago": {
                        
                    },
                    "Cura": {
                        "Quantidade": 2,
                        "Porcentagem": 25,
                    },
                    "Dano": {
                        "Quantidade": 4,
                        "Porcentagem": 1
                    },
                    "Sorte": {
                        "Quantidade": 1,
                        "Porcentagem": 1
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
                "Moeda": 0, 
                "VidaInicial": 100,
                "EstaminaInicial": 50,
                "Atributos": {
                    "Vida": 100,
                    "Dano": 6,
                    "Sorte": 8,
                },
                "Mochila": {           
                    'ArmasArqueiro': {
                    },
                  "Cura": {
                        "Quantidade": 3,
                        "Porcentagem": 25,
                    },
                    "Dano": {
                        "Quantidade": 2,
                        "Porcentagem": 1
                    },
                    "Sorte": {
                        "Quantidade": 1,
                        "Porcentagem": 1
                    },    
                },
                "Habilidades": ["Tiro Preciso", "Camuflagem"]
            }
            escolhaPersonagem()
        
        case 4:
            clear()
            personagem = {
                "Nome": nome,
                "Idade": idade,
                "Classe": "🐉ﾠInvocador",
                "Identificador": "Invocador",
                "Kills": 0,
                "CavernaExplorada": 0,
                "Estamina": 50,
                "Moeda": 0, 
                "VidaInicial": 100,
                "EstaminaInicial": 50,
                "Atributos": {
                    "Vida": 100,
                    "Dano": 9,
                    "Sorte": 5,
                },
                "Mochila": {           
                    'ArmasInvocador': {
                    },
                  "Cura": {
                        "Quantidade": 3,
                        "Porcentagem": 25,
                    },
                    "Dano": {
                        "Quantidade": 2,
                        "Porcentagem": 1
                    },
                    "Sorte": {
                        "Quantidade": 1,
                        "Porcentagem": 1
                    },    
                },
                "Habilidades": ["Tiro Preciso", "Camuflagem"]
            }
            escolhaPersonagem()
            
        case 5:
            iniciarJogo() 
        case _:
            print("Opção Inválida!")
            time.sleep(1) 
            clear()
            novoJogo()

# Escolha de personagem     
def escolhaPersonagem():
    global personagem
    
    print(f"\nVocê escolheu a classe: {personagem['Classe']}")
    print(f"Atributos: \n❤ﾠﾠVida: {personagem['Atributos']['Vida']} \n⚔ﾠﾠDano: {personagem['Atributos']['Dano']} \n🍀ﾠSorte: {personagem['Atributos']['Sorte']}")
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

# Tutorial do primeiro monstro
def tutorial():
    global personagem
    global monstros
    global inimigo
    global conseguencia
    
    clear()
    print(f"{personagem['Nome']} sai em sua primeira jornada para se tornar um grande herói")
    print("e derrotar as cavernas para livrar seu planeta dos monstros!")
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
    print(f"Você ve um {monstros['Goblin']['Classe']} atancando pessoas dentro da floresta")
    print("Se prepare pela primeira batalha!")
    inimigo = 'Goblin'
    batalha()
    
    print(f"\nObrigado por salvar nossas vidas, pegue esse Moeda como recompensa")
    ganhoMoeda = random.randint(1, 10)
    personagem['Moeda'] += ganhoMoeda + 2
    print(f"💰ﾠR$: {personagem['Moeda']}")
    time.sleep(1) 
    exploracao()

# Caminhos
def exploracao():
    global personagem
    global monstros
    global inimigo
    mudarValor = True
    caminhoSalvo = 0
    
    while True:

        if personagem["Estamina"] <= 0:
            print("Você não consegue andar mais!")
            print("Volte para vila descançar")
            time.sleep(1)
            vila()
       
       # Se não, ele anda
        else:
            clear()
            if mudarValor:
                caminho = random.randint(1, 32)
            else:
                caminho = caminhoSalvo
                mudarValor = True

        # Caminho só de estrada
        if caminho <= 5:
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
        elif caminho > 5 and caminho <= 10:
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
        
                # Caminho de estrada e caverna pequena,    
        
        # Caminho de estrada e caverna pequena
        elif caminho > 10 and caminho <= 15:
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
        elif caminho > 15 and caminho <= 20:
            print("Qual caminho devo seguir: ")
            opcao = int(input("1- Seguir estrada \n2- Seguir caverna media \nOpção: "))
            match opcao:
                case 1:
                    personagem["Estamina"] -= 2
                    pass 
                case 2:
                    personagem["Estamina"] -= 2
                    cavernaMedia()
                case _:
                    print("Opção Inválida!")
                    caminhoSalvo = caminho
                    mudarValor = False
                    time.sleep(1)
        
        # Caminho de estrada e caverna grande,
        elif caminho > 20 and caminho <= 25:
            if personagem["CavernaExplorada"] >= 10:
                print("Qual caminho devo seguir: ")
                opcao = int(input("1- Seguir estrada \n2- Seguir \033[1mcaverna misteriosa\033[0m \nOpção: "))
                
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
        elif caminho > 25 and caminho <= 27:
            chance = random.randint(1, 5)
            chanceMoeda = random.randint(1, 8)
            
            if chance == 1:
                print("Você encontrou uma casa abandonada")
                print("👜ﾠVasculhando..")
                time.sleep(1)
                personagem["Moeda"] += chanceMoeda
                
                print("Itens encontrados:")
                print(f"Moeda: {chanceMoeda}")
                time.sleep(1)
            elif chance == 2:
                print("Você encontrou uma vila abandonada")
                print("👜ﾠVasculhando..")
                time.sleep(1)
                personagem["Moeda"] += chanceMoeda
                
                print("Itens encontrados:")
                print(f"Moeda: {chanceMoeda}")
                time.sleep(1)
            elif chance == 3:
                print("Você encontrou uma campo de batalha destruido")
                print("👜ﾠVasculhando..")
                time.sleep(1)
                personagem["Moeda"] += chanceMoeda
                
                print("Itens encontrados:")
                print(f"Moeda: {chanceMoeda}")
                time.sleep(1)
            elif chance == 4:
                print("Você encontrou uma arvore estranha")
                print("👜ﾠVasculhando..")
                time.sleep(1)
                personagem["Moeda"] += chanceMoeda
                
                print("Itens encontrados:")
                print(f"Moeda: {chanceMoeda}")
                time.sleep(1)
            elif chance == 5:
                print("Você encontrou uma torre destruida")
                print("👜ﾠVasculhando..")
                time.sleep(1)
                personagem["Moeda"] += chanceMoeda
                
                print("Itens encontrados:")
                print(f"Moeda: {chanceMoeda}")
                time.sleep(1)
        
        # Bolsa no chão    
        elif caminho > 27 and caminho <= 29:
            personagem["Estamina"] -= 2
            bolsa = random.randint(1, 5)
            personagem['Moeda'] += bolsa
            print("Você encontrou uma sacola no chão!")
            print("👜ﾠVasculhando..")
            time.sleep(1)
           
            print("Itens encontrados:")
            print(f"Moeda: {bolsa}")
            
            time.sleep(1)
        
        # Inimigo no caminho
        elif caminho > 29 and caminho <= 32:
            personagem["Estamina"] -= 2
            inimigo = random.choice([m for m in monstros.keys() if m != "MoonLord"])
            print(f"Você encontrou {'um' if monstros[inimigo]['Sexo'] == "Masculino" else 'uma'} {monstros[inimigo]['Classe']} no caminho")
            time.sleep(2)
            batalha()

# Caverna pequena                 
def cavernaPequena():
    global monstros
    global inimigo
    chance = random.randint(1, 10)
    clear()
    
    print(f"Durante sua jornada, você encontra uma pequena caverna escura e silenciosa")
    print("O som de gotas caindo nas pedras ecoa por todo o lugar")
    print("Você decide que é um bom lugar para treinar, derrotando monstros e aprimorando suas habilidades...\n")
    
    # Primeira batalha
    inimigo = random.choice([m for m in monstros.keys() if m != "MoonLord"])
    print(f"Você encontra um {monstros[inimigo]['Nome']} escondido nas sombras da caverna")
    print("O monstro se aproxima com olhos brilhando na escuridão, pronto para atacar")
    print(f"Prepare-se para a batalha!")
    time.sleep(1)
    batalha()
    time.sleep(1)
    
    # Segunda batalha
    inimigo2 = random.choice([m for m in monstros.keys() if m != inimigo and m != "MoonLord" and m not in inimigo])
    inimigo = inimigo2
    print(f"Você sente uma presença sinistra vindo da caverna")
    print(f"Ao explorar, encontra um {monstros[inimigo]['Nome']}")
    print("O monstro, mais feroz que os anteriores")
    print(f"Prepare-se para a batalha!")
    time.sleep(1)
    batalha()
    time.sleep(1)

    print(f"Parabéns, {personagem['Nome']}! Você derrotou todos os monstros da Caverna!")
    print("A caverna parece estar silenciosa novamente...")
    time.sleep(1)
    
    personagem['CavernaExplorada'] = personagem['CavernaExplorada'] + 1
    if chance >= 7:
        print("Enquanto explora os restos dos monstros derrotados, você encontra alguns itens valiosos escondidos nas cavernas!")
        time.sleep(2)
        itens()
    else:
        print("Nada de interessante foi encontrado na caverna...")
        pass
    print("Continue explorando para conquistar mais itens e moedas...")

# Caverna media
def cavernaMedia():
    global monstros
    global inimigo
    chance = random.randint(1, 10)
    clear()
    
    print(f"Enquanto caminhava pela floresta em busca de novos desafios, algo chamou sua atenção à distância")
    print("Uma entrada de caverna media, parcialmente escondida por vegetação densa, parecia esconder mistérios antigos e perigos desconhecidos")
    time.sleep(3)
    print(f"Você se aproxima e sem quere cai dentro da caverna")
    print("As paredes cobertas de musgo refletem a pouca luz que entra pela entrada")
    print("No fundo, um som distante de água gotejando ecoa pela caverna")
    time.sleep(3)
    
    # Primeira batalha
    inimigo = random.choice([m for m in monstros.keys() if m != "MoonLord"])
    print(f"De repente, um {monstros[inimigo]['Nome']} surge das sombras")
    print("Sem mais avisos, avançou contra você")
    print(f"Prepare-se para a batalha!")
    time.sleep(1)
    batalha()
    time.sleep(1)
    
    print(f"Após derrotar o {monstros[inimigo]['Nome']}, você decide continuar a exploração da caverna")
    print("O ambiente vai ficando cada vez mais escuro, parece como se o lugar estivesse guardando um segredo")
    print("Enquanto caminha, o eco dos seus passos reverbera pelas paredes, criando uma sensação de que a caverna está viva e observando")
    time.sleep(2)
    
    # Segunda batalha
    inimigo2 = random.choice([m for m in monstros.keys() if m != inimigo and m != "MoonLord" and m not in inimigo and m not in inimigo])
    inimigo = inimigo2
    print(f"Você encontra um {monstros[inimigo2]['Nome']}")
    print(f"Ele bloqueia o caminho, e não há outra saída!")
    print(f"Prepare-se para a batalha!")
    time.sleep(1)
    batalha()
    time.sleep(1)
    
    # Terceira batalha
    print("A medida que o caminho vai se estreitando, você sente uma presença ainda mais ameaçadora se aproximando...")
    time.sleep(1)
    inimigo3 = random.choice([m for m in monstros.keys() if m != inimigo and m != "MoonLord" and m not in inimigo and m not in inimigo2])
    inimigo = inimigo3
    print(f"{monstros[inimigo3]['Nome']} aparece em um corredor estreito")
    print("Ele vem em sua direção com velocidade surpreendente!")
    print(f"Prepare-se para a batalha!")
    time.sleep(1)
    batalha()
    time.sleep(1)
    
    print(f"Parabéns, {personagem['Nome']}! Você derrotou todos os monstros da Caverna!")
    print("A caverna parece estar silenciosa novamente...")
    time.sleep(1)
    
    personagem['CavernaExplorada'] = personagem['CavernaExplorada'] + 2
    if chance >= 5:
        print("Enquanto explora os restos dos monstros derrotados, você encontra alguns itens valiosos escondidos nas cavernas!")
        time.sleep(1)
        itens()
    else:
        print("Nada de interessante foi encontrado na caverna...")
        pass
    print("Continue explorando para conquistar mais itens e moedas...")

# Caverna grande
def cavernaGrande():
    global monstros
    global inimigo
    global conseguencia
    
    clear()
    print("Você encontrou uma caverna misteriosa durante sua caminhada")
    print("Dela emanava uma forte aura maligna, como se algo muito sombrio estivesse à espreita")
    time.sleep(2)
    print("Você hesita por um momento, mas decide entrar. O que poderia ser mais perigoso do que o que já enfrentou?")
    print("À medida que adentra a caverna, o ambiente fica mais denso e a luz do exterior começa a desaparecer")
    print("Cada passo ecoa, amplificado pelas paredes de pedra que parecem sussurrar segredos antigos...")
    time.sleep(3)
    
    print("À medida que se aprofunda na caverna, um som suave mas inquietante começa a se manifestar à distância")
    print("Sombras estranhas dançam pelas paredes, e você percebe que não está sozinho...")
    time.sleep(2)
    
    if conseguencia == True:
        # Primeira batalha - Fadas
        inimigo = "Fadas"
        print(f"Você encontrou um grupo de duas {monstros[inimigo]['Nome']}! Eles emitem uma luz sobrenatural")
        print("Começam a atacar com feitiços de ilusão")
        print(f"Prepare-se para a batalha!")
        batalha()
        batalha()
        time.sleep(1)
        
        # Segunda batalha - Ogros
        inimigo = "Ogro"
        print(f"Após derrotar as fadas, você se depara com um {monstros[inimigo]['Nome']} gigante bloqueando o caminho")
        print("O ogro está pronto para esmagá-lo com sua força brutal")
        print(f"Prepare-se para a batalha!")
        batalha()
        time.sleep(1)
        
        # Boss final - MoonLord
        inimigo = "MoonLord"
        print(f"Após derrotar os inimigos anteriores, {personagem['Nome']} entra em uma sala secreta")
        print("Você encontra tecnologia alienígena, jamais vista antes")
        print("Você vê imagens de um reino perdido, do caos causado pela ganância do Lorde da Lua")
        time.sleep(2)
        print("A história de uma civilização destruída por sua corrupção se desenrola diante de seus olhos...")
        print("Você agora está nos domínios do MoonLord, ele está esperando por você")
        print(f"Você encontra o Boss {monstros[inimigo]['Nome']}!")
        print("Prepare-se para a batalha final, o destino do mundo está em suas mãos!")
        batalha()
        time.sleep(2)
    else:
        # Segunda batalha - Fadas
        inimigo = "Fadas"
        print(f"Você encontrou um grupo de duas {monstros[inimigo]['Nome']}! Eles emitem uma luz sobrenatural")
        print("Começam a atacar com feitiços de ilusão")
        print(f"Prepare-se para a batalha!")
        batalha()
        batalha()
        time.sleep(1)
        
        # Segunda batalha - Pessoa desconhecida
        inimigo = "Pessoaﾠdesconhecida"
        print(f"Após derrotar as fadas, uma figura misteriosa aparece no caminho")
        print(f"Essa {monstros[inimigo]['Nome']} parece não ter intenções amigáveis")
        print(f"Prepare-se para a batalha!")
        batalha()
        time.sleep(1)
        
        # Terceira batalha - Ogros
        inimigo = "Ogro"
        print(f"Você avança, mas se depara com outro dois {monstros[inimigo]['Nome']} gigante!")
        print("O ogro parece ainda mais forte, e ele se prepara para esmagá-lo com um golpe mortal!")
        print(f"Prepare-se para a batalha!")
        batalha()
        batalha()
        time.sleep(1)
 
        # Boss final - MoonLord
        inimigo = "MoonLord"
        print(f"Após derrotar os inimigos anteriores, {personagem['Nome']} entra em uma sala secreta")
        print("Você encontra tecnologia alienígena, jamais vista antes")
        print("Você vê imagens de um reino perdido, do caos causado pela ganância do Lorde da Lua")
        time.sleep(2)
        print("A história de uma civilização destruída por sua corrupção se desenrola diante de seus olhos...")
        print("Você agora está nos domínios do MoonLord, ele está esperando por você")
        print(f"Você encontra o Boss {monstros[inimigo]['Nome']}!")
        print("Prepare-se para a batalha final, o destino do mundo está em suas mãos!")
        batalha()
        time.sleep(2)
    
    print("Parabéns, você derrotou o MoonLord e completou a caverna!")
    time.sleep(2)
    print("Obrigado por acabar o nosso jogo!")
    time.sleep(1)
    print("Mas a guerra não acabou. Outros perigos podem surgir a qualquer momento.")
    time.sleep(3)
    exit()

# Lugar para poder recuperar vida e comprar poção
def vila():
    global personagem
    global conseguencia
    
    clear()
    chance = random.randint(1, 10)
    print("Você chegou a vila")
    print("Você pode visitar lugares pra recuperar vida e mercadores pra comprar poções\n")
    if chance >= 7:
        NPC()
    else:
        opcaoVila()
        
# Opões de escolha da vila   
def opcaoVila():
    clear()
    print("Você chegou em uma vila")
    print("Você pode visitar lugares pra recuperar vida e mercadores pra comprar poções")
    
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

# NPCS que irão falar uma mensagem
def NPC():
    clear()
    global personagem
    npc = random.randint(1, 25)
    print("Você chegou a vila")
    print("Você pode visitar lugares pra recuperar vida e mercadores pra comprar poções")
    
    if npc >= 24:
        moeda = random.randint(1, 10)
        print("NPC: Isso é um assalto!")
        print("NPC: Passe suas moedas ou eu vou te furar todo!")
        personagem["Moeda"] -= moeda
        print(f"Você perdeu R$: {moeda} moedas")
        print(f"Dinheiro total: {personagem['Moeda']}")
        time.sleep(1)
        opcaoVila()
        

    elif npc >= 1 and npc <= 5:
        quantidade = random.randint(1, 25)
        print("NPC: Olá amigo, sou um caçador!")
        print(f"NPC: Traga {quantidade} cabeças de monstros para receber uma quantia em moedas!")
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
            print("NPC: Ouvi rumores de uma misteriosa caverna em ruinas que habita um ser maligno")
            print("NPC: dizem por ai que ele é o motivo do nosso mundo ser assim...")
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
                print("NPC: Sinto uma aura ruim emanando de você...")
                time.sleep(1)
                opcaoVila()
            else:
                print("NPC: Sinto uma aura bondosa emanando de você..")
                time.sleep(1)
                opcaoVila()
        elif fala <= 19:
            print("NPC Mudo: ...")
            time.sleep(1)
            opcaoVila()
        elif fala == 20:
            print("Gato Preto: Miau, Miau, Miau")
            personagem["Atributos"]['Sorte'] += 1
            time.sleep(1)
            opcaoVila()

# Sistema para recuperar vida e estamina
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
                print("Você não tem moeda suficiente")
                print("Caia fora do meu motel!")
                time.sleep(1)
                vila()
            else:
                clear()
                personagem['Moeda'] -= 10 
                personagem['Atributos']['Vida'] = personagem['VidaInicial']
                personagem['Estamina'] = personagem['EstaminaInicial']
                print(f"você ainda tem R$: {personagem['Moeda']}")
                print(f"Sua saude esta recuperado: \nVida: {personagem['Atributos']['Vida']} \nEstamina: {personagem['Estamina']}")
                time.sleep(1)
                clear()
                opcaoVila()
        case 2:
            opcaoVila()
        case _:
            print("Opção Inválida!")
            time.sleep(1)
            motel()
  
# Sistema para comprar poções
def mercador():
    global personagem
    clear()
    
    while True:
        print("Bem vindo ao meu mercado, viajante!")
        print("Oque gostaria de comprar?")
        print(f"Suas moedas: {personagem['Moeda']}")
        opcao = int(input("1- R$: 25 Poção de cura \n2- R$: 50 Poção de Dano \n3- R$: 75 Poção de sorte \n4- Sair \nOpção: "))
        
        match opcao:
            case 1:
                if personagem["Moeda"] >= 25:
                    personagem["Moeda"] -= 25
                    personagem["Mochila"]['Cura']['Quantidade'] += 1
                    print(f"Você esta agora com {personagem["Mochila"]['Cura']['Quantidade']}")
                    print(f"Moeda: {personagem["Moeda"]}")
                else:
                    print("Você não tem moeda suficiente!")
                    time.sleep(1)
                    clear()   
            case 2:
                if personagem["Moeda"] >= 50:
                    personagem["Moeda"] -= 50
                    personagem["Mochila"]['Dano']['Quantidade'] += 1
                    print(f"Você esta agora com {personagem["Mochila"]['Dano']['Quantidade']}")
                    print(f"Moeda: {personagem["Moeda"]}")
                else:
                    print("Você não tem moeda suficiente!")
                    time.sleep(1)
                    clear()   
            case 3:
                if personagem["Moeda"] >= 75:
                    personagem["Moeda"] -= 75
                    personagem["Mochila"]['Sorte']['Quantidade'] += 1
                    print(f"Você esta agora com {personagem["Mochila"]['Sorte']['Quantidade']}")
                    print(f"Moeda: {personagem["Moeda"]}")
                else:
                    print("Você não tem moeda suficiente!")
                    time.sleep(1)
                    clear()  
            case 4:
                opcaoVila()
            case _:
                print("Opção Inválida!")
                time.sleep(1)
                clear()   

print(iniciarJogo())
