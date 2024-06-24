"""Pytest version of Django TDD unittest version"""
# https://www.youtube.com/watch?v=Nn3Yjea5KCI&list=PLEt8Tae2spYlVZUBBEE9PtX-NXk_hw7o4&index=3

import pytest
from model_bakery import baker

from posts.models import Post

HOMEPAGE_URL = "http://127.0.0.1:8000/posts/"


@pytest.mark.py
def test_post_model_exists(db):
    blog = Post.objects.count()

    assert blog == 0


@pytest.mark.py
def test_string_rep_of_objects(db):
    posts = Post.objects.count()
    post = baker.make(Post)
    assert str(post) == post.title


@pytest.mark.py
class TestPostModel:
    """Post model test"""

    def test_post_model_exists(self, db):
        """test Posts model exists"""
        posts = Post.objects.count()

        assert posts == 0

    def test_str_rep_of_objects(self, db):
        """test __str__"""
        post = Post.objects.create(title="First Post", body="First Post body")

        assert post.title == "First Post"


@pytest.mark.py
class HomePageTest:
    """test home page"""

    def setUp(self, db) -> None:
        self.post1 = Post.objects.create(
            title="Homepage1", body="This is the homepage1 content"
        )
        self.post2 = Post.objects.create(
            title="Homepage2", body="This is the homepage2 content"
        )

    def test_homepage_returns_correct_response(self, db):
        """test if homepage has elements"""
        response = self.client.get(HOMEPAGE_URL)
        self.assertTemplateUsed(response, "posts/index.html")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_homepage_returns_post_list(self, db):
        """test posts created"""
        response = self.client.get(HOMEPAGE_URL)

        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post2.title)
