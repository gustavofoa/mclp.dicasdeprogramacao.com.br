title: Aula 10/10 - Funções e Procedimentos
author: Gustavo Furtado de Oliveira Alves
slug: aula-10-funcoes-e-procedimentos
date: 2016-10-27
image: /images/.jpg
order: 10

#Aula (10/10) Funções e Procedimentos

Olá! Tudo bem? Chegamos à aula \#10 do **minicurso GRÁTIS de lógica de
programação**!

Nesta aula vamos aprender uma forma de melhorar a sua
programação. Utilizando **funções** e **procedimentos** nós podemos
reaproveitar código, melhorar a leitura dos algoritmos e criar códigos
mais limpos e legíveis.

Nesta aula vamos ver um pouquinho de geometria básica. Só pra
relembrar um pouquinho a escola. Mas não se assuste, vai ser fácil.

<span style="text-decoration: underline;">Duração da
aula: aproximadamente 25 minutos.</span>

##O que são Funções e Procedimentos

A primeira coisa que você tem que entender é o que eu estou
falando. Afinal, que raios são funções e procedimentos?

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

A única diferença entre uma função (function) e um procedimento
(procedure) é que a função retorna um valor (por exemplo uma função que
calcula raiz quadrada retorna um número) e o procedimento não
retorna nada (por exemplo o procedimento escreva que já falei).

A figura abaixo exemplifica como acontece a utilização de uma função, o
procedimento é a mesma coisa, menos na atribuição do resultado à
variável "a".

![função](http://www.dicasdeprogramacao.com.br/minicurso-logica-de-programacao/wp-content/uploads/2015/12/função.png){:style=".aligncenter .size-full .wp-image-385" :width="503" :height="332"}

**Funções** (e **procedimentos**) podem ou não receber parâmetros. No
caso da função de raiz quadrada, é necessário passar como parâmetro o
número que se deseja calcular a raiz, o procedimento **ESCREVA**, requer
um texto como parâmetro para apresentar na tela do usuário.

Agora que já sabemos o que são e pra quê servem. Vamos para a prática!

##Hora de praticar: Utilizando funções e procedimentos

Você lembra como calcular a hipotenusa de um triângulo retângulo?

Primeiro, vou te relembrar o que é um triângulo-retângulo. Um
triângulo em que um dos ângulos tem 90º. Ou seja, dois lados do
triângulo são perpendiculares entre si. Esses lados que formam o
ângulo de 90º (ou ângulo reto) são chamados de "catetos". E o lado
oposto ao angulo reto é a hipotenusa.

![triangulo-retangulo](http://www.dicasdeprogramacao.com.br/minicurso-logica-de-programacao/wp-content/uploads/2015/12/triangulo-retangulo-1024x670.gif){:style=".aligncenter .wp-image-388 .size-large" :width="660" :height="432"}

Quando conhecemos o tamanho dos catetos nós conseguimos calcular o
tamanho da hipotenusa. Estou falando do famoso **teorema de Pitágoras**
que diz: **A soma dos quadrados dos catetos equivale ao quadrado da
hipotenusa**. A imagem abaixo ilustra bem isso.

![teorema de
pitágoras](http://www.dicasdeprogramacao.com.br/minicurso-logica-de-programacao/wp-content/uploads/2015/12/teorema-de-pitágoras.jpg){:style=".aligncenter .size-full .wp-image-391" :width="471" :height="446"}

Então para descobrir o valor da hipotenusa, temos que encontrar a raiz
quadrada de ( b² + c² ).

Com base neste cálculo, vamos fazer um algoritmo que solicita ao usuário
o valor dos dois catetos, calcula e apresenta na tela o valor da
hipotenusa do triângulo retângulo. Para isso precisaremos usar a
função RAIZQ do Visualg para calcular a raiz quadrada pra gente.

``` {.lang:default .decode:true}
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

``` {.lang:default .decode:true}
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

``` {.lang:default .decode:true}
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

``` {.lang:default .decode:true}
      ESCREVA("Informe o número para o cálculo do Fatorial: ")
      LEIA(numeroParaFatorial)
      ESCREVA("O fatorial de ", numeroParaFatorial, " é: ", calculaFatorial(numeroParaFatorial))
```

Esse é o algoritmo completo, com a função e o fluxo principal.

``` {.lang:default .decode:true}
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

Vimos nesta aula que **Funções** e **procedimentos** são "subalgoritmos"
que podem ser chamados dentro de outros algoritmos.

São utilizados com muita frequência em desenvolvimento de softwares.
Existem vários benefícios como: evita duplicação de código quando
precisamos executar a mesma operação várias vezes, deixa o entendimento
do algoritmo mais intuitivo, pois tiramos a parte complexa do código do
fluxo principal do algoritmo, etc.

**Importante**: em linguagens orientada a objeto como java, C++ e C\#,
funções e procedimentos são chamados de **MÉTODO**. Mais por uma questão
de conceito de Orientação a Objetos, mas no fundo é a mesma coisa, podem
receber parâmetros e retornam ou não um resultado.

Para finalizar, lembra do Jogo da Velha que fizemos na aula passada e eu
te mandei o meu algoritmo (somente se você estiver inscrito neste
minicurso gratuito). Pense como você poderia criar funções e
procedimentos para melhorar ele. Amanhã eu vou mandar o mesmo algoritmo,
só que utilizando funções e procedimentos para melhorar a legibilidade
do algoritmo e tirar uma duplicação de código que tem nele. Mas
tente fazer você mesmo, antes de receber o meu algoritmo.

Até lá!
