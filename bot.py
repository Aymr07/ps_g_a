from selenium import webdriver

import os
import time
import json


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password


if __name__ == '__main__':
    with open('./config.json') as f:
        data = json.load(f)
    ig_bot = InstagramBot(data["username"], data["password"])
