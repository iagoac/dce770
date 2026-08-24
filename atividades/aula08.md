# Um algoritmo de reparo para soluções do problema do caminho mais longo

Seja o problema do caminho mais longo como definido no material anexo e disponível em [caminho_mais_longo.pdf](caminho_mais_longo.pdf). Para esta atividade (e para as demais), considere o caminho mais longo entre quaisquer par de vértices do grafo.

O objetivo desta atividade prática é desenvolver
 - Um algoritmo que verifica se uma solução é válida ou não 
 - Um algoritmo que repara uma solução inválida
 
O algoritmo de verificação deve iterar sobre as arestas da solução e verificar se a solução é válida. Note que uma solução é válida se ela não contém o mesmo vértice duas vezes.

Já o algoritmo de reparo deve receber uma solução inválida e retornar uma solução válida. Para isso, o algoritmo deve *destruir* parte da solução inválida e reconstruí-la de forma que ela se torne válida. Por exemplo, se a solução inválida contém um vértice duas vezes, o algoritmo deve remover uma das ocorrências do vértice e tentar adicionar outro vértice no lugar. O algoritmo deve parar quando a solução for válida.

O código desenvolvido deve ser entregue no [Moodle da disciplina](https://campusvirtual.unifal-mg.edu.br/moodle/mod/assign/view.php?id=154952) até o dia **31/08/2026** às **09h59**. A entrega é **individual** e valerá, além dos pontos destinados a esta atividade, presença na aula do dia 26/08/2026.

---

## Orientações

Uma estratégia válida para o reparo é utilizar um algoritmo no estilo *backtracking*. De forma simplificada, você deve retirar arestas da solução inválida em ordem inversa (do fim da solução até o início) até que ela se torne válida. Após isto, você deve reaplicar o algoritmo construtivo sobre esta solução parcial de forma a completá-la e obter uma nova solução.

Para realizar esta atividade, você deve utilizar como base o código que desenvolveu na aula 06. Além disso, você deve gerar, de forma artificial, uma solução inválida para utilizar como teste de seu algoritmo de reparo.

## Questões para reflexão e discussão

1. Como se comportou o algoritmo de reparo? Ele é rápido? Sempre consegue gerar uma solução válida?
2. O seu algoritmo de reparo é determinístico?