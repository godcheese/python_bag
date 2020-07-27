#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @author godcheese [godcheese@outlook.com]
# @date 2020-07-26
import getopt
import platform
import sys
import urllib


class InstallDevSoftware:
    version = '0.0.1'
    system_full_version = ''
    python_full_version = ''
    system_support = False
    python_support = False
    system = {'platform': '', 'version': '', 'machine': '', 'processor': '',
              'support': {
                  'macos': ['macOS 10.15.3 x86_64', 'macOS 10.15.5 x86_64', 'macOS 10.15.6 x86_64'],
                  'linux': ['Windows XP x86_64', 'Windows 7 x86_64', 'Windows 10 x86_64'],
                  'windows': ['Windows XP x86_64', 'Windows XP AMD64', 'Windows 7 x86_64', 'Windows 7 AMD64',
                              'Windows 10 x86_64', 'Windows 10 AMD64']
              },
              }
    python = {'version': '', 'support': {
        'python': ['3.7.2']
    }}

    # software_list = {
    #     'jdk': {
    #         {'jdk-1.8.0_202':
    #             [{
    #                 'name': 'jdk-8u202-linux-x64.tar.gz',
    #                 'url': 'https://repo.huaweicloud.com/java/jdk/8u202-b08/jdk-8u202-linux-x64.tar.gz',
    #                 'support_system': {'linux': system['support']['linux'], }
    #             },
    #                 {
    #                     'name': 'jdk-8u202-macosx-x64.dmg',
    #                     'url': 'https://repo.huaweicloud.com/java/jdk/8u202-b08/jdk-8u202-macosx-x64.dmg',
    #                     'support_system': {'macos': system['support']['macos'], }
    #                 },
    #             ]
    #         },
    #     },
    #     'python': {
    #         {'python-3.8.5': 'https://www.python.org/ftp/python/3.8.5/Python-3.8.5.tgz',
    #          'support_system':
    #              {'linux': system['support']['linux'], }
    #          },
    #     },
    #     'maven': {
    #         {'python-3.8.5': 'https://www.python.org/ftp/python/3.8.5/Python-3.8.5.tgz',
    #          'support_system':
    #              {'linux': system['support']['linux'], }
    #          },
    #     },
    #     'nginx': {
    #         {'python-3.8.5': 'https://www.python.org/ftp/python/3.8.5/Python-3.8.5.tgz',
    #          'support_system':
    #              {'linux': system['support']['linux'], }
    #          },
    #     },
    #     'mysql': {
    #         {'python-3.8.5': 'https://www.python.org/ftp/python/3.8.5/Python-3.8.5.tgz',
    #          'support_system':
    #              {'linux': system['support']['linux'], }
    #          },
    #     },
    #     'oracle': {
    #         {'python-3.8.5': 'https://www.python.org/ftp/python/3.8.5/Python-3.8.5.tgz',
    #          'support_system':
    #              {'linux': system['support']['linux'], }
    #          },
    #     },
    # }

    def __init__(self):
        self.show_banner()

    def run(self, argv):
        self.get_system_full_version()
        self.get_python_full_version()
        self.is_system_support()
        self.is_python_support()
        print(self.system_full_version)
        print(self.python_full_version)
        print(self.system_support)
        print(self.python_support)


    def start(self, argv):
        if self.system_support == 1:
            if self.python_support == 1:

                arg = argv[1:]
                opts = ''
                args = ''

                if len(arg) >= 1:
                    opts = arg[0]
                if len(arg) >= 2:
                    args = arg[1]
                if opts in ('-h', '--help'):
                    print('[*] Help info')
                    print('-h --help: help info')
                    print('-v --version: version info')
                    print('-i --install: install dev, example -i jdk/nginx/mysql or --install=jdk/nginx/mysql')
                    print(
                        '-itv --install_target_version: install target version dev, example -itv jdk-8u202/nginx-1.18.0/mysql-5.7.31 or --install_target_version=jdk-8u202/nginx-1.18.0/mysql-5.7.31')
                    sys.exit()
                if opts in ('-v', '--version'):
                    print('[*] Version is  ' + self.version)
                    sys.exit()
                if opts in ('-i', '--install'):
                    dev = args
                    print(dev.split('/'))
                    p = dev.split('/')
                    for n in p:
                        self.get_install_switch(n)
                    sys.exit()
                if opts in ('-itv', '--install_target_version'):
                    dev = args
                    print(dev.split('/'))
                    # self.start(dev)
                    # self.finish(dev)
                    sys.exit()

            else:
                print('不支持的 Python，无法继续操作')
        else:
            print('不支持的系统，无法继续操作')

    def finish(self, argv):
        if self.system_support == 1 and self.python_support == 1:
            self.uninstall_jdk()

    def show_banner(self):
        print('-------------------------------------------------\n'
              '| Install Dev Software                           |\n'
              '| http://github.com/godcheese/python_bag         |\n'
              '| author: godcheese [godcheese@outlook.com]      |\n'
              '-------------------------------------------------')
        print('Support system：\n'
              '-------------------------------------------------')
        for (system_name, system_full_version_list) in self.system['support'].items():
            print(system_full_version_list)
        print('-------------------------------------------------')

    # 获取当前系统版本
    def get_system_full_version(self):
        self.system['platform'] = platform.system()
        self.system['machine'] = platform.machine()
        self.system['processor'] = platform.processor()
        print(platform.version())
        if self.system['platform'] == 'Darwin':
            self.system['platform'] = 'macOS'
            sys_ver = platform.mac_ver()
            self.system['version'] = sys_ver[0]
        elif self.system['platform'] == 'Windows':
            self.system['platform'] = 'Windows'
            sys_ver = platform.win32_ver()
            self.system['version'] = sys_ver[0]
        elif self.system['platform'] == 'Linux':
            self.system['platform'] = 'Linux'
            sys_ver = platform.linux_distribution()
            self.system['version'] = sys_ver[0]
        else:
            self.system['platform'] = 'Unknown'
        self.system_full_version = self.system['platform'] + ' ' + self.system['version'] + ' ' + self.system[
            'machine']

    # 获取当前 python 版本
    def get_python_full_version(self):
        python_version = platform.python_version()
        self.python['version'] = python_version
        self.python_full_version = python_version

    # 判断当前系统是否支持此脚本
    def is_system_support(self):
        for (system_name, system_full_version_list) in self.system['support'].items():
            for system_full_version in system_full_version_list:
                if self.system_full_version.lower() == system_full_version.lower():
                    self.system_support = True
        self.system_support = False

    # 判断当前 python 是否支持此脚本
    def is_python_support(self):
        for (python_name, python_full_version_list) in self.python['support'].items():
            for python_full_version in python_full_version_list:
                if self.python_full_version.lower() == python_full_version.lower():
                    self.python_support = True
        self.python_support = False

    def get_install_switch(self):
        install_switch = {
            'jdk': self.install_jdk(),
            'python': self.install_jdk(),
            'maven': self.install_jdk(),
            'nginx': self.install_jdk(),
            'mySQL': self.install_jdk(),
            'oracle': self.install_jdk(),
        }
        return install_switch

    def get_uninstall_switch(self):
        uninstall_switch = {
            'jdk': self.install_jdk(),
            'python': self.install_jdk(),
            'maven': self.install_jdk(),
            'nginx': self.install_jdk(),
            'mySQL': self.install_jdk(),
            'oracle': self.install_jdk(),
        }
        return uninstall_switch

    # 安装 JDK
    def install_jdk(self):
        print("downloading with urllib")
        url = 'http://download.redis.io/releases/redis-5.0.5.tar.gz'
        print("downloading with urllib")
        urllib.urlretrieve(url, "demo.zip")

    # 卸载 JDK
    def uninstall_jdk(self):
        print('uninstall_jdk')

    # 安装 Python
    def install_python(self):
        print('install_python')

    # 卸载 Python
    def uninstall_python(self):
        print('uninstall_python')

    # 安装 Maven
    def install_maven(self):
        print('install_maven')

    # 卸载 Maven
    def uninstall_maven(self):
        print('uninstall_maven')

    # 安装 Nginx
    def install_nginx(self):
        print('install_nginx')

    # 卸载 Nginx
    def uninstall_nginx(self):
        print('uninstall_nginx')

    # 安装 MySQL
    def install_mysql(self):
        print('install_mysql')

    # 卸载 MySQL
    def uninstall_mysql(self):
        print('uninstall_mysql')

    # 安装 Oracle
    def install_oracle(self):
        print('install_oracle')

    # 卸载 Oracle
    def uninstall_oracle(self):
        print('uninstall_oracle')


install_dev_software = InstallDevSoftware()
install_dev_software.run(sys.argv)
