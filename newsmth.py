import time
import random
import requests

from newsmth.config import \
    INDEX_URL, POST_URL, LOGIN_URL, \
    USERNAME, PASSWORD, \
    SUBJECT, CONTENT, \
    HEADERS

__author__ = 'jiramew'


class SmthPost(object):
    def __init__(self):
        self.session = requests.session()

    def login(self):
        self.session.get(INDEX_URL)
        time.sleep(random.randint(3, 5))
        post_data = {'id': USERNAME, 'passwd': PASSWORD}
        resp = self.session.post(LOGIN_URL,
                                 data=post_data,
                                 headers=HEADERS)
        return resp.text.find(u"操作成功") != -1

    def post_job(self):
        post_data = {
            'subject': SUBJECT,
            'content': CONTENT,
            'signature': -1,
            'id': USERNAME,
        }
        self.session.post(POST_URL,
                          data=post_data,
                          headers=HEADERS)


if __name__ == '__main__':
    sp = SmthPost()
    if sp.login():
        sp.post_job()
