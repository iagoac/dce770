# Um algoritmo de busca local para o problema do caminho mais longo

Seja o problema do caminho mais longo como definido no material anexo e disponível em [caminho_mais_longo.pdf](caminho_mais_longo.pdf). Para esta atividade (e para as demais), considere o caminho mais longo entre quaisquer par de vértices do grafo.

O objetivo desta atividade prática é desenvolver
 - Um (ou mais) esquemas de vizinhança para o problema do caminho mais longo
 - Um algoritmo de busca local para o problema do caminho mais longo
 
O algoritmo de busca local deve receber uma solução (valida ou nao) e tentar refina-la através da aplicação sucessiva de movimentos no esquema de vizinhança escolhido. O algoritmo deve parar quando nao for mais possível encontrar um movimento que melhore a solução.

A solução inicial pode ser gerada pela heurística gulosa desenvolvida na aula 06. Além disso, caso necessário, o algoritmo de reparo desenvolvido na aula 08 pode ser utilizado para gerar soluções válidas a partir de soluções inválidas.

O código desenvolvido deve ser entregue no [Moodle da disciplina](https://campusvirtual.unifal-mg.edu.br/moodle/mod/assign/view.php?id=155943&forceview=1) até o dia **14/09/2026** às **09h59**. A entrega é **individual** e valerá, além dos pontos destinados a esta atividade, presença na aula do dia 02/09/2026.

---

## Orientações

Pode-se buscar inspirações de vizinhanças para problemas de caminho ou roteamento na literatura. Normalmente, estas vizinhanças englobam a remoção e inserção de uma ou mais arestas do caminho. A remoção de uma aresta faz com que a solução torne-se incompleta, sendo necessário reconectar as duas partes do caminho utilizando diferentes arestas.

## Questões para reflexão e discussão

1. O algoritmo de busca local foi capaz de refinar a solução dada pela heurística gulosa desenvolvida na aula 06?
2. Múltiplas execuções de seu algoritmo produzem soluções finais diferentes? Em caso positivo, quais seriam as causas mais prováveis para isso?