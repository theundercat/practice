import streamlit as st
import time

# Define the text you want to display line-by-line
lines = [
    "Who should win the election?",
    "Trump? or Harris?",
    "Choose wisely..:",
]

# Define the delay for each line (in seconds)
delays = [3, 3, 4]  # Custom delay for each line

# Create placeholders for each line
placeholders = [st.empty() for _ in lines]

# Display each line with its specific delay, then clear it to simulate fading
for i, line in enumerate(lines):
    placeholders[i].write(line)
    time.sleep(delays[i])  # Use the specific delay for each line
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
