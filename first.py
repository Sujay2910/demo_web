import streamlit as sl



sl.title("Welcome to web")
sl.markdown("sujay bote")

sl.code(""" for i in range(10):
                print("hello")""")

name= sl.text_input("Enter your name")
surname = sl.text_input("Enter your surname")
add= sl.text_area("Enter your address")
Class= sl.selectbox("Slect your class:",(1,2,3,4,5,6))

Button= sl.button("Submit")
if Button:
    sl.markdown(f"""
        name:{name}
        surname:{surname}
        class:{Class}""")
