i = ""
list = []
while i != "q":
    i = input("input:")
    list.append(i)
    print(list)
else:
    print("quit.")
    
    
倒序
list = [1, 2, 3, 4, 5]
print(list[::-1])


篮球
#score = 0
teama_list=[]
teamb_list=[]

team = ""

while team != 'game over':
    team = input("输入球队名称：")
    if team == "teama":
        teama_score = input("输入球队分数：")
        if teama_score.isdigit() == True:
            scorea = 0
            teama_list.append(int(teama_score))
            teama_list.append(team)
            for i in teama_list[::2]:
                scorea = scorea + i
            print(scorea)
    if team =="teamb":
        teama_score = input("输入球队分数：")
        if teama_score.isdigit() == True:
            scoreb = 0
            teamb_list.append(int(teama_score))
            teamb_list.append(team)
            for i in teamb_list[::2]:
                scoreb = scoreb + i
            print(scoreb)
else:
    if scorea > scoreb:
        print("a win")
    elif scorea < scoreb:
        print("b win")
    else:
        print("ping")
 
    
'''
    team_name = input("输入球队名称：")
team_score = input("输入球队分数：")
if team_score.isdigit() == True:
    team_list.append(team_name)
    team_list.append(int(team_score) + score)
    print(team_list)
    print(team_list.split())
else:
    print("No")
    '''
