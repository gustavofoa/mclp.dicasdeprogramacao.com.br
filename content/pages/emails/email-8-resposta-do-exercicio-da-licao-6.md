title: RESPOSTA do exercício da lição 6.
slug: email-8-resposta-do-exercicio-da-licao-6
template: email

Ontem eu enviei pra você a lição #6 do **minicurso de lógica de programação**. No final da lição eu pedi pra você resolver um exercício de lógica para informar a posição de uma letra no alfabeto usando a estrutura ESCOLHA-CASO.

Espero que você tenha tentado fazer sozinho.

Eu escrevi um algoritmo com a solução deste exercício usando a estrutura ESCOLHA-CASO. Dê uma olhada.

```
algoritmo "Posição da letra no alfabeto"
var
  letra : CARACTERE
  posicao : INTEIRO
inicio

      ESCREVA("Digite uma letra: ")
      LEIA(letra)

      ESCOLHA letra
          CASO "a"
              posicao := 1
          CASO "b"
              posicao := 2
          CASO "c"
              posicao := 3
          CASO "d"
              posicao := 4
          CASO "e"
              posicao := 5
          CASO "f"
              posicao := 6
          CASO "g"
              posicao := 7
          CASO "h"
              posicao := 8
          CASO "i"
              posicao := 9
          CASO "j"
              posicao := 10
          CASO "k"
              posicao := 11
          CASO "l"
              posicao := 12
          CASO "m"
              posicao := 13
          CASO "n"
              posicao := 14
          CASO "o"
              posicao := 15
          CASO "p"
              posicao := 16
          CASO "q"
              posicao := 17
          CASO "r"
              posicao := 18
          CASO "s"
              posicao := 19
          CASO "t"
              posicao := 20
          CASO "u"
              posicao := 21
          CASO "v"
              posicao := 22
          CASO "w"
              posicao := 23
          CASO "x"
              posicao := 24
          CASO "y"
              posicao := 25
          CASO "z"
              posicao := 26
      FIMESCOLHA

      ESCREVA("A letra ", letra, " está na posição ", posicao, " do alfabeto.")

fimalgoritmo
```

Olha um resultado da execução deste algoritmo.

