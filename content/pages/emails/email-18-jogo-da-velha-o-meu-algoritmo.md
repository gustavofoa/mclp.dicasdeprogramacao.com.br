title: Jogo da Velha: O meu Algoritmo! 
slug: email-18-jogo-da-velha-o-meu-algoritmo
template: email

Olá! Estava ancioso por este e-mail?

Na lição #9 eu prometi te enviar o meu algoritmo do jogo da velha após uma semana.

Não é um algoritmo facinho, mas já estamos chegando ao final deste minicurso 
e sei que você tem capacidade de criar este algoritmo sozinho.

Mas tinha que quebrar a cabeça um pouquinho.
Neste exercício, que passei como um desafio para você, 
é necessário utilizar várias estruturas, operadores, variáveis, etc.
Tudo que já aprendemos nas lições anteriores.

Então vamos ao meu algoritmo do jogo da velha, mas antes vamos lembrar as regras:

1 - As jogadas do jogo da velha deverão ser armazenadas numa matriz (3x3) de caractere,
chamada "tabuleiro", cada posição desta matriz armazenará um dos valores: " ", "_", "X" ou "O".
Abaixo uma representação gráfica desta matriz.
```
   1   2   3
1 ___|___|___
2 ___|___|___
3    |   |      
```

2 - A cada jogada o programa deverá mostrar na tela a situação atual do “tabuleiro”.
Por exemplo:
```
   1   2   3
1 ___|___|___
2 ___|_X_|___
3  O |   | O
```

3 - Terão dois jogadores no jogo. O programa deve solicitar o nome dos dois jogadores antes de começar o jogo. A
 cada jogada o programa deverá perguntar separadamente as posições horizontal e vertical da jogada, nesta ordem.

4 - Quando um jogador vencer o jogo, o programa deve apresentar imediatamente o vencedor e a situação do “tabuleiro”.

Abaixo você encontra o meu algoritmo do jogo, você pode copiar e colocar o algoritmo no VisuAlg.

