from os.path import exists
import time
import requests
from bs4 import BeautifulSoup
from os import makedirs


def benzi():
    global p
    html = requests.get(url)
    html1 = BeautifulSoup(html.text, 'lxml')
    cha_divs = html1.find('div', {"class": "container"}).find_all('a')
    cha = html1.find('div', {"class": "container index-container"}).find_all('a')
    for q in range(0, len(cha_divs)):
        p = cha_divs[q].attrs['href']
        tick.append(p)
        image1 = cha[q].find_all('img')[0].attrs['alt']
        tick1.append(image1)
    p1 = input("请输入文件夹名称:")
    for o in range(0, len(tick1)):
        print(str(o+1)+":"+tick1[o])
    ces = int(input("请输入序号："))
    ces = ces - 1
    image("https://zh.doghentai.com/" + tick[ces] + "list/1/", p1)


def image(url1,p1):
    html = requests.get(url1)
    html1 = BeautifulSoup(html.text, 'lxml')
    yeshu = html1.find('span', {"class": "num-pages"}).text
    image = html1.find('section', {"class": "fit-horizontal full-height"}).find_all('a')
    ima = image[0].find_all("img")
    im = ima[0].attrs['src']
    shuzi = len(im)
    pic = im[0:shuzi - 5]
    mkdir(p1+"\\")
    print("获取完成，共计"+str(yeshu)+"张")
    print("准备开始下载")
    time.sleep(2)
    for w in range(0, int(yeshu)):
        pi = pic + str(w + 1) + ".jpg"
        print("第"+str(w+1)+"张下载完毕")
        p = requests.get(pi)
        open(p1+'\\' + str(w + 1) + '.png', 'wb').write(p.content)
    print("下载完毕")


def mkdir(path):
    if not exists(path):
        makedirs(path)

tick = []
tick1 = []
url1 = input("请输入需要的类型")
url1 = url1.replace(".", "-")
print("请稍后")
url = "https://zh.doghentai.com/character/" + url1 + "/"
benzi()
time.sleep(3)
