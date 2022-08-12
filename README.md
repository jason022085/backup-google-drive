# backup-google-drive
###### tags: `selenium`

> 陽明交通大學在2022年11月要大砍校友Gsuite帳號雲端硬碟容量到5 GB，
> 本專案用自動化程式下載雲端硬碟並整理資料夾。

## Step 0: 下載此專案資料夾
1. `git clone https://github.com/jason022085/backup-google-drive.git`
2. 打開 terminal 並且進入此專案資料夾目錄底下

## Step 1: 下載所有的雲端硬碟
**注意：雲端硬碟至少要有一個資料夾才能被下載**
* email: 你的Gsuite帳號 (私人gmail有安全性問題無法使用)
* pwd: 你的密碼 (放心，程式不會記住，也不會做壞事)
* sdrive: 要下載多少個共用雲端硬碟 (預設為 0)
請輸入以下指令: 
```
python download_gdrive.py --email myaccount@nctu.edu.tw --pwd mypassword --sdrive 0  
```
## Step 2: 解壓縮且整理下載資料夾
**注意: 路徑要用斜線"/"**
* folder: 下載資料夾完整路徑 (用相對路徑可能會出錯)
請輸入以下指令: 
```
python organize_folder.py --folder D:/where/is/the/download/folder  
```