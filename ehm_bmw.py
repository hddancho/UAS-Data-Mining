import pickle
import streamlit as st

model = pickle.load(open('hargabmw.sav', 'rb'))

st.title('Estimasi Harga Mobil BMW Bekas')

year = st.number_input('Tahun Mobil')
mileage = st.number_input('Kilo Meter Mobil')
tax = st.number_input('Pajak Mobil')
mpg = st.number_input('Konsumsi BBM Mobil')
engineSize = st.number_input('Engine Mobil')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[year, mileage, tax, mpg, engineSize]]
    )
    st.write ('Estimasi Harga Mobil Bekas dalam Pound :', predict)
    st.write ('Estimasi Harga Mobil Bekas dalam Rupiah :', predict*19000)