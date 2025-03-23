
import streamlit as st

st.set_page_config(page_title="Painel de Trading - Cálculo com Taxa", layout="centered", page_icon="📈")

st.title("Painel de Trading - Cálculo com Taxa (1% na compra e 1% na venda)")

st.write("Insira os valores abaixo para calcular o lucro considerando taxa de 1% na compra e 1% na venda:")

valor_compra = st.text_input("Valor de Compra (USDT):", value="0.0000")
valor_venda = st.text_input("Valor de Venda (USDT):", value="0.0000")

if st.button("Calcular"):
    try:
        compra = float(valor_compra)
        venda = float(valor_venda)

        custo_total = compra + (compra * 0.01)  # 1% taxa de compra
        valor_recebido = venda - (venda * 0.01)  # 1% taxa de venda
        lucro = valor_recebido - custo_total
        lucro_percentual = (lucro / custo_total) * 100

        st.markdown("## ✅ Resultado do cálculo:")
        st.markdown(f"**Total Gasto (incluindo taxa 1%):** `{custo_total:.8f} USDT`")
        st.markdown(f"**Total Recebido (após taxa de 1%):** `{valor_recebido:.8f} USDT`")
        st.markdown(f"**Lucro (USDT):** `{lucro:.8f}`")
        st.markdown(f"**Lucro (%):** `{lucro_percentual:.2f}%`")

    except Exception as e:
        st.error("Por favor, insira valores numéricos válidos.")
