import streamlit as st

st.set_page_config(page_title="Aaditya Pai's Portfolio", page_icon=":computer:", layout="wide")
with st.container():
    left, right = st.columns(2)


    with left:
        st.header("Organizations  :bulb:")
        st.header("Projects Committee Co-Chair @ Project RISHI")
        st.write(
            """
            •	Raised $2,000 to donate 3,000 face masks and construct a new classroom at a local school in Arul, Madhya Pradesh, India

            •	Led a team of 15+ students to connect with underrepresented, low-income demographics across several rural communities
            """
        )

    with right:
        st.write("#")
        st.write("#")
        st.header("Director @ The Anvil (Purdue University's Startup Accelerator)")
        st.write(
            """
            •	Hosted monthly community events for students to network with startups and founders

            •	Raised approximately $20,000 for The Boiler (pre-seed accelerator)
            """
        )


        