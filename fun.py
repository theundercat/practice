import streamlit as st

offer = st.text_input("Price Offer: ")
tcost = st.text_input("Total cost:")

if offer and tcost:
    try:
        offer = int(offer)
        tcost = int(tcost)
        
        # Calculate the operating profit percentage
        op_percentage = (offer - tcost) / offer * 100
        st.write(f"O.P: {op_percentage:.2f}%")
        
        # Check if O.P is over 10%
        if op_percentage > 10:
            st.write("That's pretty good!")
            
    except ValueError:
        st.write("Numeric values only, bro.")
