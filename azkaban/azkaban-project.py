# coding: utf-8
import os

# get session id, notice: account pass info read from config file
# getSessinId = str("curl -k -X POST --data \"action=login&username=azkaban&password=5bEmBHBXjffYktuo\" http://10.80.0.231:8081/")
# print("getSessinIdCmd:", getSessinId)
# os.system(getSessinId)
sessionId = "11b5ad28-0819-4d72-85a8-cdcb5d402cd9"

for i in range(1, 2):
    print("i: ", i)
    #
    # # createProject
    # createProject = str("curl -k -X POST --data \"session.id=") + str(sessionId) + str("&name=aaaa") + str(i) + str("&description=test\" http://10.80.0.231:8081/manager?action=create")
    # print("createProjectCmd:", createProject)
    # os.system(createProject)
    #
    # # uploadfile
    # uploadfile = str("curl -k -i -X POST --form 'session.id=") + str(sessionId) + str("' --form 'ajax=upload' --form 'file=@test-flow-mysql.zip;type=application/zip' --form 'project=aaaa") + str(i) + str("' http://10.80.0.231:8081/manager")
    # print("uploadfileCmd: ", uploadfile)
    # os.system(uploadfile)

    #deleteProject
    # deleteProject = str("curl -k --get --data \"session.id=") + str(sessionId) + str("&delete=true&project=aaaa") + str(i) + str("\" http://10.80.0.231:8081/manager")
    # print("deleteProjectCmd: ", deleteProject)
    # os.system(deleteProject)

    #schedule parameter projects Pgsql
    # projectId = int(i) + 2
    # schedule = str("curl -k http://10.80.0.231:8081/schedule -d \"ajax=scheduleFlow&is_recurring=on&period=1h&flowOverride[database]=dev_jms_dw&flowOverride[user]=xxxx&flowOverride[password]=xxxx&flowOverride[host]=gp-uf6fw1e6xv35ikrj9.gpdb.rds.aliyuncs.com&flowOverride[port]=3432&flowOverride[sqlfile]=/opt/services/azkaban/azkaban-exec-server/build/install/azkaban-exec-server/bin/sql/test-sql.sql&projectName=aaaa") + str(i) + str("&flow=test-flow&projectId=") + str(projectId) + str("&scheduleTime=02,42,am,PDT&scheduleDate=02/21/2020\" -b azkaban.browser.session.id=") + str(sessionId)
    # print("scheduleCmd:", schedule)
    # os.system(schedule)

    #schedule parameter projects Mysql 无其他替换参数
    # projectId = int(i) + 209
    # schedule = str("curl -k http://10.80.0.231:8081/schedule -d \"ajax=scheduleFlow&is_recurring=on&period=1h&flowOverride[database]=dev_dw&flowOverride[user]=xxxx&flowOverride[password]=xxxx&flowOverride[host]=am-uf68cpts08jf19trn131910.ads.aliyuncs.com&flowOverride[sqlfile]=/tmp/1.sql&flowOverride[other]={}&projectName=exec-mysql") + str("&flow=test-flow&projectId=") + str(projectId) + str("&scheduleTime=23,25,pm,PDT&scheduleDate=02/26/2020\" -b azkaban.browser.session.id=") + str(sessionId)
    # print("scheduleCmd:", schedule)
    # os.system(schedule)
    #
    # #schedule parameter projects Mysql 有其他替换参数 (字典形式)：  &flowOverride[other]={'sql语句替换字段': '被替换的值'}
    # projectId = int(i) + 209
    # schedule = str("curl -k http://10.80.0.231:8081/schedule -d \"ajax=scheduleFlow&is_recurring=on&period=1h&flowOverride[database]=dev_dw&flowOverride[user]=xxxx&flowOverride[password]=xxxx&flowOverride[host]=am-uf68cpts08jf19trn131910.ads.aliyuncs.com&flowOverride[sqlfile]=/tmp/1.sql&flowOverride[other]={'midmid': '33'}&projectName=exec-mysql") + str("&flow=test-flow&projectId=") + str(projectId) + str("&scheduleTime=23,25,pm,PDT&scheduleDate=02/26/2020\" -b azkaban.browser.session.id=") + str(sessionId)
    # print("scheduleCmd:", schedule)
    # os.system(schedule)
    #
    # #schedule parameter projects Mysql 无其他替换参数  传入获取连接信息的查询条件
    # projectId = int(i) + 209
    # schedule = str("curl -k http://10.80.0.231:8081/schedule -d \"ajax=scheduleFlow&is_recurring=on&period=1h&flowOverride[connectname]=dev_ads_mysql&flowOverride[sqlfile]=/tmp/1.sql&flowOverride[other]={}&projectName=exec-mysql") + str("&flow=test-flow&projectId=") + str(projectId) + str("&scheduleTime=03,30,am,PDT&scheduleDate=02/26/2020\" -b azkaban.browser.session.id=") + str(sessionId)
    # print("scheduleCmd:", schedule)
    # os.system(schedule)

    projectId = int(i) + 210
    schedule = str("curl -k http://10.80.0.231:8081/schedule -d \"ajax=scheduleFlow&is_recurring=on&period=1h&flowOverride[connectname]=dev_ads_pg&flowOverride[sqlfile]=/tmp/2.sql&flowOverride[other]={}&projectName=exec-mysql") + str("&flow=test-flow&projectId=") + str(projectId) + str("&scheduleTime=03,37,am,PDT&scheduleDate=02/26/2020\" -b azkaban.browser.session.id=") + str(sessionId)
    print("scheduleCmd:", schedule)
    os.system(schedule)

    #unschedule parameter projects
    # scheduleId = int(i) + 464
    # unschedule = str("curl -k http://10.80.0.231:8081/schedule -d \"action=removeSched&scheduleId=") + str(scheduleId) + str("\" -b azkaban.browser.session.id=") + str(sessionId)
    # print("unscheduleCmd:", unschedule)
    # os.system(unschedule)