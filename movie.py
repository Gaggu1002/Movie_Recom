import pandas as pd
from sklearn.metrics.pairwise import linear_kernel , cosine_distances , cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
data = pd.read_csv("Movie_details.csv")
data = data.drop("Unnamed: 0",axis=1)
data = data.rename({"Movie Title":"Movie_title"},axis=1)
def mov_nam(n):
    return data[data.index == n]["Movie_title"].unique()[0]
def mov_gen(n):
    return data[data.index == n]["ggg"].unique()[0]
def mov_img(n):
    return data[data.index == n]["img"].unique()[0]
tfidf = TfidfVectorizer()
vec = tfidf.fit_transform(data["ggg"])
def movie_reco(name,n = 10):
    ind = data[data["Movie_title"]==name].index[0] # to find index
    lin = pd.DataFrame(linear_kernel(vec[ind],vec)).T
    lin.columns =[ "Score"]
    lin["Mov"] = list(map(mov_nam,list(lin.index)))
    lin["gen"] = list(map(mov_gen,list(lin.index)))
    lin["image"] = list(map(mov_img,list(lin.index)))
    ans = lin.sort_values(by="Score",ascending=False).head(n)
    return list(ans.Mov),list(ans.gen),list(ans.image)
def lism():
    return list(data.Movie_title),list(data.ggg),list(data.img)