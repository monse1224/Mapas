import streamlit as st
import pandas as pd
import numpy as np

map_data=pd.DataFrame(
    np.random.randn(1000,2)/[50,50]+[20.6094978,-100.4055597],
    columns=['lat','lon']
)

st.dataframe(map_data)
st.map(map_data)
