from app.modules.scraper import SogouScraper

# 创建抓取实例
scraper = SogouScraper()

# 执行搜索
result = scraper.search('宜宾', 1)

# 打印结果
print("=== 直接测试抓取模块 ===")
print(f"成功: {result.get('success')}")

if result.get('success'):
    print(f"关键字: {result.get('keyword')}")
    print(f"页码: {result.get('page')}")
    print(f"结果数量: {len(result.get('data', []))}")
    
    # 打印第一条结果
    if result.get('data'):
        print("\n第一条结果:")
        first_item = result['data'][0]
        print(f"标题: {first_item.get('title')}")
        print(f"来源: {first_item.get('source')}")
        print(f"URL: {first_item.get('original_url')}")
        print(f"概要: {first_item.get('summary')[:100]}...")
        print(f"封面: {first_item.get('cover')}")
else:
    print(f"错误: {result.get('error')}")