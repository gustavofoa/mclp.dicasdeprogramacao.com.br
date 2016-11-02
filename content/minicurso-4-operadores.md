title: Aula 4/10 - Operadores
author: Gustavo Furtado de Oliveira Alves
slug: aula-4-operadores
date: 2016-10-27
image: /images/.jpg
order: 04

#Aula (4/10) Operadores

Evidentemente você já resolveu alguma expressão matemática na escola.
Lembra quando o professor pedia pra gente resolver aquelas expressões
enormes? Cheia de números e *operadores* de somar, subtrair,
multiplicar, etc. Sem falar das raízes e exponenciais. Sei que muita
gente vai ter um arrepio só de lembra disso. rs

Vamos ficar no basicão ... Você sabe que na expressão **2 + 2** o sinal
**+** é um operador que representa a soma. Certo? Também sabe que essa
expressão resulta apenas um valor (4). Confirma? Então, você já entendeu
o sentido dos *operadores*. **Relacionar valores para resultar um outro
valor.**.

Existem 3 tipos de *operadores*: **Aritméticos**, **Lógicos** e
**Relacionais**.

Entender como funciona cada operador é MUITO importante para aprender
programação. Claro que, a representação simbólica de alguns operadores
muda de acordo com a linguagem, mas a essência é a mesma. **Todas as
linguagens de programação usam operadores**.

Vamos ver um pouquinho sobre cada tipo de operadores.

<span style="text-decoration: underline;">Leitura de aproximadamente 25
minutos</span>

### Operadores Aritméticos

