# -*- coding: utf-8 -*-
# @Department: 测试
# @Author: 杨凤娇
# @Description:
from PIL import Image
import pytesseract
from selenium import webdriver
import time


class VerficationCode:
    def __init__(self):
        self.driver = webdriver.Chrome("D:\webdriver\chromedriver.exe")
        self.driver.maximize_window()
        self.find_element = self.driver.find_element_by_css_selector

    def get_picture(self):
        self.driver.get("https://www.i21st.cn/story/index_1.html")
        time.sleep(1)
        self.driver.save_screenshot("D:/RF/img/org.png")
        page_snap_obj = Image.open("D:/RF/img/org.png")
        img = self.find_element('body > center:nth-child(4) > table > tbody > tr > td.border1 > div:nth-child(1) > '
                                'div.introduction.txt-12 > div.ft-family.ft-red > a > h1')
        time.sleep(1)
        location = img.location
        print(location)
        size = img.size
        # 电脑设置的显示比例为125%，location获取坐标按100%得到坐标，因此需要将得到的四个参数乘以缩放比例
        # 也可直接修改电脑显示比例   win10缩放比例修改：桌面右键 - 显示设置 - 缩放与布局 - 100%
        k = 1.25
        left = location["x"]*k
        top = location["y"]*k
        right = left + size["width"]*k
        bottom = top + size["height"]*k
        image_obj = page_snap_obj.crop((left, top, right, bottom))
        image_obj.show()
        t1 = time.strftime("%Y%m%d", time.localtime(time.time()))
        path = "D:/RF/img/"
        image_obj.save(path + t1 + "_" + ".png")
        self.driver.close()
        return image_obj

    def text(self):
        img = self.get_picture()
        con = pytesseract.image_to_string(img)
        print(con)


if __name__ == "__main__":
    t = VerficationCode()
    t.text()
