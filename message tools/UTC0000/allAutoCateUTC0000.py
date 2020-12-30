import os
import shutil
from pathlib import Path
from datetime import datetime

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

str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
NowY = str[0:4]
NowM = str[5:7]

for group in pathList:
    for name in pathDict[group]:
        if os.path.isdir(group+name):
            for f_name in os.listdir(group+name):
                  if f_name not in fileDict:
                      y = f_name[9:13]
                      m = f_name[13:15]
                      fullpath = os.path.join(group + name + "/", f_name)
                      if os.path.isfile(fullpath):
                          if NowY >= y and NowM != m:
                              if os.path.isdir(group + name + "/" + y + "." + m):     
                                  shutil.move(os.path.join(group + name + "/" , f_name), os.path.join(group + name + "/" + y + "." + m+"/", f_name));
                              else:
                                   os.mkdir(group + name + "/" + y + "." + m);
                                   shutil.move(os.path.join(group + name + "/" , f_name), os.path.join(group + name + "/" + y + "." + m+"/", f_name));
          
