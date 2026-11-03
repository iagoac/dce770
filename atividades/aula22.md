# Um algoritmo NSGA-II BRKGA para o problema do caminho mais longo bi-objetivo

Seja o problema do caminho mais longo como definido no material anexo e disponível em [caminhoMaisLongoBiobjetivo.pdf](caminhoMaisLongoBiobjetivo.pdf). Para esta atividade, considere o caminho mais longo bi-objetivo entre quaisquer par de vértices do grafo.

O objetivo desta atividade prática é desenvolver
 - Um conjunto de novas instâncias com dois pesos por aresta para o problema estudado
 - Um algoritmo NSGA-II para o a variante bi-objetivo do problema do caminho mais longo

O código desenvolvido deve ser entregue no Moodle da disciplina até o dia **09/11/2026** às **09h59**. A entrega é **individual**.

---

## Orientações

Vocês podem atualizar o gerador de instâncias do problema mono-objetivo para gerar dois pesos por aresta. Além disso, operadores evolutivos (como a seleção, cruzamento e mutação) podem ser adaptados dos algoritmos passados. Vocês podem escolher a representação qe quiserem, inclusive uma indireta utilizando chaves aleatórias e um decoder.

## Questões para reflexão e discussão

1. Como vocês realizam a comparação dos resultados?
2. Como vocês fazem a visualização dos resultados em gráficos? Vocês são capazes de plotar as fronteiras de Pareto?