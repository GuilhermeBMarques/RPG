# RPG
Este RPG é baseado em escolhas por números. O funcionamento é simples: você escolherá uma classe de personagem de acordo com sua preferência e precisará explorar várias cavernas até desbloquear a **caverna misteriosa**. Cada caverna tem uma dificuldade crescente: a caverna pequena dá 1 ponto, a caverna média dá 2 pontos, lembrando que cada caverna maior será mais desafiadora e terá mais chances de oferecer **itens** melhores! O jogo será finalizado quando você conquistar a **caverna misteriosa**. Boa sorte na sua jornada!


# Explicação do codigo
### def itens():
```
def itens():
    clear()
    global personagem
    print("Após derrotar todos os monstros da caverna você")
    
    if personagem["Identificador"] == "Guerreiro":
        armasRandom = random.choice(list(ArmasGuerreiro.keys()))
        print(f"Sua arma atual: {personagem['Mochila']['ArmasGuerreiro']}\n")
        print(f"{personagem['Nome']} encontrou uma {ArmasGuerreiro[armasRandom]['Nome']} \nRaridade: {ArmasGuerreiro[armasRandom]['Raridade']} \nDano: {ArmasGuerreiro[armasRandom]['Dano']}")
        opcao = int(input("Você deseja coletar o item? \n1- Coletar \n2- Não Pegar \nOpção: "))

        match opcao:
            case 1:
                personagem['Mochila']['ArmasGuerreiro'] = {armasRandom: ArmasGuerreiro[armasRandom]}
                print(f"{personagem['Nome']} pegou a {ArmasGuerreiro[armasRandom]} e colocou na mochila.")
            case 2:
                print("Você deixou o item no chão, talvez algum outro aventureiro faça um melhor uso...")
            case _:
                print("Opção Inválida!")
                time.sleep(1)
                itens()
    
    elif personagem["Identificador"] == "Mago":
        armasRandom = random.choice(list(ArmasMago.keys()))
        print(f"Sua arma atual: {personagem['Mochila']['ArmasMago']}\n")
        print(f"{personagem['Nome']} encontrou uma {ArmasMago[armasRandom]['Nome']} \nRaridade: {ArmasMago[armasRandom]['Raridade']} \nDano: {ArmasMago[armasRandom]['Dano']}")
        
        opcao = int(input("Você deseja coletar o item? \n1- Coletar \n2- Não Pegar \nOpção: "))

        match opcao:
            case 1:
                personagem['Mochila']['ArmasMago'] = {armasRandom: ArmasMago[armasRandom]}
                print(f"{personagem['Nome']} pegou a {ArmasMago[armasRandom]} e colocou na mochila.")
            case 2:
                print("Você deixou o item no chão, talvez algum outro aventureiro faça um melhor uso...")
            case _:
                print("Opção Inválida!")
                time.sleep(1)
                itens()

    elif personagem["Identificador"] == "Arqueiro":
        armasRandom = random.choice(list(ArmasArqueiro.keys()))
        print(f"Sua arma atual: {personagem['Mochila']['ArmasArqueiro']}\n")
        print(f"{personagem['Nome']} encontrou uma {ArmasArqueiro[armasRandom]['Nome']} \nRaridade: {ArmasArqueiro[armasRandom]['Raridade']} \nDano: {ArmasArqueiro[armasRandom]['Dano']}")
        opcao = int(input("Você deseja coletar o item? \n1- Coletar \n2- Não Pegar \nOpção: "))

        match opcao:
            case 1:
                personagem['Mochila']['ArmasArqueiro'] = {armasRandom: ArmasArqueiro[armasRandom]}
                print(f"{personagem['Nome']} pegou a {ArmasArqueiro[armasRandom]} e colocou na mochila.")
            case 2:
                print("Você deixou o item no chão, talvez algum outro aventureiro faça um melhor uso...")
            case _:
                print("Opção Inválida!")
                time.sleep(1)
                itens()

    elif personagem["Identificador"] == "Invocador":
        armasRandom = random.choice(list(ArmasInvocador.keys()))
        print(f"Sua arma atual: {personagem['Mochila']['ArmasInvocador']}\n")
        print(f"{personagem['Nome']} encontrou uma {ArmasInvocador[armasRandom]['Nome']} \nRaridade: {ArmasInvocador[armasRandom]['Raridade']} \nDano: {ArmasInvocador[armasRandom]['Dano']}")
        opcao = int(input("Você deseja coletar o item? \n1- Coletar \n2- Não Pegar \nOpção: "))

        match opcao:
            case 1:
                personagem['Mochila']['ArmasInvocador'] = {armasRandom: ArmasInvocador[armasRandom]}
                print(f"{personagem['Nome']} pegou a {ArmasInvocador[armasRandom]} e colocou na mochila.")
            case 2:
                print("Você deixou o item no chão, talvez algum outro aventureiro faça um melhor uso...")
            case _:
                print("Opção Inválida!")
                time.sleep(1)
                itens()

```
### def batalha():
```
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

                print(personagem['Mochila'])
                
                print("Digite o nome do item que deseja usar")
                print("Digite sair caso queira voltar pra batalha")
                opcao = str(input("Deseja usar algum item? \nOpção: ")).capitalize()
                clear()
                if opcao in personagem['Mochila']:
                    if personagem['Mochila'][opcao]['Quantidade'] == 0:
                        print("Vc n tem mais esse item")
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
                            print(f"Voce aumento seu dano para mais: {personagem['Mochila']['Dano']['Porcentagem']}")
                            print(f"Dano: {personagem['Atributos']['Dano']}")
                            
                        elif personagem['Mochila'][opcao] == personagem['Mochila']['Sorte']:
                            personagem['Atributos']['Sorte'] += personagem['Mochila']['Sorte']['Porcentagem']
                            print(f"Voce aumento seu sorte para mais: {personagem['Mochila']['Sorte']['Porcentagem']}")
                            print(f"Sorte: {personagem['Atributos']['Sorte']}")
                        else:
                            pass
                        
                        if monstros[inimigo]['Sorte'] >= chance:
                            print(f"Agora é o turno de {monstros[inimigo]['Nome']}")
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
                if 2 >= fugir:
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
```
### def playerMorto():
```
def playerMorto():
    global personagem
    global monstros
    global inimigo
    
    clear()
    
    if monstros[inimigo]['Sexo'] == "Masculino":
        print(f"Voce morreu para um {monstros[inimigo]['Nome']}!")
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
    else:
        print(f"Voce morreu para uma {monstros[inimigo]['Nome']}!")
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
```
### def recompensa():
```
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
```
### def iniciarJogo():
```
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
```
### def instrucoes():
```
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
```
### def novoJogo():
```
def novoJogo():
    global personagem
    
    clear()
    
    print("Bem-vindo a \033[1mTerra do Bug\033[0m!") 
    print("Se você está procurando uma aventura perigosa, com desafios difíceis, você está no lugar certo!\n")
    print("Dê \033[1mvida\033[0m ao seu herói: ")
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
                "XP": 0,
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
                "XP": 0,
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
                "XP": 0,
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
                "XP": 0,
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

```
