
import os
import cv2

#图片扣色，或者扣好了传上去也行
#self.greenScrean(self,self.uploadImgPath, self.uploadPic)

def saveFile(self,path,file,ftype,request):
    request.app.logger.info("saveFile path:%s,file:%s,ftype:%s"%(path,file,ftype))
    #不存在该路径，报错
    if not os.path.exists(path):
        request.app.logger.error("不存在该路径 path:%s" % path)
        return False,603
    #判断文件类型，保存
    save_file = ""
    if ftype == "pic":
        self.uploadPic = self.taskUUID +'.'+ file.filename.split(sep='.')[-1]
    if ftype == "video":
        self.uploadVideo = self.taskUUID +'.'+ file.filename.split(sep='.')[-1]
    save_file = os.path.join(path, self.taskUUID +'.'+ file.filename.split(sep='.')[-1])
    # else:
    #     return False,601
    #保存文件
    f = open(save_file, 'wb')
    data = file.file.read()
    f.write(data)
    f.close()
    request.app.logger.info("saveFile success filename:%s"%save_file)
    return True,200
def picToImgMask(self,video,filename,request):
    request.app.logger.info("picToImgMask request")
    picBg = self.uploadImgPath+self.cvTmpImg
    self.outputVideo = filename
    try:
        mask = (ImageClip(picBg)
                    .set_duration(video.duration) 
                    .resize(video.size))
        request.app.logger.info("picToImgMask set mask picBg:%s,outputfile:%s"%(picBg,self.outputVideo))    
        CompositeVideoClip([video, mask]).write_videofile(self.outputVideoPath+self.outputVideo)
        request.app.logger.info("picToImgMask success outputfile:%s"%self.outputVideo)
    except Exception as e:
        request.app.logger.info("picToImgMask error:%s,"%e)
    request.app.logger.info("picToImgMask success outputfile:%s"%self.outputVideo)
    return self.outputVideo
def openVideo(self,vPath,request):
    request.app.logger.info("openVideo vPath:%s"%vPath)
    clip = VideoFileClip(vPath)
    return clip
def muteVideo(self,video,request):
    request.app.logger.info("muteVideo")
    muteClip = video.without_audio()
    return muteClip
def greenScrean(self,imgPath,picName):
    # todo 读取并转换图片格式
    opencv = cv2.imread(imgPath + picName)
    hsv = cv2.cvtColor(opencv, cv2.COLOR_RGB2HSV)
    # todo 指定绿色范围,60表示绿色，我取的范围是-+10
    minGreen = np.array([40, 80, 80])
    maxGreen = np.array([80, 255, 255])
    # todo 确定绿色范围
    mask = cv2.inRange(hsv, minGreen, maxGreen)
    # todo 确定非绿色范围
    mask_not = cv2.bitwise_not(mask)
    # todo 通过掩码控制的按位与运算锁定绿色区域
    green = cv2.bitwise_and(opencv, opencv, mask=mask)
    # todo 通过掩码控制的按位与运算锁定非绿色区域
    green_not = cv2.bitwise_and(opencv, opencv, mask=mask_not)
    # todo 拆分为3通道
    b, g, r = cv2.split(green_not)
    # todo 合成四通道
    bgra = cv2.merge([b, g, r, mask_not])
    self.cvTmpImg = "cvtmp_"+self.taskUUID+".png"
    # todo 保存带有透明通道的png图片,有了这种素材之后，就可以给这张图片替换任意背景了
    cv2.imwrite(self.uploadImgPath + self.cvTmpImg, bgra)