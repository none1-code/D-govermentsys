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
print("1. 正在登录...")
login_response = session.post(login_url, data=login_data)

# 检查登录是否成功
if login_response.url == 'http://127.0.0.1:5000/':
    print("✓ 登录成功！")
    
    # 访问数据抓取页面
    scraper_page_url = 'http://127.0.0.1:5000/data-scraper'
    print("\n2. 访问数据抓取页面...")
    page_response = session.get(scraper_page_url)
    print(f"✓ 页面访问成功，状态码: {page_response.status_code}")
    
    # API URL
    api_url = 'http://127.0.0.1:5000/api/scrape'
    
    # API请求数据 - 模拟前端发送的JSON数据
    api_data = {
        'keyword': '宜宾',
        'page': 1
    }
    
    # 发送API请求 - 模拟前端的AJAX请求
    print("\n3. 发送API请求（模拟前端AJAX）...")
    headers = {
        'Content-Type': 'application/json'
    }
    api_response = session.post(api_url, json=api_data, headers=headers)
    
    # 打印响应信息
    print(f"✓ API请求成功，状态码: {api_response.status_code}")
    
    try:
        # 尝试解析JSON
        result = api_response.json()
        print("\n4. 解析JSON响应...")
        print(f"✓ JSON解析成功！")
        print(f"   - 关键字: {result.get('keyword')}")
        print(f"   - 页码: {result.get('page')}")
        print(f"   - 成功状态: {result.get('success')}")
        
        if result.get('success'):
            data_list = result.get('data', [])
            print(f"   - 返回数据数量: {len(data_list)}")
            
            # 打印前3条数据作为示例
            print("\n5. 前3条数据示例:")
            for i, item in enumerate(data_list[:3], 1):
                print(f"\n   第{i}条:")
                print(f"   - 标题: {item.get('title')}")
                print(f"   - 来源: {item.get('source')}")
                print(f"   - URL: {item.get('original_url')}")
        else:
            print(f"   - 错误信息: {result.get('error')}")
            
    except json.JSONDecodeError as e:
        print(f"✗ JSON解析失败: {e}")
        print(f"   响应内容: {api_response.text}")
    except Exception as e:
        print(f"✗ 处理响应时出错: {e}")
        import traceback
        traceback.print_exc()
else:
    print("✗ 登录失败！")
    print(f"   登录响应URL: {login_response.url}")
    print(f"   响应内容前100字符: {login_response.text[:100]}...")

print("\n测试完成！")
