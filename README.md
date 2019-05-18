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
* python版本:3.6.5
* scrapy版本:1.6.0
## 运行
`scrapy run bqb`