# Estatística Aplicada e Análise Exploratória de Dados TP2

Este TP avalia a competência de explorar dados reais com limpeza, probabilidade e visualização estatística, cobrindo regras de probabilidade e teste de independência entre variáveis, distinção entre variáveis aleatórias contínuas e discretas, interpretação de PDF e CDF, avaliação de suposições de distribuição, construção de histogramas e boxplots, scatter plots, heatmaps de correlação e cálculo de correlação e covariância (inclusive por subgrupo).

Este TP reutiliza a mesma base de tickets da CloudDesk do TP1, sem gerar dados novos. Recarregue os três arquivos brutos (tickets_suporte.csv, planos_clientes.xlsx e chatbot_triagem.json) que você já tem salvos localmente e repita, no início do seu notebook, as mesmas etapas de conversão de tipos, tratamento de nulos, remoção de duplicatas e combinação (merge) feitas no TP1, chegando ao mesmo DataFrame consolidado usado a partir daqui.

## Exercício 1

### Contexto

Na CloudDesk, o time de suporte quer saber a chance de um cliente abrir mais de um ticket na mesma semana. Antes de qualquer modelo sofisticado, seu líder técnico pediu que você estimasse essa probabilidade manualmente, a partir das frequências observadas na base consolidada de tickets do TP1, para validar a intuição do time antes de formalizar qualquer análise mais avançada.

### Tarefa
- Estime a probabilidade de um ticket ser de prioridade "alta" (P(alta)) usando a frequência relativa observada na base de tickets.
- Estime a probabilidade de um cliente abrir um segundo ticket na mesma semana.
- Estime a probabilidade de um ticket ser de prioridade "alta" OU ter sido aberto pelo canal "chat", e atentando para o caso de sobreposição entre os eventos.


## Exercício 2

### Contexto

Um colega de time sugeriu tratar tempo_resposta_horas e categoria da mesma forma ao descrever sua distribuição estatística, mas você sabe que uma é uma variável aleatória contínua e a outra é discreta (categórica). Seu líder técnico pediu que você esclarecesse essa diferença com exemplos concretos do próprio dataset de tickets, para alinhar o vocabulário estatístico do time antes da próxima reunião de produto.

### Tarefa
- Classifique tempo_resposta_horas, satisfacao_cliente (nota de 1 a 5) e categoria como variáveis contínuas ou discretas, justificando cada classificação.
- Para a variável contínua identificada, descreva que tipo de função (PDF) descreveria sua distribuição de probabilidade. Autorizado o uso de IA nessa questão para você explorar as possibilidades. Escolha e justifique.
- Para a variável discreta identificada, descreva que tipo de função (PMF) descreveria sua distribuição de probabilidade. Autorizado o uso de IA nessa questão para você explorar as possibilidades. Escolha e justifique.


## Exercício 3

### Contexto

O time de suporte precisa saber, com base na distribuição observada, qual a probabilidade de um ticket levar mais de 10 horas para receber a primeira resposta. Essa informação vai compor um SLA (Service Level Agreement) revisado. Para respondê-la corretamente, você precisa trabalhar com a função de distribuição acumulada (CDF) da variável tempo_resposta_horas, não apenas com sua média.

### Tarefa
- Estime a distribuição empírica de tempo_resposta_horas a partir dos dados da base consolidada.
- Utilize a CDF empírica para calcular a proporção de tickets com tempo de resposta acima de 10 horas.


## Exercício 4

### Contexto

Antes de qualquer conclusão sobre o tempo de resposta da CloudDesk, seu líder técnico pediu uma inspeção visual da distribuição de tempo_resposta_horas e tempo_resolucao_horas. Médias e medianas escondem outliers, como tickets que ficaram parados por dias por falha operacional, que podem distorcer decisões se não forem identificados visualmente antes de qualquer análise numérica mais profunda.

#### Tarefa
- Construa um histograma de tempo_resposta_horas, escolhendo um número de bins que revele a forma da distribuição.
- Construa um boxplot de tempo_resolucao_horas segmentado por prioridade.
- Identifique, a partir do boxplot, quais categorias de prioridade concentram mais outliers e registre essa observação em uma célula de markdown.


## Exercício 5

### Contexto

