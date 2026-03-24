#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
广西换电/充电日报 - 发送脚本
通过钉钉 Webhook 发送
"""

import urllib.request
import urllib.error
import json
from datetime import datetime

WEBHOOK_URL = "https://oapi.dingtalk.com/robot/send?access_token=460163888f0a521785e26a27ba860197a3a8df797fe10ff26572ee6dee5d14c2"

def send_markdown(title, content):
    """发送 Markdown 消息到钉钉"""
    data = {
        "msgtype": "markdown",
        "markdown": {
            "title": title,
            "text": content
        }
    }
    
    req = urllib.request.Request(
        WEBHOOK_URL,
        data=json.dumps(data).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )
    
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            result = json.loads(response.read().decode('utf-8'))
            if result.get('errcode') == 0:
                print("✅ 发送成功!")
                return True
            else:
                print(f"❌ 发送失败: {result.get('errmsg')}")
                return False
    except Exception as e:
        print(f"❌ 发送异常: {e}")
        return False

def send_text(message):
    """发送文本消息到钉钉"""
    data = {
        "msgtype": "text",
        "text": {
            "content": message
        }
    }
    
    req = urllib.request.Request(
        WEBHOOK_URL,
        data=json.dumps(data).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )
    
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            result = json.loads(response.read().decode('utf-8'))
            if result.get('errcode') == 0:
                print("✅ 发送成功!")
                return True
            else:
                print(f"❌ 发送失败: {result.get('errmsg')}")
                return False
    except Exception as e:
        print(f"❌ 发送异常: {e}")
        return False

if __name__ == "__main__":
    today = datetime.now().strftime("%Y年%m月%d日")
    
    # 测试消息
    test_content = f"""# ⚡ 广西换电/充电日报资讯

**📅 {today}**

---

✅ **Webhook 配置测试成功！**

定时任务已配置完成：
- ⏰ 每天 9:00 自动推送
- 📡 通过钉钉 Webhook 发送
- 📋 内容涵盖广西换电/充电一手资讯

---

> 测试时间: {datetime.now().strftime('%H:%M:%S')}

"""

    send_markdown("广西换电/充电日报资讯 - 测试", test_content)
