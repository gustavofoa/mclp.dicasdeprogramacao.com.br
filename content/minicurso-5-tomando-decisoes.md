title: Aula 5/10 - Tomando decisões!
author: Gustavo Furtado de Oliveira Alves
slug: minicurso-5-tomando-decisoes
date: 2016-10-27
image: /images/.jpg
order: 5

#Aula (5/10) Tomando decisões!

Olá nobre amigo(a)! Hoje vamos colocar a mão na massa e aprender a forma
mais básica de controlar o fluxo de um algoritmo.

Vamos fazer os nossos algoritmos tomarem decisões!

Para isso existem as estruturas de decisão, e a mais utilizada é a
estrutura SE-ENTÃO-SENÃO (Em inglês IF-THEN-ELSE).

<u>Leitura de aproximadamente 10 minutos.</u>

Estrutura de decisão SE-ENTÃO-SENÃO
-----------------------------------

O funcionamento é simples: com base no resultado de uma expressão lógica
(lembra da nossa última aula quando falamos dos operadores lógicos?), o
fluxo do algoritmo segue para um bloco de instruções ou não. Observe o
esquema da estrutura SE-ENTÃO-SENÃO:

``` {.toolbar-overlay:false .lang:default .decode:true .highlight:0}
SE <expressão lógica>
   ENTÃO
      <instruções a serem executadas caso a expressão booleana resulte em VERDADEIRO>
   SENÃO
      <instruções a serem executadas caso a expressão booleana resulte em FALSO>
FIM-SE
```

O bloco de código SENÃO é opcional. É comum encontrar instruções de
decisão apenas com SE-ENTÃO sem o bloco SENÃO. Veja um esquema gráfico
desta estrutura de decisão.

<p>
<center>
![estrutura-IF](http://www.dicasdeprogramacao.com.br/minicurso-logica-de-programacao/wp-content/uploads/2015/06/estrutura-IF.png){.aligncenter
.size-full .wp-image-240 width="580" height="515"}

</center>
</p>
SE-ENTÃO-SENÃO na prática!
--------------------------

Vejamos um exemplo de utilização desta estrutura com um algoritmo, para
isso vamos utilizar o
[VisuAlg](http://www.dicasdeprogramacao.com.br/download-visualg/).

Neste algoritmo, vamos simular um caixa eletrônico quando vamos sacar
dinheiro. O caixa eletrônico verifica se o valor que desejamos sacar é
menor que o saldo disponível. Assumiremos que há R\$ 1000 de saldo
disponível para o saque.

``` {.toolbar-overlay:false .lang:default .decode:true .highlight:0}
algoritmo "SacarDinheiro"
var
   SaldoDisponivel : REAL
   ValorDoSaque : REAL
inicio

      SaldoDisponivel := 1000 //Assumimos que há 1000 reais de saldo na conta disponível para saque
      ESCREVA ("Informe o valor do Saque: ")
      LEIA (ValorDoSaque)
      SE ValorDoSaque <= SaldoDisponivel ENTAO
         SaldoDisponivel := SaldoDisponivel - ValorDoSaque
         ESCREVAL ("Sacando R$ ", ValorDoSaque, ".")
      SENAO
         ESCREVAL ("O valor solicitado é maior que o valor disponível para saque!")
      FIMSE

      ESCREVAL ("Saldo disponível: R$ ", SaldoDisponivel)

fimalgoritmo
```

Abaixo a execução do algoritmo acima quando informamos valores menores
que 1000.

<p>
<center>
![Sacar-dinheiro-menor-que-10001](http://www.dicasdeprogramacao.com.br/minicurso-logica-de-programacao/wp-content/uploads/2015/06/Sacar-dinheiro-menor-que-10001.png){.aligncenter
.size-full .wp-image-247 width="681" height="199"}

</center>
Agora a execução do mesmo algoritmo, porém inserindo um valor maior que
1000 para saque.

</p>
<p>
<center>
![Sacar-dinheiro-maior-que-1000](http://www.dicasdeprogramacao.com.br/minicurso-logica-de-programacao/wp-content/uploads/2015/06/Sacar-dinheiro-maior-que-1000.png){.aligncenter
.size-full .wp-image-248 width="681" height="228"}

</center>
Perceba que o fluxo do algoritmo tomou rumos diferentes.

</p>
Essa é a estrutura de controle de fluxo mais utilizada na criação de
programas de computador. Pratique-a criando algoritmos que tomam
decisão.

Hora de praticar!
-----------------

Para aprender você deve praticar bastante criando algoritmos.

Como exercício, crie um algoritmo para verificar se um aluno foi
aprovado ou reprovado no final do ano, assim: O usuário digita as 4
notas (de 0 a 10) bimestrais do aluno e o algoritmo deve calcular a
média e verificar se é maior ou igual a 6. **Caso afirmativo**, exibe na
tela uma mensagem informando que o aluno foi aprovado, **caso
contrário**, uma mensagem informando que ele foi reprovado.

Amanhã vou enviar no seu e-mail a resposta. ;) Mas é muito importante
que você tente fazer esse algoritmo sozinho antes de ver a resposta.

Se você ainda não está inscrito neste minicurso, se inscreva agora! É
GRÁTIS! Basta clicar no botão laranja no topo. Você receberá as 10 aulas
no seu e-mail.

Na próxima aula vamos ver como fazemos para nosso algoritmo tomar
decisão quanto tem MUITAS opções.

Até a próxima aula!
