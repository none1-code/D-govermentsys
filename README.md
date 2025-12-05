# 政企智能舆情分析报告生成智能体应用系统

## 项目介绍
本项目是一个基于人工智能技术的政企智能舆情分析报告生成系统，旨在帮助政府和企业实时监控、分析和管理网络舆情信息，自动生成专业的舆情分析报告。

## 功能特点

### 核心功能
- **舆情数据抓取**：自动从各类网络平台抓取相关舆情信息
- **数据分析处理**：运用NLP技术进行情感分析、关键词提取等
- **报告自动生成**：根据分析结果生成结构化的舆情分析报告
- **用户权限管理**：支持多角色用户管理和权限控制
- **实时监控预警**：对敏感舆情进行实时监控和预警

### 辅助功能
- **数据可视化**：通过图表直观展示舆情分析结果
- **历史数据查询**：支持按时间、关键词等条件查询历史舆情
- **系统设置**：提供灵活的系统配置选项
- **日志管理**：记录系统操作日志，便于排查问题

## 技术栈

### 后端技术
- **Flask**：Python Web框架
- **SQLAlchemy**：ORM数据库框架
- **SQLite**：轻量级数据库
- **Beautiful Soup**：网页解析工具
- **NLTK/Stanford NLP**：自然语言处理

### 前端技术
- **HTML5/CSS3**：页面结构和样式
- **JavaScript**：交互逻辑
- **Layui**：UI框架
- **ECharts**：数据可视化

### 开发工具
- **PyCharm**：Python IDE
- **Git**：版本控制
- **Postman**：API测试

## 项目结构

```
├── app/                     # 主应用目录
│   ├── __init__.py          # 应用初始化
│   ├── modules/             # 核心模块
│   │   ├── __init__.py
│   │   ├── config.py        # 模块配置
│   │   ├── db.py            # 数据库连接
│   │   ├── init_data.py     # 初始化数据
│   │   ├── models.py        # 数据模型
│   │   ├── scraper.py       # 舆情抓取器
│   │   └── views.py         # 视图函数
│   ├── static/              # 静态资源
│   │   ├── css/             # 样式文件
│   │   ├── images/          # 图片资源
│   │   ├── js/              # JavaScript文件
│   │   └── layui/           # Layui框架
│   ├── templates/           # 模板文件
│   │   ├── base.html        # 基础模板
│   │   ├── data_scraper.html# 数据抓取页面
│   │   ├── index.html       # 首页
│   │   ├── login.html       # 登录页面
│   │   └── ...              # 其他页面模板
│   └── views/               # 视图目录
│       └── views.py         # 额外视图函数
├── backup_20241204/         # 备份目录
├── config/                  # 系统配置
│   └── config.py            # 全局配置
├── logs/                    # 日志目录
├── venv/                    # 虚拟环境
├── data.db                  # SQLite数据库文件
├── requirements.txt         # 依赖列表
├── run.py                   # 应用启动文件
└── README.md                # 项目说明文档
```

## 安装步骤

### 1. 环境准备
- Python 3.7+
- pip包管理器

### 2. 克隆项目
```bash
git clone <repository-url>
cd 舆情系统
```

### 3. 创建虚拟环境
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 4. 安装依赖
```bash
pip install -r requirements.txt
```

### 5. 配置数据库
```bash
# 初始化数据库
python -c "from app.modules.init_data import init_db; init_db()"
```

### 6. 启动应用
```bash
python run.py
```

应用将在 http://127.0.0.1:5000 启动

## 使用方法

### 1. 登录系统
- 访问 http://127.0.0.1:5000
- 输入用户名和密码登录（默认管理员账户：admin/admin123）

### 2. 主要功能使用

#### 舆情数据抓取
1. 进入"数据抓取"页面
2. 设置抓取关键词、时间范围等参数
3. 点击"开始抓取"按钮
4. 等待抓取完成，查看抓取结果

#### 数据分析
1. 进入"数据分析"页面
2. 选择要分析的数据范围
3. 选择分析类型（情感分析、关键词提取等）
4. 查看分析结果和可视化图表

#### 报告生成
1. 进入"报告生成"页面
2. 选择报告模板和数据来源
3. 设置报告参数
4. 点击"生成报告"按钮
5. 下载或在线查看生成的报告

#### 用户管理
1. 进入"用户管理"页面（需管理员权限）
2. 可添加、编辑、删除用户
3. 设置用户角色和权限

## 主要模块说明

### 1. 舆情抓取模块 (scraper.py)
- 支持多种数据源的舆情信息抓取
- 实现了网页内容解析和数据提取
- 支持定时抓取和增量抓取

### 2. 数据分析模块
- 基于NLP技术的情感分析
- 关键词提取和主题分析
- 数据统计和趋势分析

### 3. 报告生成模块
- 支持多种报告模板
- 自动填充分析数据
- 生成可下载的PDF/Word报告

### 4. 用户权限模块
- 基于角色的权限控制
- 支持多级用户管理
- 实现了用户登录认证和会话管理

## 配置说明

### 主要配置文件
- `config/config.py`：全局配置
- `app/modules/config.py`：模块配置

### 关键配置项
```python
# 数据库配置
SQLALCHEMY_DATABASE_URI = 'sqlite:///../data.db'

# 应用配置
SECRET_KEY = 'your_secret_key_here'
DEBUG = True

# 会话配置
PERMANENT_SESSION_LIFETIME = timedelta(days=7)
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = False  # 生产环境应设为True

# 日志配置
LOG_LEVEL = 'INFO'
LOG_FILE = '../logs/app.log'
```

## 开发说明

### 代码规范
- 遵循PEP 8编码规范
- 使用文档字符串注释关键函数和类
- 保持代码模块化和可维护性

### 开发流程
1. 创建分支进行功能开发
2. 编写单元测试
3. 提交代码并创建Pull Request
4. 代码审查和合并

### 调试模式
```bash
# 开启调试模式
DEBUG = True
```

## 测试说明

### 运行测试
```bash
# 运行所有测试
python -m pytest

# 运行特定测试
python -m pytest test_scraper.py
```

### 主要测试文件
- `test_scraper.py`：舆情抓取测试
- `test_login_api.py`：登录API测试
- `test_navigation.py`：导航功能测试
- `test_frontend_ajax.py`：前端AJAX测试

## 注意事项

1. **生产环境配置**
   - 将`DEBUG`设置为`False`
   - 设置强密码的`SECRET_KEY`
   - 将`SESSION_COOKIE_SECURE`设置为`True`
   - 配置合适的日志级别和路径

2. **数据安全**
   - 定期备份数据库
   - 保护敏感数据，避免明文存储
   - 配置合适的访问控制

3. **性能优化**
   - 对于大规模数据抓取，考虑使用异步任务
   - 优化数据库查询，添加适当的索引
   - 考虑使用缓存机制提高性能

## 许可证

本项目采用MIT许可证，详情请见LICENSE文件。

## 联系方式

如有问题或建议，请联系项目负责人。

---

**版本说明**：
- v1.0.0：初始版本，实现基本功能
- v1.1.0：优化舆情抓取功能，增加数据可视化
- v1.2.0：完善报告生成模块，支持多种报告格式

**更新时间**：2024年12月4日