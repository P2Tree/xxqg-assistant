import requests
from urllib import request as urllib2
import urllib
import re
from http import cookiejar as cookielib
import json

class Connect_to_coffers():

    def __init__(self):
        with open("coffers.cfg") as cof:
            self.cfgs = json.load(cof)

        self.baseurl = self.cfgs["site"]
        self.url = self.baseurl + "/xuexi/qiandao/"
        self.login_url = self.baseurl + "/accounts/login/?next=/xuexi/"
        self.logout_url = self.baseurl + "/accounts/logout/"
        self.cookie_name = "cookie.txt"

    def is_open(self):
        if self.cfgs["site"] == "":
            return False

        return True

    def qiandao(self, complete):
        if complete:
            r = requests.get(self.url + "1")
        else:
            r = requests.get(self.url + "0")
        return r.status_code

    def logout(self):
        r = requests.get(self.logout_url)
        return r.status_code

    def login(self):
        #  csrf, lt = self.save_cookie()
        csrf = self.save_cookie()

        headers = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36')]
        headers.append(('csrftoken', csrf))

        data = {"username": self.cfgs["username"],
                "password": self.cfgs["password"],
                "csrfmiddlewaretoken": self.cfgs["csrf"],
                "renew": self.cfgs["renew"],
                "warn": self.cfgs["warn"]}

        cookie = cookielib.MozillaCookieJar()
        cookie.load(self.cookie_name, ignore_discard=True, ignore_expires=True)

        postdata = urllib.parse.urlencode(data).encode('utf-8')
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        opener.addheaders.append(headers[0])
        opener.addheaders.append(headers[1])
        response = opener.open(self.login_url, postdata)
        print(str(response.read(), encoding = "utf-8"))

    def save_cookie(self):
        ckjar = cookielib.MozillaCookieJar(self.cookie_name)
        ckproc = urllib2.HTTPCookieProcessor(ckjar)
        opener = urllib2.build_opener(ckproc)
        f = opener.open(self.login_url)
        content = f.read()
        content = content.decode('GBK')
        pattern_csrf = re.compile(r"name='csrfmiddlewaretoken' value='(.*?)' />", re.S)
        #  pattern_lt = re.compile(r'<input id="id_lt" name="lt" type="hidden" value="(.*?)" />', re.S)
        csrf = re.findall(pattern_csrf, content)
        #  lt = re.findall(pattern_lt, content)
        f.close()
        ckjar.save(ignore_discard=True, ignore_expires=True)
        print(csrf)
        #  print(lt)
        return csrf[0]#, lt[0]

#  if __name__ == "__main__":
    #  ctc = Connect_to_coffers()
    #  r = ctc.qiandao(True)
    #  print(r)
    #  if r == 200:
        #  print("qiandao success")
    #  else:
        #  print("qiandao failed, return code: " + str(r))
    #  ctc.login()
    #  ctc.logout()

