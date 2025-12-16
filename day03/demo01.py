import pandas as pd
from pandasql import sqldf 
import streamlit as st

st.title("CSV Explorer")

# upload a CSV file
data_file = st.file_uploader("Upload a CSV file", type=["csv"])
# load it as dataframe
if data_file:
    df = pd.read_csv(data_file)
    # display the dataframe
    st.dataframe(df)

    query=st.text_area("Enter query :")
    if st.button("Run ",type="primary" ):
        result=sqldf(query, {"df":df})
        st.dataframe(result)