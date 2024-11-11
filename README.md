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

### def clear():

