import os
import time

personagem = {}

def clear():
    if os.name == 'nt': 
        os.system('cls')
    else: 
        os.system('clear')

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
    print("O jogo funcionara com os seguintes comando")
    print("O jogo tera escolha por numeros")
    
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
    
    print("Bem vindo a Terra do Bug!") 
    print("Voce é uma pessoa que procura por uma aventura pelo mundo sendo um heroi, vc pega suas coisas e vai pelo mundo a fora, oque o destino escolhera ao seu personagem?\n")
    time.sleep(5) 
    
    print("De uma vida ao seu personagem: ")
    nome = str(input("Digite o nome do seu personagem: "))
    idade = int(input("Digite a idade do seu personagem: "))
    
    print("\nEscolha um personagem:")
    print("Cada personagem tem seu atributos unicos")
    
    opcao = int(input("1- ⚔️ㅤGuerreiro \n2- 🧙 Mago \n3- 🏹 Arqueiro \n4- Voltar \nOpção: "))
    
    match opcao:
        case 1: 
            clear()
            personagem = {
                "Nome": nome,
                "Idade": idade,
                "Classe": "⚔️ㅤGuerreiro",
                "Atributos": {
                    "Vida": 100,
                    "Forca": 17,
                    "Sorte": 3,
                    "XP": 0,
                },
                "Mochilha": {
                    "Moeda": 0,
                    "Cura": 2,
                },
                "Habilidades": ["Ataque Brutal", "Escudo de Ferro"]
            }
            escolha()
        
        case 2:
            clear()
            personagem = {
                "Nome": nome,
                "Idade": idade,
                "Classe": "🧙 Mago",
                "Atributos": {
                    "Vida": 100,
                    "Forca": 14,
                    "Sorte": 4,
                    "XP": 0,
                },
                "Mochilha": {
                    "Moeda": 0,
                    "Cura": 2,      
                    "Mana": 3,        
                },
                "Habilidades": ["Bola de Fogo", "Relâmpago em Cadeia"]
            }
            escolha()
            
        case 3:
            clear()
            personagem = {
                "Nome": nome,
                "Idade": idade,
                "Classe": "🏹 Arqueiro",
                "Atributos": {
                    "Vida": 125,
                    "Forca": 12,
                    "Sorte": 7,
                    "XP": 0,
                },
                "Mochilha": {
                    "Moeda": 0,
                    "Cura": 2,
                },
                "Habilidades": ["Tiro Preciso", "Camuflagem"]
            }
            escolha()
            
        case 4:
            iniciarJogo() 
        case _:
            print("Opção Invalida!")
            time.sleep(1) 
            novoJogo()
            
def escolha():
    global personagem
    print(f"\nVocê escolheu a classe: {personagem['Classe']}")
    print("Build:")
    print(f"Atributos: {personagem['Atributos']}")
    print(f"Habilidades: {personagem['Habilidades']}")
    
    a = int(input("\nVoce tem certeza? \n1- Sim \n2- Voltar \nOpção: "))
    match a:
        case 1:
            partida()
        case 2:
            novoJogo()
        case _:
            print("Opção Invalida!")
            time.sleep(1)
            escolha()

def partida():
    global personagem
    
    print("Ola")
    
print(iniciarJogo())
