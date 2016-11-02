title: Aula 2/10 - Criando os seus primeiros programinhas.
author: Gustavo Furtado de Oliveira Alves
slug: aula-2-criando-os-seus-primeiros-programinhas
date: 2016-10-27
image: /images/.jpg
order: 02

Olá amigo(a)! Esta é a nossa segunda aula do Minicurso GRÁTIS de lógica
de programação do blog **{ Dicas de Programação }**.

Na primeira aula deste curso eu te expliquei porque você DEVE começar a
aprender programação AGORA mesmo. Também ensinei que você não precisa
saber inglês para começar e porque vamos escrever algoritmos em
PORTUGUÊS nos exercícios e exemplos deste minicurso.

Bom, vamos à segunda aula deste minicurso. Nesta aula você vai
aprender:

-   O que é um Algoritmo.
-   Como instalar o Visualg para aprender lógica de programação.
-   Criará os seus primeiros programas.

<u>Leitura de aproximadamente 20 minutos.</u>

##O que é um Algoritmo?

O primeiro passo para se aprender a programar não envolve computador,
envolve educar a sua mente a explicar em detalhes os passos necessários
para executar uma tarefa.

![Ferramenta para aprender programação](/images/fluxograma-lampada.gif)

Você deve aprender a modelar um roteiro que explica quando tomar
decisões e quando realizar determinadas tarefas, esse roteiro é chamado
de "algoritmo".

Você sabia que os primeiros processadores só sabiam realizar somas?

A partir dessa operação básica que o computador sabia fazer, você já
imagina um algoritmo para fazer multiplicações?

Talvez você ainda não saiba exatamente como é esse algoritmo, mas com
certeza já imaginou que precisa fazer repetidas somas. Certo?

É assim que nós aprendemos fazer multiplicação na escola. E essa também
é uma forma de ensinar uma máquina a fazer multiplicação.

Agora que você já pensou como faz multiplicação através de somas, vou
mostrar como eu faria um algoritmo para realizar uma multiplicação de
dois números.

> Algoritmo **Multiplicação de números positivos**
>
> **Declaração de variáveis**
>
> numero1, numero2, resultado, contador: Inteiro
>
> **Inicio**
>
> leia(numero1)
>
> leia(numero2)
>
> resultado &lt;- 0
>
> contador &lt;- 0
>
> **Enquanto** contador &lt; numero2 **Faça**
>
> resultado &lt;- resultado + numero1
>
> contador &lt;- contador + 1
>
> **Fim-Enquanto**
>
> escreva(resultado)
>
> **Fim**

Talvez este algoritmo possa ser um pouco complicado para você entender
agora, sendo o primeiro algoritmo que te mostro, mas continue lendo que
vou mostrar alguns algoritmos mais simples hoje. Ao final você entenderá
exatamente como esse algoritmo funciona... Antes vamos ver a ferramenta
que vamos usar ao longo deste minicurso.

##A melhor ferramenta para aprender lógica de programação

Sabe qual a melhor ferramenta de estudos para aprender lógica de
programação?

![Ferramenta para aprender programação](/images/caderno-lapis-borracha.jpg){:width="376" :height="250"}

**Caderno, lápis e borracha!** Sim, essa é a melhor ferramenta para
aprender lógica de programação!

Na verdade, digo isso porque foi assim que eu aprendi: escrevendo
algoritmos no caderno. No começo, usa-se mais a borracha que o lápis!
rs.

Embora naquela época não tivesse muito recurso tecnológico para aprender
lógica de programação, acredito que hoje com tantas distrações na
internet talvez seja realmente melhor se desligar disso tudo para
conseguir aprender algo.

Uma técnica que gosto muito para me ajudar na concentração e ter mais
produtividade é a **Técnica Pomodoro**.

Não é o foco deste minicurso, mas eu escrevi um artigo sobre essa
técnica. Se quiser saber mais clique no link abaixo e leia **depois
desta aula**:

