from flask import Flask, render_template, request
import requests

app = Flask(__name__)

blogs_url = "https://api.npoint.io/c75e4476df95903e294a"

response = requests.get(blogs_url)
all_blogs = response.json()

@app.route("/")
def home():

    return render_template("index.html", blogs=all_blogs)


@app.route("/blog/<int:id>")
def blog(id):
    blog_details = None
    for blog in all_blogs:
        if blog['id'] == id :
            blog_details = blog
    return render_template("post.html", blog=blog_details)

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        submit = False
        return render_template("contact.html", submitted=submit)
    else:
        submit = True

        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phonenumber"]
        message = request.form["message"]

        print(name)
        print(email)

        return render_template("contact.html", submitted=submit)



if __name__ == "__main__":
    app.run(debug=True)
