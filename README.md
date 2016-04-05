# app-scripts
---- 

详细介绍可参考我的博客 -- [开发NB-App中使用的脚本们](http://ifujun.com/kai-fa-nb-appzhong-shi-yong-de-jiao-ben-men/)。

## What is this?
---- 
这些是我在途牛开发NB-App中使用到的一些脚本，其中包括：

- diff\_project.py - 用于对比单个project中的多个target的脚本。
- gen\_zh.py - 从`Localizable.strings (English)`上自动生成`Localizable.strings (Chinese)`的脚本。
- cal\_code.py - 计算工程总代码量和有效代码量的脚本。
- cal\_svn\_commit.py - 统计SVN commit行数的脚本,自动diff并统计commit增删代码量。
- jsonserver.py - 用于代理并返回静态json的脚本，基于`web.py`，主要用于自我调试。

## How to use it?
---- 
### diff\_project.py

参照demo,将脚本添加到工程中：

	Target -> Build Phases -> New Run Script Phase

在输入框中填写为：

	python 路径+diff_project.py

例如:

	python ./Scripts/diff_project.py

在每次编译后，输出结果会出现在这里:

![image](https://raw.githubusercontent.com/Forkong/app-scripts/master/Screenshots/blogimage_script_diff_location.png)

点击对应的Build,可以看到输出结果:

![image](https://raw.githubusercontent.com/Forkong/app-scripts/master/Screenshots/blogimage_script_diff_result.png)

### gen\_zh.py

使用过程和`diff_project.py`基本一致，依然在Build中查看输出结果：

![image](https://raw.githubusercontent.com/Forkong/app-scripts/master/Screenshots/blogimage_script_gen_zh.png)

只是这个脚本需要使用`PyObjc`框架，需要提前安装一下，建议使用`pip`安装:

	pip install pyobjc
	
如果没有安装`pip`的话，可以去[官网](https://pip.pypa.io/en/stable/)安装一下。

由于我们无法要求每个Mac都安装有`pyobjc`库，所以我们必须通过其他办法来让别人也可以运行，比如：

- [virtualenv](https://github.com/pypa/virtualenv)(python 虚拟机)
- [PyInstaller](https://github.com/pyinstaller/pyinstaller)(打包成可执行文件)
- 其他

具体可参考开头博客的文章。

### cal\_code.py

demo中将此脚本直接添加于`Build Phases`中，是为了方便演示，而实际上我们一般很少需要统计代码量，所以只需要在适当的时候在终端中运行即可。

	//使用方式
	python cal_code.py (+ 目录)
	python cal_code.py 
	python cal_code.py ../
	
在终端中输出结果一般如下：

![image](https://raw.githubusercontent.com/Forkong/app-scripts/master/Screenshots/blogimage_script_code.png)

### cal\_svn\_commit.py  

由于SVN的特殊性，必须要在线连接到SVN服务器，否则无法统计。

    //使用方式
    python cal_svn_commit.py (+ 目录) (+ 统计版本个数)
    python cal_svn_commit.py
    python cal_svn_commit.py ./ 5

原理是读取目录的`svn log`,从log上获取版本号，之后使用`svn diff`命令diff版本差异，再从输出的log上统计增删的代码量，之后汇总输出。结果类似于下图：

![image](https://raw.githubusercontent.com/Forkong/app-scripts/master/Screenshots/blogimage_script_svn.png)

### jsonserver.py

`jsonserver.py`依托于[web.py](http://webpy.org/)框架，在使用此脚本之前，必须安装web.py框架:

    pip install web.py
    
`web.py`使用起来非常方便，入门又非常简单，非常适合我们这种使用场景。

现在业界比较流行的微web框架是`Flask`,`Flask`的用户量很大，开源的三方更多，如果你要做小型网站的话，`Flask`还是非常适合的。

运行方式:
	
	python jsonserver.py (+ 端口号，默认为8080)
	python jsonserver.py 
	python jsonserver.py 1234

`jsonserver`中的	`static`文件夹保存的是静态资源，只需要将返回的静态json放置于`static`文件夹中，在代码中直接返回即可。

如果对于`web.py`有疑问的，可以直接去官网查看官方文档，官方提供中文版支持。一般来说，看完基础文档也就只要半个小时、一个小时，速度很快。这也体现了这个框架的简洁、高效、轻量级。	

成功之后，将手机连到电脑ip上即可。

## License
---- 
MIT.