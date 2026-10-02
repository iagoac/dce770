# Um algoritmo genético para o problema do caminho mais longo

Seja o problema do caminho mais longo como definido no material anexo e disponível em [caminho_mais_longo.pdf](caminho_mais_longo.pdf). Para esta atividade (e para as demais), considere o caminho mais longo entre quaisquer par de vértices do grafo.

O objetivo desta atividade prática é desenvolver
 - Um algoritmo evolutivo para o problema do caminho mais longo. Mais especificamente, deverá ser implementado um algoritmo genético
 
A metaheurística poderá utilizar qualquer mecanismo desenvolvido nas aulas passadas, incluindo as heurísticas construtivas e/ou os esquemas de vizinhança das buscas locais. A metaheurística desenvolvida deverá ter, como critério de parada, um **tempo máximo de 30 segundos**. Além disso, caso necessário, o algoritmo de reparo desenvolvido na aula 08 pode ser utilizado para gerar soluções válidas a partir de soluções inválidas.

O código desenvolvido deve ser entregue no Moodle da disciplina até o dia **07/10/2026** às **09h59**. A entrega é **individual** e valerá, além dos pontos destinados a esta atividade, presença na aula de quarta-feira.

---

## Orientações

Pode-se buscar inspirações em outros artigos da literatura ou no nosso livro base. Recomenda-se que sejam utilizados mecanismos de mutação e cruzamento tradicionais da literatura ao invés de tentar criar novos operadores evolutivos.

## Questões para reflexão e discussão

1. Como é o comportamento do algoritmo evolutivo em comparação com as metaheurísticas de busca local das aulas passadas?
2. Múltiplas execuções de seu algoritmo produzem soluções finais diferentes? Em caso positivo, quais seriam as causas mais prováveis para isso?