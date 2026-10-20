# Um algoritmo BRKGA para o problema do caminho mais longo

Seja o problema do caminho mais longo como definido no material anexo e disponível em [caminho_mais_longo.pdf](caminho_mais_longo.pdf). Para esta atividade (e para as demais), considere o caminho mais longo entre quaisquer par de vértices do grafo.

O objetivo desta atividade prática é desenvolver
 - Um algoritmo de evolução diferencial ou de enxame de partículas para o problema do caminho mais longo. 

O código desenvolvido deve ser entregue no Moodle da disciplina até o dia **19/10/2026** às **09h59**. A entrega é **individual**.

---

## Orientações

Ambos os algoritmos foram originalmente desenhados para trabalhar com variáveis contínuas, sendo que o problema do caminho mais longo possui uma representação diferente. Desta forma, vocês podem optar por duas abordagens diferentes
1. Utilizar um decoder (similar ao do BRKGA) dentro do evolução diferencial ou do enxame de partículas
2. Implementar operadores evolutivos que trabalham com outros tipos de variáveis
 - Vocês podem procurar estes operadores em qualquer lugar da Internet

## Questões para reflexão e discussão

1. Se vocês utilizaram o decoder, como é o comportamento deste algoritmo em comparação com o BRKGA?
2. Se vocês criaram novos operadores, discutam a semelhança destes com os operadores de um algoritmo genético clássico.
3. Múltiplas execuções de seu algoritmo produzem soluções finais diferentes? Em caso positivo, quais seriam as causas mais prováveis para isso?