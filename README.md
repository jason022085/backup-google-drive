# backup-google-drive
###### tags: `selenium` `Windows` `Python`

陽明交通大學在2022年11月要大砍Gsuite雲端硬碟到5 GB，
本專案用自動化程式備份載雲端硬碟。

## Step 0: 前置作業
1. 下載專案資料夾 `git clone https://github.com/jason022085/backup-google-drive.git`
2. 打開 terminal 並且進入此專案資料夾目錄底下
3. 輸入指令安裝套件 `pip install -r requirements.txt`
4. 輸入指令執行程式 `main.bat` (若執行此bat檔，則可以跳過後面的step 1和step2)

## Step 1: 下載所有的雲端硬碟
* email: 你的Gsuite帳號 (私人gmail有安全性問題無法使用)
* pwd: 你的密碼 (放心，程式不會記住，也不會做壞事)
* sdrive: 要下載多少個共用雲端硬碟 (預設為 0)
* 注意：雲端硬碟**至少要有一個資料夾**才能被下載
* 注意：程式會控制你的滑鼠鍵盤，**執行中請放開雙手等待**

請輸入以下指令: 
```
python download_gdrive.py --email myaccount@nctu.edu.tw --pwd mypassword --sdrive 0  
```
之後，你將看到Chrome被自動打開:
![image](https://github.com/jason022085/backup-google-drive/blob/main/demo/demo_1.png)

接下來只要靜靜等待檔案下載完成，**完成後要手動關掉瀏覽器**。

## Step 2: 解壓縮且整理下載資料夾
**注意: 路徑要用斜線"/"**
* folder: 下載資料夾完整路徑 (用相對路徑可能會出錯)
請輸入以下指令: 
```
python organize_folder.py --folder D:/where/is/the/download/folder  
```

資料夾被整理前:
![image](https://github.com/jason022085/backup-google-drive/blob/main/demo/demo_2.png)

資料夾被整理後(碩班的血汗被合而為一、zip檔解壓縮):
![image](https://github.com/jason022085/backup-google-drive/blob/main/demo/demo_3.png)

接下來只要靜靜等待程式運行結束，**完成後可以手動刪除原本下載的zip壓縮檔**。

#### 如有任何問題，請聯絡我: jason022085@gmail.com