title: 10/10 - Funções e Procedimentos
author: Gustavo Furtado de Oliveira Alves
slug: licao-10-funcoes-e-procedimentos
date: 2016-10-27
image: /images/.jpg
order: 10

Olá! Tudo bem? Chegamos à lição \#10 do **minicurso GRÁTIS de lógica de
programação**!

Nesta lição vamos aprender uma forma de melhorar a sua
programação. Utilizando **funções** e **procedimentos** nós podemos
reaproveitar código, melhorar a leitura dos algoritmos e criar códigos
mais limpos e legíveis.

Nesta lição vamos ver um pouquinho de geometria básica. Só pra
relembrar um pouquinho a escola. Mas não se assuste, vai ser fácil.

Vamos lá?

##O que são Funções e Procedimentos

A primeira coisa que você tem que entender é, afinal, que raios são funções e procedimentos?

Bom, já adianto que você já usou procedimentos e nem percebeu!

Lembra quando você quis mostrar algum texto na tela? Você usou o
procedimento **ESCREVA** e passou um texto como parâmetro, justamente o
texto que você queria que aparecesse na tela.

> ESCREVA("Olá mundo!")

Você saberia mostrar um texto na tela sem usar esse procedimento? Não
né.

Outra pergunta: Você saberia fazer um algoritmo para calcular a raiz
quadrada de um número? Reflita um pouquinho sobre a complexidade de tal
algoritmo. E um algoritmo para gerar um número aleatório? Você saberia
fazer?

Imprimir um texto na tela, raiz quadrada, geração de número aleatório,
entre outros, são funções e procedimentos clássicos que um
programador usa, mas não precisa implementar na unha. Pra quê
re-inventar a roda??? Alguém já fez esses algoritmos e a gente apenas
usa. O que precisamos é apenas solicitar a execução desses algoritmos
dentro do nosso algoritmo.

##Qual a diferença entre função e procedimento?

A única diferença entre uma função (_function_) e um procedimento
(_procedure_) é que a função retorna um valor (por exemplo uma função que
calcula raiz quadrada retorna um número) e o procedimento não
retorna nada (por exemplo o procedimento '_escreva_' que já falei).

A figura abaixo exemplifica como acontece a utilização de uma função, o
procedimento é a mesma coisa, menos na atribuição do resultado à
variável "a".

![função](/images/função.png){:style="width: 100%"}

**Funções** (e **procedimentos**) podem ou não receber parâmetros. No
caso da função de raiz quadrada, é necessário passar como parâmetro o
número que se deseja calcular a raiz, o procedimento **ESCREVA**, requer
um texto como parâmetro para apresentar na tela do usuário.

Agora que já sabemos o que são e pra quê servem. Vamos para a prática!

##Hora de praticar: Utilizando funções e procedimentos

Você lembra como calcular a hipotenusa de um triângulo retângulo?

