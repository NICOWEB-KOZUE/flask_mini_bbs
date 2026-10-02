from flask import Flask, render_template
from peewee import PostgresqlDatabase

from models import Post

app = Flask(__name__)


# 一覧表示（GET）
@app.route("/")
def index():
    # 新しい順（created_atの降順）で全件取得する
    posts = Post.select().order_by(Post.created_at.desc())
    return render_template("index.html", posts=posts)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
