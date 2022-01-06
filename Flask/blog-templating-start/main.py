from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

def get_blogs():
    blogs_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blogs_url)
    all_blogs = response.json()

    blogs = []

    for blog in all_blogs:
        blogs.append(Post(id=blog['id'], title=blog['title'], subtitle=blog['subtitle'], body=blog['body']))

    return blogs

@app.route('/')
def home():

    blogs = get_blogs()
    return render_template("index.html", blogs=blogs)


@app.route('/blog/<int:id>')
def blog(id):

    blogs = get_blogs()

    final_blog = blogs[id-1]

    return render_template("post.html", blog=final_blog)


if __name__ == "__main__":
    app.run(debug=True)
