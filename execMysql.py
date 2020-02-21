# coding: utf-8
from connectMysql import execsql
import sys

execsql.execsqlfile(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], '0')