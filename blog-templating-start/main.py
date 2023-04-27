from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    blog_response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    blog_posts = blog_response.json()
    return render_template("index.html", blog_posts=blog_posts)


@app.route("/post/<int:post_id>")
def post(post_id):
    blog_response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    blog_posts = blog_response.json()
    for blog_post in blog_posts:
        if blog_post["id"] == post_id:
            return render_template("post.html", blog_post=blog_post)


if __name__ == "__main__":
    app.run(debug=True)
