# RPG
Este RPG é baseado em escolhas por números. O funcionamento é simples: você escolherá uma classe de personagem de acordo com sua preferência e precisará explorar várias cavernas até desbloquear a **caverna misteriosa**. Cada caverna tem uma dificuldade crescente: a caverna pequena dá 1 ponto, a caverna média dá 2 pontos, lembrando que cada caverna maior será mais desafiadora e terá mais chances de oferecer **itens** melhores! O jogo será finalizado quando você conquistar a **caverna misteriosa**. Boa sorte na sua jornada!


# Explicação do codigo
importações e estruturas do personagem, monstros e armas
```
import os
import time
import random

personagem = {}
inimigo = {}
conseguencia = False

ArmasGuerreiro = {}

ArmasMago = {}

ArmasArqueiro = {}

ArmasInvocador = {}

monstros = {}
```

### def itens()
Chama a variável global do **personagem** para atualizar o seu item em `ArmasGuerreiro[]` que inicia vazio, dependendo da classe que o jogador escolheu, o codigo verifica o indentificador pelo `if personagem["Identificador"] == "Guerreiro":` e escolha aleatoriamente uma arma do **ArmasGuerreiro** usando **random.choice()** que recebe string ou int, depois faz a listagem e o key retorna todas as armas do ArmasGuerreiro em uma lista, em seguida retorna uma arma sorteada, retorna um print mostrando a arma atual dele e pergunta o jogador deseja trocar, se o jogador querer trocar,  a nova arma é adicionada à mochila do **personagem** com `personagem['Mochila']['ArmasGuerreiro'] = {armasRandom: ArmasGuerreiro[armasRandom]}`.

### def clear()
Verifica a operação da maquina se é **Windows** ou **Linux** ele limpa a tela.

### def batalha()
Função de `batalha()` onde o **personagem** do **jogador** enfrenta um monstro, com base em escolhas e turnos, até que a vida de um dos dois chege a zero, ou o **jogador** consgiga fugir
```
while personagem['Atributos']['Vida'] > 0 and monstros[inimigo]['Vida'] > 0:
        opcao = int(input("Deseja: \n1- Atacar \n2- Usar Mochila \n3- Fugir \nOpção: "))
```
O **jogador** pode escolher entre **atacar**, **usar itens** da mochila ou **tentar fugir**, se ele atacar o ataque causa dano baseado nas armas do **personagem**, e o monstro pode atacar de volta, se o dano do monstro atingir a vida do **jogador** a zero, ele perde e leva para `playerMorto()`, se ele usar itens, pode tanto se curar, aumentar o dano ou a sorte do **personagem**, se ele tentar fugir tem uma chance de conseguir, em caso que ele n consegue, o monstro ataca novamente, o jogo continua até que um dos lados vença ou o **jogador** fuja com sucesso, tambem tem uma verificação com o **identificador** pra ver a classe ele ta usando e definir o uso de arma dele.

### def playerMorto()
Gerencia a interação quando o **jogador** morre no jogo, ela exibe uma mensagem informando o nome do inimigo que matou o **jogador**, mostrando as estatísticas do **jogador**, como o número de inimigos mortos e cavernas exploradas, após isso, o **jogador** é perguntado se deseja reiniciar o `novoJogo` ou retornar ao `iniciarJogo`, variáveis globais como **personagem**, monstros e inimigo são utilizadas para acessar as informações necessárias.

### def recompensa()
**recompensa** está sendo chamado após um inimigo ser derrotado dentro da função **batalha()**, depois declara as variaveis globais para atualizar as quantidades de moedas e as kills, `ganhoMoeda = random.randint(1, 10)`, `personagem['Kills'] += 1`, em seguida reseta a vida do inical do inimigo pela sua inicial, e exibe uma mensagem de qual genero do inimigo derrotado, e mostra as recompensas.

### def iniciarJogo()
Menu inicial do jogo "Civilização Zero", exibe três **opções:** **iniciar** um **novo jogo**, **instruções** ou **sair**, se a escolha for 1, a função chama `novoJogo()`, se for 2, chama `instrucoes()`, se for 3, o programa termina.

