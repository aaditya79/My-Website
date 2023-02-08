import streamlit as st
from PIL import Image

st.set_page_config(page_title="Aaditya Pai's Portfolio", page_icon=":computer:", layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

st.header("Hi, I'm Aaditya :wave:")
with st.container():
    st.write("---")
    left, right = st.columns(2)

    with left:

        st.subheader("I’m a fourth-year undergraduate student pursuing a Bachelor of Science in Computer Engineering. I will be graduating from Purdue University in May 2023.")
        st.subheader("[LinkedIn >](https://www.linkedin.com/in/aaditya-pai-074a8bb0/)")
        st.subheader("[GitHub >](https://github.com/aaditya79)")
        st.write("#")
        st.write("**This website was built using Python and Streamlit and was deployed on Heroku**")


    with right:
        image6 = Image.open('photo.jpg')
        st.image(image6, width=290) 



with st.container():
    st.write("---")
    left, right = st.columns(2)

    with left:
        st.header("Technical Experience  :computer:")
        st.subheader("**Software Engineer Intern @ ADVANCE.AI**")
        st.write("**May 2022-Present**")
        st.write(
            """
            •	Monitored traffic in the local Kubernetes cluster using Prometheus and Grafana by sending an alert to the administrator based on metrics collection rules (i.e., size of the request is 100+ MB, transferring 10+ MB within 10 seconds)

            •	Implemented external load balancer and virtual service for HTTP routing using CI/CD pipeline tools such as Jira and GitLab

            •	Administered and deployed Istio proxy to Kubeflow pipeline and used the Kubeflow traffic API to track the data accessed on the development environment
            """
        )
        st.write("##")
        st.subheader("**Teaching Assistant for Digital System Design @ Purdue University**")
        st.write("**Aug 2021-Dec 2021**")
        st.write(
            """
            •	Instructed 80+ students on concepts related to designing and analyzing combinational and sequential logic circuits and programming an FPGA using System Verilog
            
            •	Conducted review sessions on lab projects and homework, increasing examination results by 20% for students that attended
            """,unsafe_allow_html=False
        )
        st.write("##")
        st.subheader("**Teaching Assistant for EE Fundamentals @ Purdue University**")
        st.write("**Jan 2021-May 2021**")
        st.write(
            """
            •	Taught 50+ students fundamental electrical engineering concepts related to linear resistive circuits, first-order linear circuits with sources, and electronic circuits with diodes and transistors
        
            •	Assisted the Head of the School of Electrical and Computer Engineering professor with content creation and grading
            """,unsafe_allow_html=False
        )

    with right:
        st.write("#")
        st.write("#")

        st.subheader("**Researcher for Lunabotics @ Purdue University**")
        st.write("**Aug 2021-Dec 2021**")
        st.write(
            """
            •	Programmed an object detection algorithm reaching 500+ FPS to detect gravel and map terrain on a simulated extraterrestrial environment using OpenCV and ROS 
            
            •	Evaluated the performance of the MOSSE tracking filter using different object detection methodologies (i.e., feature matching, point detection, image tracing), achieving a near 95% confidence for relative size and shape 
            """,unsafe_allow_html=False
        )
        st.write("[See More >](https://www.youtube.com/watch?v=dcHSrHQ3_ak)")
        
        st.write("##")
        st.subheader("**Frontend Developer @ Uptone**")
        st.write("**Jul 2021-Aug 2021**")
        st.write(
            """
            •	Implemented an internal audio functionality tool allowing users to share posts to social media feed using React Native

            •	Programmed and designed an audio player with key features of play, pause, and skip using the ‘expo-av’ library and Expo CLI after interviewing 50+ users and evaluating current market trends in UI design
            """,unsafe_allow_html=False
        )

with st.container():
    st.write("---")
    st.header("Contact Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/pai19@purdue.edu" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()