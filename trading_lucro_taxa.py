
import streamlit as st

st.set_page_config(page_title="Painel de Trading - Cálculo com Taxa", layout="centered", page_icon="📈")

st.title("Painel de Trading - Cálculo com Taxa (2%)")

st.write("Insira os valores abaixo para calcular o lucro considerando taxa de 2%:")

valor_compra = st.text_input("Valor de Compra (USDT):", value="0.0000")
valor_venda = st.text_input("Valor de Venda (USDT):", value="0.0000")

if st.button("Calcular"):
    try:
        compra = float(valor_compra)
        venda = float(valor_venda)

        valor_recebido = venda - (venda * 0.02)
        lucro = valor_recebido - compra
        lucro_percentual = (lucro / compra) * 100

        st.write("## Resultado do cálculo:")
        st.write("| Descrição | Valor |")
        st.write("| --- | --- |")
        st.write(f"| Total Gasto | {compra:.8f} |")
        st.write(f"| Total Recebido (após taxa 2%) | {valor_recebido:.8f} |")
        st.write(f"| Lucro (USDT) | {lucro:.8f} |")
        st.write(f"| Lucro (%) | {lucro_percentual:.2f}% |")
    except:
        st.error("Por favor, insira valores numéricos válidos.")
