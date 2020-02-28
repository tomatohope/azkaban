# coding: utf-8
from connectMysql import execsql
import sys
import os

file = '/opt/services/azkaban/azkaban-exec-server/build/install/azkaban-exec-server/bin/sql/connection'
with open(file, "r") as f:
    con = f.readline()

os.environ['file'] = file

def get_con_info(key):
    os.environ['key'] = key
    return os.popen("cat $file | grep $key | awk -F \"=\" '{print $2}' | tr '\n' ' ' | sed 's/ //g'").read()

# para: host, user, passwd, database, sql, result,dict
execsql.execsqlfile(get_con_info("DW_ADB_MYSQL_HOST"), get_con_info("DW_ADB_MYSQL_USERNAME"), get_con_info("DW_ADB_MYSQL_PASSWORD"), get_con_info("DW_ADB_MYSQL_DATABASE"), sys.argv[1], '0', sys.argv[2])
