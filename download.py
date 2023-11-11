import streamlit as st
import pandas as pd
import numpy as np
st.title('난 천재')
dataframe = pd.DataFrame({'first column':[1,2,3,4],'second column':[10,20,30,40],})
st.dataframe(dataframe,use_container_width=True)
st.table(dataframe)
st.metric(label="온도,value="10°C",delta="1.2°C")
sst.metric(label="삼성전자",value="61000원",delta="-1200")
