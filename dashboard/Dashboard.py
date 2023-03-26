import streamlit as st
import pandas as pd
import numpy as np
st.title('Med Deck')
col1, col2, col3 = st.columns(3)
col1.warning('No of Appointments : 12', icon="📊")
col2.warning('No of Doctors Onsite : 13', icon="🩺")
col3.warning('Report Claims : 4', icon="📄")
col1, col2 = st.columns(2)
col1.error('No of Inpatients : 14', icon="👨🏻‍🦲")
col2.error('No of Outpatients : 13', icon="👨🏻‍🦲")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['Doctor visit', 'Patient visit', 'Discharge summaries'])

st.line_chart(chart_data)
dataset_url = "https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv"

# read csv from a URL
@st.experimental_memo
def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset_url)

df = get_data()