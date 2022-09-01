import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

streamlit.title('My Parents New Healthy Diner!')

streamlit.header('Breakfast Favorites ')
streamlit.write('🥣 Omega3 & Blueberry Oatmeal')
streamlit.write('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.write('🐔 Hard-Boiled Free-Range Egg')
streamlit.write('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
