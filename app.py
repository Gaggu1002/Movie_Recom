from email.mime import image
from flask import Flask,render_template,request
from movie import movie_reco ,lism
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/res",methods = ["POST","GET"])
def result():
    if request.method == "POST":
        inpu = request.form["user_input"]
        Mov,gen,image =movie_reco(inpu,10)
        ans = zip(Mov,gen,image)
        return render_template("results.html",ans = ans)
    return render_template("results.html")

@app.route("/lis")
def lis():
    Movie_title,ggg,img = lism()
    ans = zip(Movie_title,ggg,img)
    return render_template("list.html",ans=ans)

if __name__ == "__main__":
    app.run(debug=True)