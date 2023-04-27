import streamlit
streamlit.title('My Parents new healthy Diner')
streamlit.header('🥣Breakfast Menu')
streamlit.text('🥗Omega 3 & blueberry Oatmeal')
streamlit.text('🐔kate, spinach & Rocket Smootie')
streamlit.text('🥑Hard-Boiled Free-Range Egg')
streamlit.text('🍞Abocado Toast')
    
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

steamlit.dataframe(my_fruit_list)
