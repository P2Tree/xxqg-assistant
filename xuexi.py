import time

from utils import say, goon

from process import p_read_article, \
                    p_watch_video, p_watch_video, \
                    p_daily_answer, p_weekend_answer, \
                    p_specific_answer, p_challenge_answer, \
                    p_likesome, p_watch_local_video, p_fightforup_answer, \
                    p_guide_all

from things import completed_todo
from coffers import Connect_to_coffers

p = say("欢迎使用学习强国引导助手")
p.wait()

while True:

    print("=====================引导菜单====================")
    print("      0. 全部得分任务")
    print("      1. 全部得分任务与足额点点通")
    print("      2. 阅读文章与观看视频得分任务与足额点点通")
    print("      3. 阅读文章时间得分任务")
    print("      4. 阅读文章次数得分任务")
    print("      5. 观看视频时间得分任务")
    print("      6. 观看视频次数得分任务")
    print("      7. 挑战答题得分任务")
    print("      x. 退出程序")
    print("=================================================")
    p = say("请输入数字选择引导得分任务")
    sel = input()
    p.kill()

    if sel != '0' and sel != '1' and sel != '2' and sel != '3' and sel != '4' \
                  and sel != '5' and sel != '6' and sel != '7' and sel != 'x':
        p = say("输入有误，请重新输入数字选择引导模块，模块编号请参考屏幕输出")
        sel = input()
        p.kill()

    if sel == '3':
        p_read_article(6, 60)
    if sel == '4':
        p_read_article(6, 5)
    if sel == '5':
        p_watch_video(6, 60)
    if sel == '6':
        p_watch_video(6, 5)
    if sel == '7':
        p_challenge_answer()
    if sel == '0' or sel == '1' or sel == '2':
        time_start = time.time()

        if sel != '2':
            p_daily_answer()
            p_weekend_answer()
            p_specific_answer()
            print("提示：点点通任务需要答对 15 道挑战答题题目")
            p_challenge_answer()
            p_likesome()
            p_watch_local_video()

        p_read_article(6, 60)  # 阅读 6 篇，每篇 60 秒
        p_watch_video(6, 60)  # 收听 6 个，每个 60 秒

        if sel != '2':
            p_fightforup_answer()

        if sel != '0':
            print("提示：点点通任务需要阅读 12 篇文章、观看 12 个视频")
            p_read_article(6, 5)  # 阅读 6 篇，每篇 5 秒
            p_watch_video(6, 5)  # 收听 6 个，每个 5 秒

        time_end = time.time()
        time_during = (time_end - time_start) / 60    # min
        p = say("总用时" + str(int(time_during)) + "分钟")
        p.wait()

    if sel == 'x' or sel == '0' or sel == '1' or sel == '2':
        # qiandao to coffers
        ctc = Connect_to_coffers()
        if not ctc.is_open():
            p = say("coffers 未启用")
            p.wait()
        else:
            r = ctc.qiandao(True)
            if r == 200:
                p = say("已通知 coffers 标记完成任务")
            else:
                p = say("未联系到 coffers，标记失败")
            p.wait()

        say("程序正在退出，祝您生活愉快")
        p.wait()
        exit(1)

