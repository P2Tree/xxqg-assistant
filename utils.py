import subprocess
import requests
import json

def say(something):
    print(something)
    p = subprocess.Popen(['say', something])
    return p

def goon(s, end = "输入回车键继续"):
    p = say(s + ", \n" + end)
    r = input()
    p.kill()
    return r

def num2hanzi(n):
    if n == 0:
        return "零"
    elif n == 1:
        return "一"
    elif n == 2:
        return "二"
    elif n == 3:
        return "三"
    elif n == 4:
        return "四"
    elif n == 5:
        return "五"
    elif n == 6:
        return "六"
    elif n == 7:
        return "七"
    elif n == 8:
        return "八"
    elif n == 9:
        return "九"
    else:
        return ""

def tiaozhanSearch(keyWord):
    url = 'https://api.deeract.com/l2s/api/questions?keyword=' + keyWord
    result = requests.get(url)
    user_dict = json.loads(result.text)
    #  print("搜索到" + str(len(user_dict)) + "个结果")
    answer = []
    for i in user_dict:
        answer.append(i['title'])
        #  print(i['title'])
    return answer
