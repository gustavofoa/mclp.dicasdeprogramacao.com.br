title: 5/10 - Tomando decisões!
author: Gustavo Furtado de Oliveira Alves
slug: licao-5-tomando-decisoes
date: 2016-10-27
image: /images/.jpg
order: 05

Olá nobre amigo(a)! Hoje vamos colocar a mão na massa e aprender a forma
mais básica de controlar o fluxo de um algoritmo.

Vamos fazer os nossos algoritmos tomarem decisões!

Para isso existem as estruturas de decisão, e a mais utilizada é a
estrutura SE-ENTÃO-SENÃO (Em inglês IF-THEN-ELSE).

##Estrutura de decisão SE-ENTÃO-SENÃO

O funcionamento é simples: com base no resultado de uma expressão lógica
(lembra da nossa última lição quando falamos dos operadores lógicos?), o
fluxo do algoritmo segue para um bloco de instruções ou não. Observe o
esquema da estrutura SE-ENTÃO-SENÃO:

```
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

![estrutura-IF](/images/estrutura-IF.png){:width="100%"}

Simples assim. Essa estrutura não tem segredos. Agora é hora de praticar! Vamos lá?

##SE-ENTÃO-SENÃO na prática!

Vejamos um exemplo de utilização desta estrutura com um algoritmo, você pode usar o
[VisuAlg](http://www.dicasdeprogramacao.com.br/download-visualg/) para testar esse algoritmo e ver o resultado.

Neste algoritmo, vamos simular um caixa eletrônico quando vamos sacar
dinheiro. O caixa eletrônico verifica se o valor que desejamos sacar é
menor que o saldo disponível. Assumiremos que há R$ 1000 de saldo
disponível para o saque. Se o valor que o usuário quer sacar é menor ou igual ao saldo disponível, então o algoritmo permite o saque, caso contrário, não.

```
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


![Sacar-dinheiro-menor-que-10001](/images/Sacar-dinheiro-menor-que-10001.png){:width="100%"}

Agora a execução do mesmo algoritmo, porém inserindo um valor maior que
1000 para saque.

![Sacar-dinheiro-maior-que-1000](/images/Sacar-dinheiro-maior-que-1000.png){:width="100%"}

Perceba que o fluxo do algoritmo tomou rumos diferentes.

Essa é a estrutura de controle de fluxo mais utilizada na criação de
programas de computador. Pratique-a criando algoritmos que tomam
decisão.

##Hora de praticar!

Para aprender você deve praticar bastante criando algoritmos.

Lembra do exercício que você fez na lição #2? Aquele que calcula a média de um aluno. Vamos incrementar ele e informar se ele foi aprovado ou reprovado.

Então o algoritmo deve ser assim assim: O usuário digita as 4
notas (de 0 a 10) bimestrais do aluno e o algoritmo deve calcular a
média. Depois o algoritmo deve verificar se a média é maior ou igual a 6. **Caso afirmativo**, exibe na
tela uma mensagem informando que o aluno foi aprovado, **caso
contrário**, uma mensagem informando que ele foi reprovado.

Na próxima lição eu vou mostrar o meu algoritmo para solucionar este exercício.
Mas é muito importante que você tente fazer esse algoritmo sozinho antes de ver a resposta. Ok?

Além disso você vai aprender como fazemos para nosso algoritmo tomar decisão quanto tem MUITAS opções.
Fique atento ao seu e-mail.

Até a próxima!
