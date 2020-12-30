import os
import fnmatch
from datetime import datetime
import calendar
import time



def changeTime(f_name, y, m, d, hour, minute, sec):
    s = y + "-" + m + "-" + d + " " + hour + ":" + minute + ":" + sec
    try:      
        d = datetime.strptime(s,"%Y-%m-%d %H:%M:%S")
        ts = calendar.timegm(d.utctimetuple())
        local = str(datetime.fromtimestamp(ts))
    except ValueError:
        return "Have been cganged"

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

hinatazaka46Path1st = "/日向坂46／櫻坂46 メッセージ/日向坂46/"
hinatazaka46Path2nd = "/日向坂46／櫻坂46 メッセージ/日向坂46 二期生/"
hinatazaka46Path3rd = "/日向坂46／櫻坂46 メッセージ/日向坂46 三期生/"


sakurazaka46Path1st = "/日向坂46／櫻坂46 メッセージ/櫻坂46 一期生/"
sakurazaka46Path2nd = "/日向坂46／櫻坂46 メッセージ/櫻坂46 二期生/"

pathDict = { hinatazaka46Path1st : hinatazaka46List1st,
             hinatazaka46Path2nd : hinatazaka46List2nd,
             hinatazaka46Path3rd : hinatazaka46List3rd,
             sakurazaka46Path1st : sakurazaka46List1st,
             sakurazaka46Path2nd : sakurazaka46List2nd}

pathList = [hinatazaka46Path1st, hinatazaka46Path2nd, hinatazaka46Path3rd, sakurazaka46Path1st, sakurazaka46Path2nd]


for group in pathList:
    for name in pathDict[group]:
        if os.path.isdir(group+name):
            for fOrDir in os.listdir(group + name):
                if os.path.isdir(group + name + "/" + fOrDir):
                    for f_name in os.listdir(group + name + "/" + fOrDir):
                         y = f_name[9:13]
                         m = f_name[13:15]
                         d = f_name[15:17]
                         hour = f_name[17:19]
                         minute = f_name[19:21]
                         sec = f_name[21:23]
                         file = f_name[23:]
                         st = changeTime(f_name, y, m, d, hour, minute, sec)
                         if st != "Have been cganged":
                             os.rename(group + name + "/" +  fOrDir + "/" + f_name, group + name + "/" +  fOrDir + "/" +  st + "_" + f_name[7:8] + "_" + f_name[0:6] + file)
                else:
                    y = fOrDir[9:13]
                    m = fOrDir[13:15]
                    d = fOrDir[15:17]
                    hour = fOrDir[17:19]
                    minute = fOrDir[19:21]
                    sec = fOrDir[21:23]
                    file = fOrDir[23:]
                    st = changeTime(fOrDir, y, m, d, hour, minute, sec)
                    if st != "Have been cganged":
                        os.rename(group + name + "/" + fOrDir, group + name + "/" +  st + "_" + fOrDir[7:8] + "_" + fOrDir[0:6] + file)


