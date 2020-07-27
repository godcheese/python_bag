#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @author godcheese [godcheese@outlook.com]
# @date 2020-07-26
import getopt
import platform
import sys
import os
import tarfile
import urllib


class InstallDevSoftware:
    version = '0.0.1'
    system_full_version = ''
    python_full_version = ''
    system = {'platform': '', 'version': '', 'machine': '', 'processor': ''}
    python = {'version': ''}
    current_path = ''
    directory_separator = '/'

    def __init__(self):
        self.show_banner()

    def run(self, argv):
        self.get_system_full_version()
        self.get_python_full_version()
        if self.system['platform'] == 'Windows':
            self.directory_separator = '\\'
        if self.system['platform'] == 'Linux' or self.system['platform'] == 'macOS':
            self.directory_separator = '/'
        self.current_path = os.getcwd()
        self.start(argv)

    def start(self, argv):
        args = argv[1:]
        opts = ''
        if len(args) >= 1:
            opts = args[0]
        if opts in ('-h', '--help'):
            print('[*] Help info')
            print('-h --help: help info')
            print('-v --version: install dev software version info and system version info')
            print(
                '-ofi --offline_install: offline install version dev, example: -ofi jdk /webwork/software/jdk/jdk8 /file/jdk.tar.gz or --offline_install=jdk /webwork/software/jdk/jdk8 /file/jdk.tar.gz')
            print(
                '-oni --offline_install: offline install version dev, example: -oni jdk /webwork/software/jdk/jdk8 http://jdk.tar.gz or --online_install=jdk /webwork/software/jdk/jdk8 http://jdk.tar.gz')
            sys.exit()
        if opts in ('-v', '--version'):
            print('[*] Version info')
            print('install dev software version: ' + self.version)
            print('system version: ' + self.system_full_version)
            print('python version: ' + self.python_full_version)
            sys.exit()
        if opts in ('-ofi', '--offline_install'):
            if len(args) >= 4:
                install_type = args[1]
                install_path = args[2]
                install_package_path = args[3]
                self.get_install_switch(install_type, install_path, install_package_path, None)
            sys.exit()
        if opts in ('-oni', '--online_install'):
            if len(args) >= 4:
                install_type = args[1]
                install_path = args[2]
                download_package_url = args[3]
                self.get_install_switch(install_type, install_path, None, download_package_url)
            sys.exit()

    def finish(self, argv):
        # if self.system_support == 1 and self.python_support == 1:
            self.uninstall_jdk()

    def show_banner(self):
        print('-------------------------------------------------\n'
              '| Install Dev Software                           |\n'
              '| http://github.com/godcheese/python_bag         |\n'
              '| author: godcheese [godcheese@outlook.com]      |\n'
              '-------------------------------------------------')

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
            'machine'] + ' ' + self.system['processor']

    # 获取当前 python 版本
    def get_python_full_version(self):
        python_version = platform.python_version()
        self.python['version'] = python_version
        self.python_full_version = python_version

    def get_install_switch(self, install_type, install_path, install_package_path, download_package_url):
        if install_type.lower() == 'jdk':
            self.install_jdk(install_path, install_package_path, download_package_url)
        if install_type.lower() == 'python':
            self.install_python(install_path, install_package_path, download_package_url)
        if install_type.lower() == 'maven':
            self.install_maven(install_path, install_package_path, download_package_url)
        if install_type.lower() == 'nginx':
            self.install_nginx(install_path, install_package_path, download_package_url)
        if install_type.lower() == 'mysql':
            self.install_mysql(install_path, install_package_path, download_package_url)
        if install_type.lower() == 'oracle':
            self.install_oracle(install_path, install_package_path, download_package_url)

    def get_uninstall_switch(self, install_type, install_path, install_package_path, download_package_url):
        if install_type.lower() == 'jdk':
            self.uninstall_jdk(install_path, install_package_path, download_package_url)
        if install_type.lower() == 'python':
            self.uninstall_python(install_path, install_package_path, download_package_url)
        if install_type.lower() == 'maven':
            self.uninstall_maven(install_path, install_package_path, download_package_url)
        if install_type.lower() == 'nginx':
            self.uninstall_nginx(install_path, install_package_path, download_package_url)
        if install_type.lower() == 'mysql':
            self.uninstall_mysql(install_path, install_package_path, download_package_url)
        if install_type.lower() == 'oracle':
            self.uninstall_oracle(install_path, install_package_path, download_package_url)

    # 安装 JDK
    def install_jdk(self, install_path, install_package_path, download_package_url):
        if install_package_path is None:
            basename = os.path.basename(download_package_url)
            file = os.path.splitext(basename)
            file_name = file[0]
            file_type = file[1]
            print('正在下载文件..')
            urllib.urlretrieve(download_package_url, basename)
            print('下载完成..')
            print('正在解压文件..')
            print(self.current_path + self.directory_separator + basename)
            self.extrac_tar_gz(self.current_path + self.directory_separator + basename, install_path)
            print('解压完成，路径地址：：{}'.format(install_path))
        if download_package_url is None:
            basename = os.path.basename(install_package_path)
            file = os.path.splitext(basename)
            file_name = file[0]
            file_type = file[1]
            print('正在解压文件..')
            self.extrac_tar_gz(install_package_path, install_path)
            print('解压完成，路径地址：：{}'.format(install_path))

    # 卸载 JDK
    def uninstall_jdk(self, install_path, install_package_path, download_package_url):
        print('uninstall_jdk')

    # 安装 Python
    def install_python(self, install_path, install_package_path, download_package_url):
        print('install_python')

    # 卸载 Python
    def uninstall_python(self, install_path, install_package_path, download_package_url):
        print('uninstall_python')

    # 安装 Maven
    def install_maven(self, install_path, install_package_path, download_package_url):
        print('install_maven')

    # 卸载 Maven
    def uninstall_maven(self, install_path, install_package_path, download_package_url):
        print('uninstall_maven')

    # 安装 Nginx
    def install_nginx(self, install_path, install_package_path, download_package_url):
        print('install_nginx')

    # 卸载 Nginx
    def uninstall_nginx(self, install_path, install_package_path, download_package_url):
        print('uninstall_nginx')

    # 安装 MySQL
    def install_mysql(self, install_path, install_package_path, download_package_url):
        print('install_mysql')

    # 卸载 MySQL
    def uninstall_mysql(self, install_path, install_package_path, download_package_url):
        print('uninstall_mysql')

    # 安装 Oracle
    def install_oracle(self, install_path, install_package_path, download_package_url):
        print('install_oracle')

    # 卸载 Oracle
    def uninstall_oracle(self, install_path, install_package_path, download_package_url):
        print('uninstall_oracle')

    # 解压 .tar.gz 文件
    def extrac_tar_gz(self, fname, dirs):
        try:
            t = tarfile.open(fname)
            t.extractall(path=dirs)
            return True
        except Exception as e:
            print(e)
            return False


install_dev_software = InstallDevSoftware()
install_dev_software.run(sys.argv)
