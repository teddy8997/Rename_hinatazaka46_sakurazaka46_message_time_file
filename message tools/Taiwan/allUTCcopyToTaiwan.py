import os
import fnmatch
from datetime import datetime
import calendar
import time
import shutil

def changeTime(f_name, y, m, d, hour, minute, sec):
    s = y + "-" + m + "-" + d + " " + hour + ":" + minute + ":" + sec
    #try:      
    d = datetime.strptime(s,"%Y-%m-%d %H:%M:%S")
    ts = calendar.timegm(d.utctimetuple())
    local = str(datetime.fromtimestamp(ts))
    #except ValueError:
        #return "Have been cganged"
    y = local[0:4]
    m = local[5:7]
    d = local[8:10]
    hour = local[11:13]
    minute = local[14:16]
    sec = local[17:]
    stamp = y + m + d + hour + minute + sec 
    return stamp


hinatazaka46List1st = ["潮紗理菜", "影山優佳", "加藤史帆", "齊藤京子", "佐々木久美", "佐々木美玲", "高瀬愛奈", "高本彩花","東村芽依"]

hinatazaka46List2nd = ["金村美玖", "河田陽菜", "小坂菜緒", "富田鈴花", "丹生明里", "濱岸ひより", "松田好花", "宮田愛萌","渡邉美穂"]

hinatazaka46List3rd = [ "上村ひなの", "髙橋未来虹", "森本茉莉", "山口陽世"]

sakurazaka46List1st = ["上村莉菜", "尾関梨香", "小池美波", "小林由依", "齋藤冬優花", "菅井友香", "土生瑞穂", "原田葵","守屋茜",
                    "渡辺梨加", "渡邉理佐"]

sakurazaka46List2nd = ["井上梨名", "遠藤光莉", "大園玲", "大沼晶保", "幸阪茉里乃", "関有美子","武元唯衣",
                    "田村保乃", "藤吉夏鈴", "増本綺良", "松田里奈", "松平璃子", "森田ひかる", "守屋麗奈", "山﨑天"]

hinatazaka46Path1st = "/MESSAGE/日向坂46/"
hinatazaka46Path2nd = "/MESSAGE/日向坂46 二期生/"
hinatazaka46Path3rd = "/MESSAGE/日向坂46 三期生/"


sakurazaka46Path1st = "/MESSAGE/櫻坂46 一期生/"
sakurazaka46Path2nd = "/MESSAGE/櫻坂46 二期生/"

pathDict = { hinatazaka46Path1st : hinatazaka46List1st,
             hinatazaka46Path2nd : hinatazaka46List2nd,
             hinatazaka46Path3rd : hinatazaka46List3rd,
             sakurazaka46Path1st : sakurazaka46List1st,
             sakurazaka46Path2nd : sakurazaka46List2nd}

pathList = [hinatazaka46Path1st, hinatazaka46Path2nd, hinatazaka46Path3rd, sakurazaka46Path1st, sakurazaka46Path2nd]
pathT = "/日向坂46／櫻坂46 メッセージ/"

"""如果有新增成員記得要把剛登入會送出的固定訊息的格林威治版本加在下面fileDict中
   增加方法就是在最後一個元素加入  ,"xxx.txt": 1
"""

fileDict = {"19408_0_20200609140404.txt" : 1 , "19409_0_20200609141904.txt" : 1,
            "50_0_20200609140727.txt" : 1, "51_0_20200609142227.txt": 1,
            "47_0_20200816082432.txt": 1, "85_0_20200816080932.txt": 1,
            "66_0_20200713121527.txt": 1, "67_0_20200713123027.txt": 1,
            "76_0_20200609140312.txt": 1, "77_0_20200609141812.txt": 1,
            "62_0_20201217050612.txt": 1, "63_0_20201217052112.txt": 1,
            "19406_0_20200609135732.txt": 1,"19407_0_20200609141232.txt": 1,
            "19400_0_20200610022029.txt": 1, "19401_0_20200610023529.txt": 1,
            "19398_0_20201225050817.txt": 1, "19399_0_20201225052317.txt": 1,
            "19412_0_20200609135532.txt": 1, "19413_0_20200609141031.txt": 1,
            "19408_0_20200609140404.txt": 1, "19409_0_20200609141904.txt": 1,
            "19410_0_20201116143158.txt": 1, "19411_0_20201116144658.txt": 1,
            "19404_0_20201224123618.txt": 1, "19405_0_20201224125118.txt": 1,
            "19402_0_20201224123703.txt": 1, "19403_0_20201224125203.txt": 1,
            "110382_0_20200609140210.txt": 1, "110383_0_20200609141710.txt": 1,
            "115_0_20200609135712.txt": 1, "116_0_20200609141212.txt": 1,
            "98_0_20200609135518.txt": 1, 
            "48_0_20200609135531.txt": 1, "73_0_20200609140839.txt": 1,
            "153_0_20200801061909.txt": 1, "154_0_20200801063409.txt": 1,
            "108_0_20201015102107.txt": 1,
            "87_0_20200801061809.txt": 1,"88_0_20200801063309.txt": 1,
            "110339_0_20200703023120.txt": 1, "110340_0_20200703024620.txt": 1,
            "110380_0_20200609140113.txt": 1, "110381_0_20200609141613.txt": 1,
            "181971_0_20200703023011.txt": 1, "181972_0_20200703024511.txt": 1,
            "110337_0_20200801061839.txt": 1}

