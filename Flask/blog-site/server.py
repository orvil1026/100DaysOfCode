from flask import Flask, render_template
import random , requests
from datetime import date


app = Flask(__name__)

genderizer_endpoint = "https://api.genderize.io"
agify_endpoint = "https://api.agify.io"


@app.route("/")
def home():
    random_num = random.randint(1, 10)
    curr_year = date.today().year

    return render_template("index.html", num=random_num, year=curr_year)


@app.route("/guess/<name>")
def guess(name):
    response = requests.get(url=f"{genderizer_endpoint}/?name={name}")
    print(response.json())
    gender = response.json()["gender"]

    response = requests.get(url=f"{agify_endpoint}", params={'name': name})
    print(response.json())
    age = response.json()["age"]

    return render_template("guess.html", name=name, age=age, gender=gender)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)

    all_blogs = response.json()

    return render_template("blog.html", blogs=all_blogs)

if __name__ == "__main__":
    app.run(debug=True)