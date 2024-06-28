import streamlit as st 
import pandas as pd 
#import requests
#from st_aggrid import AgGrid

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
#read json file dari data covid 
#flight_passanger_api = requests.post('https://forecastpassengerapi.herokuapp.com/forecast_timeseries',json={
  "month_limit": "2020-01-01",
  "window_size": 12
}).json()

def main() : 
  st.write('Contoh dataframe')
  st.dataframe(house)
  if __name__ == '__main__' : 
  main()
