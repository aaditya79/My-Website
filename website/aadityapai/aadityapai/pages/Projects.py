import streamlit as st

st.set_page_config(page_title="Aaditya Pai's Portfolio", page_icon=":computer:", layout="wide")

with st.container():
    left, right = st.columns(2)

    with left:
        st.header("Projects  :file_folder:")
        st.header("Lunar Lander (1979 Atari Arcade Game)")
        st.write(
            """
        •	Recreated the Lunar Lander game in Assembly Language by enabling GPIO ports, handling ISRs, configuring timers and updating the LED based on values stored in the IDR

        •	Built a STM32F091RCTx circuit by connecting a keypad and LED display to 8-bit DMOS Sink Driver, PN2970A transistors, and 74H138 3-to-8-line decoder/demultiplexer
            """
        )
        st.write("##")
        st.header("Genome Assembly Algorithm")
        st.write(
            """
            •	Developed a Genome Assembly Algorithm that aligned and merged DNA fragments to recover the original DNA sequence
            
            •	Wrote a C program that took the input of a DNA sequence text file and traversed through the De Bruijn Graph to recover a longer DNA sequence
            """
        )
        st.write("##")
        st.header("Personal Assistant")
        st.write(
            """
            •	Assembled a cloud-enabled standalone personal assistant using Raspberry Pi and programmed functionality using Python 3
            
            •	Engineered security alarm mechanism to detect movement using infrared sensor, dictation of up-to date news under any news category using Google News API and enabled ability to move based on voice command
            """
        )

    with right:
        st.write("#")
        st.write("#")
        st.header("Advanced Encryption Standard (AES-256)")
        st.write(
            """
            •	Wrote a Python 3 script to implement an AES algorithm with a 256-bit key size incorporating single-byte based substitution, row-wise permutation, column-wise mixing, and addition of the round key 
            
            •	Incorporated both encryption and decryption functions that can be used on text files and images
            """
        )
        st.write("##")
        st.header("Sorting Algorithm Visualizer")
        st.write(
            """
            •	Built a Python 3 application using the Tkinter GUI package for visualizing different sorting algorithms
            
            •	Incorporated Selection Sort, Insertion Sort, Bubble Sort, Quick Sort, and Shell Sort with the option to select sorting speed, data size and minimum/maximum values of the data set
            """
        )
        st.write("[See More >](https://www.youtube.com/watch?v=p6FwsV0LEpE)")
        
        st.write("##")
        st.header("Decimal and Hexadecimal Calculator")
        st.write(
            """
            •	Implemented a Simple Decimal Calculator using SystemVerilog on an FPGA Simulator

            •	Designed sequential logic components using BCD adders, carry look-ahead adders, BCD multipliers, asynchronous resets, and decoders
            """
        )