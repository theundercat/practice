candidate1 = "Trump"
candidate2 = "Harris"

# Display the question using Streamlit's st.write function
st.write("Who will win the election?")
st.write(f"{candidate1}? or {candidate2}?")

# Use st.text_input to allow the user to type their choice
Choice = st.text_input("Type your choice and pick wisely:")

# Display the result based on the user's typed input
if Choice:
    if Choice.lower() == candidate1.lower():
        st.write("MURICA")
    elif Choice.lower() == candidate2.lower():
        st.write("AMERICA")
    else:
        st.write("Nice try.")
