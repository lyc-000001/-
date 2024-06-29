# encoding=utf-8
import base64
import random
import time

import cv2
from Conf.config import Config


# 页面公共方法封装
class BasePage:
    def __init__(self, page):
        self.page = page

    # 预览发布
    def preview_release(self, edit_url, selector1, selector2):
        self.page.goto(edit_url)
        self.page.wait_for_timeout(3000)
        self.page.locator(
            '#root > div > div.ko-editor-top > div.right > div:nth-child(2) > div:nth-child(2) > div').click()
        self.page.wait_for_timeout(3000)
        try:
            element = self.wait_for_selector_(selector1)
            return element
        except Exception as e:
            print('元素位置改变,正在继续查找', e)
            element = self.wait_for_selector_(selector2)
            return element

    def open_url(self, url):
        """打开网页"""
        self.page.goto(url)

    def get_title(self):
        return self.page.title()

    def close_page(self):
        self.page.close()

    # 点击元素
    def click_button(self, element, exact=None):
        self.page.get_by_text(text=element, exact=exact).click()

    # 按照路径点击元素
    def click_element(self, element):
        self.page.locator(element).click()

    # 查找元素并返回值
    def select_element(self, element):
        result = self.page.query_selector(element)
        return result

    # 获取元素背景颜色
    def get_background_color(self, element):
        element = self.page.locator(element)
        color = element.evaluate('(element) => window.getComputedStyle(element).backgroundColor')
        return color

    # 获取元素颜色
    def get_color(self, element):
        element = self.page.locator(element)
        color = element.evaluate('(element) => window.getComputedStyle(element).color')
        return color

    # 获取图片的url
    def get_picture(self, element):
        img = self.page.query_selector(element)
        img_url = img.get_attribute('src') if img else None
        return img_url

    # 获取元素文本
    def get_text(self, element):
        element = self.page.locator(element)
        text = element.text_content()
        return text

    # 等待元素、等待某个元素出现
    def wait_for_selector_(self, element):
        el = self.page.wait_for_selector(element, state="visible")
        return el

    # 获取当前页面url
    def get_page_url(self):
        ret = self.page.url()
        return ret

    def waits(self):
        """延迟关闭页面，用例调试用"""
        self.page.wait_for_timeout(3000)

    # 登录滑块验证方法
    def random_name(self, length_=16):
        """
        生成一个指定长度的随机字符串
        """
        random_str = ''
        base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz'
        length = len(base_str) - 1
        for i in range(length_):
            random_str += base_str[random.randint(0, length)]
        return random_str

    def download_png(self, src_url):
        png_name = self.random_name()
        png_path = Config.test_img_dir + png_name + '.jpg'
        base64_image_data = src_url.split(",")[1]
        data = base64.b64decode(base64_image_data)
        with open(str(png_path), mode="wb+") as f:
            f.write(data)
            f.close()
        return png_path

    def get_notch_location(self, slider_img, backdrop_img):
        """
        根据文件进行识别
        :param slider_img: 滑块图片的文件路径
        :param backdrop_img: 背景图片的文件路径
        :return:
        """
        bg_img = cv2.imread(slider_img, 0)
        tp_img = cv2.imread(backdrop_img, 0)  # 读取到两个图片，进行灰值化处理

        # img = cv2.imread(backdrop_img)  # 读取图片画框直观可以看到，上边是灰度的所以重新打开一个原图

        res = cv2.matchTemplate(self._tran_canny(bg_img), self._tran_canny(tp_img), cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = max_loc[0]  # 横坐标
        # 展示圈出来的区域
        x, y = max_loc  # 获取x,y位置坐标
        w, h = bg_img.shape[::-1]  # 宽高
        # 矩形画图
        # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.rectangle(tp_img, (x, y), (x + w, y + h), (7, 249, 151), 2)
        # 显示
        # cv2.imshow('Show', name)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        # 这个是滑块要移动的距离
        return round(top_left / 2)

    def get_track(self, distance):  # distance为传入的总距离
        # 移动轨迹
        track = []
        # 当前位移
        current = 0
        # 减速阈值
        mid = distance * 4 / 5
        # 计算间隔
        t = 0.2
        # 初速度
        v = 1

        while current < distance:
            if current < mid:
                # 加速度为2
                a = 4
            else:
                # 加速度为-2
                a = -3
            v0 = v
            # 当前速度
            v = v0 + a * t
            # 移动距离
            move = v0 * t + 1 / 2 * a * t * t
            # 当前位移
            current += move
            # 加入轨迹
            track.append(round(move))
        return track

    def _tran_canny(self, image):
        """消除噪声"""
        image = cv2.GaussianBlur(image, (3, 3), 0)
        return cv2.Canny(image, 50, 150)

    def slider_validation(self, backdrop_img, slider_img, slider_button):
        """
        :param backdrop_img: 背景图位置
        :param slider_img: 滑块图片位置
        :param slider_button: 滑动条按钮
        :return:
        """
        backdrop_src = self.page.get_attribute(backdrop_img, name='src')
        slider_src = self.page.get_attribute(slider_img, name='src')
        slider_path = self.download_png(slider_src)
        backdrop_path = self.download_png(backdrop_src)

        top_left = self.get_notch_location(slider_path, backdrop_path)

        slider_element = self.page.wait_for_selector(slider_button, strict=True)  # 根据实际情况指定滑块元素的选择器
        box = slider_element.bounding_box()
        self.page.mouse.move(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)
        self.page.mouse.down()
        x = box["x"] + box["width"] / 2
        y = box["y"] + box["height"] / 2

        tracks = self.get_track(top_left)

        m = 1
        for track in tracks:
            # 循环鼠标按照轨迹移动
            # strps 是控制单次移动速度的比例是1/10 默认是1 相当于 传入的这个距离不管多远0.1秒钟移动完 越大越慢
            self.page.mouse.move(x + track, y, steps=10)
            m += 1
            x += track
        # 移动结束鼠标抬起
        time.sleep(1)
        self.page.mouse.up()
        print('等待调试')
        time.sleep(6)
