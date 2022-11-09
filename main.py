import json
import logging
import os
import sys

from exceptions import ApplicationException
from initialize import init_logger, parse
from wiki import (get_fullurl, get_page, get_sections, get_text, get_title,
                  init_wiki)

log = logging.getLogger(__name__)


if __name__ == "__main__":
    try:
        args = parse()
        init_logger()
        log.info("Init successful")
        page_info = {}
        log.info("Get information from Wiki API")
        wiki = init_wiki(args["lang"])
        page = get_page(wiki, args["title"])
        title = get_title(page)
        text = get_text(page)
        full_url = get_fullurl(page)
        sections_content = get_sections(page.sections, level=0)
        log.info("Success!")
        page_info.update({"title": title})
        page_info.update({"url": full_url})
        page_info.update({"sections": sections_content})
        page_info.update({"text": text})
        log.info("Dump information to json")
        if not os.path.exists("result"):
            os.mkdir("result", mode=0o777)
        with open("result/output.json", "w") as fp:
            json.dump(page_info, fp)
        log.info("Information successfully dumped into output.json")
    except ApplicationException as e:
        log.error(e)
        sys.exit(1)
    except Exception:
        log.exception("### Something went wrong ###")
        sys.exit(2)
