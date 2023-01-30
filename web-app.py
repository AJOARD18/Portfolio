#Working on the code in a seperate kernel:
#Copying and pasting:

import streamlit
import pandas
import requests
from urllib.error import URLError
from PIL import Image
 

streamlit.title('Associate Data Consultant - Abdul-Hafiz Joarder')



# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "AJ-CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"
 

streamlit.header('Profile')
streamlit.text('I am an Associate Data Consultant with expertise in Excel and data cleaning. With\nvast knowledge of programming languages SQL and Python including various Pandas\nlibraries. Skilled in utilising data visualisation tools such as PowerBI and Tableau\nwith a strong ability to analyse and manipulate data, as well as a proven track\nrecord of effectively communicating high-quality, key insights to Stakeholders via\nwritten report or presentation.')




 

#streamlit.write('Thanks for viewing my profile')
