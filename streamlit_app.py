import streamlit as st 
import pandas as pd 
#import requests
from st_aggrid import AgGrid
import time
import plotly.express as px 
import matplotlib.pyplot as plt

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
  #Input (Typing)
  num_input = st.number_input('Input Berapapun')
  st.write('Kuadrat dari {} adalah {}'.format(num_input,num_input**2))
  #sidebar
  sidebar_checkbox = st.sidebar.checkbox('Checkbox di Sidebar')
  sidebar_radio_button = st.sidebar.radio('Pilih Menu',options=['A','B','C'])
  
  #columns :
  col1, col2, col3 = st.columns([1,2,1])

  with col1:
      st.header("A cat")
      st.image("https://static.streamlit.io/examples/cat.jpg")
  #atau dengan assignment 
  #image_col1 = col1.image("https://static.streamlit.io/examples/cat.jpg")

  with col2:
      st.header("A dog")
      st.image("https://static.streamlit.io/examples/dog.jpg")

  with col3:
      st.header("An owl")
      st.image("https://static.streamlit.io/examples/owl.jpg")
    
  #expander 
  #dengan with atau dengan assignment 
  expander = st.expander("Klik Untuk Detail ")
  expander.write('Anda Telah Membuka Detail')
  #sidebar 
  with st.form("Data Diri"):
      st.write("Inside the form")
      slider_val = st.slider("Form slider",21,120)
      checkbox_val = st.checkbox("Form checkbox")

  # Every form must have a submit button.
      submitted = st.form_submit_button("Submit")
      if submitted:
          st.write("Usia Anda", slider_val, "Hasil Validasi", checkbox_val)

  st.write("Outside the form")
  # Insert containers separated into tabs:
  tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
  tab1.write("this is tab 1")
  tab2.write("this is tab 2")
  with tab1:
    st.radio("Select one:", [1, 2])
  with tab2:
     st.button('Click Aing')
  # Show a spinner during a process
  with st.spinner(text="In progress"):
     time.sleep(3)
     st.success("Done")

  # Show and update progress bar
  bar = st.progress(50)
  time.sleep(3)
  bar.progress(100)

  with st.status("Authenticating...") as s:
      time.sleep(2)
      st.write("Some long response.")
      s.update(label="Response")
  
  #matplotlib chart 
  fig,ax = plt.subplots()
  plt.scatter(house['price'],house['sqft_lot'])
  st.pyplot(fig)
  plotly_fig = px.scatter(house['price'],house['sqft_living'])
  st.plotly_chart(plotly_fig)
  st.bar_chart(house['price'])
  st.bar_chart(house['price'], horizontal=True)

  # Work with user selections
  event = st.plotly_chart(
    house['price'],
    on_select="rerun"
  )
  event = st.altair_chart(
    chart,
    on_select="rerun"
  )
  event = st.vega_lite_chart(
    house['price'],
    spec,
    on_select="rerun"
  )

if __name__ == '__main__' : 
  datahouse()