memberDict = {"潮紗理菜" : "日向坂46", "影山優佳": "日向坂46", "加藤史帆": "日向坂46", "齊藤京子": "日向坂46",
              "佐々木久美": "日向坂46", "佐々木美玲": "日向坂46", "高瀬愛奈": "日向坂46", "高本彩花": "日向坂46","東村芽依": "日向坂46",
              "金村美玖": "日向坂46 二期生", "河田陽菜": "日向坂46 二期生", "小坂菜緒": "日向坂46 二期生", "富田鈴花": "日向坂46 二期生",
              "丹生明里": "日向坂46 二期生", "濱岸ひより": "日向坂46 二期生", "松田好花": "日向坂46 二期生", "宮田愛萌": "日向坂46 二期生",
              "渡邉美穂": "日向坂46 二期生",
              "上村ひなの": "日向坂46 三期生", "髙橋未来虹": "日向坂46 三期生", "森本茉莉": "日向坂46 三期生", "山口陽世": "日向坂46 三期生",
              "上村莉菜":"櫻坂46 一期生", "尾関梨香":"櫻坂46 一期生", "小池美波":"櫻坂46 一期生", "小林由依":"櫻坂46 一期生",
              "齋藤冬優花":"櫻坂46 一期生", "菅井友香":"櫻坂46 一期生", "土生瑞穂":"櫻坂46 一期生", "原田葵":"櫻坂46 一期生",
              "守屋茜":"櫻坂46 一期生", "渡辺梨加":"櫻坂46 一期生", "渡邉理佐":"櫻坂46 一期生",
              "井上梨名": "櫻坂46 二期生", "遠藤光莉": "櫻坂46 二期生", "大園玲": "櫻坂46 二期生", "大沼晶保": "櫻坂46 二期生",
              "幸阪茉里乃": "櫻坂46 二期生", "関有美子": "櫻坂46 二期生","武元唯衣": "櫻坂46 二期生",
             "田村保乃": "櫻坂46 二期生", "藤吉夏鈴": "櫻坂46 二期生", "増本綺良": "櫻坂46 二期生", "松田里奈": "櫻坂46 二期生",
              "松平璃子": "櫻坂46 二期生", "森田ひかる": "櫻坂46 二期生", "守屋麗奈": "櫻坂46 二期生", "山﨑天": "櫻坂46 二期生"}
for group in pathList:
    for name in pathDict[group]:
        if os.path.isdir(group+name):
            for f_name in os.listdir(group+name):
                if os.path.isfile(group + name + "/" + f_name) and f_name not in fileDict:
                    y = f_name[9:13]
                    m = f_name[13:15]
                    d = f_name[15:17]
                    hour = f_name[17:19]
                    minute = f_name[19:21]
                    sec = f_name[21:23]
                    seq = f_name[0:6]
                    cata = f_name[7:8]
                    file = f_name[23:]
                    timeToT = changeTime(f_name, y, m, d, hour, minute, sec)
                    if not os.path.isfile(pathT + memberDict[name] + "/" + name + "/" + timeToT + "_" + cata + "_" + seq + file):
                        shutil.copy(os.path.join(group + name + "/", f_name), os.path.join(pathT + memberDict[name] + "/" + name + "/", f_name));
            
   

