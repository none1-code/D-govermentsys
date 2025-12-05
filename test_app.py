import requests
import json

# 测试基础URL
BASE_URL = 'http://localhost:5000'

# 测试登录功能
def test_login():
    print("测试登录功能...")
    
    # 测试管理员登录
    login_data = {
        'username': 'admin',
        'password': 'admin123'
    }
    
    response = requests.post(f'{BASE_URL}/login', data=login_data)
    
    if response.status_code == 200:
        print("✓ 登录请求成功")
        
        # 检查响应内容
        if '登录成功' in response.text:
            print("✓ 登录验证通过")
            return True
        else:
            print("✗ 登录验证失败")
            return False
    else:
        print(f"✗ 登录请求失败，状态码: {response.status_code}")
        return False

# 测试获取用户列表
def test_get_users(session):
    print("\n测试获取用户列表...")
    
    response = session.get(f'{BASE_URL}/api/users')
    
    if response.status_code == 200:
        print("✓ 获取用户列表请求成功")
        data = response.json()
        
        if data['code'] == 0:
            print(f"✓ 返回用户数: {len(data['data'])}")
            return True
        else:
            print(f"✗ 获取用户列表失败: {data['msg']}")
            return False
    else:
        print(f"✗ 获取用户列表请求失败，状态码: {response.status_code}")
        return False

# 测试获取角色列表
def test_get_roles(session):
    print("\n测试获取角色列表...")
    
    response = session.get(f'{BASE_URL}/api/roles')
    
    if response.status_code == 200:
        print("✓ 获取角色列表请求成功")
        data = response.json()
        
        if data['code'] == 0:
            print(f"✓ 返回角色数: {len(data['data'])}")
            return True
        else:
            print(f"✗ 获取角色列表失败: {data['msg']}")
            return False
    else:
        print(f"✗ 获取角色列表请求失败，状态码: {response.status_code}")
        return False

# 主测试函数
def main():
    print("=== 舆情系统功能测试 ===")
    
    # 创建会话
    session = requests.Session()
    
    # 测试登录
    if not test_login():
        print("登录测试失败，无法继续其他测试")
        return
    
    # 使用会话进行其他测试
    session.post(f'{BASE_URL}/login', data={'username': 'admin', 'password': 'admin123'})
    
    # 测试获取用户列表
    test_get_users(session)
    
    # 测试获取角色列表
    test_get_roles(session)
    
    print("\n=== 测试完成 ===")

if __name__ == '__main__':
    main()