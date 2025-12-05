import sqlite3

# 连接到数据库
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# 获取所有表名
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("数据库中的表:")
for table in tables:
    print(f"- {table[0]}")
    
    # 获取表结构
    cursor.execute(f"PRAGMA table_info({table[0]});")
    columns = cursor.fetchall()
    print("  表结构:")
    for column in columns:
        print(f"    - {column[1]} ({column[2]})")
    
    print()

# 关闭连接
conn.close()