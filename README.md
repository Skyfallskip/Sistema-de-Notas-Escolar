# Sistema-de-Notas-Escolar
Um sistema web onde é possível enviar um arquivo Excel com a planilha da disciplina da turma. O sistema então irá solicitar o nome do aluno, a etapa ou bimestre e o instrumento avaliativo e inserir esses dados na planilha. Apos isso gera um novo arquivo Excel atualizado ao final.

# Objetivo do Sistema
Facilitar a inserção de notas em planilhas, exibir uma análise da turma e futuramente ser implementado em um sistema escolar completo


# Sequência de eventos

- 1°Solicita um arquivo Excel como base;

-  2° Escaneia o arquivo para saber as colunas que deve inserir as notas;
  
- 3° Seleção de qual nota você quer inserir ( I1, I2, Prova, Recuperação );

- 4° Insere os dados por meio de um formulário com os campos:
Nome aluno ( mecanismo de auto completar );
Instrumento avaliativo ( I1, I2...);
Nota;
Bimestre ou etapa;

- 5° Sistema calcula automaticamente os alunos que estão de recuperação;
  
- 6° Sistema calcula automaticamente media da turma, aprovados e reprovados;
  
- 7° Sistema gera um gráfico geral da turma, onde é possível ver as todas as matérias e suas informações (quantidade de recuperações, média da matéria, etc);

# Ferramentas Utilizadas

- Html
- Css
- Javascript
- Python
  Django;
  Pandas;
  Pygraph;
