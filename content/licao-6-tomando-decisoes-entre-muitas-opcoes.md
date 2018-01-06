title: 6/10 - Tomando decisões entre muitas opções
author: Gustavo Furtado de Oliveira Alves
slug: licao-6-tomando-decisoes-entre-muitas-opcoes
date: 2016-10-27
image: /images/hub-e-switch.png
order: 06

Olá querido aluno, conseguiu resolver o exercício da última lição?
No final da lição de hoje você poderá ver a minha solução para você conferir com o seu algoritmo.

Na última lição nós falamos da estrutura **SE-ENTÃO-SENÃO**, que é usada para
fazer os nossos programas tomarem decisões por si só.

Dei o exemplo do caixa eletrônico, em que o programa deveria verificar
se o valor que desejamos sacar é menor que o saldo disponível.

Na lição de hoje vamos ver qual estrutura de controle de fluxo devemos
utilizar quando temos muitas opções para tomar decisão.

Antes de aprender a estrutura ESCOLHA-CASO, vamos ver uma coisa que a
princípio não tem nada a ver com o nosso assunto, mas vai te ajudar a
entender como funciona esta estrutura.

##Equipamentos de rede de computadores

Talvez você já saiba mais ou menos algumas coisas sobre rede de
computadores. Existem várias topologias de redes: estrela, barramento,
anel, etc...

Mas quero chamar a sua atenção para dois equipamentos utilizados nas
redes de computadores. Um é o **HUB** e o outro é o **SWITCH**.

![hub e
switch](/images/hub-e-switch.png){:style="text-align:center;" width="100%"}

Esses dois equipamentos são muito parecidos, algumas pessoas até pensam
que são a mesma coisa. Mas há uma pequena diferença entre eles.

A tarefa é a mesma, transferir dados entre as portas, a diferença é a
forma com que a tarefa é realizada por cada equipamento.

Basicamente o **HUB é burro** e o **SWITCH é inteligente**. Como assim?

Simples, quando o HUB recebe dados por uma porta, ele reenvia esses
dados para TODAS as portas.

Por exemplo, se o computador ligado na porta 1 enviou um pacote de dados
para o computador ligado na porta 5, o HUB enviará os dados para todas
as portas, 1, 2, 3, 4, 5, 6... O computador de destino que vai descobrir
se o pacote de dados é pra ele ou não, caso não o seja ele vai ignorar o
pacote de dados.

Isso significa que os HUBs deixam a rede lenta, pois haverá muito
congestionamento de dados na rede e processamento desnecessário pelos
computadores. Além disso, apenas um pacote estará trafegando na rede por
vez.

Ou seja, o **HUB é burro**!

Já o SWITCH é mais inteligente. Quando o SWITCH recebe um pacote de
dados, ele identifica a porta correta para encaminhar aquele pacote de
dados.

Por exemplo, se o computador ligado na porta 1 enviou um pacote de dados
para o computador ligado na porta 5, o SWITCH enviará os dados apenas
para a porta 5.

Dessa forma há menos congestionamento na rede e é possível trafegar
vários pacotes na rede paralelamente.

##Lembra que inglês é importante?

Talvez você esteja se perguntando o que tem a ver o HUB e o SWITCH com a
lição de hoje. Tudo!

A estrutura ESCOLHA-CASO funciona da mesma forma que o SWITCH das redes
de computadores só que ao invés de enviar um pacote de dados para uma
determinada porta, vamos enviar o fluxo do algoritmo para um determinado
ponto do código. A ideia é a mesma!

A propósito, como eu disse na primeira lição, inglês é essencial para
trabalhar com programação, EMBORA NÃO SEJA IMPEDITIVO. E quando você
estiver programando em inglês verá que ESCOLHA-CASO é conhecido como
SWITCH-CASE.

##A estrutura ESCOLHA-CASO

Lembra do SE-ENTÃO-SENÃO da lição passada? Imagine que você tem um menu
de opções e o usuário deve escolher uma opção, dentre várias. Como
você identificaria qual opção o usuário digitou?

Talvez você faria algo assim ...

```
SE opção = 1 ENTÃO
    “instruções a serem executadas caso opção = 1”
SENÃO
    SE opção = 2 ENTÃO
        “instruções a serem executadas caso opção = 2”
    SENÃO
        SE opção = 3 ENTÃO
            “instruções a serem executadas caso opção = 3”
        SENÃO
            ...
        FIM-SE
    FIM-SE
FIM-SE
```

