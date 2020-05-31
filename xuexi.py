import time

from utils import say

from process import p_read_article_by_num, p_read_article_by_time, \
                    p_watch_video_by_num, p_watch_video_by_time, \
                    p_daily_answer, p_weekend_answer, \
                    p_specific_answer, p_challenge_answer, \
                    p_likesome, p_watch_local_video, p_guide_all

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

    if sel == '1':
        p_read_article_by_num()
    if sel == '2':
        p_read_article_by_time()
    if sel == '3':
        p_watch_video_by_num()
    if sel == '4':
        p_watch_video_by_time()
    if sel == '5':
        p_daily_answer()
    if sel == '6':
        p_weekend_answer()
    if sel == '7':
        p_specific_answer()
    if sel == '8':
        p_challenge_answer()
    if sel == '9':
        p_likesome()
    if sel == '10':
        p_watch_local_video()
    if sel == '0':
        time_start = time.time()
        p_guide_all()
        time_end = time.time()
        time_during = (time_end - time_start) / 60    # min
        p = say("总用时" + str(int(time_during)) + "分钟")
        p.wait()
    if sel == 'x' or sel == '0':
        say("程序正在退出，祝您生活愉快")
        p.wait()
        exit(1)

