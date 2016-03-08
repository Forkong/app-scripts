# app-scripts
---- 

详细介绍可参考我的博客[开发NB-App中使用的脚本们](#)(http://ifujun.com/kai-fa-nb-appzhong-shi-yong-de-jiao-ben-men/)

## What is this?
---- 
这些是我在途牛开发NB-App中使用到的一些脚本，其中包括：

- diff\_project.py - 用于对比单个project中的多个target的脚本。
- gen\_zh.py - 从`Localizable.strings (English)`上自动生成`Localizable.strings (Chinese)`的脚本。
- cal\_code.py - 计算工程总代码量和有效代码量的脚本。
- cal\_svn\_commit.py - 统计SVN commit行数的脚本,自动diff并统计commit增删代码量。
- jsonserver.py - 用于代理并返回静态json的脚本，基于web.py，主要用于自我调试（即将开源）

## How to use it?
---- 
### diff\_project.py

参照demo,将脚本添加到工程中：

	Target -> Build Phases -> New Run Script Phase

在输入框中填写为：

	python 路径+diff_project.py

例如:

	python ./Scripts/diff_project.py

### gen\_zh.py

和`diff_project.py`基本一致，只是这个脚本需要使用PyObjc框架，需要提前安装一下，建议使用pip安装:

	pip install pyobjc
	
如果没有安装pip的话，可以去[官网](https://pip.pypa.io/en/stable/)安装一下。

由于我们无法要求每个mac都安装有`pyobjc`库，所以我们必须通过其他办法来让别人也可以运行，比如：

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

### cal\_svn\_commit.py  

由于SVN的特殊性，必须要在线连接到SVN服务器，否则无法统计。

    //使用方式
    python cal_svn_commit.py (+ 目录) (+ 统计版本个数)
    python cal_svn_commit.py
    python cal_svn_commit.py ./ 5

原理是读取目录的`svn log`,从log上获取版本号，之后使用`svn diff`命令diff版本差异，再从输出的log上统计增删的代码量，之后汇总输出。结果类似于下图：

![image](http://7i7i81.com1.z0.glb.clouddn.com/blogimage_script_5.png)

### jsonserver.py

暂未开源。

## License
---- 
MIT.