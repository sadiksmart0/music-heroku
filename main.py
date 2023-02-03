#=============================   Import Dependencies  =========================================#
from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel
import gensim
from gensim.models.doc2vec import Doc2Vec
from nltk.tokenize import word_tokenize
import pandas as pd
import numpy as np



#================================= Validating File  ============================================#
class Data(BaseModel):
    text: list

#================================= Declaring FASTAPI  ============================================#
app = FastAPI(title='Emotional Recommender', version='1.0',
              description='BERT Models are used to predict the emotion from song lyrics')


#================================= File Prediction ==========================================+#
@app.post("/lyrics")
def user_lyrics(lyrics: Data):
    lyrics = lyrics.text
    lyrics = get_similar(lyrics)
    json_string = lyrics.to_json(orient='records')
    return {"mood": json_string}




#============================  GET SIMILAR BASED ON COSINE SIMILARITY =====================#
def get_similar(song_lyrics):
    model = Doc2Vec.load("models/sim.model")
    v1 = model.infer_vector(song_lyrics)
    similar_doc = model.docvecs.most_similar(v1)
    sim  = filter(similar_doc)
    return sim

#============================  FILTER SIMILAR RESULT ========================================#
def filter(result):
    df = pd.read_csv("dataset/lyrics.csv")
    index_list = []
    for i in result:
        index_list.append(int(i[0]))
    filtered_df = df[df.index.isin(index_list)]
    return filtered_df
