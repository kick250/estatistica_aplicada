# Estatística Aplicada e Análise Exploratória de Dados TP3

Este TP avalia a competência de avaliar análises de dados produzidas com suporte de IA generativa, cobrindo formulação de prompts para geração de código de limpeza, avaliação crítica de código gerado por IA, formulação de perguntas analíticas com apoio de IA, execução de análise descritiva com código gerado por LLM, aplicação de testes de hipótese com SciPy via LLM (com foco em intervalos de confiança, não apenas p-valor), interpretação de p-valor e intervalo de confiança, e avaliação da qualidade de interpretações geradas por LLMs.

Este TP reutiliza a mesma base de tickets da CloudDesk dos TPs anteriores, sem gerar dados novos. Recarregue os três arquivos brutos (tickets_suporte.csv, planos_clientes.xlsx e chatbot_triagem.json) que você já tem salvos localmente e repita, no início do seu notebook, as mesmas etapas de conversão de tipos, tratamento de nulos, remoção de duplicatas e combinação (merge) feitas no TP1, chegando ao mesmo DataFrame consolidado usado a partir daqui.

## Exercício 1

### Contexto
Na CloudDesk, a demanda por relatórios de dados cresceu, e seu líder técnico pediu que você acelerasse a etapa de limpeza de dados usando um LLM (ChatGPT, Gemini , Claude, Grok, outros) como copiloto, em vez de escrever manualmente cada linha de tratamento como nas etapas anteriores da disciplina, sobre a mesma base de tickets já usada no TP1 e no TP2. A tarefa não é delegar a decisão ao modelo, e sim usar o LLM para gerar candidatos de código que você mesmo vai revisar. Um prompt vago produz código genérico; um prompt específico, com o schema e as regras de negócio do dataset, produz código diretamente aplicável.

### Tarefa
1. Escreva um prompt para um LLM pedindo código pandas que trate valores ausentes em tempo_resposta_horas e remova duplicatas em ticket_id, incluindo no prompt o nome exato das colunas e o critério de negócio (ex.: preencher com a mediana por categoria).
2. Cole a resposta do LLM no notebook, junto com o prompt utilizado.
3. Execute o código gerado sobre a base de tickets e confirme se o resultado é equivalente ao obtido manualmente no TP1.


## Exercício 2

### Contexto
O código gerado pelo LLM no Exercício 1 pode parecer correto à primeira vista, mas só um engenheiro de dados com domínio da base sabe se ele realmente respeita as regras de negócio da CloudDesk. Seu líder técnico é enfático: nenhum código gerado por IA entra em produção sem revisão crítica de quem entende o dataset.

### Tarefa
1. Liste três aspectos do código gerado no Exercício 1 que precisam ser verificados manualmente antes de confiar no resultado (ex.: a estratégia de preenchimento escolhida pelo LLM realmente corresponde à mediana por categoria pedida, ou o modelo usou a mediana global por engano).
2. Identifique, se houver, algum erro, suposição incorreta ou comportamento inesperado no código gerado, testando-o sobre um subconjunto conhecido dos dados.
3. Corrija o código, se necessário, e registre no notebook a diferença entre a versão gerada pelo LLM e a versão corrigida por você.


## Exercício 3

### Contexto
Antes de pedir qualquer análise a um LLM, um engenheiro de dados precisa saber exatamente que pergunta está tentando responder. Seu líder técnico pediu que você formule, com apoio de IA, as perguntas analíticas mais relevantes para entender o que mais influencia a satisfação do cliente na CloudDesk, antes de qualquer linha de código ser escrita.

### Tarefa
1. Use um LLM para gerar uma lista de perguntas analíticas candidatas sobre os fatores associados à satisfação do cliente, fornecendo como contexto as colunas disponíveis no dataset de tickets.
2. Selecione, entre as perguntas geradas, as três mais respondíveis com os dados disponíveis e justifique a escolha.
3. Descarte explicitamente qualquer pergunta gerada que exigiria dados que a CloudDesk não possui, explicando por quê.


## Exercício 4

### Contexto
Com as perguntas analíticas definidas no Exercício 3, é hora de produzir as respostas. Em vez de escrever manualmente cada agregação e gráfico como nos TPs anteriores, você vai usar um LLM para gerar o código pandas necessário, revisando e executando cada trecho antes de aceitar o resultado como parte da análise final.

### Tarefa
1. Para cada uma das três perguntas selecionadas no Exercício 3, peça ao LLM que gere o código pandas de análise descritiva correspondente (agregações, filtros, estatísticas).
2. Execute cada trecho de código gerado sobre a base de tickets e registre o resultado.
3. Para cada resultado, escreva uma frase de interpretação em linguagem de negócio, conectando o número aos fatores associados à satisfação do cliente investigados no Exercício 3.


## Exercício 5

### Contexto
Suponha que uma das perguntas respondidas no Exercício 4 sugere que tickets abertos pelo canal "chat" têm satisfação média menor que tickets abertos por "email". Seu líder técnico quer saber se essa diferença é real ou apenas ruído amostral, antes de recomendar qualquer mudança operacional. Ao pedir a um LLM que estruture esse tipo de comparação, é comum que ele sugira de cara um teste de hipótese clássico baseado em p-valor, por ser o método mais popular. Mas seu líder técnico quer que a equipe realmente entenda o que um p-valor diz e não diz, e prefere que ela raciocine em termos de intervalos de confiança, que comunicam melhor o tamanho da diferença e a incerteza em torno dela. Você precisa estar pronto para redirecionar a análise nessa direção caso o LLM proponha outra coisa primeiro, e para isso precisa entender o suficiente sobre p-valor para não aceitar a primeira sugestão sem questionar.