**[Clique AQUI para conhecer a técnica pomodoro!](http://www.dicasdeprogramacao.com.br/melhore-sua-produtividade-com-a-tecnica-pomodoro/)**

Voltando ao curso, se não vai usar lápis e borracha e quiser utilizar um
software para te ajudar a aprender programação. Neste minicurso vamos
utilizar o Visualg para escrever códigos em português.

Na minha opinião o VisuAlg é a melhor IDE (Ambiente de desenvolvimento)
para iniciantes em programação implementarem seus algoritmos.

O Visualg foi criado por um brasileiro (Claudio Morgado de Souza), é
fácil de ser usado e compila pseudo-códigos escritos em português,
também conhecidos como “Portugol”.

### Instalando o Visualg no seu computador

A instalação do VisuAlg é muito simples e o software pode ser instalado
em Windows 95 ou posterior. Para instalar o o Visualg basta baixá-lo
através do link abaixo, extrair o executável e rodar. Pronto.

**[Clique AQUI para fazer o download do
Visualg](http://www.dicasdeprogramacao.com.br/download-visualg/)**

Obs: Quem usa linux, o Visualg funciona perfeitamente no Wine. Eu mesmo
uso o Visualg no Linux.

![Visualg](/images/visualg-pagina-inicial.png)

A tela do VisuAlg compõe-se da barra de menu, barra de tarefas, barra de
ferramentas, do editor de textos (que toma toda a sua metade superior),
do quadro de variáveis (no lado esquerdo da metade inferior), do
simulador de saída (no correspondente lado direito) e da barra de
status. O programa já inicia com o "esqueleto" de um algoritmo. Como
você pode ver na figura acima.

O professor **Antonio Carlos Nicolodi** reformulou o Visualg e lançou a
versão 3.0 com uma interface nova e algumas melhorias. Para este
minicurso você pode usar a versão 3.0 ou a 2.5. Como você preferir.

##Criando o seu primeiro programa!

Agora que você já tem o Visualg, é hora de criar o seu primeiro
programa. O famoso "Hello World". Abra o visualg e escreva o algoritmo
abaixo:

![Hello World Visualg](/images/2015/05/Hello-World.png)

Vamos entender esse primeiro programa que você criou.

1º Na primeira linha, nós colocamos o nome do algoritmo
**"BoasVindas"**.

2º As quatro linhas seguintes são comentário, ou seja, é ignorado pelo
compilador, não é um comando de algoritmo. Os comentários no Visualg
começam com duas barras. Assim: //

<div style="margin: 5px 50px 5px 50px;">

**Nota para o iniciante**: Embora os comentários não sejam interpretados
na hora de executar o programa, eles são muito importantes quando se
escreve software, pois através dos comentários a gente explica o que uma
parte do código faz para um outro programador que trabalhará neste mesmo
código no futuro. Lembre-se: este programador pode ser você! É uma boa
prática comentar códigos.

</div>

3º Em seguida vemos as declarações de variáveis. Nós declaramos uma
variável chamada **nome** do tipo **CARACTERE**. Na próxima aula eu vou
explicar o que é uma variável, mas por agora só entenda que nós podemos
armazenar valores em uma variável.

4º O programa começa de fato após a cláusula **inicio**. Perceba que
depois do início tem outro comentário.

5º A primeira coisa que fazemos no programa é escrever na tela para o
usuário: **Olá! digite o seu nome:**

Nós fizemos isso através da função **ESCREVA**.

6º Na linha seguinte, nós capturamos o que o usuário digitou através da
função **LEIA**. E armazenamos o texto que o usuário digitou na variável
**nome**.

7º Por fim, nós mostramos na tela (novamente através da função
**ESCREVA**): **Seja bem vindo (o valor da variável nome)!**

Note que nós juntamos ao texto **Seja bem vindo** o valor da variável
nome. Se o usuário digitou **José** o programa vai exibir na tela:
**Seja bem vindo José!**

Veja na imagem abaixo como acontece a execução do programa que acabamos
de criar.

![resultado algoritmo básico](/images/resultado-algoritmo_basico.png)

Entendendo o algoritmo da multiplicação
---------------------------------------

Agora que você criou o seu primeiro programa, vamos tentar entender
aquele algoritmo da Multiplicação que eu falei no começo da aula de
hoje. Antes vamos implementá-lo no Visualg.

![algoritmo de multiplicação](/images/algoritmo_multiplicacao.png)

Para entender o algoritmo, é importante definir algumas coisas:

 

-   **Variável** é um espaço alocado na memória para armazenar dados. No
    algoritmo, foram criadas 4 variáveis: **numero1**, **numero2**,
    **resultado** e **contador**
-   O símbolo “:=” representa uma atribuição de valor a uma variável.
    Por exemplo, (**resultado := resultado + numero1**) atribui à
    variável resultado, o valor da própria variável resultado, acrescido
    do valor da variável numero1.
-   O comando **leia(numero1)**, significa que o algoritmo está lendo o
    que o usuário digita e armazenando na variável **numero1**.
-   O comando **ENQUANTO** é uma estrutura de controle de fluxo do tipo
    “Estrutura de repetição”. Vamos ver isso na aula 5 deste minicurso.

 

Vamos ver qual seria o resultado da execução deste algoritmo?

![resultado do algoritmo de multiplicação](/images/resultado_algoritmo_multiplicacao.png)

Este algoritmo eu não vou explicar aqui. Preferi dar as informações que
você precisava para entender. Você precisa se esforçar um pouco pra
entender o algoritmo.

Se você não conseguiu entender este algoritmo da multiplicação, não se
preocupe, tem coisa nele que eu ainda vou explicar. Mas já dá pra você
ter uma ideia de como um algoritmo funciona, como eu transferi a forma
de resolver o problema da multiplicação da maneira que eu sei fazer,
porque aprendi quando criança, para o computador resolver sozinho.

Por hoje é só.

Mas eu queria deixar um exercício para você fazer ...

Quero que você escreva um algoritmo para calcular a média de um aluno
através de suas 4 notas no ano letivo.

Ou seja, o algoritmo precisa ler as quatro notas que o usuário digitar,
calcular a média e exibir na tela para o usuário.

Vou dar a resposta na próxima aula, mas é muito importante que você
tente fazer este exercício sozinho. Com o que você aprendeu até agora,
você já é capaz de resolver este exercício.

Na próxima aula (você receberá por e-mail) vamos começar a fazer os
nossos programas tomarem decisões.

Enquanto isso, tente praticar criando alguns algoritmos básicos. As
dificuldades no primeiro contato com programação é normal, mas nesse
minicurso você vai aprender como superar isso fazendo exercícios.

Aprender lógica de programação é como aprender matemática. Tem que
praticar!

Nos vemos na próxima aula!
