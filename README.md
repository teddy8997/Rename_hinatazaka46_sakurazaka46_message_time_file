# Rename_hinatazaka46_sakurazaka46_message_time_file
本工具需搭配colmsg這個程式使用

這個tools主要是將櫻坂/日向坂的message app備份下來的檔案做處理，主要功能有三個:

1.將原本下載下來檔案名為格林威治時間轉換為台灣時間，並且將台灣時間提前
ex: 原本檔名構造為<序列號>_<訊息類型>_<格林威治時間的年月日時分秒>.<副檔名>，將它改成<台灣時間的年月日時分秒>_<訊息類型>_<序列號>.<副檔名> 如此一來可以解決序列號在前面影響到訊息的閱讀順序

2.將格林威治時間的資料夾MESSAGE下的每個成員檔案夾中新下載的檔案，自動複製一份到台灣時間的每個成員的資料夾

3.將每個成員的資料夾下檔案依月份分類

目錄中 Taiwan 資料夾中的檔案分別為自動依月份分類、將新下載的訊息從MESSAGE資料夾複製到日向坂46／櫻坂46 メッセージ資料夾、自動將格林威治時間改成台灣時間

UTC0000 資料夾下的檔案則是自動將檔案依月份分好


1.請創一個資料夾名稱為"日向坂46／櫻坂46 メッセージ" ，下載下來的Message的所有資料夾複製一份到裡面，並將用來存下載下來的Message資料夾命名為MESSAGE

2.寫一個搭配colmsg自動下載message的bat檔，利用windows工作排程器設定執行時間

3.將 Taiwan 資料夾中的3個bat檔也個別在windows工作排程器設定執行時間(自動分類的檔案請是設定每個月的5號執行)

4.UTC0000 資料夾下的自動分類bat檔請設定每個月的5號執行

推薦另外設定: 若是搭配Air explorer這類程式則可以使用裡面的資料夾同步功能將MESSAGE以及日向坂46／櫻坂46 メッセージ資料夾的新檔案定時上傳來達到全自動下載及上傳功能

注意: 若是有新增的成員需要自行先複製一份到日向坂46／櫻坂46 メッセージ資料夾，並且在程式碼有fileDict的地方將它的登入就會傳的message檔名加上。