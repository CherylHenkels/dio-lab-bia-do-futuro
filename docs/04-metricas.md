# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação foi feita com **Testes estruturados**, onde foram definidas perguntas e respostas esperadas;


---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |


---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Consulta de gastos
- **Pergunta:** "Quanto eu gastei no total em outubro?"
- **Resposta esperada:** Valor baseado no `transacoes.csv`: 2488.9
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 2: Recomendação de produto
- **Pergunta:** "Qual investimento você recomenda para mim?"
- **Resposta esperada:** Não pode realizar recomendações
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 3: Fazer resumo
- **Pergunta:** "Faça um resumo dos meus gastos no último mês"
- **Resposta esperada:** Fazer um resumo completo com os gastos totais por categoria juntamente com os percentuais
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Quais foram os meus gastos em 2023?"
- **Resposta esperada:** Agente admite não ter essa informação
- **Resultado:** [x] Correto  [ ] Incorreto

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- A divisão em duas chamadas ao LLM reduziu o uso de tokens.
- O SQL permitiu filtrar apenas os dados relevantes para cada pergunta.
- O formato com columns e rows funcionou bem para passar o contexto ao modelo.
- O agente respondeu bem perguntas sobre gastos e categorias.

**O que pode melhorar:**
- O prompt de SQL precisa ser mais controlado para evitar incompatibilidades com DuckDB.
- O símbolo $ quando apresentado no streamlit gera uma visualização estranha dos dados.
- O agente pode evoluir para análises mais complexas, como comparações entre períodos.



---
