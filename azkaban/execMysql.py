# coding: utf-8
from connectMysql import execsql
import sys
import os

os.environ['file'] = '/opt/services/azkaban/azkaban-web-server/build/install/azkaban-web-server/conf/azkaban.properties'

azkaban_host = os.popen("cat $file | grep mysql.host | awk -F \"=\" '{print $2}' | tr '\n' ' ' | sed 's/ //g'").read()
azkaban_database = os.popen("cat $file | grep mysql.database | awk -F \"=\" '{print $2}' | tr '\n' ' ' | sed 's/ //g'").read()
azkaban_user = os.popen("cat $file | grep mysql.user | awk -F \"=\" '{print $2}' | tr '\n' ' ' | sed 's/ //g'").read()
azkaban_password = os.popen("cat $file | grep mysql.password | awk -F \"=\" '{print $2}'| tr '\n' ' ' | sed 's/ //g'").read()

sql = "SELECT * from connection where name = '" + sys.argv[1] + "' and is_delete = '0';"

connect = execsql.execsql(azkaban_host, azkaban_user, azkaban_password, azkaban_database, sql, '1', "{}")

#para: host, user, passwd, database, sql, result,dict
execsql.execsqlfile(connect[0][1], connect[0][2], connect[0][3], connect[0][4], sys.argv[2], '0', sys.argv[3])
