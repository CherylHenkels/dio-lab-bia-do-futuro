# Base de Conhecimento

## Dados Utilizados

Foi usado como base de conhecimento o arquivo da pasta `data`:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente |

> [!NOTA]
> A base foi enriquecida com mais registros para simular mais situações de interesse do cliente.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Sim, a base de transações foi enriquecida com mais registros para simular mais situações de interesse do cliente.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

[ex: O CSV é carregado no início da sessão usando pandas e incluídos no user prompt]

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Como a base contém muitas transações ao longo de um ano inteiro, enviar todos os dados diretamente ao LLM seria ineficiente e aumentaria desnecessariamente o consumo de tokens.

Por isso, foi adotada uma arquitetura com **duas chamadas** ao modelo:

Na primeira chamada, o LLM recebe a pergunta do usuário e gera uma consulta SQL. Essa consulta é usada para buscar, filtrar e organizar apenas os dados relevantes na base.

Na segunda chamada, o LLM recebe a pergunta original junto com os dados já filtrados e estruturados. Esses dados são enviados no **user prompt**. A partir disso, o modelo produz a resposta final, com resumo, insights e explicações para o cliente.

Assim, os dados são consultados dinamicamente, de acordo com a pergunta feita, e apenas a parte necessária da base é enviada ao modelo.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

Antes de chegar ao LLM, os dados relevantes são obtidos com SQL. O resultado da aplicação do SQL no dataset (pandas database) é convertido para um formato simples, para que o agente consiga ler e interpretar as informações com facilidade.

O formato escolhido possui duas partes:
- `columns:` lista com os nomes das colunas do resultado;
- `rows:` lista com os valores de cada linha do resultado.

Ou seja, o agente recebe:
- quais são os campos disponíveis;
- e quais valores apareceram em cada registro.

```markdown
```json
{
  "columns": ["coluna1", "coluna2"],
  "rows": [
    ["linha1_valor1", "linha1_valor2"],
    ["linha2_valor1", "linha2_valor2"]
  ]
}
```

Exemplo prático:

```markdown
```json
Dados: {"columns": ["categoria", "total_categoria", "percentual_gasto", "total_entrada", "total_saida"], 
           "rows": [["lazer", 46.0, 1.84, 5300.0, 2497.0], 
                    ["transporte", 299.0, 11.97, 5300.0, 2497.0], 
                    ["moradia", 1335.0, 53.46, 5300.0, 2497.0], 
                    ["alimentacao", 636.0, 25.47, 5300.0, 2497.0], 
                    ["saude", 181.0, 7.25, 5300.0, 2497.0]]}
Pergunta: Faça um resumo dos meus gastos no último mês
...
```
