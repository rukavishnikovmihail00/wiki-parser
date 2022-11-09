#!/usr/bin/env bash
python3 -m pip install --upgrade flake8 black isort

python3 -m black --verbose -- . # reformat the code
python3 -m flake8 --count --filename *.py # count stylistic mistakes
python3 -m isort . # sort imports

pytest -q -s --url "https://www.wikipedia.org" --title "Docker_(software)" --lang "en" test/test_wiki.py

docker build -t "$1"/wiki-parser:latest -f docker/Dockerfile .

docker push "$1"/wiki-parser:latest