Ou seja, vários SE-ENTÃO-SENÃO aninhados, um no SENÃO do outro...

A proposta do ESCOLHA-CASO é ser uma solução mais elegante para este
caso. Levando o fluxo do programa direto ao bloco de código
correto (igual o switch), dependendo do valor de uma variável de verificação.

Essa é a estrutura ESCOLHA-CASO.

```
ESCOLHA <variável de verificação>
    CASO <valor1> FAÇA
        “instruções a serem executadas caso <variável de verificação> = <valor1>”
    CASO <valor2> FAÇA
        “instruções a serem executadas caso <variável de verificação> = <valor2>”
    CASO <valor3> FAÇA
        “instruções a serem executadas caso <variável de verificação> = <valor3>”
    ...
FIM-ESCOLHA
```

O esquema visual do fluxograma desta estrutura é como a figura abaixo.

![estrutura-ESCOLHA-CASO](/images/estrutura-ESCOLHA-CASO.png){:style="text-align:center;" width="100%"}

##ESCOLHA-CASO na prática!

Nada melhor para aprender programação do que praticar. Bastante! Então
vamos ver um exemplo prático da utilização do ESCOLHA-CASO em comparação
ao SE-ENTÃO-SENÃO.

(Novamente vamos usar o Visualg para criar os nossos algoritmos, você
pode fazer com lápis e papel, mas caso queira baixar o Visualg,
**[clique aqui para fazer o
download](https://dicasdeprogramacao.com.br/download-visualg/)**)

Imagine a seguinte situação: Você deseja criar um algoritmo para uma
calculadora, o usuário digita o primeiro número, a operação que deseja
executar e o segundo número. Dependendo do que o usuário informar como
operador, o algoritmo executará um cálculo diferente (soma, subtração,
multiplicação ou divisão).

Vejamos como seria este algoritmo utilizando a estrutura SE-ENTÃO-SENÃO.

```
algoritmo "CalculadoraBasicaComSE"
var
   numero1 : REAL
   numero2 : REAL
   operacao : CARACTERE
   resultado : REAL
inicio

      ESCREVA ("Digite o primeiro número: ")
      LEIA (numero1)
      ESCREVA ("Digite a operação: ")
      LEIA (operacao)
      ESCREVA ("Digite o segundo número: ")
      LEIA (numero2)

      SE operacao = "+" ENTAO
         resultado := numero1 + numero2
      SENAO
         SE operacao = "-" ENTAO
            resultado := numero1 - numero2
         SENAO
            SE operacao = "*" ENTAO
               resultado := numero1 * numero2
            SENAO
               SE operacao = "/" ENTAO
                  resultado := numero1 / numero2
               FIMSE
            FIMSE
         FIMSE
      FIMSE

      ESCREVA ("Resultado: ", resultado)

fimalgoritmo
```

Veja como os SEs aninhados (dentro dos SENÃOs) deixam o código mais
complexo. Dá pra entender a lógica, mas não é muito elegante. Agora
vamos ver como ficaria a mesma lógica com a estrutura ESCOLHA-CASO.

```
algoritmo "CalculadoraBasicaComESCOLHA_CASO"
var
   numero1 : REAL
   numero2 : REAL
   operacao : CARACTERE
   resultado : REAL
inicio

      ESCREVA ("Digite o primeiro número: ")
      LEIA (numero1)
      ESCREVA ("Digite a operação: ")
      LEIA (operacao)
      ESCREVA ("Digite o segundo número: ")
      LEIA (numero2)

      ESCOLHA operacao
         CASO "+"
            resultado := numero1 + numero2
         CASO "-"
            resultado := numero1 - numero2
         CASO "*"
            resultado := numero1 * numero2
         CASO "/"
            resultado := numero1 / numero2
      FIMESCOLHA

      ESCREVA ("Resultado: ", resultado)

fimalgoritmo
```

Bem mais bonito! Né? Agora a lógica tá mais visível e elegante. O
resultado dos dois algoritmos é o mesmo. Mas o código com o ESCOLHA-CASO
é mais fácil de entender.

##CASO NÃO TRATADO NA ESTRUTURA (OUTROCASO)

Além das opções tratadas na estrutura, é possível identificar quando o
valor da variável não é equivalente a nenhum valor informado como opção
nos CASOs, ou seja, é um “OUTROCASO”.

No algoritmo que fizemos anteriormente, imagine se o usuário digitasse
um valor diferente de “+”, “-“, “\*” e “/”. Caso quiséssemos apresentar
uma mensagem para o usuário informando que ele digitou uma opção
inválida, utilizaríamos esse recurso da estrutura ESCOLHA-CASO. Veja.

```
ESCOLHA operacao
   CASO "+"
      resultado := numero1 + numero2
   CASO "-"
      resultado := numero1 - numero2
   CASO "*"
      resultado := numero1 * numero2
   CASO "/"
      resultado := numero1 / numero2
   OUTROCASO
      ESCREVA("A operação digitada é inválida!")
FIMESCOLHA
```

Como você pôde observar, em termos de organização de código a estrutura
ESCOLHA-CASO é uma opção muito elegante quando se tem muitos
SE-ENTÃO-SENÃO para verificar a mesma variável. Facilita a leitura do
algoritmo e a manutenção do código.

##Minha solução para o exercício da lição #5

No final da lição #5 do **minicurso de lógica de programação** eu pedi pra você tentar resolver um exercício de lógica para verificar se um aluno foi aprovado ou reprovado no final do ano.

Você fez? Espero que sim! Teve alguma dificuldade? Bom, abaixo eu mostro como eu escrevi um algoritmo para resolver esse exercício. Compare com o que você fez. Se o seu não deu certo, continue lendo que eu explico cada parte do algoritmo.

Esse é o algoritmo:

```
algoritmo "AprovacaoFinalDeAno"
var
   nota1, nota2, nota3, nota4, media: real
inicio

      escreva("Informe a nota (de 0 a 10) do primeiro bimestre: ")
      leia(nota1)
      escreva("Informe a nota (de 0 a 10) do segundo bimestre: ")
      leia(nota2)
      escreva("Informe a nota (de 0 a 10) do terceiro bimestre: ")
      leia(nota3)
      escreva("Informe a nota (de 0 a 10) do quarto bimestre: ")
      leia(nota4)

      media := (nota1 + nota2 + nota3 + nota4) / 4

      escreval("Sua média foi: ", media)

      se media >= 6 entao
         escreva("Você foi APROVADO!")
      senao
         escreva("Você foi REPROVADO!")
      fimse

fimalgoritmo
```

Entendendo o algoritmo.
Primeiro eu declarei 5 variáveis do tipo REAL. Elas têm que ser do tipo REAL porque as notas podem ter valores decimais, por exemplo 5.5.

Depois eu escrevi na tela "Digite a nota (de 0 a 10) do primeiro bimestre: " e armazenei na variável nota1 o valor que o usuário digitou. Fiz o mesmo para as outras 3 notas.

Na sequência e calculei a média das 4 notas e armazenei o resultado na variável "media". Importante colocar o parênteses para somar as notas ANTES de dividir por 4.

Agora que vem a parte da decisão, o SE-ENTÃO-SENÃO.

Eu verifiquei se a média é MAIOR OU IGUAL a 6. Se SIM ENTÃO imprimi na tela a mensagem informando que o aluno foi aprovado. SENÃO imprimi a mensagem informando que o aluno foi reprovado.

Veja abaixo o resultado da execução do algoritmo no Visualg, quando a média era menor que 6 e quando foi maior.

Viu como foi simples? Se você teve dificuldades para resolver, não se preocupe. No início parece difícil mesmo. Mas como sempre digo, é preciso praticar!

Se conseguiu resolver sem dificuldades ótimo, mas continue praticando.

##Exercício da lição de hoje!

Aprender programação é como aprender matemática, tem que praticar muito
fazendo exercícios. Portanto vou deixar mais um exercício para você resolver
sozinho, com o assunto que vimos hoje.

\* Crie um algoritmo em que o usuário digita uma letra qualquer e o
programa verifica qual a ordem dessa letra no alfabeto, por exemplo: se
o usuário digitar a letra ‘G’ o programa deve imprimir na tela, “A letra
G está na posição 7 do alfabeto”. Implemente com a estrutura ESCOLHA-CASO
e depois com a estrutura SE-ENTÃO-SENÃO para perceber a diferença
gritante no código.

Amanhã enviarei um e-mail para você com uma solução para exercício. Mas
é muito importante que você tente fazer os algoritmos sozinho antes de
ver a resposta. Ok?

Na próxima lição que você receberá por e-mail, vou te ensinar a fazer
**estruturas de repetição**. Fique atento à caixa de entrada do seu e-mail.

Bons estudos!
