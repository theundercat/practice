import streamlit as st
import time

# Define the path or URL to your GIF
gif_god_of_sales = "https://raw.githubusercontent.com/theundercat/practice/refs/heads/main/giphy.gif"
gif_really_good = "https://raw.githubusercontent.com/theundercat/practice/refs/heads/main/point-at-you-point.gif"
gif_pretty_good = "https://raw.githubusercontent.com/theundercat/practice/refs/heads/main/Brent-Rambo-Approves.gif"
gif_better_than_that = "https://raw.githubusercontent.com/theundercat/practice/refs/heads/main/cat-foot.gif"
gif_comeon = "https://raw.githubusercontent.com/theundercat/practice/refs/heads/main/comeon.gif"
gif_confused = "https://raw.githubusercontent.com/theundercat/practice/refs/heads/main/calculating.gif"
gif_alert = "https://raw.githubusercontent.com/theundercat/practice/refs/heads/main/kimjongun-rocket.gif"


# Get user inputs
offer = st.text_input("Price:")
tcost = st.text_input("Cost:")

if offer and tcost:
    try:
        # Convert inputs to integers
        offer = float(offer)
        tcost = float(tcost)
        
        # Calculate Operating Profit (OP) percentage
        OP = (offer - tcost) / offer * 100
        st.write(f"O.P: {OP:.2f}%")
        
        # Conditional messages based on OP percentage with ranges
        if OP > 30:
            st.write("When your sales pitch is so good, even the GIFs are impressed.")
            st.image(gif_god_of_sales, width=500)
        elif 20 < OP <= 30:
            st.write("This would be such a tremendous, fantastic sale, you'll make America great again.")
            st.image(gif_really_good, width=500)
        elif 15 < OP <= 20:
            st.write("You’ll be squeezing the clients dry, and they’ll say, ‘Thank you, may I have another?'")
            st.image(gif_pretty_good, width=500)  
        elif 10 <= OP <= 14.99:
            st.write("15% is so close you can almost taste it!")
            st.image(gif_better_than_that, width=500)  
        elif  5 <= OP <= 9.99:
            st.write("The price is so low, even Kim Jong Un could afford it!")
            st.image(gif_comeon, width=500) 
        elif OP < 5:
            st.write("HQ has been notified of your failure. Self-destruct sequence initiated.")
            
            # Initialize the countdown timer in session state to 10 seconds
            if 'timer' not in st.session_state:
                st.session_state.timer = 10  # Set the timer to 10 seconds
            
            # Countdown loop
            while st.session_state.timer > 0:
                mins, secs = divmod(st.session_state.timer, 60)
                timer_display = f"{st.session_state.timer:02d}"
                
                # Display the countdown
                st.write(f"Exploding in {timer_display}")
                
                # Update timer
                time.sleep(1)  # Wait for 1 second
                st.session_state.timer -= 1
                
            # Display final message when countdown reaches 0
            st.write("Boom!")
            
            # Display the GIF after the countdown ends
            st.image(gif_alert, width=500)  # Adjust width as needed
            
    except ValueError:
        st.write("Loading... Please wait.")
        st.image(gif_confused, width=500)
