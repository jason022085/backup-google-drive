@echo off
echo "第一步：下載雲端硬碟的檔案"
rem 設定變數email的值為使用者在命令列輸入的值
set /p email="Gsuite email:"
echo %email%

rem 設定變數pwd的值為使用者在命令列輸入的值
set /p pwd="Gsuite password:"
echo %pwd%

rem 設定變數sdrive的值為使用者在命令列輸入的值
set /p sdrive="Number of shared drives:"
set /a sdrive = %sdrive%
echo %sdrive%

@python download_gdrive.py --email %email% --pwd %pwd% --sdrive %sdrive%
pause

echo "第二步：整理下載資料夾"
rem 設定變數folder的值為使用者在命令列輸入的值
set /p folder="Your download folder directory:"
echo %folder%
@python organize_folder.py --folder %folder%
pause