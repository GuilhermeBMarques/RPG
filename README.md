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

### def clear():
Verifica a operação da maquina se é **Windows** ou **Linux** ele limpa a tela

### def recompensa():
**recompensa** está sendo chamado após um inimigo ser derrotado dentro da função **batalha()**, depois declara as variaveis globais para atualizar as quantidades de moedas e as kills, `ganhoMoeda = random.randint(1, 10)`, `personagem['Kills'] += 1`, em seguida reseta a vida do inical do inimigo pela sua inicial, e exibe uma mensagem de qual genero do inimigo derrotado, e mostra as recompensas


### def itens():
Chama a variavel global do personagem para atualizar o seu `ArmasGuerreiro[]` que inicia vazio, dependendo da classe que o jogador escolheu, pelo `if personagem["Identificador"] == "Guerreiro":` e seleciona aleatoriamente uma arma do ArmasGuerreiro que passa pelo choice que recebe string ou int, depois faz a listagem e o key retorna todas as armas do ArmasGuerreiro em uma lista,
depois retorna um print mostrando a arma atual dele e depois acontece uma pergunta se ele quer trocar ou não, caso que ele quer troca a variavel dde `personagem['Mochila']['ArmasGuerreiro'] = {armasRandom: ArmasGuerreiro[armasRandom]}`









### def mercador():
O def puxa o global personagem para saber quantas poções tem na mochila e o dinheiro que você tem.
Se o valor das moedas na sua mochila for igual ou maior do que o preço para comprar a poção ela vai ser aumentada em +1 na "Quantidade" da "Mochila".
Se o Valor das moedas na sua mochila for meno que o valor ele vai printar que não moedas o suficiente
Se você colocar um valor que não esta nas opcções aparecerá uma mensagem de opcção invalida

### def motel():
O def puxa o global personagem para saber quantas moedas você tem na mochila.
Se as moedas da sua Mochila forem menos que 10, sera printado na tela que você não tem dinheiro o suficiente.
Se as Moedas da sua Mochila forem iguais ou maiores que 10, você tera sua vida e estamina redefinidos para a VidaInicial e a EstaminaInicial


### def NPC():
O def vai utilizar um random.randint(1, 25) para definir um numero randomizado.
Um NPC especifico vai pedir uma quantia de Cabeças de monstros que serão igualados ao 
