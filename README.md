## 警語
- 本程式只是示範功能用，用的是自建的本地資料庫，並沒有連結到清大圖書館的資料庫，意即不能預約到"真正"的清大夜讀區座位。  
如果您有預約"真正"夜讀區的需求，請走 https://libsms.lib.nthu.edu.tw/build  
  
  
- 同上，由於我也沒有 "真正" 的清大學生資料表，因此資料庫裡的學生資料是用 data_generator 裡頭的 user_generator.ipynb 生成的隨機資料，並非真實的在讀清大生。意即，這裡無法使用 "真正" 的清大學生身分登入，因為資料庫裡沒有。  
如果想要體驗這個bot的功能的話，可以來信 tc.chang@gapp.nthu.edu.tw，向我索取一個用戶身分。  
  
  
- 由於本bot還處於開發階段，且我們沒有像樣的伺服器，因此所有程式目前都是在我的筆電運行。  
`所以有時候bot沒反應，是因為我的筆電沒開機😖，或者 清、大、網、路、太、爛` 


# 夜讀區小幫手 Line Bot  

`夜讀區小幫手` Line Bot 使用 `Python` 搭配 `Flask` 框架和 `PostgreSQL` 資料庫開發。  
  
  
  
  
以下為 `夜讀區小幫手` 提供的功能:  

- 清大學生 `登入`  
  
  
- `預約/取消預約` 清大圖書館的 `夜讀區座位`
  
  
- 查看並修改 `個人預約訊息`
  
  
- 查看 `清大夜讀區` 相關資訊  
   
   
- 用戶支援
  
  
  
  
## 使用方法
### 1. 添加Line Bot為好友  
打開 `Line`，至 主頁 > 加入好友 > 搜尋，點選ID輸入`@680qnkmj` 查詢，並加入好友。 
  
或複製連結 `https://line.me/R/ti/p/%40680qnkmj` 至line開啟，並加入好友  
  
  
### 2. 登入  
點選 `選單` 中的 `登入` 按鈕 ，或直接發送 `@登入` 訊息  
  
再依 `bot` 指示的格式，輸入帳號密碼
  
  
  
### 3. 使用功能  
#### 成功登入後，可使用以下功能:  

- 點選 `選單` 中的 `預約` 按鈕 ，或直接發送 `@預約` 訊息，以 `預約夜讀區座位` 
  
  
- 點選 `選單` 中的 `取消預約` 按鈕 ，或直接發送 `@取消預約` 訊息，以 `取消預約`  
  
  
- 點選 `選單` 中的 `我的` 按鈕 ，或直接發送 `@我的` 訊息，以 `查看個人預約資訊` 或 `取消預約`  
  
  
  
  
  
  

#### 以下為不需登入，也可使用的功能:
  
- 點選 `選單` 中的 `關於` 按鈕 ，或直接發送 `@關於` 訊息，可選擇 `使用說明` 、 `常見問題` 或 `聯絡我們` 進行了解 
  
  
- 點選 `選單` 中的 `其他` 按鈕 ，或直接發送 `@其他` 訊息，可選擇 `夜讀區地點` 、 `夜讀區開放時間` 、 `夜讀區使用規則` 或 `聯絡我們` 進行了解  
  
  
  
  
  
### 4. 問題反饋

若使用上有遇到任何問題，或者有想提的建議，可發送 `@聯絡我們` 訊息以獲取 `反饋表單`  填寫
  
  
  
## 使用技術及套件
### 本專案
- 使用 `Flask框架` 來構建 Web應用程式。
  
  
- 使用 `LINE Messaging API SDK for Python` 與 Line Bot進行通信
  
  
- 使用 `PostgreSQL` 資料庫儲存 line用戶資訊、學生資訊、座位資訊及預約訊息
  
  
- 透過 `Flask-Migrate` 進行資料庫遷移管理
  
  
- 透過 `Flask-SQLAlchemy` 進行資料庫操作  


## 其他
這個專案由於是犧牲讀期末的時間一個人拼命趕工趕出來的，部分地方寫的比較暴力，還需要優化和整理。  
未來暑假如果有時間的話，可能會再更新個 v2。  
  
屆時除了代碼優化外，應該也會部屬到雲端的運算平台，也就不用一直開著電腦才能運作了XD
