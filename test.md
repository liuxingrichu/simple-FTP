
服务器测试数据：
-------------------------------------------------------------------
2017-02-13 22:25:16.992743 Lucy 登陆！
2017-02-13 22:25:23.613122 Lucy 退出！
2017-02-13 22:25:32.279617 127.0.0.1 断开连接！
2017-02-13 22:25:55.120924 Tom 登陆！
2017-02-13 22:26:05.040491 Tom 异常退出！
======================================================================

客户端测试数据：

-------------------------------FTP客户端------------------------------
【1】登录 【2】上传文件 【3】下载文件 【4】查看文件列表 【5】退出
---------------------------------end----------------------------------
>>1
Enter username : Lucy
Enter password :123
	欢迎Lucy登陆
-------------------------------FTP客户端------------------------------
【1】登录 【2】上传文件 【3】下载文件 【4】查看文件列表 【5】退出
---------------------------------end----------------------------------
>>2
	请输入上传文件名称，例如test.txt
Enter upload file name : test2.txt
	文件上传成功！
-------------------------------FTP客户端------------------------------
【1】登录 【2】上传文件 【3】下载文件 【4】查看文件列表 【5】退出
---------------------------------end----------------------------------
>>2
	请输入上传文件名称，例如test.txt
Enter upload file name : test4.txt
	文件不存在
-------------------------------FTP客户端------------------------------
【1】登录 【2】上传文件 【3】下载文件 【4】查看文件列表 【5】退出
---------------------------------end----------------------------------
>>3
	请输入下载文件名称，例如test.txt
Enter download file name : test1.txt
	文件下载成功！
-------------------------------FTP客户端------------------------------
【1】登录 【2】上传文件 【3】下载文件 【4】查看文件列表 【5】退出
---------------------------------end----------------------------------
>>4
-------------文件列表-------------
test1.txt
test2.txt
test3.txt
---------------end---------------
-------------------------------FTP客户端------------------------------
【1】登录 【2】上传文件 【3】下载文件 【4】查看文件列表 【5】退出
---------------------------------end----------------------------------
>>5

Process finished with exit code 0

-------------------------------FTP客户端------------------------------
【1】登录 【2】上传文件 【3】下载文件 【4】查看文件列表 【5】退出
---------------------------------end----------------------------------
>>1
Enter username : Tom
Enter password :123456
	欢迎Tom登陆
-------------------------------FTP客户端------------------------------
【1】登录 【2】上传文件 【3】下载文件 【4】查看文件列表 【5】退出
---------------------------------end----------------------------------
>>2
	请输入上传文件名称，例如test.txt
Enter upload file name : test1.txt
	文件上传成功！
-------------------------------FTP客户端------------------------------
【1】登录 【2】上传文件 【3】下载文件 【4】查看文件列表 【5】退出
---------------------------------end----------------------------------
>>2
	请输入上传文件名称，例如test.txt
Enter upload file name : test2.txt
	文件上传成功！
-------------------------------FTP客户端------------------------------
【1】登录 【2】上传文件 【3】下载文件 【4】查看文件列表 【5】退出
---------------------------------end----------------------------------
>>3
	请输入下载文件名称，例如test.txt
Enter download file name : test1.txt
	文件下载成功！
-------------------------------FTP客户端------------------------------
【1】登录 【2】上传文件 【3】下载文件 【4】查看文件列表 【5】退出
---------------------------------end----------------------------------
>>4
-------------文件列表-------------
test1.txt
test2.txt
---------------end---------------
-------------------------------FTP客户端------------------------------
【1】登录 【2】上传文件 【3】下载文件 【4】查看文件列表 【5】退出
---------------------------------end----------------------------------
>>5

Process finished with exit code 0