Para baixar o Visualg Acesse: 
[http://dicasdeprogramacao.com.br/download-visualg/](http://www.dicasdeprogramacao.com.br/download-visualg/){:target=blank}

Veja o algoritmo, entenda, [execute-o](http://www.dicasdeprogramacao.com.br/download-visualg/){:target=blank},
observe porque usei cada estrutura PARA-FAÇA, REPIRA-ATÉ, SE-ENTÃO-SENÃO,
cada variável, operadores lógicos (E e OU) etc.

```
algoritmo "JogoDaVelha"
var
  tabuleiro: vetor[1..3,1..3] de caractere
  nomeJogador1, nomeJogador2, jogadorAtual, vencedor : caractere
  linhaJogada, colunaJogada, i, j : inteiro
inicio
  escreval("###Jogo da velha###")
  
  //Inicialização do tabuleiro com "_" nas linhas 1 e 2 e " " na terceira linha
  //i é a linha e j é a coluna.
  para j de 1 ate 3 faca
       para i de 1 ate 2 faca
            tabuleiro[i,j] := "_"
       fimpara
       tabuleiro[3,j] := " "
  fimpara

  escreva("Informe o nome do(a) primeiro(a) jogador(a): ")
  leia(nomeJogador1)
  escreva("Informe o nome do(a) segundo(a) jogador(a): ")
  leia(nomeJogador2)

  escreval("Vamos começar o jogo.")
  
  jogadorAtual := nomeJogador1
  vencedor := ""

  repita
    //Apresenta a situação atual do tabuleiro
    escreval("Neste momento o tabuleiro está assim:")
    escreval("   1   2   3")
    escreval("1 _", tabuleiro[1,1], "_|_", tabuleiro[1,2], "_|_", tabuleiro[1,3], "_")
    escreval("2 _", tabuleiro[2,1], "_|_", tabuleiro[2,2], "_|_", tabuleiro[2,3], "_")
    escreval("3  ", tabuleiro[3,1], " | ", tabuleiro[3,2], " | ", tabuleiro[3,3], " ")

    escreval("É a vez do(a) jogador(a): ", jogadorAtual)

    repita
          repita
              escreva("Informe o número da linha da sua jogada: ")
              leia(linhaJogada)
              //Valida se o usuário digitou um valor válido
              se (linhaJogada < 1) ou (linhaJogada > 3) entao
                 escreval("A linha deve ser entre 1 e 3")
              fimse
          ate (linhaJogada >= 1) e (linhaJogada <= 3)
          repita
              escreva("Informe o número da coluna da sua jogada: ")
              leia(colunaJogada)
              //Valida se o usuário digitou um valor válido
              se ((colunaJogada < 1) ou (colunaJogada > 3)) entao
                 escreval("A coluna deve ser entre 1 e 3")
              fimse
          ate ((colunaJogada >= 1) e (colunaJogada <= 3))
          
          //Valida se a posição jogada á está preenchida
          se (tabuleiro[linhaJogada,colunaJogada] <> "_") e (tabuleiro[linhaJogada,colunaJogada] <> " ") entao
             escreval("A posição ", linhaJogada,", ", colunaJogada, " já está preenchida.")
          fimse
    ate (tabuleiro[linhaJogada,colunaJogada] = "_") ou (tabuleiro[linhaJogada,colunaJogada] = " ")
    
    se jogadorAtual = nomeJogador1 entao
       tabuleiro[linhaJogada,colunaJogada] := "X"
       jogadorAtual := nomeJogador2
    senao
       tabuleiro[linhaJogada,colunaJogada] := "O"
       jogadorAtual := nomeJogador1
    fimse
    
    //Valida se alguem ganhou o jogo
    para j de 1 ate 3 faca
         //Verifica as colunas
         //_X_|_O_|_X_
         //_X_|_O_|_X_
         // X | O | X
         se ((tabuleiro[1,j] = "X") ou (tabuleiro[1,j] = "O")) e (tabuleiro[1,j] = tabuleiro[2,j]) e (tabuleiro[2,j] = tabuleiro[3,j]) entao
            vencedor := tabuleiro[1,j]
         fimse
    fimpara
    para i de 1 ate 3 faca
         //Verifica as linhas
         //_X_|_X_|_X_
         //_O_|_O_|_O_
         // X | X | X
         se ((tabuleiro[i,1] = "X") ou (tabuleiro[i,1] = "O")) e (tabuleiro[i,1] = tabuleiro[i,2]) e (tabuleiro[i,2] = tabuleiro[i,3]) entao
            vencedor := tabuleiro[i,1]
         fimse
    fimpara
    
    //Verifica as diagonais
    //_X_|___|_X_
    //___|_X_|___
    // X |   | X
    se (((tabuleiro[2,2] = "X") ou (tabuleiro[2,2] = "O")) e ((tabuleiro[1,1] = tabuleiro[2,2]) e (tabuleiro[2,2] = tabuleiro[3,3])) ou ((tabuleiro[3,1] = tabuleiro[2,2]) e (tabuleiro[2,2] = tabuleiro[1,3]))) entao
       vencedor := tabuleiro[2,2]
    fimse
    
    //Verifica se deu velha
    se ((vencedor <> "") e (tabuleiro[1,1] <> "_") e (tabuleiro[1,2] <> "_") e (tabuleiro[1,3] <> "_") e (tabuleiro[2,1] <> "_") e (tabuleiro[2,2] <> "_") e (tabuleiro[2,3] <> "_") e (tabuleiro[3,1] <> " ") e (tabuleiro[3,2] <> " ") e (tabuleiro[3,3] <> " ")) entao
         vencedor := "V"
    fimse
    
  ate vencedor <> ""
  
  //Apresenta a situação atual do tabuleiro
  escreval("Neste momento o tabuleiro está assim:")
  escreval("   1   2   3")
  escreval("1 _", tabuleiro[1,1], "_|_", tabuleiro[1,2], "_|_", tabuleiro[1,3], "_")
  escreval("2 _", tabuleiro[2,1], "_|_", tabuleiro[2,2], "_|_", tabuleiro[2,3], "_")
  escreval("3  ", tabuleiro[3,1], " | ", tabuleiro[3,2], " | ", tabuleiro[3,3], " ")

  
  se vencedor = "X" entao
     escreva("O vencedor do jogo foi: ", nomeJogador1)
  fimse
  se vencedor = "O" entao
     escreva("O vencedor do jogo foi: ", nomeJogador2)
  fimse
  se vencedor = "V" entao
     escreva("O jogo deu Velha!")
  fimse
  
    
fimalgoritmo
```

Se tiver dúvida, acesse as lições anteriores que enviei para o seu e-mail, 
onde falo sobre cada um desses assuntos.

Aguarde a próxima lição de número #10 deste minicurso.
Vamos ver como podemos melhorar este algoritmo do jogo da velha utilizando funções e procedimentos.

Até lá!

-Gustavo