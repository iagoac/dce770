# Uma heurística construtiva para o problema do caminho mais longo

Seja o problema do caminho mais longo como definido no material anexo e disponível em [caminho_mais_longo.pdf](caminho_mais_longo.pdf). Para esta atividade (e para as demais), considere o caminho mais longo entre quaisquer par de vértices do grafo.

O objetivo desta atividade prática é desenvolver uma (ou mais) heurística(s) construtiva(s) para o problema do caminho mais longo. Vocês devem utilizar como base a implementação disponível neste diretório, não sendo permitido alterar a maneira como são fornecidas as entradas ou como são produzidas as saídas do programa. 

Um conjunto de instâncias básicas de teste são fornecidas junto com o código do problema. Além disso, um gerador de instâncias também está disponível caso vocês se interessem em avaliar um conjunto diferente de casos de teste.

O código desenvolvido deve ser entregue no [Moodle da disciplina](https://campusvirtual.unifal-mg.edu.br/moodle/mod/assign/view.php?id=154104&forceview=1). A entrega é **individual** e valerá, além dos pontos destinados a esta atividade, presença na aula do dia **19/08/2026**.

---

## Orientações

Uma estratégia válida para a solução do problema é utilizar uma heurística construtiva para escolher qual vértice adicionar ao caminho, em cada iteração, visando "explorar" o grafo da melhor maneira possível. 

Neste sentido, uma primeira heurística construtiva é a seguinte:

1. **Escolha um vértice inicial** de forma arbitrária (por exemplo, o de menor grau).
2. **Escolha o próximo vértice** a ser adicionado ao caminho como aquele que possui o **maior grau** entre os vértices ainda não visitados.
3. **Repita** o passo 2 até que todos os vértices tenham sido visitados.

## Questões para reflexão e discussão

1. Esta heurística se mostrou eficiente? Por que?
2. Como poderíamos modificá-la para melhorar o resultado? Você consegue imaginar alguma outra heurística que poderia funcionar? Quais seriam os prós e contras em relação à primeira?
3. Como poderíamos avaliar a qualidade de uma heurística construtiva? Quais métricas você acha que seriam interessantes de serem avaliadas?
4. Você consegue pensar em alguma outra maneira de atacar o problema do caminho mais longo? (Não é necessário implementar as soluções, apenas discuti-las.)
5. A heurística proposta é gulosa. É possível pensar em alguma solução que não seja gulosa? Quais seriam os prós e contras em relação à solução gulosa?