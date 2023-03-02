import time 
import maskapi

class Tiktok:
    postList = []
    #点开发布视频
    def startVideo(self,d):
        m = maskapi.MaskAPI()
        self.postList = m.getPostContent()

        for post in self.postList:
            self.recordNewVideo(d)
            self.createVideo(d)
            self.setVideoContent(d,post)
            self.setPostContent(d,post)


    def recordNewVideo(self,d):
        d.click(556,2148)
        time.sleep(2)

    #创建视频
    def createVideo(self,d):
        print("长按录制视频")
        d.long_click(556,1802,6)
        time.sleep(2)

        print("点击确定")
        d.click(965,1829)
        time.sleep(2)

    #设置视频内容
    def setVideoContent(self,d,post):
        print("点击添加文案")
        d(text="Text").click()
        time.sleep(2)

        print("点击设置剪贴板")
        d.set_clipboard(post['video_content'], 'label')
        time.sleep(2)
        print("粘贴内容")
        d.long_click(535,680,2)
        time.sleep(1)
        d.click(500,500)

        print("切换样式")
        d.click(80,1115)
        time.sleep(2)

        print("点击确定")
        d(text="Done").click()
        time.sleep(2)

        print("点击确定")
        d(text="Add sound").click()
        time.sleep(2)

        print("点击搜索音乐")
        d.click(1000,1200)
        time.sleep(10)

        print("点击收藏音乐")
        tmp = d(text="Favorites")
        tmp.click()
        y = 0
        if tmp != None:
            y = tmp.info['bounds']['right']

        if abs(y-750) > 100:
            print("选择第一个音乐")
            d.click(400, 1100)
            time.sleep(1)
        
            print("选择音乐")
            d.click(950, 1100)
            time.sleep(5)
        else:
            print("选择第一个音乐")
            d.click(400, 950)
            time.sleep(1)
        
            print("选择音乐")
            d.click(950, 950)
            time.sleep(5)

        print("落下弹窗")
        d.click(100, 1000)
        time.sleep(5)

        print("点击确定")
        d(text="Next").click()
        time.sleep(2)

    #设置发布页内容
    def setPostContent(self,d,post):
        print("点击输入文案")
        d.click(100,300)
        time.sleep(2)

        print("敲个空格")
        d.click(530, 2070)
        time.sleep(2)

        print("点击设置剪贴板")
        d.set_clipboard(post['post_content'], 'label')
        time.sleep(2)
        print("粘贴内容")
        d.long_click(100,300,2)
        time.sleep(1)
        d.click(150,170)
        
        print("敲个空格")
        d.click(530, 2070)
        time.sleep(2)

        for product in post['product_list']:
            print("点击收回键盘")
            d.click(180, 2226)
            time.sleep(2)

            print("点击发布链接")
            d(text="Add link").click()
            time.sleep(2)

            print("点击商品链接")
            d(text="Product").click()
            time.sleep(10)

            print("点击设置剪贴板")
            d.set_clipboard(product, 'label')
            time.sleep(2)
            print("粘贴内容")
            d.long_click(188,300,2)
            time.sleep(1)
            d.click(150,200)

            print("点击键盘搜索")
            d.click(1000, 2070)
            time.sleep(10)

            print("点击商品链接")
            d(text="Add").click()
            time.sleep(5)

            print("选择产品添加")
            d(text="Add").click()
            time.sleep(5)

        print("点击收回键盘")
        d.click(180, 2226)
        time.sleep(2)
        print("发出视频")
        d.click(770,2107)
        time.sleep(300)