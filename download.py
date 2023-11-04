import streamlit as st
import pandas as pd
import numpy as np
st.title('난 천재')
dataframe = pd.DataFrame({'first column':[1,2,3,4],'second column':[10,20,30,40]})
st.dataframe(dataframe,use_container_widthy=False)
st.table(datasframe)
