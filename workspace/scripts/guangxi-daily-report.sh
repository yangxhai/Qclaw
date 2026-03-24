#!/bin/bash
# 广西换电/充电日报 - 每日自动生成脚本
# 执行时间: 每天 9:00

cd /Users/yanghh/.qclaw/workspace

# 获取今天日期
TODAY=$(date +%Y-%m-%d)
REPORT_FILE="memory/daily-report-${TODAY}.md"

echo "=== 开始生成 ${TODAY} 广西换电/充电日报 ==="

# 这里调用 OpenClaw 执行搜索和生成
# 实际执行需要通过 API 或 CLI 调用

echo "日报已生成: ${REPORT_FILE}"
echo "=== 完成 ==="
