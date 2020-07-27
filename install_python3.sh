#!/usr/bin/env bash

# http://github.com/godcheese/shell_bag
# author: godcheese [godcheese@outlook.com]

    echo -e "\033[32m
    -------------------------------------------------
    | Install Python3                               |
    | http://github.com/godcheese/python_bag         |
    | author: godcheese [godcheese@outlook.com]     |
    -------------------------------------------------
    \033[0m"

current_path=`pwd`
software_path=/webwork/software
install_path=${software_path}/python/python3

download_version=Python-3.8.5
# curl -O https://www.python.org/ftp/python/3.8.5/${download_version}.tgz
tar -zxvf ${download_version}.tgz
cd ${download_version}
mkdir -p install_path
./configure --prefix=${install_path}
make all && make install
make clean && make distclean
cd ${current_path}
rm -rf ${download_version}.taz