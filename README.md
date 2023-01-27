# Minecraft_TextutrePack_Resolution_Converter
A resolution converter for Minecraft texture pack.\
一个用于转换Minecraft材质包分辨率的工具

*NOTE: This MarkDown file is Chinese and English mixed / 这个MarkDown文档是中英混合的*\
**If any part of this MarkDown file was translated incorrectly, plase tell me by creating an [issues](https://github.com/HarcicYang/Minecraft_TextutrePack_Resolution_Converter/issues)** 

## For developers / 开发者:
To pack the program with [pyinstaller](https://github.com/pyinstaller/pyinstaller) / 您可以使用 [pyinstaller](https://github.com/pyinstaller/pyinstaller)打包程序:\
`pyinstaller debug.spec` or / 或`pyinstaller release.spec` 
##### Python environment / Python环境需要：
- Python 3
- PyQt5 == 5.15.7 (PyQt5-sip == 12.11.0)
- Tkinter
- os
- sys
- zipfile
- shutil
- pywin32
- atexit

## For users / 普通用户:
You can download the program in [release](https://github.com/HarcicYang/Minecraft_TextutrePack_Resolution_Converter/releases/tag/1.0). / 您可以在[release](https://github.com/HarcicYang/Minecraft_TextutrePack_Resolution_Converter/releases/tag/1.0)中下载程序。
## Useage / 用法:
1. Choose a texture pack / 选择一个材质包(资源包);
2. Wait the program to prepare the files / 等待程序准备文件；
3. Set the out put options / 设置输出选项；
4. Click "start" / 点击“开始”.

## FAQ
#### Q: Can CTM and PBR work after converting?
####   转换后CTM纹理和PBR能正常工作吗?
#### A: Yes.
####   转换后仍然可以正常工作。
#### Q: Can this help my poor computer get better performance while I playing Minecraft?
####   它可以帮助我的破电脑在游玩Minecraft获得更好的性能吗？
#### A: Yes, but just a little (for some texture packs), it may because of the CTM and the POM.
####   可以，但是（对于部分材质包）帮助很有限， 这可能是一些材质包使用了CTM连接纹理和POM导致的。
