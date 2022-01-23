#第一届PGR音游组 Rank计算器

import math

game_code = ["Phigros", "Arcaea", "Muse Dash"]

p_name = input("\n请输入选手的名字/昵称：")
game = input("\n请输入所游玩的游戏编号：")
game = int(game)

if (game == 0):
    print("\n你选择的游戏是：Phigros")
    song_score = input("\n请输入曲目定数：")
    p1_score = input("\n请输入本次最终分数：")
    p1_acc = input("\n请输入本次准度（ACC，只输入百分号前面的数字即可）：")
    p_rks = input("\n请输入选手的最高rks：")
    pgr_yp = input("\n选手本次选择的模式是否为严判模式？若是请输入1，否则输入0：")

elif (game == 1):
    print("\n你选择的游戏是：Arcaea")
    song_score = input("\n请输入曲目定数：")
    p1_score = input("\n请输入本次最终分数：")
    p1_acc = input("\n请输入本次准度（ACC，只输入百分号前面的数字即可）：")
    p_rks = input("\n请输入选手的最高ptt：")

elif (game==2):
    print("\n你选择的游戏是：Muse Dash")
    song_score = input("\n请输入曲目定数：")
    p1_score = input("\n请输入本次最终分数：")
    p1_acc = input("\n请输入本次准度（ACC，只输入百分号前面的数字即可）：")
    p_rks = input("\n请输入本次Great+Miss总数：")

game_code[game] = "".join(game_code[game])

pgr_yp = int(pgr_yp)

print("\n请核对信息哟~~\n选手名字："+p_name+"\n游玩游戏："+game_code[game])
if(game == 0 and pgr_yp == 1):
    print("[严判模式]")
print("\n曲目定数："+song_score+"\n本次分数："+p1_score+"\n本次ACC%："+p1_acc+"%\n选手rks："+p_rks)

song_score = float(song_score)
p1_acc = float(p1_acc)
p_rks = float(p_rks)
p1_score = float(p1_score)

if(pgr_yp == 1):
    rscore = math.log(song_score/100.00*p1_acc*1000000) / p_rks / 0.40
elif(pgr_yp == 0):
    rscore = math.log(song_score/100.00*p1_acc*1000000) /p_rks / 0.80

rscore = str(rscore)

print("\n小鸽子，你的最终分数出来啦~！\n你的最终分数是："+rscore+"\n继续加油哟~")
