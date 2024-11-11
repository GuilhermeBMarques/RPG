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
