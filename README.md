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
Verifica o sistema de operação da maquina se é **Windows** ou **Linux** e limpa a tela

### def recompensa():
**recompensa** está sendo chamado após um inimigo ser derrotado no **def batalha():**, ai começa a chamar as estruturas como global, faz um ganhoMoeda = random pra dar uma certa quantidade de dinheiro, aumenta as kills para + 1 e as moedas do personagem, reseta a vida inical do mostros[inimigo] e da um print com um if dentro que verifica o genero do mostro  e mostra os ganhoos




### def clear():

