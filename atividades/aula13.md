# Uma metaheurística de busca local para o problema do caminho mais longo

Seja o problema do caminho mais longo como definido no material anexo e disponível em [caminho_mais_longo.pdf](caminho_mais_longo.pdf). Para esta atividade (e para as demais), considere o caminho mais longo entre quaisquer par de vértices do grafo.

O objetivo desta atividade prática é desenvolver
 - Uma metaheurística de busca local para o problema do caminho mais longo. Podem ser desenvolvidas
   - Um algoritmo VND
   - Um algoritmo VNS
   - Um algoritmo GRASP
 
A metaheurística desenvolvida deverá utilizar os esquemas de vizinhança e a heurística construtiva desenvolvidas nas aulas passadas. A metaheurística desenvolvida deverá ter, como critério de parada, um **tempo máximo de 30 segundos**. Além disso, caso necessário, o algoritmo de reparo desenvolvido na aula 08 pode ser utilizado para gerar soluções válidas a partir de soluções inválidas.

O código desenvolvido deve ser entregue no [Moodle da disciplina](https://campusvirtual.unifal-mg.edu.br/moodle/mod/assign/view.php?id=157192) até o dia **21/09/2026** às **09h59**. A entrega é **individual** e valerá, além dos pontos destinados a esta atividade, presença na aula do dia 02/09/2026.

---

## Orientações

Pode-se buscar inspirações em outros artigos da literatura ou no nosso livro base. Caso as estruturas de vizinhança já estejam bem feitas, será simples implementar a metaheurística escolhida.

## Questões para reflexão e discussão

1. A metaheurística desenvolvida é capaz de obter melhores resultados que a busca local simples da aula anterior?
2. Múltiplas execuções de seu algoritmo produzem soluções finais diferentes? Em caso positivo, quais seriam as causas mais prováveis para isso?