"""Test detail page"""


from http import HTTPStatus

import pytest
from django.urls import reverse

from posts.models import Post
from posts.views import index, post_detail

POSTS_URL = "http://127.0.0.1:8000/post"


@pytest.mark.py
@pytest.mark.django_db
def test_detail_page_returns_correct_response(client):
    """test homepage response"""
    url = f"{POSTS_URL}/1"
    response = client.get(url)

    assert response.status_code == HTTPStatus.MOVED_PERMANENTLY
    assert response.status_code in [200, 301]

    assert response.context.get("post") == None
