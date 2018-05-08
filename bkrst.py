# Author: Charles Mac (charlesmacaron)
# Created: 04 mai 2018

import filecmp
import os
import shutil
import sys
import time

class class_backup:
    def __init__(self, path_src, path_dst):
        if os.path.exists(path_src):
            self.print_msg('Source file or directory is ready')
            self.execute_backup(path_src, path_dst)
        else:
            self.print_msg('ERROR: Source file or directory does not exist')
            sys.exit()
    
    def execute_backup(self, path_src, path_dst):
        if os.path.exists(path_dst):
            if os.path.isdir(path_dst):
                self.print_msg('Destination directory is ready')
            elif os.path.isfile(path_dst):
                self.print_msg('ERROR: Destination directory cannot be a file')
                sys.exit()
            else:
                self.print_msg('ERROR: Failed to prepare destination directory')
                sys.exit()
        else:
            os.mkdir(path_dst)
            self.print_msg('Destination directory is created')
        name_src = os.path.basename(path_src)
        name_dst = time.strftime('%Y%m%d%H%M%S', time.localtime()) + name_src
        if os.path.isfile(path_src):
            if os.path.exists(os.path.join(path_dst, name_dst)):
                os.remove(os.path.join(path_dst, name_dst))
            shutil.copy(path_src, os.path.join(path_dst, name_dst))
        else:
            if os.path.exists(os.path.join(path_dst, name_dst)):
                shutil.rmtree(os.path.join(path_dst, name_dst))
            shutil.copytree(path_src, os.path.join(path_dst, name_dst))
        self.print_msg(name_src + ' has been backed up as ' + name_dst)
    
    def print_msg(self, message):
        print('[', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), '] ', message)

class class_restore:
    def __init__(self, path_src, path_dst):
        name_src = os.path.basename(path_src)
        if len(name_src) < 15:
            self.print_msg('ERROR: Name length of source file or directory is not valid')
            sys.exit()
        else:
            if not name_src[:14].isdigit():
                self.print_msg('ERROR: Name format of source file or directory is not valid')
                sys.exit()
        datetime_src = self.format_datetime(name_src[:14])
        name_dst = name_src[14:]
        if os.path.exists(path_src):
            self.print_msg('Source file or directory is ready')
            self.execute_restore(path_src, path_dst, datetime_src, name_dst)
        else:
            self.print_msg('ERROR: Source file or directory does not exist')
            sys.exit()
    
    def execute_restore(self, path_src, path_dst, datetime_src, name_dst):
        if os.path.exists(path_dst):
            if os.path.isdir(path_dst):
                self.print_msg('Destination directory is ready')
            elif os.path.isfile(path_dst):
                self.print_msg('ERROR: Destination directory cannot be a file')
                sys.exit()
            else:
                self.print_msg('ERROR: Failed to prepare destination directory')
                sys.exit()
        else:
            os.mkdir(path_dst)
            self.print_msg('Destination directory is created')
        if os.path.isfile(path_src):
            if os.path.exists(os.path.join(path_dst, name_dst)):
                os.remove(os.path.join(path_dst, name_dst))
            shutil.copy(path_src, os.path.join(path_dst, name_dst))
        else:
            if os.path.exists(os.path.join(path_dst, name_dst)):
                shutil.rmtree(os.path.join(path_dst, name_dst))
            shutil.copytree(path_src, os.path.join(path_dst, name_dst))
        self.print_msg(name_dst + ' has been restored from ' + datetime_src)
    
    def format_datetime(self, datetime_str):
        year = datetime_str[:4]
        month = datetime_str[4:6]
        day = datetime_str[6:8]
        hour = datetime_str[8:10]
        minute = datetime_str[10:12]
        second = datetime_str[12:14]
        return year + '-' + month + '-' + day  + ' ' + hour  + ':' + minute  + ':' + second
    
    def print_msg(self, message):
        print('[', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), '] ', message)

def bk(path_src, path_dst):
    class_backup(path_src, path_dst)

def rst(path_src, path_dst):
    class_restore(path_src, path_dst)

def demo():
    bk_or_rst = input('Would you like to back up (b) or restore (r)?')
    if bk_or_rst == 'b' or bk_or_rst == 'B':
        path_src = input('File or directory to be backed up: ')
        path_dst = input('Directory to store the backup copies: ')
        bk(path_src, path_dst)
    elif bk_or_rst == 'r' or bk_or_rst == 'R':
        path_src = input('File or directory to restore from: ')
        path_dst = input('Directory to store the restored copies: ')
        rst(path_src, path_dst)
    else:
        print('Illegal user input!')

if __name__ == '__main__':
    demo()