### def instrucoes()
Exibe as instruções do jogo no terminal, informando ao jogador como os comandos funcionam, o objetivo do jogo e como interagir com o sistema.

### def novoJogo()
Inicia um novo jogo, apresentando uma introdução da historia e solicitando ao **jogador** o **nome**, **idade** e a escolha da **classe** do **personagem**, com base na escolha, ela cria um dicionário contendo as informações do personagem, incluindo atributos como vida, dano, sorte, habilidades e itens da mochila, o **jogador** pode escolher entre quatro classes: Guerreiro, Mago, Arqueiro ou Invocador, e as informações são armazenadas no `personagem = {}` conforme a classe selecionada.

### def escolhaPersonagem()
Exibe as informações do **personagem** selecionado, como classe, atributos (vida, dano e sorte) e habilidades, em seguida, pede ao **jogador** para confirmar a escolha, se o jogador confirmar opção 1, o jogo segue para o `tutorial()`, enquanto se escolher voltar, ele retorna `novoJogo()`, se a entrada for inválida, uma mensagem de erro é exibida.

### def tutorial()
Inicia o enredo do jogo, onde o jogador onde tem seu nome armazenado em `personagem['Nome']` confrontado com duas **escolhas:** investigar ou ir embora, se o **jogador** fugir, o personagem perde pontos de sorte `personagem['Atributos']['Sorte'] -= 2` e uma consequência é marcada `conseguencia = True`, se o **jogador** investigar, encontra um Goblin atacando na floresta, iniciando a sua primeira `batalha()`, após derrotar o inimigo, o personagem recebe uma recompensa em moedas `personagem['Moeda'] += ganhoMoeda + 2` de um random ganhoMoeda, jogo então prossegue com a `exploracao()`.

### def exploracao()
Exploração do **personagem** em diferentes caminhos, com base no nível de estamina do **personagem**, permite que ele explore áreas diversas **incluem:** estradas, vilas, cavernas, locais abandonados, inimigos, bolsas no chão, cada área consome estamina `personagem["Estamina"] -= 2` e pode oferecer recompensas, como moedas, ou batalhas contra monstros, utiliza variáveis globais para acessar informações do **personagem** e dos **monstros**, e armazena o caminho salvo para evitar que o **personagem** quando clicar em uma opção invalida, ele vai pra um caminho.

### def cavernaPequena()
Uma caverna onde o **jogador** enfrenta duas batalhas contra monstros aleatórios, exceto o "MoonLord"
`inimigo = random.choice([m for m in monstros.keys() if m != "MoonLord"])`, após derrotar os inimigos, a caverna é marcada como **explorada** e o **jogador** tem uma chance `chance = random.randint(1, 10)` de encontrar uma arma para classe dele
```
personagem['CavernaExplorada'] = personagem['CavernaExplorada'] + 1
    if chance >= 7:
        print("Enquanto explora os restos dos monstros derrotados, você encontra alguns itens valiosos escondidos nas cavernas!")
        time.sleep(2)
        itens()
```
sistema com if para verificar inimigo e não repetir o mesmo monstros 
```
inimigo2 = random.choice([m for m in monstros.keys() if m != inimigo and m != "MoonLord" and m not in inimigo and m not in inimigo])
    inimigo = inimigo2
```
se nada for encontrado, o jogo incentiva a continuação da exploração, e volta para `exploracao()`.

