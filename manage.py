#!/usr/bin/env python3
"""Django's command-line utility for administrative tasks."""
import os
import psutil
import sys


def main():
    from django.core.management.commands.runserver import Command as Runserver
    Runserver.default_addr = psutil.net_if_addrs()['eth0'][0][1]  # 修改默认地址
    Runserver.default_port = '8080'  # 修改默认端口
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smart_im.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
