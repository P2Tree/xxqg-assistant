import datetime
import time
from beepy import beep
import readline

from utils import say, goon, num2hanzi, tiaozhanSearch

def p_read_article(times = 6, ts = 60):
    print("------ 文章学习得分任务 ------")
    goon("阅读" + str(times) + "篇新文章，每篇阅读" + str(ts) + "秒，\n请选择一篇未阅读过的文章")
    t = 1
    while True:
        say("阅读第" + str(t) + "篇文章")
        time.sleep(int(ts))
        t = t + 1
        if t > times:
            break
        goon("请选择下一篇文章")
    beep('coin')
    p = say("恭喜已完成该任务")
    p.wait()

def p_watch_video(times = 6, ts = 60):
    print("------ 视听学习得分任务 ------")
    goon("观看" + str(times) + "个新视频，每个观看" + str(ts) + "秒， \n请选择一个未观看过的视频")
    t = 1
    while True:
        say("观看第" + str(t) + "个视频")
        time.sleep(int(ts))
        t = t + 1
        if t > times:
            break
        goon("请选择下一个视频")
    beep('coin')
    p = say("恭喜已完成该任务")
    p.wait()

def p_daily_answer():
    print("------ 每日答题得分任务 ------")
    goon("完成每日答题，\n请完成后")
    beep('coin')
    p = say("恭喜已完成该任务")
    p.wait()

def p_weekend_answer():
    print("------ 每周答题得分任务 ------")
    print("提示：本系统默认设置为每周一完成每周答题任务")
    wd = datetime.datetime.now().weekday()
    if wd == 0: # 周一
        goon("完成每周答题，要小心别手残答错哟,  \n请完成后")
        beep('coin')
        p = say("恭喜已完成该任务")
        p.wait()

def p_specific_answer():
    print("------ 专项答题得分任务 ------")
    goon("检查一下有没有专项答题新题，当天只需答一份,  \n请完成后")
    beep('coin')
    p = say("恭喜已完成该任务")
    p.wait()

def p_challenge_answer():
    print("------ 挑战答题得分任务 ------")
    p = say("完成挑战答题，输入 x 退出查询")
    p.wait()
    while True:
        p = say("请输入关键字：")
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
    p = say("恭喜已完成该任务")
    p.wait()

def p_likesome():
    print("------ 评论、转发、订阅得分任务 ------")
    print("提示：强国号多订阅无效")
    goon("选择一篇文章，评论 1 次，转发 2 次, 选择订阅 2 个新的强国号,  \n请完成后")
    beep('coin')
    p = say("恭喜已完成该任务")
    p.wait()

def p_watch_local_video():
    print("------ 观看本地频道得分任务 ------")
    goon("打开本地频道，至少瞅一眼，\n请完成后")
    beep('coin')
    p = say("恭喜已完成该任务")
    p.wait()

def p_guide_all():
    print("------ 视听学习得分任务 ------")
    goon("请打开电台，选择一个未听过的大于6首歌曲的专辑，并后台播放")

    p_daily_answer()
    p_weekend_answer()
    p_specific_answer()
    p_challenge_answer()
    p_likesome()

    p_read_article_by_num(5)  # 这里只需要看 5 篇，另外 1 篇在点赞任务中完成
    p_read_article_by_time()
    p_watch_local_video()

    while True:
        r = goon("请检查视听学习次数任务是否完成", "请输入未得分数，全部完成输入回车键")
        if r:
            try:
                ri = int(r)
            except:
                goon("输入错误，请重新输入")
            else:
                if ri <= 0 or ri > 6:
                    goon("输入错误，请重新输入")
                    continue
                p_watch_video_by_num(ri)
                break
        else:
            break

    while True:
        r = goon("请检查视听学习时间任务是否完成", "请输入未得分数，全部完成输入回车键")
        if r:
            try:
                ri = int(r)
            except:
                goon("输入错误，请重新输入")
            else:
                if ri < 0 or ri > 6:
                    goon("输入错误，请重新输入")
                    continue
                p_watch_video_by_time(ri)
                break
        else:
            break

    beep('coin')
    p = say("恭喜已完成全部任务")
    p.wait()

