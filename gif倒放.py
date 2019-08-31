import imageio
import os
from PIL import Image, ImageSequence, ImageDraw
from os import startfile, path
import tkinter
# import tkinter.font as tkFont  # # 引入字体模块
from tkinter import filedialog
from tkinter.filedialog import askdirectory
import re

# os.open(r'D:\file\下载\DouYinPhotoToHTML.bkill.com\抖音图片转代码工具 v2.0免费版')
# gif图就是动态图，它的原理和视频有点类似，也是通过很多静态图片合成的
# 利用Python快速合成gif图，主要利用Python的第三方库imageio

flie_name = ''


class Video(object):
    def __init__(self, path):
        self.path = path

    def play(self):
        # Python标准库os中的方法startfile（)可以用来打开外部程序或文件，系统会自动关联相应的程序来打开
        startfile(self.path)


class Movie_MP4(Video):
    type = 'MP4'


root = tkinter.Tk()
root.geometry('500x300')  # 指定窗口大小

root.resizable(0, 0)  # 进制最大化
root.title('gif处理小工具')
# ft1 = tkinter.font.Font(size=20, weight='bold')
s = tkinter.StringVar()
path = tkinter.StringVar()


# 打开文件对话框路径
def open_path():
    global flie_name
    default_dir = r"C:\Users\lenovo\Desktop"  # 设置默认打开目录
    flie_name = filedialog.askopenfilename(
        title=u"选择文件", initialdir=(
            os.path.expanduser(default_dir)))
    print(flie_name)
    # return entry1['text'] = flie_name
    s.set(flie_name)
    return s.get()


# #绑定entry内容
# def rtnkey(event=None):
#     print(e.get())

# 打开文件目录
def selectPath():
    global path_
    path_ = askdirectory()

    path.set(path_)
    return path.get()

    # 开始处理图片


def img_begin():
    global flie_name, path_

    im = Image.open(flie_name)  # 选择图片
    print('over,请打开相对应的文件夹查看...')

    # gif图片流的迭代器
    iter = ImageSequence.Iterator(im)
    index = 1
    for frame in iter:

        # print每一帧图片的一些信息
        # print("image %d:size %s" % (index, frame.size))

        # 若保存的路径不存在，则创建文件夹
        path = "imgs"
        if path not in os.listdir():
            os.makedirs(path)

        frame.save("{}/imgs {}.png".format(path_, index))  # 将每一帧图片命名为imgs开头的文件
        index += 1
    # 将gif拆分成图片流
    imgs = [frame.copy() for frame in ImageSequence.Iterator(im)]

    # 将图片流反序
    imgs.reverse()

    # 将反序后的图片流保存并输出
    imgs[0].save("{}/out1111.gif".format(path_),
                 save_all=True, append_images=imgs[1:])
    # 输出路径


# img_begin()

# tk布局
def tk_home():
    tkinter.Label(root, text='源 gif 图像：').place(relx=0.05, rely=0.2)     #label1 =
    tkinter.Label(root, text='输出目录：').place(relx=0.05, rely=0.4)     #label2 =
    tkinter.Label(root, text='——' * 17).place(relx=0.05, rely=0.5)     #label3 =

    entry1 = tkinter.Entry(
        root,
        width=30,
        validate='key',
        textvariable=s).place(
        relx=0.25,
        rely=0.2)
    entry2 = tkinter.Entry(
        root, width=30, textvariable=path).place(
        relx=0.25, rely=0.4)

    button1 = tkinter.Button(
        root, text='确定', command=img_begin).place(
        relx=0.3, rely=0.6)
    button2 = tkinter.Button(
        root, text='退出', command=root.quit).place(
        relx=0.6, rely=0.6)
    button3 = tkinter.Button(
        root,
        text='选择图片',
        command=open_path).place(
        relx=0.78,
        rely=0.2)
    button4 = tkinter.Button(
        root,
        text='选择保存地址',
        command=selectPath).place(
        relx=0.78,
        rely=0.4)

    button_over = tkinter.Button(
        root, text='打开目的文件夹').place(
        relx=0.7, rely=0.8)


tk_home()

root.mainloop()
