import streamlit as st
import subprocess
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Configure
st.set_page_config(
    page_title="Online Retail Dataset EDA",
    layout="wide"
)
st.title('Online Retail Dataset EDA')

import streamlit.components.v1 as components
path_to_html = "rmd.html" 

with open(path_to_html,'r') as f: 
    html_data = f.read()

# Show in webpage
st.header("R Markdown Result")
st.markdown("""
In this analysis, I'm using R and R Markdown to create an interactive HTML report by knitting the document. This approach allows for easier visualization of results compared to running the R code directly in Streamlit.
""")
st.components.v1.html(html_data, scrolling=True, height=17500)