![triangulo-retangulo](https://dicasdeprogramacao.com.br/minicurso-logica-de-programacao/wp-content/uploads/2015/12/triangulo-retangulo-1024x670.gif){:style="float: right; width: 300px; margin: 0px 5px 5px 30px;"}

Primeiro, vou te relembrar o que é um triângulo-retângulo. Um
triângulo em que um dos ângulos tem 90º. Ou seja, dois lados do
triângulo são perpendiculares entre si. Esses lados que formam o
ângulo de 90º (ou ângulo reto) são chamados de "catetos". E o lado
oposto ao angulo reto é a hipotenusa.

Quando conhecemos o tamanho dos catetos nós conseguimos calcular o
tamanho da hipotenusa. Este é o famoso **teorema de Pitágoras**
que diz: **A soma dos quadrados dos catetos equivale ao quadrado da
hipotenusa**. A imagem abaixo ilustra bem isso.

![teorema de
pitágoras](https://dicasdeprogramacao.com.br/minicurso-logica-de-programacao/wp-content/uploads/2015/12/teorema-de-pitágoras.jpg){:style="float: left; width: 100%; padding: 20px;"}

Então para descobrir o valor da hipotenusa, temos que encontrar a raiz
quadrada de ( b² + c² ).

Com base neste cálculo, vamos fazer um algoritmo que solicita ao usuário
o valor dos dois catetos, calcula e apresenta na tela o valor da
hipotenusa do triângulo retângulo. Para isso precisaremos usar a
função RAIZQ do Visualg para calcular a raiz quadrada pra gente.

```
algoritmo "Hipotenusa"
var
    a, b, c : REAL
inicio

      ESCREVA ("Digite o valor do primeiro cateto do triângulo retângulo: ")
      LEIA (b)
      ESCREVA ("Digite o valor do segundo cateto do triângulo retângulo: ")
      LEIA (c)

      a := RAIZQ ( b*b + c*c )//Cálculo da hipotenusa utilizando a FUNÇÃO RAIZQ,

      ESCREVA ("O valor da hipotenusa é: ", a)

fimalgoritmo
```

Observe que utilizamos a função RAIZQ para calcular a raiz quadrada do
valor que passamos como parâmetro (valor entre parênteses) “b\*b +
c\*c”, o valor retornado por essa função armazenamos na variável “a”.

Como criar as suas próprias funções e procedimentos
---------------------------------------------------

Você também pode criar as suas próprias funções e procedimentos. Entre
as vantagens de criar as próprias funções e procedimentos cito duas,
melhora a legibilidade do código, tirando complexidades de dentro do
fluxo principal do seu algoritmo e remove repetição de código.

Abaixo a sintaxe para criação das suas próprias funções e procedimentos
no Visualg.

```
funcao <nome-de-função> [(<seqüência-de-declarações-de-parâmetros>)]: <tipo-de-dado>
// Seção de Declarações Internas
inicio
// Seção de Comandos
fimfuncao


procedimento <nome-de-procedimento> [(<seqüência-de-declarações-de-parâmetros>)]
// Seção de Declarações Internas
inicio
// Seção de Comandos
fimprocedimento
```

Vamos criar e usar uma função pra praticar. Vamos criar uma função que
recebe um número inteiro e retorna o fatorial deste número.

Fatorial é a multiplicação de todos os números entre 1 e o número
especificado.

Exemplo: Fatorial de 5 (ou 5!) corresponde a: 1 \* 2 \* 3 \* 4 \* 5 =
120

Então vamos ver como ficaria esta função.

```
funcao calculaFatorial(numero: inteiro): inteiro
var
      fatorial: inteiro
      contador: inteiro
inicio
     fatorial <- 1
     ENQUANTO numero > 1 FACA
              fatorial <- fatorial * numero
              numero <- numero - 1
     FIMENQUANTO
     retorne fatorial
fimfuncao
```

O fluxo principal do nosso Algoritmo poderia ser assim.

```
ESCREVA("Informe o número para o cálculo do Fatorial: ")
LEIA(numeroParaFatorial)
ESCREVA("O fatorial de ", numeroParaFatorial, " é: ", calculaFatorial(numeroParaFatorial))
```

Esse é o algoritmo completo, com a função e o fluxo principal.

```
algoritmo "Cacula Fatorial"
var

   numeroParaFatorial: inteiro

   funcao calculaFatorial(numero: inteiro): inteiro
   var
          fatorial: inteiro
          contador: inteiro
   inicio
         fatorial <- 1
         ENQUANTO numero > 1 FACA
                  fatorial <- fatorial * numero
                  numero <- numero - 1
         FIMENQUANTO
         retorne fatorial
   fimfuncao

inicio

      ESCREVA("Informe o número para o cálculo do Fatorial: ")
      LEIA(numeroParaFatorial)
      ESCREVA("O fatorial de ", numeroParaFatorial, " é: ", calculaFatorial(numeroParaFatorial))

fimalgoritmo
```

##Resumindo

Vimos nesta lição que **Funções** e **procedimentos** são "subalgoritmos"
que podem ser chamados dentro de outros algoritmos.

São utilizados com muita frequência em desenvolvimento de softwares.
Existem vários benefícios como: evita duplicação de código quando
precisamos executar a mesma operação várias vezes, deixa o entendimento
do algoritmo mais intuitivo, pois tiramos a parte complexa do código do
fluxo principal do algoritmo, etc.

**Importante**: em linguagens orientada a objeto como java, C++ e C\#,
funções e procedimentos são chamados de **MÉTODOS**. Mais por uma questão
de conceito de Orientação a Objetos, mas no fundo é a mesma coisa, podem
receber parâmetros e retornam ou não um resultado.

Para finalizar, lembra do Jogo da Velha que fizemos na lição passada e eu
te mandei o meu algoritmo. Pense como você poderia criar funções e
procedimentos para melhorar ele. Amanhã eu vou mandar o mesmo algoritmo,
só que utilizando funções e procedimentos para melhorar a legibilidade
do algoritmo e tirar uma duplicação de código que tem nele. Mas
tente fazer você mesmo, antes de receber o meu algoritmo.

Até lá!
