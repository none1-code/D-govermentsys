import requests
import json

# 登录函数
def login():
    login_url = 'http://127.0.0.1:5000/login'
    session = requests.Session()
    
    # 获取登录页面的csrf令牌或其他必要信息
    session.get(login_url)
    
    # 提交登录表单
    login_data = {
        'username': 'admin',
        'password': 'admin123'
    }
    
    response = session.post(login_url, data=login_data)
    
    if response.status_code == 302 and '/login' not in response.url:
        print("✓ 登录成功")
        return session
    else:
        print("✗ 登录失败")
        return None

# 测试数据抓取功能
def test_scraper(session):
    print("\n=== 测试数据抓取功能 ===")
    
    # 测试API端点
    scrape_url = 'http://127.0.0.1:5000/api/scrape'
    
    # 测试参数
    test_keyword = '宜宾'
    test_page = 1
    
    # 构造请求数据
    payload = {
        'keyword': test_keyword,
        'page': test_page
    }
    
    # 设置请求头
    headers = {
        'Content-Type': 'application/json'
    }
    
    try:
        # 发送请求
        response = session.post(scrape_url, data=json.dumps(payload), headers=headers)
        
        # 检查响应状态
        if response.status_code != 200:
            print(f"✗ 请求失败，状态码: {response.status_code}")
            print(f"响应内容: {response.text}")
            return False
        
        # 解析响应内容
        result = response.json()
        
        # 检查结果
        if result.get('success'):
            print(f"✓ 抓取成功")
            print(f"关键字: {result.get('keyword')}")
            print(f"页码: {result.get('page')}")
            print(f"找到 {len(result.get('data', []))} 条结果")
            
            # 打印前几条结果
            if result.get('data'):
                print("\n前3条结果：")
                for i, item in enumerate(result['data'][:3]):
                    print(f"\n第{i+1}条结果:")
                    print(f"标题: {item.get('title', '无')}")
                    print(f"来源: {item.get('source', '无')}")
                    print(f"URL: {item.get('original_url', '无')[:50]}...")
                    print(f"概要: {item.get('summary', '无')[:100]}...")
                    print(f"封面: {'有' if item.get('cover') else '无'}")
            
            return True
        else:
            print(f"✗ 抓取失败: {result.get('error', '未知错误')}")
            return False
            
    except Exception as e:
        print(f"✗ 发生异常: {str(e)}")
        return False

# 主函数
def main():
    # 登录
    session = login()
    
    if session:
        # 测试数据抓取
        test_scraper(session)

if __name__ == "__main__":
    main()