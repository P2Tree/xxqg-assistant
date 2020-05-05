import os
import subprocess
import time
import datetime
import json
import requests
import readline
from beepy import beep

def say(something):
    print(something)
    #  os.system('say "' + something + '"')
    p = subprocess.Popen(['say', something])
    return p
def goon(p):
    p.wait()
    p1 = say("输入回车键继续")
    wait = input()
    p.kill()
    p1.kill()
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


time_start = time.time()
p = say("欢迎使用学习强国引导助手")
p.wait()

while True:

    print("=============引导菜单==============")
    print("      0. 引导全部得分任务")
    print("    1. 阅读文章次数得分任务")
    print("    2. 阅读文章时间得分任务")
    print("    3. 观看视频次数得分任务")
    print("    4. 观看视频时间得分任务")
    print("      5. 每日答题得分任务")
    print("      6. 每周答题得分任务")
    print("      7. 专项答题得分任务")
    print("      8. 挑战答题得分任务")
    print("  9. 评论点赞收藏订阅得分任务")
    print("   10. 观看本地频道得分任务")
    print("          x. 退出程序")
    print("===================================")
    p = say("请输入数字选择引导得分任务")
    sel = input()
    p.kill()

    if sel != '0' and sel != '1' and sel != '2' and sel != '3' and sel != '4' \
                  and sel != '5' and sel != '6' and sel != '7' and sel != '8' \
                  and sel != '9' and sel != '10' and sel != 'x':
        p = say("输入有误，请重新输入数字选择引导模块，模块编号请参考屏幕输出")
        sel = input()
        p.kill()

    if sel == '1' or sel == '0':
        times = 6
        print("------ 阅读文章次数得分任务 ------")
        p = say("阅读6篇未阅读过的文章，每篇阅读至少5秒,  \n请选择一篇未阅读过的文章")
        goon(p)
        ts = 5  # second
        while True:
            say("阅读第" + str(7-times) + "篇文章")
            time.sleep(int(ts))
            times = times - 1
            if not times:
                break
            p = say("请选择下一篇未阅读过的文章")
            goon(p)
        beep('coin')
        p = say("恭喜已完成：阅读文章次数得分任务")
        p.wait()
    if sel == '2' or sel == '0':
        print("------ 阅读文章时间得分任务 ------")
        p = say("选择一篇未阅读过的文章，阅读12分钟，小心不要熄屏哟")
        goon(p)
        ts = 12
        say("开始阅读")
        time.sleep(int(ts)*60)
        beep('coin')
        p = say("恭喜已完成：阅读文章时间得分任务")
        p.wait()
    if sel == '3' or sel == '0':
        print("------ 观看视频次数得分任务 ------")
        times = 6
        p = say("观看6个未观看过的视频，每个观看至少5秒 \n请选择一个未观看过的视频")
        goon(p)
        ts = 5
        while True:
            say("观看第" + str(7-times) + "个视频")
            time.sleep(int(ts))
            times = times - 1
            if not times:
                break
            p = say("请选择下一个未观看过的视频")
            goon(p)
        beep('coin')
        p = say("恭喜已完成：观看视频次数得分任务")
        p.wait()
    if sel == '4' or sel == '0':
        print("------ 观看视频时间得分任务 ------")
        p = say("请打开今天的新闻联播，观看至少18分钟")
        goon(p)
        ts = 18
        say("开始观看")
        time.sleep(int(ts)*60)
        beep('coin')
        p = say("恭喜已完成：观看视频时间得分任务")
        p.wait()
    if sel == '5' or sel == '0':
        print("------ 每日答题得分任务 ------")
        p = say("请完成每日答题，一定要至少答对10道题呦,  \n请完成后")
        goon(p)
        beep('coin')
        p = say("恭喜已完成：每日答题得分任务")
        p.wait()
    if sel == '6' or sel == '0':
        print("------ 每周答题得分任务 ------")
        print("备注：本系统默认设置为每周一完成每周答题任务")
        wd = datetime.datetime.now().weekday()
        if wd != 0:
            if wd != 6:
                weekday_hanzi = num2hanzi(wd+1)
                p = say("今天是周" + weekday_hanzi + "，每周答题任务不必完成")
                p.wait()
            else:
                p = say("今天是周日，每周答题任务不必完成")
                p.wait()
        else:
            p = say("请完成每周答题，要小心别手残答错哟,  \n请完成后")
            goon(p)
            beep('coin')
            p = say("恭喜已完成：每周答题得分任务")
            p.wait()
    if sel == '7' or sel == '0':
        print("------ 专项答题得分任务 ------")
        p = say("请去检查一下有没有专项答题新题，建议每次只答一份,  \n请完成后")
        goon(p)
        beep('coin')
        p = say("恭喜已完成：专项答题得分任务")
        p.wait()
    if sel == '8' or sel == '0':
        print("------ 挑战答题得分任务 ------")
        p = say("请完成挑战答题，一定要连续至少答对5道题2次或10道题1次呦")
        p.wait()
        while True:
            p = say("请输入查询关键字(输入x退出查询)：")
            keyWord = input()
            p.kill()
            if keyWord == 'x':
                break
            answerList = tiaozhanSearch(keyWord)
            p = say("搜索到" + str(len(answerList)) + "个结果")
            for i in range(0, len(answerList)):
                print(str(i) + '. ' + answerList[i])
            p.wait()
        beep('coin')
        p = say("恭喜已完成：挑战答题得分任务")
        p.wait()
    if sel == '9' or sel == '0':
        print("------ 评论、点赞、收藏、订阅得分任务 ------")
        p = say("请打开一篇未阅读的文章，评论2次，点赞2次，收藏2次, \n请自主决定是否需订阅新的强国号,  \n请完成后")
        goon(p)
        beep('coin')
        p = say("恭喜已完成：评论、点赞、收藏、订阅得分任务")
        p.wait()
    if sel == '10' or sel == '0':
        print("------ 观看本地频道得分任务 ------")
        p = say("请打开本地频道，并至少瞅一眼 \n请完成后")
        goon(p)
        beep('coin')
        p = say("恭喜已完成：观看本地频道得分任务")
        p.wait()
    if sel == '0':
        time_end = time.time()
        time_during = (time_end - time_start) / 60    # min
        p = say("已完成今日全部学习任务")
        p.wait()
        p = say("总用时" + str(int(time_during)) + "分钟")
        p.wait()
    if sel == 'x' or sel == '0':
        say("程序正在退出，祝您生活愉快")
        p.wait()
        exit(1)

