import os

import yaml


class Globals:
    def __init__(self, base_url, src_dir):
        self.base_url = base_url
        self.src_dir = src_dir

    def static(self, path):
        path = os.path.join("assets", path)
        return "/" + path.removeprefix("/")

    def load_header_context(self):
        with open(os.path.join(self.src_dir, "header_context.yml")) as f:
            return yaml.safe_load(f)

    def get_nav_link(self, item):
        link = item["index"].removesuffix("index")
        if link != "":
            link = link.removesuffix("/")

        return "/" + link.removeprefix("/")

    def get(self):
        return {
            "static": self.static,
            "header_context": self.load_header_context(),
            "get_nav_link": self.get_nav_link,
        }