### Tarefa
1. Peça a um LLM que proponha uma forma de comparar a satisfação média entre os canais "chat" e "email", e registre a sugestão recebida.
2. Peça ao LLM que explique, em termos conceituais, o que o p-valor de um teste de hipótese representa, o que um analista deveria (e não deveria) concluir a partir dele, e como ele se relaciona com a distribuição amostral da estatística testada. Valide essa explicação: aponte, por escrito, se ela está completa e correta ou se omite alguma limitação importante do p-valor (por exemplo, não informar o tamanho do efeito).
3. Se a primeira sugestão do LLM (item 1) tiver sido um teste de hipótese com p-valor, peça explicitamente que ele refaça a proposta usando intervalos de confiança em vez disso, e execute o código gerado para calcular, com scipy.stats.bootstrap, o intervalo de confiança de 95% da satisfação média de cada canal.
4. Compare os dois intervalos (sobrepõem-se ou não) e registre, em uma frase, o que essa sobreposição (ou ausência dela) sugere sobre a diferença entre os canais.


## Exercício 6

### Contexto
Os dois intervalos de confiança do Exercício 5 não significam nada para o time de suporte se não forem traduzidos em uma conclusão de negócio clara. Seu líder técnico pediu que você use IA para ajudar a interpretar o resultado, mas a decisão final sobre o que comunicar é sua, não do modelo.

### Tarefa
1. Peça a um LLM que interprete a comparação de intervalos de confiança do Exercício 5.
2. Peça ao LLM que explique, passo a passo, o raciocínio por trás dessa interpretação: por que a sobreposição (ou ausência dela) entre os dois intervalos sugere algo sobre a diferença real entre os canais, e como esse raciocínio se conecta à distribuição amostral estimada pelo bootstrap no Exercício 5. Use essa explicação para validar a interpretação do item 1, apontando por escrito, frase por frase, se cada afirmação do LLM está correta ou se contém algum erro (ex.: tratar intervalos que não se sobrepõem como prova automática de que a diferença importa na prática, sem considerar o tamanho real da diferença entre os canais).
3. Escreva a conclusão final, em linguagem acessível ao time de suporte, sobre se o canal de abertura do ticket influencia a satisfação do cliente de forma relevante o suficiente para justificar uma mudança operacional.


## Exercício 7

### Contexto
Antes de apresentar a comparação entre canais (Exercícios 4 a 6) à liderança da CloudDesk, seu líder técnico quer um gráfico que comunique o achado de forma visual, e pediu que você use um LLM para acelerar essa etapa também. Um gráfico gerado por IA pode parecer pronto para uso, mas carrega as mesmas armadilhas de qualquer código gerado sem revisão: um tipo de gráfico mal escolhido, um eixo que distorce a diferença real, ou uma agregação que esconde a variabilidade por trás da média, podem levar a liderança a uma conclusão errada mesmo com os números corretos por trás do gráfico.

### Tarefa
1. Peça a um LLM que gere, com matplotlib ou seaborn, um gráfico que visualize a comparação de satisfação média entre os canais "chat" e "email" (Exercícios 4 a 6), fornecendo como contexto o DataFrame disponível e a pergunta que o gráfico deve responder.
2. Execute o código gerado e avalie criticamente as escolhas feitas pela IA: o tipo de gráfico é adequado para comparar dois grupos, o eixo começa em zero ou foi recortado de forma a exagerar a diferença visualmente, e a agregação usada (média) esconde alguma variabilidade relevante que um boxplot ou uma faixa de intervalo de confiança comunicaria melhor?
3. Corrija o gráfico onde a avaliação do item 2 identificou um problema, e escreva um título e uma legenda que comuniquem o achado de forma precisa ao time de suporte, sem exagerar a diferença real entre os canais.


## Exercício 8

### Contexto
Para consolidar tudo o que foi trabalhado neste TP, seu líder técnico pediu um mini pipeline de análise assistida por IA, do início ao fim, sobre um recorte diferente do dataset: os tickets da categoria "bug" nos 30 dias mais recentes do período coberto pela base. O objetivo é demonstrar que você consegue conduzir o ciclo completo (limpeza com IA, formulação de perguntas, análise descritiva, comparação por intervalo de confiança e avaliação crítica) de forma independente, sem depender de um roteiro exercício a exercício.

### Tarefa
1. Use um LLM para gerar e revisar o código de limpeza do recorte de tickets de categoria "bug" nos 30 dias mais recentes do período coberto pela base.
2. Formule, com apoio de IA, uma pergunta analítica relevante sobre esse recorte que envolva comparar uma métrica numérica entre dois subgrupos, e obtenha a resposta com código gerado por LLM.
3. Peça ao LLM que estruture essa comparação; se ele sugerir um teste de hipótese clássico com p-valor, redirecione a análise para intervalos de confiança via scipy.stats.bootstrap, como praticado nos Exercícios 5 e 6, e peça ao LLM que explique o resultado. Valide essa explicação por escrito antes de aceitá-la.
4. Feche com uma avaliação crítica de todo o processo: aponte um ponto em que a IA foi confiável e um ponto em que sua revisão humana foi indispensável.
