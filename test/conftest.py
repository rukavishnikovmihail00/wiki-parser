import pytest


@pytest.fixture(scope="session")
def url(pytestconfig):
    return pytestconfig.getoption("url")


@pytest.fixture(scope="session")
def title(pytestconfig):
    return pytestconfig.getoption("title")


@pytest.fixture(scope="session")
def lang(pytestconfig):
    return pytestconfig.getoption("lang")


def pytest_addoption(parser):
    parser.addoption("--url", action="store")
    parser.addoption("--title", action="store")
    parser.addoption("--lang", action="store")
