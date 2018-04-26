import os
import sys
import django


# 本脚本可以传入以下参数：
# clear, data, user,run, rebuild, new
# 在不传入参数的情况下默认执行 data 操作
if __name__ == "__main__":
    try:
        print('Importing Django...')
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "newbie.settings")
        from django.core.management import execute_from_command_line

        def create_user():
            print('\n创建管理员用户：')
            try:
                django.setup()
                from django.contrib.auth.models import User
                User.objects.create_superuser('admin', 'admin@test.com', 'admin123456')
            except BaseException:
                print('>> 用户创建失败！')
            else:
                print('>> 成功！\n>>')
                print('   用户名：admin')
                print('     密码：admin123456')


        def clear_data():
            os.system('python clear.py')


        def format_data():
            print('\n执行 Makemigrations 操作：')
            execute_from_command_line(['manage.py', 'makemigrations'])
            print('\n执行 Migrate 操作：')
            execute_from_command_line(['manage.py', 'migrate'])


        def run_server():
            print('\n运行测试服务器：')
            # 使用此代码可以避免重新加载Django,因此会提高运行速度
            # 但是，直接运行会引起程序重复执行，初步判断是因为creat_user中执行了django.setup()
            #execute_from_command_line(['manage.py', 'runserver'])
            os.system('python manage.py runserver')


    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    else:
        if len(sys.argv)>1:
            # 清空数据库
            if 'clear' in sys.argv[1:]:
                clear_data()
            # 初始化数据库
            if 'data' in sys.argv[1:]:
                format_data()
            # 创建默认管理员用户
            if 'user' in sys.argv[1:]:
                create_user()
            # 运行测试服务器
            if 'run' in sys.argv[1:]:
                run_server()
            # 重新初始化整个项目
            if 'rebuild' in sys.argv[1:]:
                clear_data()
                format_data()
                create_user()
                run_server()
            # 初始化新项目
            if 'new' in sys.argv[1:]:
                format_data()
                create_user()
                run_server()
        else:
            # 默认执行：只更新数据库
            format_data()


