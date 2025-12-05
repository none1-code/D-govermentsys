from app.modules.scraper import SogouScraper

# 创建抓取实例
scraper = SogouScraper()

# 执行搜索
result = scraper.search('宜宾', 1)

# 打印结果
print("=== 测试关键字'宜宾'的抓取结果 ===")
print(f"成功: {result.get('success')}")

if result.get('success'):
    print(f"关键字: {result.get('keyword')}")
    print(f"页码: {result.get('page')}")
    print(f"结果数量: {len(result.get('data', []))}")
    
    # 打印前5条结果
    print("\n前5条结果:")
    for i, item in enumerate(result.get('data', [])[:5], 1):
        print(f"\n第{i}条:")
        print(f"标题: {item.get('title')}")
        print(f"来源: {item.get('source')}")
        print(f"URL: {item.get('original_url')}")
        print(f"概要: {item.get('summary', '无')[:100]}...")
        print(f"封面: {item.get('cover', '无')}")
else:
    print(f"错误: {result.get('error')}")