![resultado do algoritmo da letra do alfabeto](http://mclp.dicasdeprogramacao.com.br/images/resultado-letra-do-alfabeto.png){:style="text-align:center;"}

É possível implementar um algoritmo com a estrutura SE-ENTÃO-SENÃO, mas ficaria bem maior. Veja só um inicio deste algoritmo.

```
algoritmo "Posição da letra no alfabeto com SE"
var
  letra : CARACTERE
  posicao : INTEIRO
inicio

      ESCREVA("Digite uma letra: ")
      LEIA(letra)

      SE letra = "a" ENTÃO
            posicao := 1
      SENÃO
            SE letra = "b" ENTÃO
                  posicao := 2
            SENÃO
                  SE letra = "c" ENTÃO
                        posicao := 3
                  SENÃO
                        SE letra = "d" ENTÃO
                              posição := 4
                        SENÃO
                              SE letra = "e" ENTÃO
                                    posicao := 5
                              SENÃO
                                    SE ....
                                    .....
                                    FIMSE
                              FIMSE
                        FIMSE
                  FIMSE
            FIMSE
      FIMSE

      ESCREVA("A letra ", letra, " está na posição ", posicao, " do alfabeto.")

fimalgoritmo
```

Bom agora eu tenho uma surpresa pra você!
Se você acompanhou esse exercício até aqui e está gostando do minicurso,
eu vou te ensinar como fazer todo o trabalho dessa estrutura ESCOLHA-CASO
com apenas UMA LINHA de código e sem usar nenhuma estrutura de controle de fluxo!

Isso mesmo, um algoritmo que diz a ordem da letra no alfabeto
sem usar nenhuma estrutura de controle de fluxo como você aprendeu nas duas últimas lições.
Ficou curioso? A malandragem é a seguinte...

Na computação, todos os caracteres tem um correspondente numérico
para que este caractere possa ser armazenado na forma de bits.

Existe uma tabela chamada **Tabela ASCII** para sabermos qual o número de uma letra.
E as letras do alfabeto estão em sequência nesta tabela.

Veja a baixo uma parte da tabela ASCII e identifique o valor numérico do caractere "a".

| Número  | Caractere | Número  | Caractere | Número  | Caractere | Número  | Caractere | Número  | Caractere | Número  | Caractere |
|---      |---        |---      |---        |---      |---        |---      |---        |---      |---        |---      |---        |
| 32      | ESPAÇO    | 48      | 0         | 64      | @         | 80      | P         | 96      | `         | 112     | p         |
| 33      | !         | 49      | 1         | 65      | A         | 81      | Q         | 97      | a         | 113     | q         |
| 34      | "         | 50      | 2         | 66      | B         | 82      | R         | 98      | b         | 114     | r         |
| 35      | #         | 51      | 3         | 67      | C         | 83      | S         | 99      | c         | 115     | s         |
| 36      | $         | 52      | 4         | 68      | D         | 84      | T         | 100     | d         | 116     | t         |
| 37      | %         | 53      | 5         | 69      | E         | 85      | U         | 101     | e         | 117     | u         |
| 38      | &         | 54      | 6         | 70      | F         | 86      | V         | 102     | f         | 118     | v         |
| 39      | '         | 55      | 7         | 71      | G         | 87      | W         | 103     | g         | 119     | w         |
| 40      | (         | 56      | 8         | 72      | H         | 88      | X         | 104     | h         | 120     | x         |
| 41      | )         | 57      | 9         | 73      | I         | 89      | Y         | 105     | i         | 121     | y         |
| 42      | *         | 58      | :         | 74      | J         | 90      | Z         | 106     | j         | 122     | z         |
| 43      | +         | 59      | ;         | 75      | K         | 91      | [         | 107     | k         | 123     | {         |
| 44      | ,         | 60      | <         | 76      | L         | 92      | \         | 108     | l         | 124     | |         |
| 45      | -         | 61      | =         | 77      | M         | 93      | ]         | 109     | m         | 125     | }         |
| 46      | .         | 62      | >         | 78      | N         | 94      | ^         | 110     | n         | 126     | ~         |
| 47      | /         | 63      | ?         | 79      | O         | 96      | _         | 111     | o         | 127     | DELETE    |

Viu que o valor do caractere "a" é 97 e que as outras letras estão na sequência? b = 98, c = 99, d = 100, ...

Agora ficou fácil, só precisamos descobrir o valor da letra que o usuário digitou e subtrair 96. Certo?

Para descobrir o valor ASCII de um caractere no Visualg, podemos utilizar a _função ASC_,
passando como parâmetro a letra que o usuário digitou.

**Importante!** Vamos falar mais sobre ***funções*** e ***procedimento*** na lição 10, não se preocupe.
Por hora só saiba que uma função executa uma tarefa pra gente.
(Talvez a função ASC use a estrutura ESCOLHA-CASO internamento para retornar o número ASCII da letra.)

A função ASC(caracter) retorna o número da tabela ASCII da letra que passamos como parâmetro.

Logo, o nosso algoritmo ficaria assim.

```
algoritmo "Posição da letra no alfabeto"
var
  letra : CARACTERE
  posicao : INTEIRO
inicio

      ESCREVA("Digite uma letra: ")
      LEIA(letra)

      posicao := ASC(letra) - 96

      ESCREVA("A letra ", letra, " está na posição ", posicao, " do alfabeto.")

fimalgoritmo
```

O resultado é o mesmo do algoritmo que usa a estrutura ESCOLHA-CASO ou SE-ENTÃO-SENÃO.

Gostou dessa sacada?

Na nossa próxima lição vamos aprender a usar as estruturas de repetição.

Fique atento ao seu e-mail que enviarei o link da próxima lição amanhã!

Até mais ...
