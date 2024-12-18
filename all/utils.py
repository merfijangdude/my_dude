import json


def get_posts_all():
    with open(r"data/posts.json", "r", encoding="utf-8") as file:
        file = json.load(file)
    return file


def get_posts_by_user(user_name):
    posts = []
    for post in get_posts_all():
        if post["poster_name"] == user_name:
            posts.append(post)
    return posts


def get_comments_by_post_id(post_id):
    with open(r"data/comments.json", "r", encoding="utf-8") as file:
        file = json.load(file)

    list_of_comments = []
    for comment in file:
        if str(comment["post_id"]) == str(post_id):
            list_of_comments.append(comment)

    return list_of_comments


def search_for_posts(query):
    posts = get_posts_all()

    list_of_posts = []
    for post in posts:
        if query in post["content"]:
            list_of_posts.append(post)

    return list_of_posts


def get_post_by_pk(pk):
    posts = get_posts_all()

    for post in posts:
        if str(post["pk"]) == str(pk):
            return post
