import streamlit as st
import time

# Define the path or URL to your GIF
gif_god_of_sales = "https://raw.githubusercontent.com/theundercat/practice/refs/heads/main/giphy.gif"
gif_really_good = "https://raw.githubusercontent.com/theundercat/practice/refs/heads/main/point-at-you-point.gif"
gif_pretty_good = "https://raw.githubusercontent.com/theundercat/practice/refs/heads/main/Brent-Rambo-Approves.gif"
gif_better_than_that = "https://raw.githubusercontent.com/theundercat/practice/refs/heads/main/confused-thin-air.gif"
gif_comeon = "https://raw.githubusercontent.com/theundercat/practice/refs/heads/main/comeon.gif"
gif_confused = "https://raw.githubusercontent.com/theundercat/practice/refs/heads/main/calculating.gif"
gif_alert = "https://raw.githubusercontent.com/theundercat/practice/refs/heads/main/kimjongun-rocket.gif"


# Get user inputs
offer = st.text_input("Price Offer: ")
tcost = st.text_input("Total cost:")

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
            st.image(gif_god_of_sales, width=500)  # Display GIF for "God of Sales"
        elif 20 < OP <= 30:
            st.write("In Trump's voice: This sale would be so big, so tremendous, we might have to rename the company after you. Wonderful job.")
            st.image(gif_really_good, width=500)  # Display GIF for "That's really good"
        elif 15 < OP <= 20:
            st.write("You’re squeezing them dry, and they’re saying, ‘Thank you, may I have another?")
            st.image(gif_pretty_good, width=500)  # Display GIF for "That's pretty good!"
        elif 10 <= OP <= 15:
            st.write("This is like eating pierogi with no fried onions. Go for over 15% and make it like a full-on Polish Christmas Eve!")
            st.image(gif_better_than_that, width=500)  # Display GIF for "You can do better than that.."
        elif  5 <= OP <= 9.99:
            st.write("Not even 10%? Kim Jong Un's missiles have better odds of hitting their targets than that!")
            st.image(gif_comeon, width=500)  # Display GIF for "You can do better than that.."
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
