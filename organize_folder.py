import os, fnmatch, argparse, shutil
from tqdm import tqdm
from zipfile import ZipFile
from pathlib import Path

def __delete_empty_folder(folder) -> None:
    """
    刪除空的資料夾
    """
    for dirs, subdirs, files in os.walk(folder, topdown = False):
        try:
            os.rmdir(dirs)
        except OSError as e:
            pass

def __unzip_folder(folder) -> None:
    """
    將以"download"開頭命名的zip檔案解壓縮
    注意：執行第二次時，要先刪除執行第一次留下的檔案。
    """
    print("解壓縮中：")
    progress = tqdm(total=len(os.listdir(folder)))
    for file in os.listdir(folder):
        if fnmatch.fnmatch(file, "drive-download-*.zip"):
            with ZipFile(os.path.join(folder, file), 'r') as zip:
                for fn in zip.namelist():
                    extracted_path = Path(zip.extract(fn, path=folder))
                    try:
                        fn_readable = fn.encode('cp437').decode('cp950') # 處理中文亂碼問題
                    except:
                        fn_readable = fn
                    try:
                        extracted_path.rename(os.path.join(folder, fn_readable))
                    except OSError as e:
                        # 未刪除第一次執行殘留的檔案會遇到error
                        # print(f"錯誤:{e.strerror}")
                        pass
        progress.update(1)
    __delete_empty_folder(folder)

def __move_subfile(file_source, file_destination) -> None:
    """
    搬移每一層子資料夾的檔案
    """
    for dirs, subdirs, files in os.walk(file_source, topdown = False):
        for f in files:
            sub_file_source = os.path.join(dirs, f)
            child_path = sub_file_source.split(os.path.split(file_destination)[-1])[-1]
            sub_file_destination = file_destination + child_path
            # print(sub_file_destination)
            sub_file_destination_prefix, sub_file_name = os.path.split(sub_file_destination)
            # 將檔案搬到不完全存在的目標資料夾時，要先建立資料夾
            os.makedirs(sub_file_destination_prefix, exist_ok =True)
            shutil.move(sub_file_source, sub_file_destination)

def __merge_same_folder(folder) -> None:
    """
    將多個符合命名格式的第一層子資料夾 
    (e.g. "大學生活-20220808T022653Z-001"、"大學生活-20220808T022653Z-002"、"drive-download-2022-001")
    裡面的第二層子資料夾移動到上一層 (e.g. "大學生活"、drive)
    注意：有些檔案無權限被存取，所以無法被此程式自動整合。
    """
    print("合併資料夾中：")
    fTree = os.walk(folder, topdown = True)
    dirs_1st, subdirs_1st, files_1st = next(fTree) # 第一層子資料夾
    progress = tqdm(total=len(subdirs_1st))
    for dir in subdirs_1st:
        if (len(dir.split('-')) == 3) or (dir.startswith('drive-download-')):
            for file in os.listdir(os.path.join(folder, dir)):
                file_source = os.path.join(folder, dir, file)
                file_destination = os.path.join(folder, file)
                # 若原資料夾已存在則不能搬運整個同名資料夾，只能搬運底下的資料。
                if os.path.exists(file_destination):
                    __move_subfile(file_source, file_destination)
                else:
                    shutil.move(file_source, file_destination)
        progress.update(1)
    __delete_empty_folder(folder)

def organize_foler(folder):
    __unzip_folder(folder)
    __merge_same_folder(folder)
    
if __name__ == "__main__":
    """
    使用指令: python organize_folder.py --folder D:/雲端硬碟_大學帳號
    注意: 路徑要用斜線"/"
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--folder', type=str, default="./download_folder", required=False,
                        help='The path you save files from Google Drive')
    args = parser.parse_args()
    folder = args.folder
    organize_foler(folder)