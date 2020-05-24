import os, wget
from datetime import datetime


def download_with_wget(url, savepath, need_overwrite):
    filename = os.path.basename(url)
    # 判断文件是否存在，如果不存在则下载
    if not os.path.exists(os.path.join(savepath, filename)):
        print(f'Downloading data from {url}')
        wget.download(url, os.path.join(savepath, filename))
        print(f'Download file {filename} finished!')
    else:
        if need_overwrite:
            print(f'Downloading data from {url}')
            wget.download(url, os.path.join(savepath, filename))
            print(f'Overwrite file {filename} finished!')
        else:
            print(f'File {filename} need not be downloaded.')


def record_size(folder_path):
    folder_size = 0
    for filename in os.listdir(folder_path):
        # 获取文件大小
        folder_size += os.path.getsize(os.path.join(folder_path, filename))

    # 文件大小默认以Bytes计， 转换为MB
    msg = f'{datetime.now()} ==>> The size of all files in the folder {folder_path} = {folder_size / 1024 / 1024:.2f} MB'
    with open(os.path.join(folder_path, 'folder_size.txt'), encoding='utf-8', mode='w') as f:
        f.write(msg)

if __name__ == '__main__':
    input_path = '../links.txt'
    output_path = '../files'
    with open(input_path, encoding='utf-8', mode='r') as lst:
        # 以下载cifar-10数据集为例
        link_info = lst.readline().strip().split(',')
        assert len(link_info) == 2
        url, need_overwrite = [x.strip() for x in link_info]
        assert need_overwrite in ['0', '1']
        download_with_wget(url, savepath=output_path, need_overwrite=int( need_overwrite ))
        record_size(folder_path=output_path)