![operadores-aritméticos](http://www.dicasdeprogramacao.com.br/minicurso-logica-de-programacao/wp-content/uploads/2015/05/operadores-aritméticos-300x169.jpg){:width="300" :height="169"} Esses são os mais fáceis! Aprendemos na escola fundamental.
Em programação, esses operadores são tão simples quanto você aprendeu na
escola. Apenas alguns que você pode não conhecer.

Além dos mais simples (soma "+", subtração "-", multiplicação "\*" e
divisão "/"), dois outros operadores aritméticos não recebem muita
atenção e pode ser que você não os conheça, eles são o **div** e o
**mod**, que resultam, respectivamente, o quociente (a parte inteira do
resultado da divisão) e o resto da divisão. Observe as operações abaixo:

> 14 / 4 = 3,5\
> 14 **div** 4 = 3\
> 14 **mod** 4 = 2

O operador mod em muitas linguagens de programação (java por exemplo) é
representado pelo símbolo “%“, assim:

> 14 **%** 4 = 2

Uma das maiores utilizações do operador **mod** é para verificar se um
número é *par* ou *ímpar*. Quando o número "**mod**" 2 resulta 0, ele é
par, caso contrário, é ímpar. Veja.

> 14 **mod** 2 = 0 **14 é par**\
> 15 **mod** 2 = 1 **15 é ímpar**

Um outro operador aritmético que existe em algumas linguagens de
programação é o \^ e executa a operação de potência, mas geralmente essa
operação é realizada através de uma função chamada **pow**, bem como a
operação de radiciação (função **sqrt**). Veja um exemplo do operador
\^:

> 2 \^ 5 = 32 (dois elevado a cinco)

Operadores aritméticos de radiciação também são fornecidos por algumas
linguagens de programação, mas esses são bem mais raros. O Postgres por
exemplo oferece os símbolos **|/** e **||/** para operações de raiz
quadrada e raiz cúbica, respectivamente.

#### Precedência entre os operadores

Da mesma forma que na matemática, os operadores de multiplicação e
divisão têm precedência de execução em relação aos operadores de soma e
subtração. Aliás se tiver parênteses na expressão estes têm precedência
ainda maior.

Os operadores de mesma prioridade são interpretados da esquerda para a
direita. Para exemplificar essa questão de precedência, observe a
solução da expressão abaixo:

> 5 + 3 \* **( 3 – 1 )** – 2 \^ 5 / 4 – 1\
> 5 + 3 \* 2 – **2 \^ 5** / 4 – 1\
> 5 + **3 \* 2** – 32 / 4 – 1\
> 5 + 6 – **32 / 4** – 1\
> **5 + 6** – 8 – 1\
> **11 – 8** – 1\
> **3 – 1**\
> 2

### Operadores Lógicos

Lembra dos tipos de dados &lt;em&lt;lógico que falei um pouco acima
nesta aula? Viu que dentre os tipos de dados tinha o tipo **lógico**?
Então, enquanto os operadores aritméticos trabalha com números, os
operadores lógicos trabalha com dados **lógicos**, ou **booleanos**.

A ideia dos operadores continua é a mesma: **Relacionar valores para
resultar um outro valor.**. Isso significa que os operadores lógicos
relacionam valores lógicos (verdadeiro/falso, 1/0, aceso/apagado,
ligado/desligado, true/false, sim/não, etc.) e o resultado de uma
expressão lógica também é outro valor lógico. Simples assim!

Vamos conhecer os operadores lógicos ... Enquanto os operadores
aritméticos (que você conhece muito bem) são +, -, \*, /, mod e div, os
operadores lógicos são: E, OU, NÃO, NÃO-E, NÃO-OU, OU-EXCLUSIVO e
NÃO-OU-EXCLUSIVO. Não é difícil, basta você acostumar (praticando) com
esses operadores. Vamos ver como funciona cada um desses ...

#### Operador E(AND)

![portas-lógicas-AND](http://www.dicasdeprogramacao.com.br/minicurso-logica-de-programacao/wp-content/uploads/2015/06/portas-lógicas-AND.jpg){:width="233" :height="117"}
O Operador “E” ou “AND” resulta em um valor VERDADEIRO se os dois
valores de entrada da operação forem VERDADEIROS, caso contrário o
resultado é FALSO. Abaixo a **tabela-verdade** da operação E.

  ---------------- ---------------- ----------------
  **VALOR 1**      **VALOR 2**      **OPERAÇÃO E**
  **VERDADEIRO**   **VERDADEIRO**   **VERDADEIRO**
  VERDADEIRO       FALSO            FALSO
  FALSO            VERDADEIRO       FALSO
  FALSO            FALSO            FALSO
  ---------------- ---------------- ----------------

#### Operador OU(OR)

![portas-lógicas-AND](http://www.dicasdeprogramacao.com.br/minicurso-logica-de-programacao/wp-content/uploads/2015/06/portas-lógicas-OR.jpg){:width="233" :height="117"}

O Operador “OU” ou “OR” resulta em um valor VERDADEIRO se ao menos UM
dos dois valores de entrada da operação for VERDADEIRO, caso contrário o
resultado é FALSO. Abaixo a **tabela-verdade** da operação OU.

  ---------------- ---------------- -----------------
  **VALOR 1**      **VALOR 2**      **OPERAÇÃO OU**
  **VERDADEIRO**   **VERDADEIRO**   **VERDADEIRO**
  **VERDADEIRO**   FALSO            **VERDADEIRO**
  FALSO            **VERDADEIRO**   **VERDADEIRO**
  FALSO            FALSO            FALSO
  ---------------- ---------------- -----------------

#### Operador NÃO(NOT)

![portas-lógicas-AND](http://www.dicasdeprogramacao.com.br/minicurso-logica-de-programacao/wp-content/uploads/2015/06/portas-lógicas-NOT.jpg){:width="233" :height="117"}\

O Operador “NÃO” ou “NOT” é o único operador que recebe como entrada
apenas um valor, e sua função é simplesmente inverter os valores. Ou
seja, se o valor de entrada for VERDADEIRO, o resultado será FALSO e se
o valor de entrada for FALSO, o resultado será VERDADEIRO. Abaixo a
**tabela-verdade** da operação NÃO.

  ---------------------- ------------------
  **VALOR DE ENTRADA**   **OPERAÇÃO NÃO**
  **VERDADEIRO**         FALSO
  FALSO                  **VERDADEIRO**
  ---------------------- ------------------

#### Operador NÃO-E(NAND)

![portas-lógicas-AND](http://www.dicasdeprogramacao.com.br/minicurso-logica-de-programacao/wp-content/uploads/2015/06/portas-lógicas-NAND.jpg){:width="233" :height="117"}\
O Operador “NÃO-E” ou “NAND” é o contrário do operador E (AND), ou seja,
resulta em VERDADEIRO, se ao menos um dos dois valores for FALSO, na
verdade este é o operador E (AND) seguido do operador NÃO (NOT). Abaixo
a **tabela-verdade** da operação NÃO-E.

  ------------- ------------- -------------------
  **VALOR 1**   **VALOR 2**   **OPERAÇÃO NAND**
  VERDADEIRO    VERDADEIRO    FALSO
  VERDADEIRO    **FALSO**     **VERDADEIRO**
  **FALSO**     VERDADEIRO    **VERDADEIRO**
  **FALSO**     **FALSO**     **VERDADEIRO**
  ------------- ------------- -------------------

#### Operador NÃO-OU(NOR)

![portas-lógicas-AND](http://www.dicasdeprogramacao.com.br/minicurso-logica-de-programacao/wp-content/uploads/2015/06/pórtas-lógicas-NOR.jpg){:width="233" :height="117"}\
O Operador “NÃO-OU” ou “NOR” é o contrário do operador OU (OR), ou seja,
resulta em VERDADEIRO, se os dois valores forem FALSO, na verdade este é
o operador OU (OR) seguido do operador NÃO (NOT). Abaixo a
**tabela-verdade** da operação NÃO-OU.

  ------------- ------------- ------------------
  **VALOR 1**   **VALOR 2**   **OPERAÇÃO NOR**
  VERDADEIRO    VERDADEIRO    FALSO
  VERDADEIRO    FALSO         FALSO
  FALSO         VERDADEIRO    FALSO
  **FALSO**     **FALSO**     **VERDADEIRO**
  ------------- ------------- ------------------

#### Operador OU-EXCLUSIVO(XOR)

![portas-lógicas-AND](http://www.dicasdeprogramacao.com.br/minicurso-logica-de-programacao/wp-content/uploads/2015/06/portas-lógicas-XOR.jpg){:width="233" :height="117"}\
O Operador “OU-EXCLUSIVO” ou “XOR” é uma variação interessante do
operador OU (OR), ele resulta em VERDADEIRO se apenas um dos valores de
entrada for VERDADEIRO, ou seja, apenas se os valores de entrada forem
DIFERENTES. Abaixo a **tabela-verdade** da operação OU-EXCLUSIVO.

  ---------------- ---------------- ------------------
  **VALOR 1**      **VALOR 2**      **OPERAÇÃO XOR**
  VERDADEIRO       VERDADEIRO       FALSO
  **VERDADEIRO**   FALSO            **VERDADEIRO**
  FALSO            **VERDADEIRO**   **VERDADEIRO**
  FALSO            FALSO            FALSO
  ---------------- ---------------- ------------------

#### Operador NÃO-OU-EXCLUSIVO(XNOR)

![portas-lógicas-AND](http://www.dicasdeprogramacao.com.br/minicurso-logica-de-programacao/wp-content/uploads/2015/06/portas-lógicas-XNOR.jpg){:width="233" :height="117"}\
O Operador “NÃO-OU-EXCLUSIVO” ou “XNOR” é o contrário do operador
OU-EXCLUSIVO (XOR), ou seja, resulta VERDADEIRO se os valores de entrada
forem IGUAIS. Observe a tabela abaixo:

  ---------------- ---------------- -------------------
  **VALOR 1**      **VALOR 2**      **OPERAÇÃO XNOR**
  **VERDADEIRO**   **VERDADEIRO**   **VERDADEIRO**
  VERDADEIRO       FALSO            FALSO
  FALSO            VERDADEIRO       FALSO
  **FALSO**        **FALSO**        **VERDADEIRO**
  ---------------- ---------------- -------------------

#### Operadores lógicos em programação

Cada linguagem de programação tem uma forma de representar os operadores
lógicos. A simbologia mais encontrada são:

-   **AND**, **OR** e **NOT** em linguagens como: Pascal, Visual Basic
    e SQL.
-   **&&**, **||** e **!** em linguagens como: Java e C\#

No nosso caso, criando algoritmos em português, os operadores lógicos
são E, OU, etc. Por exemplo.

> VERDADEIRO **E** FALSO = FALSO

Algumas linguagens oferecem operadores lógicos para o nível de bit
(também chamado de operadores bitwise). Ou seja, podemos fazer operações
lógicas com os bits de dois números. Em java, por exemplo esses
operadores são & e |. Veja o código abaixo escrito em java.

``` {.lang:java .decode:true}
public class TesteBitwise {
    public static void main (String []a){
        System.out.println("10 & 7 = " + (10 & 7));
        System.out.println("10 | 7 = " + (10 | 7));
    }
}
```

Abaixo o resultado deste programa.

![resultado-bitwise](http://www.dicasdeprogramacao.com.br/minicurso-logica-de-programacao/wp-content/uploads/2015/06/resultado-bitwise.png)

Essas operações lógicas são realizadas com os bits dos números de
entrada. Assim:

> Convertemos o número 10 e o número 7 para binário:\
> 10 = 1010 em binário\
> 7 = 0111 em binário\
> depois realizamos as operações lógicas com cada bit dos dois números.
> Da direita para a esquerda aplicamos as operações lógicas para cada
> big.
>
> 0 E 1 = 0\
> 1 E 1 = 1\
> 0 E 1 = 0\
> 1 E 0 = 0
>
> Logo,
>
> 10 & 7 = 0010 = 2 em números decimais.
>
> O mesmo para o operador OU:
>
> 0 OU 1 = 1\
> 1 OU 1 = 1\
> 0 OU 1 = 1\
> 1 OU 0 = 1
>
> Logo,
>
> 10 | 7 = 1111 = 15

Não é o foco aqui deste minicurso, essa parte das operações em nível de
bit foi só para curiosidade. Você não precisa saber fazer conversões de
bases numéricas para aprender lógica de programação, mas se quiser
aprender um pouco mais sobre isso, leia este post que escrevi no blog
**{ Dicas de Programação }**:

[As 10 conversões numéricas mais utilizadas na computação](http://www.dicasdeprogramacao.com.br/as-10-conversoes-numericas-mais-utilizadas-na-computacao/)

### Operadores Relacionais

Operadores relacionais são utilizados para comparar valores, o resultado
de uma expressão relacional é um valor booleano (VERDADEIRO ou FALSO).
Os operadores relacionais são: **igual**, **diferente**, **maior**,
**menor**, **maior ou igual**, **menor ou igual**.

Não é necessário explicar cada um, pois eles são auto-explicativos. Mas
para quem é iniciante em desenvolvimento de softwares algumas
informações podem ser importantes, principalmente pelo fato de haver
diferença entre linguagens de programação.

Os operadores relacionais são diferente dependendo da linguagem de
programação, mas conhecendo os símbolos mais comuns, a maioria da
linguagens de programação fica mais fácil aprender. No
[VisuAlg](http://www.dicasdeprogramacao.com.br/download-visualg/), os
símbolos dos operadores relacionais são: =, &lt;&gt;, &gt;, &lt;, &gt;=,
&lt;=. Vamos testar esses operadores no Visualg com o algoritmo abaixo.

``` {.toolbar-overlay:false .lang:default .decode:true .highlight:0}
algoritmo "TesteOperadoresRelacionais"
var
  numero1 : INTEIRO
  numero2 : INTEIRO
  resultado : LOGICO
inicio

      numero1 := 5
      numero2 := 3
      resultado := numero1 = numero2
      ESCREVAL (numero1, " =  ", numero2, "? ", resultado)
      resultado := numero1 <> numero2
      ESCREVAL (numero1, " <> ", numero2, "? ", resultado)
      resultado := numero1 > numero2
      ESCREVAL (numero1, " >  ", numero2, "? ", resultado)
      resultado := numero1 < numero2
      ESCREVAL (numero1, " <  ", numero2, "? ", resultado)
      resultado := numero1 >= numero2
      ESCREVAL (numero1, " >= ", numero2, "? ", resultado)
      resultado := numero1 <= numero2
      ESCREVAL (numero1, " <= ", numero2, "? ", resultado)

      numero1 := 5
      numero2 := 5
      resultado := numero1 = numero2
      ESCREVAL (numero1, " =  ", numero2, "? ", resultado)
      resultado := numero1 <> numero2
      ESCREVAL (numero1, " <> ", numero2, "? ", resultado)
      resultado := numero1 > numero2
      ESCREVAL (numero1, " >  ", numero2, "? ", resultado)
      resultado := numero1 < numero2
      ESCREVAL (numero1, " <  ", numero2, "? ", resultado)
      resultado := numero1 >= numero2
      ESCREVAL (numero1, " >= ", numero2, "? ", resultado)
      resultado := numero1 <= numero2
      ESCREVAL (numero1, " <= ", numero2, "? ", resultado)

      numero1 := 5
      numero2 := 8
      resultado := numero1 = numero2
      ESCREVAL (numero1, " =  ", numero2, "? ", resultado)
      resultado := numero1 <> numero2
      ESCREVAL (numero1, " <> ", numero2, "? ", resultado)
      resultado := numero1 > numero2
      ESCREVAL (numero1, " >  ", numero2, "? ", resultado)
      resultado := numero1 < numero2
      ESCREVAL (numero1, " <  ", numero2, "? ", resultado)
      resultado := numero1 >= numero2
      ESCREVAL (numero1, " >= ", numero2, "? ", resultado)
      resultado := numero1 <= numero2
      ESCREVAL (numero1, " <= ", numero2, "? ", resultado)

fimalgoritmo
```

A intenção deste algoritmo é mostrar o funcionamento dos operadores
relacionais com 3 possibilidades de valores: um número menor que o
outro, dois números iguais e um número maior que outro. Abaixo o
resultado da execução.

![resultado-operadores-relacionais](http://www.dicasdeprogramacao.com.br/minicurso-logica-de-programacao/wp-content/uploads/2015/06/resultado-operadores-relacionais.png){:style=".aligncenter .size-full .wp-image-220" :width="681" :height="333"}

#### Operadores lógicos em programação

Em todas as linguagens de programação existem símbolos para executarmos
essas operações. As operações maior, menor, maior ou igual e menor ou
igual na maioria das linguagens de programação são os mesmos símbolos
(até hoje não encontrei uma linguagem que tenha símbolo diferente para
estes operadores): &gt; (maior), &lt; (menor), &gt;= (maior ou igual) e
&lt;=(menor ou igual).

Mas os vilões dos iniciantes são os símbolos para testar igualdade e
diferença. Em cada linguagem é de um jeito! Em java, C, C\#,
javascript,… por exemplo, os símbolos de igual e diferente são: == e !=.
Já em Pascal, SQL, Visual Basic, … os símbolos de igual e diferente são:
= e &lt;&gt;. Então fique esperto quando for aprender alguma dessas
linguagens!

Em java, não é possível testar Strings (textos) com o operador de
igualdade (==), pois String é uma classe e não um tipo primitivo, e para
testar a igualdade entre objetos deve-se utilizar o método *equals()*.
Assim: nome.equals(“João”).

Em algumas linguagens de programação (Python por exemplo) é possível
utilizar os operadores maior e menor para verificar a precedência
alfabética de um texto em relação a outro. Por exemplo: ”Pedro” &lt;
“Paulo” resulta em FALSO, pois o texto “Pedro” alfabeticamente aparece
depois do texto “Paulo”.

Essa foi a aula sobre os **operadores**. Espero que agora você já esteja
craque e manjando tudo sobre os operadores.

Importante lembrar que do mesmo jeito que aprendemos os operadores
aritméticos nas escola, para aprender os operadores relacionais e
lógicos é necessário bastante prática!

Quer um exercício simples? Faça um algoritmo que solicite um número ao
usuário e informe se este número é **par** ou **ímpar**.

Outro exercício? Solicite a idade do usuário e informe se ele é maior de
dade ou não, se ele pode votar (acima de 16 anos) e se ele
é **obrigado** a votar (entre 18 e 65 anos).

Até a próxima aula!
