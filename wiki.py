import backoff
import requests
import wikipediaapi


@backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_tries=10)
def init_wiki(lang: str):
    return wikipediaapi.Wikipedia(lang)


@backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_tries=10)
def get_page(wiki, title: str):
    return wiki.page(title)


@backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_tries=10)
def get_text(page):
    return page.text


@backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_tries=10)
def get_title(page):
    return page.title


@backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_tries=10)
def get_fullurl(page):
    return page.fullurl


@backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_tries=10)
def get_links(page):
    return page.links


@backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_tries=10)
def get_sections(sections, level=0):
    sections_content = {}
    for s in sections:
        sections_content.update({s.title: s.text[0:40]})
        get_sections(s.sections, level + 1)
    return sections_content
