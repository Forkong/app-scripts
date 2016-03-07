# app-scripts
---- 

详细介绍可参考我的博客[开发NB-App中使用的脚本们](#)(http://ifujun.com/kai-fa-nb-appzhong-shi-yong-de-jiao-ben-men/)

## What is this?
---- 
这些是我写途牛开发NB-App中使用的系列脚本，其中包括：

- diff\_project.py - 用于对比单个project的多个target的脚本
- gen\_zh.py - 从`Localizable.strings (English)`上自动生成`Localizable.strings (Chinese)`的脚本
- cal\_code.py - 计算工程总代码量和有效代码量的脚本
- cal\_svn\_commit.py - SVN commit 行数统计脚本,自动diff并统计commit增删代码量（即将开源）
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

和`diff\_project.py`基本一致，只是这个脚本需要PyObjc框架，需要提前安装一下，建议使用pip安装:

	pip install pyobjc

由于我们无法要求每个mac都安装有`pyobjc`库，所以我们必须通过其他办法来让别人可以运行，比如：

- [virtualenv](https://github.com/pypa/virtualenv)(python 虚拟机)
- [PyInstaller](https://github.com/pyinstaller/pyinstaller)(打包成可执行文件)
- 其他

具体可参考开头博客的文章。

### cal\_code.py

demo中将此脚本直接添加于`Build Phases`中，是为了方便演示。而实际上我们一般很少统计代码量，所以只需要在适当时候在终端中运行即可。

	//使用方式
	python cal_code.py (+ 目录)
	python cal_code.py 
	python cal_code.py ../

### cal\_svn\_commit.py  

暂未开源。

### jsonserver.py

暂未开源。

## License
---- 
MIT.