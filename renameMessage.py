import os
import fnmatch
from datetime import datetime
import calendar
import time

''' 主要是把櫻坂/日向坂的message app備份下的檔案名的時間戳記從格林威治時間改成台灣時區
    使用時請創一個資料夾名稱為"日向坂46／櫻坂46 メッセージ"而裡面的資料夾分成兩個"日向坂46","櫻坂46"
    這兩個資料夾下再各自創成員的資料夾，主要修改的是放在各自成員的資料夾下的檔案，若各自成員的資料夾下還有資料夾裡面那個資料夾的檔案不會做處理
    EX: 若是加藤史帆資料夾下還有一個資料夾為2020.11 放在2020.11資料夾裡面的檔案不會被修改
    只會修改放在加藤史帆資料夾下的檔案，也就是放在加藤史帆資料夾下的檔案修改完後就能夠在加藤史帆資料夾下再創資料夾分類已經改好檔名的檔案
'''

#這個funcion主要是將原本檔案的格林威治時間=> 年月日時分秒 轉成台灣時區並將轉出來的結果回傳

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

    
#主要就是讀日向坂46／櫻坂46 メッセージ資料夾下的日向坂46以及櫻坂46資料夾下的每個成員資料夾裡的檔案名稱，用迴圈一個一個取原本檔案顯示的格林威治時間年月日時分秒 傳到changeTime做處理
#再利用os.rename將原本檔名格林威治時間的部分改成台灣時區
hinatazaka46List = ["潮紗理菜", "影山優佳", "加藤史帆", "齊藤京子", "佐々木久美", "佐々木美玲", "高瀬愛奈", "高本彩花","東村芽依",
                    "金村美玖", "河田陽菜", "小坂菜緒", "富田鈴花", "丹生明里", "濱岸ひより", "松田好花", "宮田愛萌","渡邉美穂",
                    "上村ひなの", "髙橋未来虹", "森本茉莉", "山口陽世"]

sakurazaka46List = ["上村莉菜", "尾関梨香", "小池美波", "小林由依", "齋藤冬優花", "菅井友香", "土生瑞穂", "原田葵","守屋茜",
                    "渡辺梨加", "渡邉理佐", "井上梨名", "遠藤光莉", "大園玲", "大沼晶保", "幸阪茉里乃", "関有美子","武元唯衣",
                    "田村保乃", "藤吉夏鈴", "増本綺良", "松田里奈", "松平璃子", "森田ひかる", "守屋麗奈", "山﨑天"]

hinatazaka46Path = "/日向坂46／櫻坂46 メッセージ/日向坂46/"
sakurazaka46Path = "/日向坂46／櫻坂46 メッセージ/櫻坂46/"

pathDict = { hinatazaka46Path : hinatazaka46List,
             sakurazaka46Path : sakurazaka46List}

pathList = [hinatazaka46Path, sakurazaka46Path]

for group in pathList:
    for n in pathDict[group]:
        if os.path.isdir(group + n):
            for f_name in os.listdir(group + n):
                    y = f_name[9:13]
                    m = f_name[13:15]
                    d = f_name[15:17]
                    hour = f_name[17:19]
                    minute = f_name[19:21]
                    sec = f_name[21:23]
                    file = f_name[23:]
                    st = changeTime(f_name, y, m, d, hour, minute, sec)
                    if st != "Have been cganged":
                        os.rename(group + n + "/" + f_name, group + n + "/" +  st + "_" + f_name[7:8] + "_" + f_name[0:6] + file)
        else:
            continue

