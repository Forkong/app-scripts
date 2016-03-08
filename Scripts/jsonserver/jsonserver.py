#!/usr/bin/python
# -*- coding: utf-8 -*-

import web
import requests
import time

sleep_time = 1

server = "http://www.baidu.com/"

web_headers = {"version":"1.4"}

urls = (
    '/tgas/group/queryGroupInfo', 'queryGroupInfo',
    '/tgas/group/queryGroupList', 'queryGroupList',
    '/(.*)', 'other',
)

app = web.application(urls, globals())

# 其他直接透传
class other:
    def GET(self, url):
        r = requests.get(server+url, data=web.input(), headers=web_headers)
        print 'text = ', r.text
        return r.text

    def POST(self, url):
        r = requests.post(server+url, data=web.data(), headers=web.headers)
        print 'text = ', r.text
        return r.text

class queryGroupInfo:
    def GET(self):
        time.sleep(sleep_time)
        # json
        raise web.seeother('/static/queryGroupInfo.json')

class queryGroupList:
    def GET(self):
        time.sleep(sleep_time)
        # base64 json
        raise web.seeother('/static/queryGroupList_64.json')

if __name__ == "__main__":
    app.run()
