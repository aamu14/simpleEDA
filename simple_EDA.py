import streamlit as st
import subprocess
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

import streamlit.components.v1 as components
path_to_html = "Nur-Muhammad-Herlim---KitaLulus-Technical-Test--Data-Analyst-Intern-.html" 

with open(path_to_html,'r') as f: 
    html_data = f.read()

# Show in webpage
st.header("Show an external HTML")

st.components.v1.html(html_data, scrolling=True, height=1000, width= 1000)
