import streamlit as st

offer = st.text_input("Price Offer: ")
tcost = st.text_input("Total cost:")

if offer and tcost:
    try:
        offer = int(offer)
        tcost = int(tcost)
        st.write(f"O.P:{(offer - tcost)/offer*100:.2f}%")
    except ValueError:
        st.write("Numeric values only bro.")
