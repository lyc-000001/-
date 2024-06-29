#### 介绍+UI自动化

python+pytest+playwright

#### 软件架构

python语言,pytest+playwright测试框架,pom页面对象模型封装。

pytest简介：

playwright简介:

#### 安装教程

1. python 3.8
2. pip install -r requirements.txt

#### 架构组成

1. 执行runner.py运行，会自动收集测试用例
2. BasePage：封装playwright的基础方法
3. BuildInLibrary：环境变量存放文件夹，可进行用例参数关联
4. Common：存放公共方法抽离文件夹
5. Config：配置文件存放文件夹
6. TestLog：存放运行日志
7. Pages：存放页面对象文件
8. TestCases：存放测试用例
9. TestDatas：存放测试数据


### 脚本录制

1. playwright录制命令简介
   python -m playwright codegen -o 'Test_Demo.py' --target python -b
   chromium https://www.pre.webullbroker.com/ko-builder/1688104531632-997e68
2. o或–output 指定保存脚本的文件路径及文件名
   target 指定生成脚本的语言：Python、JavaScript、C#
   b 指定录制使用的浏览器：如：-b chromium（Chrome浏览器）、-b firefox、-b webkit三种

### 环境配置

pip freeze >requirements.txt
pip install -r requirements.txt

### allure测试报告生成
trace.zip查看：
1、playwright show-trace trace.zip
2、访问   https://trace.playwright.dev/     把文件拖入即可查看


allure generate ./TestReport/result/ -o ./TestReport/AllureReport/ --clean