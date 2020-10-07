# Flask 网站项目实践

## 初始内容

* 这个 README
* `data.py` 网站原始数据，后面会用到
* `.gitignore` git忽略文件，不用管。

## 课程步骤

### 第一部分——你好，世界

* 创建项目文件夹
* 初始化虚拟环境
* 激活虚拟环境
* 安装flask
* 新建 `app` 文件夹
* 在 `app` 文件夹里创建 `__init__.py`
* 在 `__init__.py` 里：
  * 导入 Flask
  * 创建 app
  * 导入路由
* 在 `app` 文件里创建 `route.py`
  * 里边写一个 `index` 函数，让它在路由到 `/` 或者 `/index` 的时候，返回 `Hello, World`。
* 在根目录创建总入口文件 `poetry.py`
* 在里边导入`app`
* 设置 FLAKSK_APP 环境变量为 `poetry.py`
* 命令行启动 Flask 应用

设置：

* 安装 python-dotenv
* 根目录创建 `.flaskenv` 文件，在里边设置环境变量 `FLAKSK_APP`

### 第二部分——模板设置

* 修改 `index` 函数，让它返回HTML（可以是不完整的HTML页面）
* 重启 Flask 应用，刷新浏览器检查
* 修改 `index` 函数，让它返回带变量的字符串 `f"Hello, {user['name']}"`
* 重启 Flask 应用，刷新检查
* 修改 `.flaskenv` 文件，加上 `FLASK_ENV=development`
* `app` 下创建 `templates/index.html`,里边包含
  * html -> head -> title (title 为变量)
  * ... -> body -> h1 -> Hello, {{user.name}}
* 修改 `index` 函数
  * 创建一个 `user` 变量，字典
  * 导入 `render_template`
  * 使用 `render_template`，参数为 title 和 user

模板进阶

* 修改模板，让它里边包含条件语句 if, else, endif
  * 以 title 为修改对象
  * 在 `index` 函数里传入或者不传入 title，看浏览器结果
* 修改模板，让它里边包含 for endfor
  * 在 `index` 函数里创建一个数组，里边包含之前爬到的诗
  * 把 `data.py` 里的诗传入模板，看浏览器结果
* 创建 `base.html`，里边包含基础架构，以及 block, endblock (content)
* 简化 `index.html`:
  * 让它扩展 `base.html`，extends
  * 创建 block (content), endblock，中间是 for 循环
  * 检查结果

## 第三部分——表单处理

* 安装 flask-wtf
* 配置密钥
  * 在根目录创建 `config.py`
  * 里边写一个 `Config` 类
  * 加一个类属性叫 `SECRET_KEY`，让它从环境变量获取同名变量，或者设为固定值
  * 在 `__init__.py` 里导入 `Config`，使用 `app.config.from_object`
* 在 app 下创建添加诗的表单 `forms.py`
  * 导入 form 相关的库
  * 创建 Poem form类，包含 title, poem, poet 三个属性
  * 其中 poet 来自data.py，为 key, name 格式显示
* 在routers.py里创建 `add_poem` 函数，让它把诗歌加到假数据库里边
  * route是 add_poem，方法是 get 和 post
  * 初始化 form
  * 若是 form 有验证提交，则把数据加进来
  * 发信息到UI（flash)
  * 跳转到主页
  * 正常将form传给render_template
* 创建模板文件
  * form，空action，方法为post，默认不验证
  * 加 form.hidden_tag()
  * 加三个栏位
  * 添加提交按钮
  * 为每个栏位添加正确性验证
* 打开 add_poem 页面，看是不是能用

### 第四部分——数据库

* 安装依赖 flask-sqlalchemy flask-migrate
* 在 config 里配置数据库
  * SQLALCHEMY_DATABASE_URI，配置到根目录 app.db
  * SQLALCHEMY_TRACK_MODIFICATIONS = False
* 修改 `__init__.py`：
  * 导入安装的库
  * 初始化 db 和 migrate
  * 从 app 导出 models
* 在 app 下添加 models.py
  * 从 app 导入 db
  * 创建 Poem 和 Poet 两个类，参考 data.py 里的格式
  * id是主键，列可以加索引
  * 注意 poet_id 是外键，另外 Poet 可以有 poems 关联属性
  * 添加 `__repr__` 函数
* 数据库更新
  * `flask db init`
  * `flask db migrate -m "poems and poets"`
  * `flask db upgrade` 创建表
* 修改 `poetic.py` 将数据库暴露给 flask shell
  * 导入 db 和 models
  * 创建 shell context，映射名称
  * 运行 flask shell，看映射是否存在
* 准备原始数据
  * 在 flash shell 里导入 data.py
  * 将 data.py 里的数据导入数据库（注意数据库索引从1开始）
  * 检查是否导入成功
* 修改 forms.py，让它从数据库读取诗人列表
* 修改 routes.py，让它读写数据库
* 测试应用是否工作正常
