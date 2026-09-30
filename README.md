# course-group-dev-web

## 基本介绍

课题组展示与内容管理网站，使用 Vue 3、Django 5.2 和 MySQL 8，支持桌面和移动端访问。

## 如何使用

准备 Python 3.12、Node.js 和 MySQL 8，然后克隆项目：

```powershell
git clone git@github.com:China6577/course-group-dev-web.git
cd course-group-dev-web
```

### 启动后端

在 MySQL 中创建空数据库 `course_group_db`。参考 `course_group_api/.env.example`，在当前终端设置数据库连接环境变量和 `DJANGO_SECRET_KEY`；该文件不会自动加载。

```powershell
cd course_group_api
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py createsuperuser
.\.venv\Scripts\python.exe manage.py runserver 127.0.0.1:8000
```

已有 `.venv` 时直接复用，跳过创建环境。访问 `http://127.0.0.1:8000/admin/`，使用创建的管理员账号录入内容。

### 启动前端

另开终端，在项目根目录执行：

```powershell
cd course_group_vue
npm ci
npm run serve -- --host 127.0.0.1 --port 8080
```

访问 `http://127.0.0.1:8080/`。前端默认连接 8000 端口的后端。

## 具体功能

- 课题组介绍：展示团队简介和主要研究领域。
- 研究方向：展示研究领域及详细介绍。
- 团队成员：按成员类别展示，查看个人资料及毕业去向。
- 学术成果：按论文类型、年份和关键词筛选，查看摘要、论文链接和 BibTeX 引用。
- 合作伙伴：展示合作机构介绍和网站链接。
- 加入我们：展示招募说明和联系信息，可修改页面中的占位邮箱与地址。
- 后台管理：管理研究方向、成员、论文和合作伙伴，设置展示顺序。
