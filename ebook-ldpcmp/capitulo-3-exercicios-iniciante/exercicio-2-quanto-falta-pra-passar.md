Sabe quando você fica com aquela dúvida de quais notas precisa tirar no último bimestre do ano pra passar naquela disciplina difícil? Então, hoje você vai acabar com esse problema.

Neste exercício você vai criar um algoritmo que calcula quanto você precisa tirar de nota a cada bimestre.

O que o algoritmo deve fazer:

- Solicitar ao usuário a média necessária para passar. (Ex. 6.0, 7.0…)
- Solicitar a nota do primeiro bimestre.
- Calcular e apresentar na tela quais notas em média deverão ser tirada nos próximos 3 bimestres para ser aprovado.
- Solicitar a nota do segundo bimestre.
- Calcular e apresentar na tela quais notas em média deverão ser tirada nos próximos 2 bimestres para ser aprovado.
- Solicitar a nota do terceiro bimestre.
- Calcular e apresentar na tela qual nota deverá ser tirada no último bimestre para ser aprovado.

##Cálculos

Não sei se você é craque em matemática, mas caso não seja vou explicar os cálculos que você deverá fazer neste exercício.

1. Quando o usuário informa a média usada na escola, nós precisamos calcular a nota total que o aluno precisa tirar para ser aprovado. Ou seja, a média necessária para passar x 4. No caso estamos considerando 4 bimestres no ano letivo. Certo?

Então temos a seguinte equação:

notaTotalParaPassar = mediaMinima * 4

2. Quando o usuário informa a nota do primeiro bimestre. Nós devemos verifica quanto falta para atingir o total para passar e depois verificar a nota média necessária para cada bimestre restante.
Ou seja:

totalRestante = notaTotalParaPassar - notaPrimeiroBimestre

mediaRestante = totalRestante / 3

3. O mesmo procedimento deve acontecer após o usuário informar a nota do segundo bimestre. Calcular o total restante e a nota média mínima para os próximos 2 bimestres.

4. Após o usuário informar a nota 3. Não precisa mais calcular a média restante, pois só falta 1 bimestre. Então só precisamos calcular o total restante.

Agora é com você. Mão na massa! Após escrever o seu algoritmo, você pode conferir o algoritmo que eu fiz para este exercício.
