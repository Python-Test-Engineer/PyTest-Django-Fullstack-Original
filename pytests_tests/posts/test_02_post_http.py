"""Test based on Pybites demo"""
# https://www.youtube.com/watch?v=L5jWFU2sVXQ


import pytest

from posts.models import Post
from posts.views import index

HOMEPAGE_URL = "http://127.0.0.1:8000/posts/"


@pytest.fixture
def post_entry(db):
    """fixture for posts"""
    return Post.objects.create(
        title="Test Blog",
        body="Test Body",
    )


@pytest.mark.py
@pytest.mark.pybites
def test_blog_list(client, post_entry):
    """test homepage response"""
    response = client.get(HOMEPAGE_URL)
    assert response.status_code == 200
    assert list(response.context["posts"]) == [post_entry]