Um analista de produto levantou a hipótese de que tickets com tempo de resposta maior tendem a ter tempo de resolução maior também, o que faria sentido operacionalmente. Antes de calcular qualquer correlação numérica, seu líder técnico pediu uma inspeção visual dessa relação usando scatter plots, prática comum para detectar padrões, tendências não lineares ou ausência de relação antes de qualquer modelagem.

### Tarefa
- Construa um scatter plot de tempo_resposta_horas (eixo X) contra tempo_resolucao_horas (eixo Y).
- Construa um segundo scatter plot de tempo_resposta_horas contra satisfacao_cliente.
- Descreva, em uma frase por gráfico, se a relação visual sugere associação linear, não linear ou ausência de relação aparente.


## Exercício 6

### Contexto

Seu líder técnico quer um panorama geral de como todas as variáveis numéricas do dataset de tickets se relacionam entre si, antes de decidir quais pares merecem investigação mais profunda. Em vez de gerar dezenas de scatter plots individuais, a prática recomendada é construir um único heatmap de correlação que revele os pares mais fortemente relacionados de uma só vez.

### Tarefa
- Selecione as colunas numéricas relevantes do dataset de tickets (tempo_resposta_horas, tempo_resolucao_horas, satisfacao_cliente, entre outras disponíveis).
- Construa um heatmap de correlação dessas variáveis usando seaborn.
- Aponte, com base no heatmap, os dois pares de variáveis com maior correlação (positiva ou negativa) e proponha uma hipótese de negócio para cada um.


## Exercício 7

### Contexto

Os coeficientes visuais do heatmap do Exercício 6 precisam ser confirmados numericamente antes de entrarem em qualquer relatório oficial para a liderança da CloudDesk. Coeficientes de correlação e covariância exatos permitem comparar a força da relação entre pares de variáveis de forma objetiva, sem depender apenas da leitura visual do heatmap.

### Tarefa
- Calcule a matriz de correlação de Pearson das variáveis numéricas selecionadas com pandas.corr().
- Calcule a matriz de covariância das mesmas variáveis com pandas.cov().
- Explique, em uma frase, por que o coeficiente de correlação é mais interpretável entre variáveis com escalas diferentes do que a covariância bruta.


## Exercício 8

### Contexto

Seu líder técnico pediu uma primeira síntese sobre a variável mais crítica do negócio: satisfacao_cliente.

### Tarefa
- Construa um histograma da distribuição de satisfacao_cliente e descreva sua forma (simétrica, assimétrica à esquerda ou à direita).
- Identifique, usando a matriz de correlação do Exercício 7, qual variável tem a correlação mais forte com satisfacao_cliente e escreva um parágrafo curto conectando distribuição e correlação nessa conclusão.


## Exercício 9

### Contexto

Um colega do time afirmou, sem verificar, que tempo_resposta_horas segue uma distribuição normal, e quer usar essa suposição para calcular um novo SLA baseado em média e desvio padrão. Antes de aceitar esse ponto de partida, você precisa checar se a suposição é razoável, porque um SLA calculado sobre a distribuição errada vai subestimar ou superestimar o tempo real de resposta.

### Tarefa
- Calcule a assimetria (skewness) da distribuição de tempo_resposta_horas.
- Construa um histograma da variável sobreposto a uma curva normal com a mesma média e o mesmo desvio padrão dos dados observados.
- Com base na assimetria calculada e na comparação visual, responda em célula de markdown se a suposição de normalidade do colega é razoável.
- Proponha uma família de distribuição probabilística mais adequada para tempo_resposta_horas. Autorizado o uso de IA para este item 4.


## Formato de entrega

- Deve ser criado um notebook Jupyter em um único arquivo .ipynb, com o código executado de todos os exercícios, bem como as respostas textuais pertinentes.
- As respostas devem incluir a explicação ou justificativa das decisões tomadas (estratégias de tratamento de nulos, critérios de merge, escolhas de tipo, etc.).
- O código deve estar organizado por exercício, com células de markdown separando cada etapa.
- Inclua o output das inspeções (shape, dtypes, contagens, gráficos) como evidência no próprio notebook.
- Assim que terminar, salve seu trabalho em um arquivo .ipynb, nomeando-o conforme a regra “nome_sobrenome_DR1_TP2.ipynb” e envie como resposta a este TP.

Mãos à obra e bons estudos!