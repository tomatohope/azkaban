# coding: utf-8
from connectPgsql import execsql
import sys
import os

file = '/opt/services/azkaban/azkaban-exec-server/build/install/azkaban-exec-server/bin/sql/connection'
with open(file, "r") as f:
    con = f.readline()

os.environ['file'] = file

def get_con_info(key):
    os.environ['key'] = key
    return os.popen("cat $file | grep $key | awk -F \"=\" '{print $2}' | tr '\n' ' ' | sed 's/ //g'").read()

#para: database, user, passwd, host port, sql, result,dict
execsql.execsqlfile(get_con_info("DW_ADB_PGSQL_DATABASE"), get_con_info("DW_ADB_PGSQL_USERNAME"), get_con_info("DW_ADB_PGSQL_PASSWORD"), get_con_info("DW_ADB_PGSQL_HOST"), get_con_info("DW_ADB_PGSQL_PORT"), sys.argv[1], '0', sys.argv[2])
