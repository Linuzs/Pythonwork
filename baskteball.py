#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:Linuz
"""

team_a_list=[]
team_b_list=[]
team_a = input("初始化球队1名称：")
team_b = input("初始化球队2名称：")
team = ""
score_a = 0
score_b = 0

while team != 'game over':
    if team_a.strip() != team_b.strip() and team_a.strip() != "game over" and team_b.strip() != "game over"  and team_a.strip() != "" and team_b.strip() != "":
        #a球队与b球队名称不能相等，并且名称不能为“game over”，过滤首位空格，过滤空名称
        team = input("输入球队名称：")
        if team == team_a:
            #只有输入的队伍名与初始化的队伍名相等才会继续下面的操作，否则直接退出
            team_a_score = input("输入球队分数：")
            if team_a_score.isdigit() == True and int(team_a_score) <= 3:
                #分数需要纯数字，并且小于等于3分，否则提示错误
                score_a = 0
                team_a_list.append(int(team_a_score))
                team_a_list.append(team)
                #先插入队伍分数，后插入队伍名
                for i in team_a_list[::2]:
                    #指定格式追加到列表，分数步长为2，所以可以把所有的分数遍历相加
                    score_a = score_a + i
                print("球队<%s>的分数为:%d\n球队<%s>的分数为:%d"%(team_a, score_a, team_b, score_b))
            else:
                print("请输入正确的分数！")
        elif team == team_b:
            team_b_score = input("输入球队分数：")
            if team_b_score.isdigit() == True and int(team_b_score) <= 3:
                score_b = 0
                team_b_list.append(int(team_b_score))
                team_b_list.append(team)
                for i in team_b_list[::2]:
                    score_b = score_b + i
                print("球队<%s>的分数为:%d\n球队<%s>的分数为:%d"%(team_b, score_b, team_a, score_a))
            else:
                print("请输入正确的分数！")
        elif team == 'game over':
            pass
        else:
            print("该球队名称未定义！")
    else:
        print("球队名称有误，请重新输入！")
        break

else:
    if score_a > score_b:
        print("球队<%s>赢了！总分为：%d\n球队<%s>的总分为：%d"%(team_a, score_a, team_b, score_b))
    elif score_a < score_b:
        print("球队<%s>赢了！总分为：%d\n球队<%s>的总分为：%d"%(team_b, score_b, team_a, score_a))
    else:
        print("平局！\n球队<%s>的总分为：%d\n球队<%s>的总分为：%d"%(team_a, score_a, team_b, score_b))
