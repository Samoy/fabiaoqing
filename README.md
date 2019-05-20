# 发表情爬虫

## **<font color='red'>注意(非常重要)</font>**:
为了避免上传敏感信息，将settings.py文件重命名为了settings.example.py，运行时需要将此文件重新改为settings.py，并修改其中的数据库信息:
```
MYSQL_HOST = '数据库地址'
MYSQL_DATABASE = '数据库名'
MYSQL_USER = '数据库用户名'
MYSQL_PASSWORD = '数据库密码'
MYSQL_PORT = '数据库端口号'
```
## 介绍
本项目使用scrapy框架爬取了[发表情](http://www.fabiaoqing.com)网站的表情包，并将所获取的数据存入了MySQL数据库。
## 系统要求
* python:3.6.5
* scrapy:1.6.0
* pymsql:0.9.3
* docker(可选)
## 运行及部署
1. ### 创建数据库
    database.sql文件是Mysql数据库创建文件，使用该文件创建数据可和表。
2. ### [修改文件](#注意非常重要)
    重命名settings.example.py文件为settings.py，并修改其中的数据库相关配置
3. ### 运行
    有两种运行方式，任选一种，首先需要进入项目根目录下
    >#### 直接运行
    第一步：`pip3 install -r requirements.txt`
    
    第二步: `scrapy run bqb`
    > #### 使用docker运行
    第一步:下载并安装Docker，关于Docker的使用在此不再赘述。
    
    第二步:`docker build bqb:1.0 .`
    
    第三步:`docker run bqb:1.0`

## TODO List
1. 防止重复爬取
2. 图片下载
3. 表情包制作