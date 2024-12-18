from all.utils import *


class TestUtils:
    def test_get_posts_all(self):
        file = get_posts_all()
        assert type(file) == list, "Файл не является списком"
        assert file[0]["poster_name"] == "leo", "не выводится имя"
        assert file[2]["poster_name"] == "hank", "не выводится имя"
        assert str(file[0]["pk"]) == "1", "Не выводится по pk"

    def test_get_posts_by_user(self):
        posts = get_posts_by_user("larry")
        assert type(posts) == list, "Посты по пользователю не в списке"
        assert len(posts) > 0, "Нет постов"

    def test_get_comments_by_post_id(self):
        comments = get_comments_by_post_id(1)
        assert type(comments) == list, "Файл не является списком"
        assert len(comments) > 0, "Нет комментариев"

    def test_search_for_posts(self):
        posts  = search_for_posts("Вот")
        assert type(posts) == list, "Посты по пользователю не в списке"
        assert posts != None
        assert len(posts[0]["content"]) > 3, "Неправильное кол во символов"

    def test_get_post_by_pk(self):
        post = get_post_by_pk(1)
        assert type(post) == dict, "Посты по пользователю не в словаре"
        assert str(post["pk"]) == "1", "неправильное отображение pk"



