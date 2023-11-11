import streamlit as st
import pandas as pd
import numpy as np
st.title('난 천재')
dataframe = pd.DataFrame({'first column':[1,2,3,4],'second column':[10,20,30,40],})
st.dataframe(dataframe,use_container_width=True)
st.table(dataframe)
st.metric(label="온도",value="10°C",delta="1.2°C")
st.metric(label="삼성전자",value="61000원",delta="-1200")
col1,col2,col3 =st.columns(3)
col1.metric(label="달러USD",value="1228원",delta="-1200")
col2.metric(label="일본Jpy(100)엔",value="958.63원",delta="-7.44원")           
col2.metric(label="유럽연합EUR",value="1335.82원",delta="11.44원")         
tab1,tab2=st.tabs(["Cat","Dog"])
with tabl:
  st.header("A cat")
  st.image("https://static.streamlit.io/examples/cat.jpg",width=200)
with tab2:
  st.header("A dog")
  st.image("https://static.streamlit.io/examples/dog.jpg",width=200)
