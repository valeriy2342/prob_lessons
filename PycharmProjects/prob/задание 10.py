import os

def sozdatel_papok():
    for i in range(0, 9):
        imya_papki = f'dir_{i}'
        os.mkdir(imya_papki)


def udalitel_papok():
    for i in range(0, 9):
        imya_papki = f'dir_{i}'
        os.rmdir(imya_papki)


udalitel_papok()