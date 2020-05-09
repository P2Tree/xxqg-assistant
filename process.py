import datetime
import time
from beepy import beep
import readline
import sqlite3

from utils import say, goon, num2hanzi, tiaozhanSearch

def p_read_article_by_num():
    times = 6
    print("------ 阅读文章次数得分任务 ------")
    goon("阅读6篇未阅读过的文章，每篇阅读至少5秒,  \n请选择一篇未阅读过的文章")
    ts = 5  # second
    while True:
        say("阅读第" + str(7-times) + "篇文章")
        time.sleep(int(ts))
        times = times - 1
        if not times:
            break
        goon("请选择下一篇未阅读过的文章")
    beep('coin')
    p = say("恭喜已完成：阅读文章次数得分任务")
    p.wait()

def p_read_article_by_time():
    print("------ 阅读文章时间得分任务 ------")
    goon("选择一篇文章，阅读12分钟，小心不要熄屏哟")
    ts = 12
    say("开始阅读")
    time.sleep(int(ts)*60)
    beep('coin')
    p = say("恭喜已完成：阅读文章时间得分任务")
    p.wait()

def p_watch_video_by_num():
    print("------ 观看视频次数得分任务 ------")
    times = 6
    goon("观看6个未观看过的视频，每个观看至少5秒， \n请选择一个未观看过的视频")
    ts = 5
    while True:
        say("观看第" + str(7-times) + "个视频")
        time.sleep(int(ts))
        times = times - 1
        if not times:
            break
        goon("请选择下一个未观看过的视频")
    beep('coin')
    p = say("恭喜已完成：观看视频次数得分任务")
    p.wait()

def p_watch_video_by_time():
    print("------ 观看视频时间得分任务 ------")
    goon("请打开今天的新闻联播，观看至少18分钟")
    ts = 18
    say("开始观看")
    time.sleep(int(ts)*60)
    beep('coin')
    p = say("恭喜已完成：观看视频时间得分任务")
    p.wait()

def p_daily_answer():
    print("------ 每日答题得分任务 ------")
    goon("请完成每日答题，一定要至少答对10道题呦,  \n请完成后")
    beep('coin')
    p = say("恭喜已完成：每日答题得分任务")
    p.wait()

def p_weekend_answer():
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
        goon("请完成每周答题，要小心别手残答错哟,  \n请完成后")
        beep('coin')
        p = say("恭喜已完成：每周答题得分任务")
        p.wait()

def p_specific_answer():
    print("------ 专项答题得分任务 ------")
    goon("请去检查一下有没有专项答题新题，建议每次只答一份,  \n请完成后")
    beep('coin')
    p = say("恭喜已完成：专项答题得分任务")
    p.wait()

def p_challenge_answer():
    print("------ 挑战答题得分任务 ------")
    p = say("请完成挑战答题，一定要连续至少答对5道题2次或10道题1次呦")
    p.wait()
    while True:
        p = say("请输入查询关键字(输入x退出查询)：")
        keyWord = input()
        p.kill()
        if keyWord == 'x':
            break
        searchRet = tiaozhanSearch(keyWord)
        answerList = []
        remove_str = "温馨提示：相似题目，注意区分"
        for sr in searchRet:
            for s in sr.split('· '):
                s = s.replace(remove_str, '')
                s = s.replace("\r\n\r\n", '')
                s = s.replace("【", "\033[1;31m【")
                s = s.replace("】", "】\033[0m")
                answerList.append(s)
        answerList = list(filter(None, answerList))
        p = say("搜索到" + str(len(answerList)) + "个结果")
        for i in range(0, len(answerList)):
            print('\033[1;36m <' + str(i+1) + '>\033[0m ' + answerList[i])
        p.wait()
    beep('coin')
    p = say("恭喜已完成：挑战答题得分任务")
    p.wait()

def p_likesome():
    print("------ 评论、点赞、收藏、订阅得分任务 ------")
    goon("请打开一篇文章，评论2次，点赞2次，收藏2次, \n请自主决定是否需订阅新的强国号,  \n请完成后")
    beep('coin')
    p = say("恭喜已完成：评论、点赞、收藏、订阅得分任务")
    p.wait()

def p_watch_local_video():
    print("------ 观看本地频道得分任务 ------")
    goon("请打开本地频道，并至少瞅一眼 \n请完成后")
    beep('coin')
    p = say("恭喜已完成：观看本地频道得分任务")
    p.wait()
