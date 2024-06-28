import streamlit as st 
import pandas as pd 
#import requests
from st_aggrid import AgGrid

def utama() : 
  st.write('Minimal Example')

if __name__ == '__main__' : 
  utama()

def main() : 
  st.header('Halaman Streamlit Asep Rusdiana')
  st.subheader('This is SubHeader')
  st.markdown('# Rendering Markdown ')
  st.write('Some Phytagorean Equation : ')
  st.latex('c^2 = a^2+b^2')

if __name__ == '__main__' : 
  main()

#baca dataframe dari file csv 
house = pd.read_csv('house_clean.csv')

def datahouse() : 
  st.write('Contoh dataframe')
  st.dataframe(house)
  ##Untuk membuat metrik
  st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
  

  ##untuk menampilkan Aggrid--masih error
  #st.write('Menampilkan Dataframe dengan St AgGrid')
  #AgGrid(house)
  #st.table([x for x in range(1,5)])
  ###untuk membuat tombol
  click_me_btn = st.button('Click Me')
  st.write(click_me_btn) #Return True kalo di Click 
  check_btn = st.checkbox('Klik Jika Setuju')
  if check_btn :
     st.write('Anda Setuju')
  radio_button= st.radio('Choose below',[x for x in range(1,3)])
  st.write('Anda Memilih',radio_button)

#membuat slider
age_slider = st.slider('Berapa Usia Anda',0,100)
st.write('Usia Anda',age_slider)

if __name__ == '__main__' : 
  datahouse()

