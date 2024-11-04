import streamlit as st
import time

# Define the text you want to display line-by-line
lines = [
    "Who will win the election?",
    "Trump? or Harris?",
    "Type your choice and pick wisely:",
]

# Create placeholders for each line
placeholders = [st.empty() for _ in lines]

# Display each line with a delay, and then clear it to simulate fading
for i, line in enumerate(lines):
    placeholders[i].write(line)
    time.sleep(2)  # Display each line for 2 seconds
    placeholders[i].empty()  # Clear the line to simulate fading

# Now prompt for input after lines fade
candidate1 = "Trump"
candidate2 = "Harris"
Choice = st.text_input("Type your choice here:")

# Display the result based on input
if Choice:
    if Choice.lower() == candidate1.lower():
        st.write("MURICA")
    elif Choice.lower() == candidate2.lower():
        st.write("AMERICA")
    else:
        st.write("Nice try.")
