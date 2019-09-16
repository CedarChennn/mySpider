# myspider
## 生成crawlspider的
scrapy genspider -t crawl cbirc cbirc.gov.cn
## 创建项目
创建一个scrapy项目
scrapy startproject mySpider

生成一个爬虫
scrapy genspider itcast "itcast.cn”

提取数据
完善spider，使用xpath等方法

保存数据
pipeline中保存数据

命令：scrapy startproject +<项目名字>
	   scrapy startproject myspider
![img](./img/001_project_tree.png)

## 完善spider
![img](./img/002_完善_01.png)
![img](./img/003_完善_02.png)

## spider的数据传到pipeline
![img](./img/004.png)

## 使用pipline
完成pipline代码后需要在setting中开启

## 简单设置log
为了让我们自己希望输出到终端的内容能容易看一些：
	我们可以在setting中设置log级别
	在setting中添加一行（全部大写）：LOG_LEVEL = "WARNING”
	默认终端显示的是debug级别的log信息
## 实现翻页请求
scrapy.Request(next_page_url,callback=self.parse)
scrapy.Request能够构建一个request，同事指定提取数据的callback函数
scrapy.Request常用参数：
	callback:指定传入的url交给那个解析函数去处理
	meta:实现在不同的解析函数中传递数据，mata默认会带携带部分信息，比如下载延迟，请求深度等
	dont_filter:默认url会经过allow_domain过滤。如果dont_filter设置为true，则当前地址不会被过滤
