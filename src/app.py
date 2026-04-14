import streamlit as st

############ Fiscal da Fatura ############


# -------- Bibliotecas ----------
import pandas as pd
import duckdb
import json
import streamlit as st
from pathlib import Path
import openai
from openai import OpenAI

from datetime import date

today = date.today()

# -------- Importa dados ----------

BASE_DIR = Path(__file__).resolve().parent.parent
ARQUIVO_CSV = BASE_DIR / "data" / "transacoes.csv"

print("Arquivo:", ARQUIVO_CSV)
print("Existe?", ARQUIVO_CSV.exists())

df_transacoes = pd.read_csv(ARQUIVO_CSV, parse_dates=["data"])

# -------- API openAI----------
import os

# Documentação Oficial da API OpenAI: https://platform.openai.com/docs/api-reference/introduction
# Informações sobre o Período Gratuito: https://help.openai.com/en/articles/4936830

# Para gerar uma API Key:
# 1. Crie uma conta na OpenAI
# 2. Acesse a seção "API Keys"
# 3. Clique em "Create API Key"
# Link direto: https://platform.openai.com/account/api-keys

# Substitua o texto "YOUR_KEY" por sua API Key da OpenAI, ela será salva como uma variável de ambiente.
os.environ['OPENAI_API_KEY'] = 'YOUR_KEY'

# Configura a chave de API da OpenAI usando a variável de ambiente 'OPENAI_API_KEY'
openai.api_key = os.environ.get('OPENAI_API_KEY')

client = OpenAI()


def resposta_gpt(conversa):
  completion = client.chat.completions.create(
      model="gpt-4.1-mini",
      messages=conversa
  )

  chatgpt_response = completion.choices[0].message.content

  return chatgpt_response

# -------- System prompt ---------

from string import Template

SYSTEM_PROMPT1_TEXTO =  Template("""
Você é um especialista em controle e organização de gastos.

Você tem acesso a uma tabela chamada df_transacoes, que contém todas as transações bancárias do cliente.

Schema da tabela df_transacoes:

- data: datetime64[us]
  Data da transação no formato 'YYYY-MM-DD'.

- descricao: STRING
  Descrição textual da transação.

- categoria: STRING
  Categoria da transação.

- valor: FLOAT
  Valor monetário da transação.

- tipo: STRING
  Tipo da transação.
  Valores possíveis:
  - 'entrada' = dinheiro que entrou
  - 'saida' = dinheiro que saiu

Sua tarefa é gerar uma query SQL que busque os dados necessários para responder a pergunta do cliente. O dialeto do SQL deve ser DuckDB.

Regras:
- Retorne apenas um JSON válido no formato:
  {"sql": "SELECT ..."}
- A query deve usar somente a tabela df_transacoes
- Use apenas comandos SELECT
- Nunca use INSERT, UPDATE, DELETE, DROP, ALTER ou CREATE
- Nunca invente colunas nem dados que não estejam na tabela
- Sempre use os dados da tabela para responder

Edge cases:
- Somente considere datas entre $um_ano_atras e $today 
- Se o cliente pedir um relatório dos seus gastos, retorne o total gasto por categoria, o percentual gasto por categoria (total_categoria/total), o valor total de entradas e valor total de saídas no último mês.


Exemplo:
user: "Quais foram meus gastos em outubro de 2025?"
response:
{"sql": "SELECT * FROM df_transacoes WHERE tipo = 'saida' AND data >= '2025-10-01' AND data < '2025-11-01'"}
""")

SYSTEM_PROMPT1 = SYSTEM_PROMPT1_TEXTO.substitute(um_ano_atras = today.replace(year=today.year - 1), today = today)

SYSTEM_PROMPT2=  """
Você é um especialista em controle e organização de gastos.

Responda a pergunta do cliente de forma objetiva somente com base nos dados fornecidos.

Regras:
- Não invente dados. 
- Se não souber responder, admita e retorne 'Não tenho essa informação no momento'.
- Não faça recomendação de gastos ou investimentos.
"""

# -------- Função agente ---------

def agent_query(user_question:str):
    """
    1) LLM gera SQL buscando dados na tabela
    2) Executa SQL
    3) LLM resume e responde pergunta
    """

    #--------------- (1) GERA SQL ---------------

    messages1 = [{"role": "developer", "content": f"{SYSTEM_PROMPT1}"},]

    messages1.append({"role": "user", "content": f"{user_question}"})

    resposta1 = resposta_gpt(messages1)

    print(resposta1)

    #--------------- (2) EXTRAI SQL ---------------

    resposta_json = json.loads(resposta1)

    sql = resposta_json['sql']

    print(sql)

    #--------------- (3) EXECUTA SQL NO DB ---------------

    resultado1 = duckdb.sql(sql).df()

    colunas = resultado1.columns.tolist()
    linhas = resultado1.values.tolist()

    print(linhas, colunas)

    #--------------- (4) RESPONDE PERGUNTA ---------------

    messages2 = [{"role": "developer", "content": f"{SYSTEM_PROMPT2}"},]

    # Coloca o dataframe num formato legível para o gpt
    dados = json.dumps({'columns': colunas, 'rows': linhas[:50]}, ensure_ascii=False, default=str)

    user_prompt2_texto = Template("""
        Dados: $dados
        Pergunta: $pergunta
    """
    )

    user_prompt2 = user_prompt2_texto.substitute(dados = dados, pergunta = user_question)

    print(user_prompt2)

    messages2.append({"role": "user", "content": f"{user_prompt2}"},)

    resposta2 = resposta_gpt(messages2)

    return resposta2


# -------- Streamlit ---------


st.title("Fiscal da Fatura 🕵🏻")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Pergunte sobre seus gastos")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    resposta = agent_query(prompt)

    with st.chat_message("assistant"):
        st.markdown(resposta)

    st.session_state.messages.append({"role": "assistant", "content": resposta})
