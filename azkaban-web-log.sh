#!/bin/bash
expect -c "
spawn ssh root@10.80.0.231
set timeout 1
expect {
 \"(yes/no)\" {send \"\yes\r\"}
 }
expect {
 \"password:\" {send \"RQaIt0VIWBLyM0p7\r\"}
}
expect {
 \"]#\" {send \"cd /opt/services/azkaban/azkaban-web-server/build/install/azkaban-web-server/bin\r\"}
}
expect {
 \"]#\" {send \"rm logs/*.log -f\r\"}
}
expect {
 \"]#\" {send \"rm webServerLog* -f\r\"}
}
expect {
 \"]#\" {send \"exit\r\"}
}
set timeout 3600
expect eof
"
