from flask import Flask, render_template, request, redirect, url_for

from models import Post

app = Flask(__name__)


# 一覧表示（GET）
@app.route("/")
def index():
    # 新しい順（created_atの降順）で全件取得する
    posts = Post.select().order_by(Post.created_at.desc())
    # 投稿件数
    count = posts.count()
    return render_template("index.html", posts=posts, count=count)


# 投稿(POST)
@app.route("/posts", methods=["POST"])
def create():
    name = request.form["name"]
    body = request.form["body"]
    # 名前か本文が空なら保存しないで一覧に戻る
    if name == "" or body == "":
        return redirect(url_for("index"))
    Post.create(name=name, body=body)
    # 保存できたら一覧へリダイレクトする
    return redirect(url_for("index"))


# 削除（POST）
@app.route("/posts/<int:post_id>/delete", methods=["POST"])
def delete(post_id):
    try:
        post = Post.get_by_id(post_id)
    except Post.DoesNotExist:
        return redirect(url_for("index"))

    post.delete_instance()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(port=8000, debug=True)
