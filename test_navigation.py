import requests
from bs4 import BeautifulSoup

# 先登录获取会话
login_data = {
    'username': 'admin',
    'password': 'admin123'
}

with requests.Session() as session:
    # 登录
    login_response = session.post('http://127.0.0.1:5000/login', data=login_data)
    
    if login_response.status_code == 302:  # 登录成功应该重定向
        print("登录成功！")
        
        # 获取首页内容，检查导航结构
        response = session.get('http://127.0.0.1:5000/')
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 检查导航菜单结构
            nav_items = soup.find_all('li', class_='layui-nav-item')
            print(f"\n导航菜单结构：")
            for item in nav_items:
                a_tag = item.find('a')
                if a_tag:
                    href = a_tag.get('href')
                    text = a_tag.get_text().strip()
                    is_active = 'layui-this' in item.get('class', [])
                    print(f"  - {text} (href: {href}, active: {is_active})")
            
            # 检查JavaScript代码是否存在
            scripts = soup.find_all('script')
            js_code = '\n'.join([script.string for script in scripts if script.string])
            
            if 'setNavActive' in js_code:
                print(f"\n✓ 导航选中状态设置的JavaScript函数已存在")
            else:
                print(f"\n✗ 没有找到导航选中状态设置的JavaScript函数")
                
            if 'window.addEventListener(\'load\', setNavActive)' in js_code:
                print(f"✓ JavaScript函数已在页面加载时调用")
            else:
                print(f"✗ JavaScript函数没有在页面加载时调用")
        else:
            print(f"首页请求失败，状态码 {response.status_code}")
    else:
        print(f"登录失败，状态码 {login_response.status_code}")