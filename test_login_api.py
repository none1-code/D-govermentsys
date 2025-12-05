import requests
import json

# 创建会话
session = requests.Session()

# 登录URL
login_url = 'http://127.0.0.1:5000/login'

# 1. 先获取登录页面，查看是否有CSRF令牌
print('1. 获取登录页面...')
get_response = session.get(login_url)
print(f'GET响应状态码: {get_response.status_code}')

# 2. 检查是否有CSRF令牌
csrf_token = ''
if 'csrf_token' in get_response.text:
    print('发现CSRF令牌')

# 3. 提交登录表单
login_data = {
    'username': 'admin',
    'password': 'admin123'
}

# 如果有CSRF令牌，添加到登录数据中
if csrf_token:
    login_data['csrf_token'] = csrf_token

print('\n2. 发送登录请求...')
print(f'登录数据: {login_data}')

# 发送登录请求
response = session.post(login_url, data=login_data)
print(f'登录响应状态码: {response.status_code}')
print(f'登录响应URL: {response.url}')
print(f'登录响应头: {dict(response.headers)}')

# 检查是否登录成功
# 如果响应URL是首页，说明登录成功
if response.url == 'http://127.0.0.1:5000/':
    print('✓ 登录成功，已跳转到首页')
    
    # 检查session中的cookie
    print(f'\n3. 当前会话的cookies: {dict(session.cookies)}')
    
    # 测试API接口
    api_url = 'http://127.0.0.1:5000/api/scrape'
    
    # API请求参数
    api_data = {
        'keyword': '测试',
        'page': 1
    }
    
    # 设置请求头
    headers = {
        'Content-Type': 'application/json'
    }
    
    # 发送API请求
    print('\n4. 发送API请求...')
    api_response = session.post(api_url, data=json.dumps(api_data), headers=headers)
    print(f'API响应状态码: {api_response.status_code}')
    print(f'API响应内容: {api_response.text}')
    
    try:
        # 尝试解析JSON响应
        result = api_response.json()
        print(f'\n5. 解析后的JSON响应: {json.dumps(result, ensure_ascii=False, indent=2)}')
    except json.JSONDecodeError as e:
        print(f'\n5. JSON解析错误: {e}')
        print(f'   完整响应内容: {api_response.text}')
        
        # 检查是否是HTML响应（如登录页面）
        if '<html' in api_response.text.lower():
            print('\n   响应是HTML页面，可能需要重新登录或权限不足')
else:
    print('✗ 登录失败')
    print(f'登录响应URL: {response.url}')
    print(f'登录响应内容: {response.text[:300]}...')
    print(f'响应头: {dict(response.headers)}')
