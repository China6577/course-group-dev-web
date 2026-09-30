# course-group-dev-web

研究团队网站，使用 Vue 3、Django 5.2 和 MySQL 8。

## 仓库内容

只包含应用源码和配置。SQL 备份、数据库内容、真实环境变量、上传媒体、静态收集文件、构建产物、依赖目录和虚拟环境均不上传。页面联系邮箱、地址与部署域名已替换为占位内容，需要自行配置。

## 本地开发

后端使用 `course_group_api` 的独立 Python 3.12 环境。依赖通过该环境的解释器安装：

```powershell
cd course_group_api
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

参考 `course_group_api/.env.example` 设置当前终端的 `DB_HOST`、`DB_PORT`、`DB_NAME`、`DB_USER`、`DB_PASSWORD` 和 `DJANGO_SECRET_KEY` 环境变量。示例文件不会自动加载；真实配置不要提交。

先创建空的 MySQL 数据库，再初始化表结构并启动后端：

```powershell
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py runserver 127.0.0.1:9000
```

另开终端启动前端：

```powershell
cd course_group_vue
npm ci
$env:COURSE_GROUP_API_TARGET = 'http://127.0.0.1:9000'
npm run serve -- --host 127.0.0.1 --port 9001
```

访问 `http://127.0.0.1:9001/`。9000 和 9001 用于避开本机 Windows 保留的默认端口范围。

可通过 `manage.py createsuperuser` 创建自己的管理员并录入内容。仓库不包含现有用户、密码、成员信息或数据库备份。

## Docker 配置

现有 `docker-compose.yml` 引用了未提交的私有环境文件，也保留了原有资源名称。使用前须自行准备配置，并按项目命名要求统一为 `course-group-dev-web`，检查已有数据卷的迁移方式。上传操作没有修改这些外部资源标识，也没有启动容器。
