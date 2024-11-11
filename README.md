# RPG
Este RPG é baseado em escolhas por números. O funcionamento é simples: você escolherá uma classe de personagem de acordo com sua preferência e precisará explorar várias cavernas até desbloquear a **caverna misteriosa**. Cada caverna tem uma dificuldade crescente: a caverna pequena dá 1 ponto, a caverna média dá 2 pontos, lembrando que cada caverna maior será mais desafiadora e terá mais chances de oferecer **itens** melhores! O jogo será finalizado quando você conquistar a **caverna misteriosa**. Boa sorte na sua jornada!


# Explicação do codigo
## Estruturas
Estrutura basica para armazenar as classes dos personagens, itens e monstros
```
import os
import time
import random

personagem = {}
inimigo = {}
conseguencia = False

# Armas das classes dos personagens
ArmasGuerreiro = {
}

ArmasMago = {
}

ArmasArqueiro = {
}

ArmasInvocador = {
}

# Monstros
monstros = {
}
```
## def itens()
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
```
```
```
```
```
```
```
```
```
```
```
``````
```
