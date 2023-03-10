import requests
import json
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import neattext as nt
from nltk.tokenize import word_tokenize


#================================ CLEAN TEXT ============================#
def clean_text(text):
    docx = nt.TextFrame(text)
    song = docx.remove_stopwords().text
    song = docx.remove_puncts().text
    song = docx.remove_special_characters().text
    
    return song


#================================ TOKENIZE WORDS  ============================#
def tokenize_lyrics(text):
    cleaned_song = clean_text(text)
    tokenized = word_tokenize(cleaned_song.lower())
    return tokenized


#================================ PREDICT WITH LYRICS ============================#
def recommend_with_lyrics(text):
    song = tokenize_lyrics(text)
    response = requests.post("https://music-mood.herokuapp.com/lyrics", json={"text": song})
    response = json.loads(response.text)
    return  response


#================================ RECOMMENDED  ===============================#
def final_recommended(df):
    tracklist = []
    for i in df["dzr_sng_id"].values:
        response = requests.get(f"https://api.deezer.com/track/{i}")
        response = json.loads(response.text)
        tracklist.append(response)
    return tracklist












