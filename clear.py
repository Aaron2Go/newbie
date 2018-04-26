import os
import os.path
import shutil

#请在将项目共享时，先执行本操作

if __name__ == "__main__":
    print('数据清理操作：\n')
    for parent,dirs,files in os.walk(os.getcwd()):
        if "Upload" in dirs:
            try:
                shutil.rmtree(parent+"\\Upload")
            except BaseException:
                print('>> 删除：' + parent + "\\Upload" + ' ... ×')
            else:
                print('>> 删除：' + parent+"\\Upload" + ' ... √')
        if "db.sqlite3" in files:
            try:
                os.remove(parent+"\\db.sqlite3")
            except BaseException:
                print('>> 删除：' + parent + "\\db.sqlite3" + ' ... ×')
            else:
                print('>> 删除：' + parent+"\\db.sqlite3" + ' ... √')

        if parent.split('\\')[-1]=='migrations':
            for file in files:
                if file!='__init__.py':
                    try:
                        os.remove(parent + "\\" + file)
                    except BaseException:
                        print('>> 删除：' + parent + "\\" + file + ' ... ×')
                    else:
                        print('>> 删除：' + parent + "\\" + file + ' ... √')
    print('>> 完成！')