import os
import sys
import django

# 本脚本可以传入以下参数：
# clear, data, user,rebuild, new
# 在不传入参数的清空下默认执行 data 操作
if __name__ == "__main__":
    print('Importing Django...')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "newbie.settings")
    django.setup()

    try:
        from django.core.management import execute_from_command_line
        from django.contrib.auth.models import User
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
                os.system('python clear.py')
            # 初始化数据库
            if 'data' in sys.argv[1:]:
                print('\n执行 Makemigrations 操作：')
                execute_from_command_line(['manage.py', 'makemigrations'])
                print('\n执行 Migrate 操作：')
                execute_from_command_line(['manage.py', 'migrate'])
            # 创建默认管理员用户
            if 'user' in sys.argv[1:]:
                print('\n创建管理员用户：')
                try:
                    user = User.objects.create_superuser('admin', 'admin@test.com', 'admin123456')
                except BaseException:
                    print('>> 用户创建失败！')
                else:
                    print('>> 成功！\n>>')
                    print('   用户名：admin')
                    print('     密码：admin123456')
            # 重新初始化整个项目
            if 'rebuild' in sys.argv[1:]:
                os.system('python clear.py')
                print('\n执行 Makemigrations 操作：')
                execute_from_command_line(['manage.py', 'makemigrations'])
                print('\n执行 Migrate 操作：')
                execute_from_command_line(['manage.py', 'migrate'])
                print('\n创建管理员用户：')
                try:
                    user = User.objects.create_superuser('admin', 'admin@test.com', 'admin123456')
                except BaseException:
                    print('>> 用户创建失败！')
                else:
                    print('>> 成功！\n>>')
                    print('   用户名：admin')
                    print('     密码：admin123456')
            # 初始化新项目
            if 'new' in sys.argv[1:]:
                print('\n执行 Makemigrations 操作：')
                execute_from_command_line(['manage.py', 'makemigrations'])
                print('\n执行 Migrate 操作：')
                execute_from_command_line(['manage.py', 'migrate'])
                print('\n创建管理员用户：')
                try:
                    user = User.objects.create_superuser('admin', 'admin@test.com', 'admin123456')
                except BaseException:
                    print('>> 用户创建失败！')
                else:
                    print('>> 成功！\n>>')
                    print('   用户名：admin')
                    print('     密码：admin123456')
        else:
            # 默认执行：只更新数据库
            print('\n执行 Makemigrations 操作：')
            execute_from_command_line(['manage.py', 'makemigrations'])
            print('\n执行 Migrate 操作：')
            execute_from_command_line(['manage.py', 'migrate'])