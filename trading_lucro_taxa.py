
import streamlit as st

def interpretar_taxa(valor):
    if not valor or valor.strip() == "":
        return 0.01  # padrão 1%
    valor = valor.replace("%", "").strip()
    taxa_float = float(valor) / 100 if float(valor) > 1 else float(valor)
    return taxa_float

st.set_page_config(page_title="Painel de Trading Avançado", layout="centered", page_icon="📈")


st.title("Painel de Trading - Cálculo de Lucro com Taxas Personalizadas")

st.write("Preencha os dados abaixo. Se não informar a taxa, será usado o valor padrão de 1%. Você pode digitar o valor como número ou com o símbolo %, exemplo: `0.1`, `0.1%`, `1` ou `1%`.")


st.subheader("Compra")

preco_compra = st.text_input("Preço unitário de compra (USDT):")

qtd_compra = st.text_input("Quantidade comprada:")

taxa_compra = st.text_input("Taxa de compra (opcional):")


st.subheader("Venda")

preco_venda = st.text_input("Preço unitário de venda (USDT):")

qtd_venda = st.text_input("Quantidade vendida:")

taxa_venda = st.text_input("Taxa de venda (opcional):")


if st.button("Calcular"):

    try:

        preco_c = float(preco_compra)

        preco_v = float(preco_venda)

        qtd_c = float(qtd_compra)

        qtd_v = float(qtd_venda)


        taxa_c = interpretar_taxa(taxa_compra)

        taxa_v = interpretar_taxa(taxa_venda)


        total_compra = (preco_c * qtd_c) + ((preco_c * qtd_c) * taxa_c)

        total_venda = (preco_v * qtd_v) - ((preco_v * qtd_v) * taxa_v)


        lucro = total_venda - total_compra

        lucro_percentual = (lucro / total_compra) * 100


        st.markdown("## ✅ Resultado do cálculo:")

        st.markdown(f"**Total Gasto (incluindo taxa de compra):** `{total_compra:.8f} USDT`")

        st.markdown(f"**Total Recebido (após taxa de venda):** `{total_venda:.8f} USDT`")

        st.markdown(f"**Lucro (USDT):** `{lucro:.8f}`")

        st.markdown(f"**Lucro (%):** `{lucro_percentual:.2f}%`")


    except Exception as e:

        st.error("Por favor, insira todos os valores corretamente.")

