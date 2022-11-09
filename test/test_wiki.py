import json
import ssl
import urllib.request

import pytest
import wikipediaapi

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def test_connection(url):
    response = urllib.request.urlopen(url, context=ctx)
    assert response


def test_ssl_error(url):
    with pytest.raises(Exception):
        response = urllib.request.urlopen(url)
        assert response


def test_page(title, lang):
    wiki = wikipediaapi.Wikipedia(lang)
    page = wiki.page(title, lang)
    assert page.exists()


def test_nonexistant_page(title, lang):
    with pytest.raises(Exception):
        wiki = wikipediaapi.Wikipedia(lang)
        title += "qwerty"
        page = wiki.page(title, lang)
        assert page.exists()


def test_empty_title(title, lang):
    with pytest.raises(Exception):
        wiki = wikipediaapi.Wikipedia(lang)
        title = ""
        page = wiki.page(title, lang)
        assert page.exists()


def test_json_dump(title, lang):
    wiki = wikipediaapi.Wikipedia(lang)
    page = wiki.page(title, lang)
    with open("test_output.json", "w") as fp:
        json.dump({"title": page.title}, fp)
