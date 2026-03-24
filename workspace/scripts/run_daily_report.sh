#!/bin/bash
# 广西换电/充电日报 - 每日定时执行脚本
# 执行时间: 每天 9:00

LOG_FILE="/Users/yanghh/.qclaw/workspace/logs/daily-report.log"
WEBHOOK_URL="https://oapi.dingtalk.com/robot/send?access_token=460163888f0a521785e26a27ba860197a3a8df797fe10ff26572ee6dee5d14c2"

echo "========================================" >> $LOG_FILE
echo "广西换电/充电日报 - $(date '+%Y-%m-%d %H:%M:%S')" >> $LOG_FILE
echo "========================================" >> $LOG_FILE

# 调用 Python 脚本发送日报
cd /Users/yanghh/.qclaw/workspace/scripts
/usr/bin/python3 send_daily_report.py >> $LOG_FILE 2>&1

echo "执行完成: $(date)" >> $LOG_FILE
echo "" >> $LOG_FILE
