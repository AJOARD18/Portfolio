#Working on the code in a seperate kernel:
#Copying and pasting:

import streamlit as st
import pandas
import requests
from urllib.error import URLError
from PIL import Image
 

st.title('Associate Data Consultant - Abdul-Hafiz Joarder')

EMAIL = "abdul.joarder@outlook.com"
SOCIAL_MEDIA = {
    "NAME": "Abdul-Hafiz Joarder",
    "LinkedIn": "https://www.linkedin.com/in/abdul-hafizjoarder/",
    "GitHub": "https://github.com/AJOARD18",
}

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image('AJ.jfif', width=230)

with col2:
  
    st.write("📫", EMAIL)
    
 
streamlit.image(image)



 

streamlit.header('Profile')
streamlit.text('I am an Associate Data Consultant with expertise in Excel and data cleaning. With\nvast knowledge of programming languages SQL and Python including various Pandas\nlibraries. Skilled in utilising data visualisation tools such as PowerBI and Tableau\nwith a strong ability to analyse and manipulate data, as well as a proven track\nrecord of effectively communicating high-quality, key insights to Stakeholders via\nwritten report or presentation.')




 

#streamlit.write('Thanks for viewing my profile')
