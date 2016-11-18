# -*- coding: utf-8 -*-

import requests


class WechatUtils(object):
    def __init__(self):
        self.API_DOMAIN = 'https://api.weixin.qq.com'
        self.OPEN_DOMAIN = 'https://open.weixin.qq.com'

    def get(self, url, verify=False, **kwargs):
        res = requests.get(url.format(**kwargs), verify=verify)
        res.encoding = 'utf-8'
        return res.json()
