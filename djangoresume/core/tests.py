from django.test import TestCase
import pytest

_test_case = TestCase()

assert_contains = _test_case.assertContains
assert_not_contains = _test_case.assertNotContains
assert_template = _test_case.assertTemplateUsed


@pytest.fixture
def resp(client):
    resp = client.get('/')
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_template(resp):
    assert_template(resp, 'core/home.html')


def test_html(resp):
    """HTML must contain"""
    assert_contains(resp, 'Francisco Bustamante')
    assert_contains(resp, 'Python developer')
    assert_contains(resp, '<article', 8)
