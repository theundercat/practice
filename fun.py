import streamlit as st
import time

# Define the path or URL to your GIF
gif_url = "gif_url = "https://raw.githubusercontent.com/theundercat/practice/main/path/to/kimjongun-rocket.gif""  # Example GIF URL

# Get user inputs
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
            st.write("Automatic alert e-mail has been sent to HQ. Device exploding in 10 seconds.")
            
            # Initialize the countdown timer in session state to 10 seconds
            if 'timer' not in st.session_state:
                st.session_state.timer = 10  # Set the timer to 10 seconds
            
            # Countdown loop
            while st.session_state.timer > 0:
                mins, secs = divmod(st.session_state.timer, 60)
                timer_display = f"{mins:02d}:{secs:02d}"
                
                # Display the countdown
                st.write(f"Countdown: {timer_display}")
                
                # Update timer
                time.sleep(1)  # Wait for 1 second
                st.session_state.timer -= 1
                
            # Display final message when countdown reaches 0
            st.write("Boom!")
            
            # Display the GIF after the countdown ends
            st.image(gif_url, width=300)  # Adjust width as needed
            
    except ValueError:
        st.write("Numeric values only, bro.")
