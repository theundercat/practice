import streamlit as st

offer = st.text_input("Price Offer: ")
tcost = st.text_input("Total cost:")

if offer and tcost:
    try:
        # Convert inputs to integers
        offer = int(offer)
        tcost = int(tcost)
        
        # Calculate Operating Profit (OP) percentage
        OP = (offer - tcost) / offer * 100
        st.write(f"O.P: {OP:.2f}%")
        
        # Conditional messages based on OP percentage with ranges
        if OP > 30:
            st.write("God of Sales")
        elif 20 < OP <= 30:
            st.write("That's really good.")
        elif 15 < OP <= 20:
            st.write("That's pretty good!")
        elif 10 <= OP <= 15:
            st.write("You can do better than that..")
        elif OP < 5:
            st.write("Automatic alert e-mail has been sent to HQ. Your laptop will explode in 60 seconds.")
            
    except ValueError:
        st.write("Numeric values only, bro.")
