import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Painel de Vendas", layout="wide")

# Carregamento do arquivo
st.title("📦 Painel de Desempenho - Vendas Online")
arquivo = st.file_uploader("📁 Envie o arquivo de vendas (.xlsx ou .csv)", type=["xlsx", "csv"])

@st.cache_data
def carregar_dados(arquivo):
    if arquivo.name.endswith(".csv"):
        df = pd.read_csv(arquivo, sep=";")
    else:
        df = pd.read_excel(arquivo)

    df.columns = df.columns.str.strip().str.lower()
    df.rename(columns={
        "data_pedido": "data",
        "descricao_produto": "produto",
        "valor_venda": "venda",
        "preco_unitario": "preco",
        "qtde": "quantidade",
        "cod_cidade": "cidade"
    }, inplace=True)

    df['data'] = pd.to_datetime(df['data'], dayfirst=True, errors='coerce')
    df['preco'] = df['preco'].astype(str).str.replace(",", ".").str.strip().astype(float)
    df['venda'] = df['venda'].astype(str).str.replace(",", ".").str.strip().astype(float)
    df['quantidade'] = pd.to_numeric(df['quantidade'], errors='coerce').fillna(0).astype(int)
    
    return df.dropna(subset=["data"])

if arquivo:
    df = carregar_dados(arquivo)

    # Filtros
    col1, col2 = st.columns(2)
    with col1:
        data_ini, data_fim = st.date_input("📅 Intervalo de datas", [df["data"].min(), df["data"].max()])
    with col2:
        produtos = st.multiselect("🛍️ Produtos", df["produto"].unique(), default=list(df["produto"].unique()))

    filtrado = df[
        (df["data"] >= pd.to_datetime(data_ini)) &
        (df["data"] <= pd.to_datetime(data_fim)) &
        (df["produto"].isin(produtos))
    ]

    # KPIs
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("💰 Total de Vendas", f'R$ {filtrado["venda"].sum():,.2f}')
    col2.metric("🧾 Total de Pedidos", filtrado["numero_pedido"].nunique())
    col3.metric("📦 Produtos Vendidos", filtrado["quantidade"].sum())
    ticket_medio = filtrado["venda"].sum() / max(filtrado["numero_pedido"].nunique(), 1)
    col4.metric("📈 Ticket Médio", f'R$ {ticket_medio:,.2f}')

    st.divider()

    # Gráficos
    col1, col2 = st.columns(2)
    vendas_tempo = filtrado.groupby("data")["venda"].sum().reset_index()
    fig1 = px.line(vendas_tempo, x="data", y="venda", title="📆 Vendas ao Longo do Tempo", markers=True)
    col1.plotly_chart(fig1, use_container_width=True)

    top_produtos = filtrado.groupby("produto")["quantidade"].sum().reset_index().sort_values(by="quantidade", ascending=False)
    fig2 = px.bar(top_produtos, x="produto", y="quantidade", title="🏆 Produtos Mais Vendidos")
    col2.plotly_chart(fig2, use_container_width=True)

    # Mapa (opcional: requer código IBGE correto)
    st.subheader("🗺️ Vendas por Cidade")
    vendas_cidade = filtrado.groupby("cidade")["venda"].sum().reset_index()
    st.dataframe(vendas_cidade)

    # Tabela final
    st.subheader("📄 Dados Detalhados")
    st.dataframe(filtrado, use_container_width=True)

else:
    st.info("Por favor, envie um arquivo para iniciar a análise.")
