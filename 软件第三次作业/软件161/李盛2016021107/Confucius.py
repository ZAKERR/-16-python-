'''
开发人：  李盛
开发时间：2018_09_23
程序功能：简单归纳孔夫子一生中各时间段的行为
'''
while True:
    age = int(input("Please input Confucius's ages: "))
    if 0 <= age < 15:
        print("孔氏，名丘，字仲尼，公元前551年9月28日，春秋末期生人。")
        continue
    elif 15 <= age < 30:
        print("孔子立志，从师而学，欲穷游而知世事。")
        continue
    elif 30 <= age < 40:
        print("三十而立，可独存于世间，可参世宿世情。")
        continue
    elif 40 <= age < 50:
        print("孔丘不惑于俗，目世事而知其本源，不为表象所扰。")
        continue
    elif 50 <= age < 60:
        print("耳顺者，正视各家之言，耳聪目明，安心立命，畅意于世间，而未有诽谤者。孔子已至于此境矣。"
            )
        continue
    elif 60 <= age < 72:
        print("从心所欲不逾矩，飘飘乎如意于世，所行所言铜镜也，受敬于诸国，可为天下师。")
        continue
    elif age >= 72:
        print("公元前479年4月11日，孔子卒，享年71岁，后世奉之为至圣先师，圣人之首者，孔子也。")
        continue
    else:
        print("Are you kidding me?????Bitch.")
        continue
