import requests
import json
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import neattext as nt
import pandas as pd
import numpy as np


#================================ CLEAN TEXT ============================#
def clean_text(text):
    docx = nt.TextFrame(text)
    song = docx.remove_stopwords().text
    song = docx.remove_puncts().text
    song = docx.remove_special_characters().text
    
    return song



def tokenize_lyrics(text):
    cleaned_song = clean_text(text)
    tokenized = word_tokenize(cleaned_song.lower())
    return tokenized


#================================ PREDICT WITH LYRICS ============================#
def recommend_with_lyrics(text):
    song = tokenize_lyrics(text)
    response = requests.post("http://127.0.0.1:8000/lyrics", json={"text": song})
    response = json.loads(response.text)
    return  response



#============================  GET SIMILAR BASED ON COSINE SIMILARITY =====================#
def get_similar(song_lyrics):
    all_songs, ref_song = vectorize_search(song_lyrics)
    for i in range(len(all_songs)):
        sim = all_songs[i].similarity(ref_song)
        sims.append(sim)
        doc_id.append(i)
        sims_docs = pd.DataFrame(list(zip(doc_id, sims)), columns=["doc_id","sims"])
        sims_docs_sorted = sims_docs.sort_values(by = "sims", ascending=False)
        top = song_lyrics.iloc[sims_docs_sorted["doc_id"][:10]]
        return top







