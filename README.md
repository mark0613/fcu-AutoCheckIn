# fcu-AutoCheckIn

逢甲自動打卡程式

## 免責聲明
- 此程式僅用於精進 selenium 與 pyqt 等技術
- 此程式需要索取帳號密碼，請自行斟酌
- 用此程式自動打卡不等同課堂上點名，但此行為表該帳戶實際做出打卡行為，若於事後遭課堂老師、助教、學生等人員發現或舉發而受到懲處，將與此程式無任何關聯，亦與創作者無關
- 自動打卡行為造成的後果，請先深思
- 請勿將此用於商業或其他獲利行為，否則持有者有權提出告訴

## 參考版本
- Python: 3.8.11
    + selenium: 3.141.0
    + PyQt5: 5.15.4
- Chromedriver: 94.0.4606.41
    + 此版本似乎需要與該裝置的 chrome 相同版本(待確認)

## 操作
1. 執行 main .py，將出現如圖介面<br><br> ![](https://i.imgur.com/saaMZLr.png)
2. 於右側填入帳號密碼，勾選記住(自行斟酌)
3. 於左側勾選自己上課的時間點，並點選儲存(否則課堂不會儲存，下次啟動就需要再填一次)
4. 點選執行即可(將啟動 chromedriver)

#### 注:
1. 不要關閉填寫介面和上方 4.所開啟的瀏覽器介面
2. 確保網路是連線狀態
3. 確保帳號密碼正確
4. 若要中斷程式，強制將其關閉即可

## 其他
- 有任何問題或建議皆可與該程式擁有者聯繫
- 尚未考慮特定網域才能打卡之問題

## 持有者
- mark0613
- HSBearBig
