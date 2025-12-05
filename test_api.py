import requests
import json

# 创建会话
session = requests.Session()

# 登录URL
login_url = 'http://127.0.0.1:5000/login'

# 登录凭证
login_data = {
    'username': 'admin',
    'password': 'admin123'
}

# 发送登录请求
print("正在登录...")
login_response = session.post(login_url, data=login_data)

# 检查登录是否成功
if login_response.url == 'http://127.0.0.1:5000/':
    print("登录成功！")
    
    # API URL
    api_url = 'http://127.0.0.1:5000/api/scrape'
    
    # API请求数据
    api_data = {
        'keyword': '测试',
        'page': 1
    }
    
    # 发送API请求
    print("\n正在发送API请求...")
    api_response = session.post(api_url, json=api_data)
    
    # 打印响应信息
    print(f"响应状态码: {api_response.status_code}")
    print(f"响应内容: {api_response.text[:500]}...")
    
    try:
        # 尝试解析JSON
        result = api_response.json()
        print("\n解析JSON成功！")
        print(f"JSON格式: {json.dumps(result, ensure_ascii=False, indent=2)}")
    except json.JSONDecodeError:
        print("\nJSON解析失败")
else:
    print("登录失败！")
    print(f"登录响应URL: {login_response.url}")
