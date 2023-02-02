import streamlit as st
from predict import recommend_with_lyrics, final_recommended
import base64
import uuid
import datetime
import json
import pandas as pd
import uvicorn
import nltk
nltk.download('punkt')



#================ Gif loader ===================#
file_ = open("images/prof.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

#================ Side Bar ===================#
add_selectbox = st.sidebar.selectbox(
    "Explore our top 10",
    ("Happy", "Sad", "Angry","Relaxed")
)




#================ App Header ===================#
head, photo = st.columns(2)    
with head:   
    st.title("With music there is no tension.")

with photo:
    st.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">', unsafe_allow_html=True,)



#========================   RECOMMMENDATION VIEW  ==================================#
def view(result):
    with st.spinner("Loading ..."):
        st.empty()
        img_col, play_col = st.columns(2)
        for song in result:
            with img_col:
                st.subheader(song["title"])
                st.write(song["artist"]["name"])
                st.image(song["artist"]["picture"])
            with play_col:
                st.subheader(song["album"]["title"])
                st.write(f'Duration: {round(song["duration"]/60,2)} min')
                st.markdown(f"[![Foo](https://cdn-icons-png.flaticon.com/128/9458/9458362.png)]({song['preview']})")



st.subheader("Search by Lyrics")
txt = st.text_area('Insert Song Lyrics', '''
It was the best of times, it was the worst of times, it was
the age of wisdom, it was the age of foolishness, it was
the epoch of belief, it was the epoch of incredulity, it
was the season of Light, it was the season of Darkness, it
was the spring of hope, it was the winter of despair, (...)
''')

lyrics_data = {
    'lyrics_id': str(uuid.uuid1()),
    'timestamp': datetime.datetime.now(),
    'lyrics': txt
}

if st.button('Submit'):
    mood = recommend_with_lyrics(txt)
    mood = json.loads(mood["mood"])
    result = pd.DataFrame(mood)
    result = final_recommended(result)
    view(result)














