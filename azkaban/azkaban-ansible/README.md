##实现方法  这里是账户密码信息通过ansible 统一管理获取
先 创建个project: 负责定时任务 和 传参
再 curl 调azkaban API 触发 scheduler
最后 scheduler 执行 命令（这个命令是 python 通过 sql文件执行sql）


##关于传参
https://azkaban.readthedocs.io/en/latest/ajaxApi.html#schedule-a-period-based-flow-deprecated
#执行project 的两个参数，见模板文件： test-flow-mysql.zip
    两个参数是： 
		参数一：需要执行的sql文件名
		参数二：查询条件

		备注：
			参数名由 test-flow-mysql.zip定义
			关于参数一；连接名： 背景是不让python 脚本直接从外部传入数据库账户密码信息使得azkaban log显示出来; 所以这里让脚本自己去获取 
		
##关于创建cron步骤
#1 先创建flow.zip格式的文件
https://azkaban.readthedocs.io/en/latest/createFlows.html

#2 准备sql文件 和连接信息 和脚本文件
	sql文件是执行cron的脚本文件，如果里面涉及查询条件的关键字段时应将对应的值换成统一字符便于替换；比如 where mid = midmid
	模板脚本文件是 execMysql.py execPgsql.py
	
#3 API 接口触发 cron: 见文档 azkaban-project.py
	先获取session 
	再schedule
	