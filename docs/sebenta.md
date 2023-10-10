---
title: Sebenta de TTI - FTT
author:
 - Tiago Barata
 - J.J. Almeida
date: 2023
---

# Cultura geral

## Sublime Text

### Comandos úteis

~~~ 
   Alt            Mostra o barra de menu
   Ctrl+F         find
   Ctrl+H         find-replace
   Ctrl+Shift+F   find-grep! (selecionar ou não contexto/ER/...)
   Alt+F3         to multi-select all occurences.
   Ctrl+L         (Expand Selection to Line).
   Ctrl+G         goto to line
   Ctrl+N         new buffer/file
~~~ 

selecionar bloco = shit+botaoDir

Preferences → Settings – Distraction Free 

### Abrir uma tab

~~~
[view]→[layout]→[columns1]   

ou 

(Alt+Shift+1)
~~~

### Abrir duas tabs

~~~
[view]→[layout]→[columns2]   

ou 

(Alt+Shift+2)
~~~

- Mastering your text editor
  - Exemplo Sublime
  - configuração
    - encodings
    - distraction free
    - ...
  - Expressões Regulares

### Find

```
- .*     selecionar expressões regulars
- '',,   palavras completas
- Aa     ignore case
- =      find grep com contexto
```

Selecionar + Ctr+F     (contar numero de ocorrências)

Selecionar + Ctr+Shift-F     (Find Grep lista de linhas contendo padrão)

## See Also

- https://regex101.com

# Terminologia

## [NATerm](https://natura.di.uminho.pt/jjbin/naterm)

### Exemplo

~~~
%title Chess Dictionary PT - EN 
%author TBarata
%date 2023-09-27
%lang EN PT
%inv hpr hpn
%rellang EN

== Chess

=== Piece

PT: Rei
+G: m
EN: King
def: The king is the most important piece. The object of the game is to capture the opponants King. The King can move one square in any direction. The King may never move into check. Each player starts with one king.
!img: king.jpg

=== Outcome

PT: Desistir
EN: Resign
def: To concede loss of the game. The traditional way to resign is by tipping over one’s king.
!img: regign.jpg

=== Special Move

PT: Promoção
EN: Promotion
hpr: Special Move
def: When a pawn advances to his opponent’s side of the board, as a part of the move it is promoted and must be exchanged for the player’s choice of queen, rook, bishop, or knight of the same color.  Usually, the pawn is chosen to be promoted to a queen, but in some cases another piece is chosen; this is called underpromotion.There is no restriction placed on the piece that is chosen on promotion, so it is possible to have more pieces of the same type than at the start of the game (for example, two queens).
!img: promotion.gif
~~~

Nota<sub>1</sub> : Os atributos de cada entrada são todos opcionais. Use o mais conveniente.

Nota<sub>2</sub> : Entre cada entrada, é necessário deixar uma linha em branco.

Nota<sub>3</sub> : As imagens devem ser colocadas numa pasta MEDIA.zip e carregada juntamente com a terminologia.

## goldendict e o formato XDXF

XDXF = XML Dictionary eXchange Format

# Alinhadores

## LF Aligner

# CAT Tools

## SmartCat

## OmegaT