### def cavernaMedia()
Uma caverna onde o **jogador** enfrenta três batalhas contra monstros aleatórios, exceto o "MoonLord"
`inimigo = random.choice([m for m in monstros.keys() if m != "MoonLord"])`, após derrotar os inimigos, a caverna é marcada como **explorada**" e o **jogador** tem uma chance `chance = random.randint(1, 10)` de encontrar uma arma para classe dele
```
personagem['CavernaExplorada'] = personagem['CavernaExplorada'] + 2
    if chance >= 5:
        print("Enquanto explora os restos dos monstros derrotados, você encontra alguns itens valiosos escondidos nas cavernas!")
        time.sleep(2)
        itens()
```
sistema com if para verificar inimigo e não repetir o mesmo monstros 
```
inimigo2 = random.choice([m for m in monstros.keys() if m != inimigo and m != "MoonLord" and m not in inimigo and m not in inimigo])
    inimigo = inimigo2
```
se nada for encontrado, o jogo incentiva a continuação da exploração, e volta para `exploracao()`.

### def cavernaGrande()
Caverna final que enfrenta uma série de batalhas, dependendo do valor da variável conseguencia no começo do jogo, o jogador enfrentará diferentes sequências de inimigos, incluindo **fadas**, **ogros** e o **boss final:** **MoonLord**
```
if conseguencia == True:
        # Primeira batalha - Fadas
        inimigo = "Fadas"
        print(f"Você encontrou um grupo de duas {monstros[inimigo]['Nome']}! Eles emitem uma luz sobrenatural")
        print("Começam a atacar com feitiços de ilusão")
        print(f"Prepare-se para a batalha!")
        batalha()
        batalha()
```
a função utiliza a `batalha()` para gerenciar os confrontos, após derrotar o MoonLord, o jogo termina com uma mensagem de agradecimento

### def vila()
Simula a chegada do **personagem** à **vila**, com uma chance de encontrar **NPCS** ou o **mercador** e locais de **cura**, se `chance = random.randint(1, 10)` for `if chance >= 7:` gera uma função `NPC()`.

### def opcaoVila()
Intereção com o **jogador** para levar a uma parte da vila, **incluem:** motel, mercador e exploracao.

### def NPC()
Interação com o jogador em uma vila, selecionando aleatoriamente o tipo de encontro com `npc = random.randint(1, 25)` dependendo do numero gerado, um npc tera dialago com o jogador, **incluem:** rumores sobre uma caverna misteriosa, uma saudação personalizada ao jogador, observações sobre a aura do personagem, ou uma interação silenciosa com um NPC, uma queste de matar monstros e com um gato preto que aumenta a sorte do **personagem**.

### def motel()
Utiliza a variável global **personagem** para saber quantas moedas você tem na mochila, caso o jogador tenha 10 ou mais moedas, o jogo subtrai 10 moedas do inventário e restaura a vida `personagem['Atributos']['Vida'] = personagem['VidaInicial']` e a estamina `personagem['Estamina'] = personagem['EstaminaInicial']` do jogador para seus valores iniciais.
```
    personagem['Moeda'] -= 10 
    personagem['Atributos']['Vida'] = personagem['VidaInicial']
    personagem['Estamina'] = personagem['EstaminaInicial']
    print(f"você ainda tem R$: {personagem['Moeda']}")
    print(f"Sua saude esta recuperado: \nVida: {personagem['Atributos']['Vida']} \nEstamina: {personagem['Estamina']}")
```
se o jogador tiver menos de 10 moedas, uma mensagem informa que ele não tem dinheiro suficiente e o redireciona para a vila.

### def mercador()
Utiliza a variável global **personagem** para saber a quantidade de poções e de moedas que tem na mochila, se o quantidade de moedas for igual ou maior do que o preço da poção selecionada `if personagem["Moeda"] >= 25:` a função desconta o valor e aumentada em `personagem["Mochila"]['Cura']['Quantidade'] += 1` de poção comprada na mochila 
```
match opcao:
    case 1:
        if personagem["Moeda"] >= 25:
            personagem["Moeda"] -= 25
            personagem["Mochila"]['Cura']['Quantidade'] += 1
            print(f"Você esta agora com {personagem["Mochila"]['Cura']['Quantidade']}")
            print(f"Moeda: {personagem["Moeda"]}")
```
caso o **personagem** não tenha moedas suficientes, é exibida uma mensagem informando que ele não possui moedas suficientes para a comprar, e retorna pra **vila()**.

