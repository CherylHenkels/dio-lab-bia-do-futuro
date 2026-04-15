# Pitch (3 minutos)

> [!TIP]
> Você pode usar alguns slides pra apoiar no seu Pitch e mostrar sua solução na prática.
 
## Roteiro Sugerido

### 1. O Problema (30 seg)
> Qual dor do cliente você resolve?

Você já chegou ao fim do mês, viu a fatura do cartão e se assustou com o valor?
E então se perguntou:  Para onde foi o meu dinheiro?

Bom, você não está sozinho. Muitas pessoas têm dificuldade de acompanhar seus gastos e entender para onde o dinheiro está indo ao longo do mês.
Mesmo tendo acesso às transações, muitas vezes falta uma forma simples e rápida de controlar os gastors e transformar esses dados em respostas úteis para o dia a dia.

### 2. A Solução (1 min)
> Como seu agente resolve esse problema?

Pensando nesse problema, eu criei um agente capaz de responder dúvidas relacionadas aos gastos do usuário nos últimos 12 meses.

Agora, a pessoa não precisa mais passar horas montando planilhas ou olhando a fatura do cartão para tentar descobrir para onde o dinheiro foi.
O Fiscal da Fatura foi criado justamente para responder essas dúvidas e ajudar o usuário a identificar se está gastando mais do que o planejado em alguma categoria.

Basta fazer uma pergunta pelo chat, e ele responde de forma rápida e objetiva.

E como essa solução funciona?

Quando o usuário envia uma pergunta no chat, ela é enviada para um LLM, que interpreta a solicitação e gera uma query SQL para buscar os dados necessários.
Depois, usamos o DuckDB para executar essa consulta e obter os dados relevantes.
Por fim, chamamos novamente o LLM, agora com os dados já filtrados, para gerar uma resposta final clara e fácil de entender para o usuário.


### 3. Demonstração (1 min)
> Mostre o agente funcionando (pode ser gravação de tela)

E agora, vamos ver como isso funciona na prática?

Aqui vocês podem ver a interface do nosso chat. O funcionamento é bem simples: basta digitar a pergunta na caixa de texto e clicar em enviar.
Nesse momento, o sistema processa a pergunta, consulta os dados e gera a resposta.

E pronto: temos a resposta de forma rápida e organizada.

Mas não precisamos nos limitar apenas a perguntas curtas. Também podemos pedir, por exemplo, um relatório de gastos de um período específico.
Nesse caso, o agente organiza as informações e apresenta uma visão mais clara dos gastos realizados, inclusive por categoria.

Além disso, é importante destacar que o agente trabalha com as transações dos últimos 12 meses e não faz recomendações financeiras.
Se o usuário pedir algo fora desse escopo, ele informa que não possui dados suficientes para responder naquele momento.


### 4. Diferencial e Impacto (30 seg)
> Por que essa solução é inovadora e qual é o impacto dela na sociedade?

O grande diferencial do **Fiscal da Fatura** é transformar dados financeiros em respostas simples, acessíveis e úteis por meio de uma conversa natural.

Em vez de exigir que a pessoa saiba montar planilhas ou interpretar extratos complexos, o agente permite que ela simplesmente pergunte o que quer saber.

Com isso, a solução ajuda o usuário a ter mais controle sobre seus gastos, evitar sustos no fim do mês e gerar insights importantes sobre sua vida financeira de forma prática e intuitiva.

---

## Checklist do Pitch

- [x] Duração máxima de 3 minutos
- [x] Problema claramente definido
- [x] Solução demonstrada na prática
- [x] Diferencial explicado
- [x] Áudio e vídeo com boa qualidade

---

## Link do Vídeo

> Cole aqui o link do seu pitch (YouTube, Loom, Google Drive, etc.)

[\[Link do vídeo\]](https://youtu.be/qot8jr5taSs)
