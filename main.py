import ffm_video as ff
import mk_video as mk
import json
import os
from datetime import datetime
import sys
import msvcrt
import time

#读取配置文件data.json
def get_device_name():
    #读取本地的tmp.json文件
    with open('token.json', encoding='utf-8') as f:
        data = json.load(f)
        return  data

#创建一个以当前时间戳为名字的文件夹
def mkdir(key):
    #获取当前时间戳
    now = datetime.now()
    #转换成字符串
    dirname = str("mkvideo_"+key+"_"+now.strftime("%Y%m%d%H%M%S"))
    #创建文件夹
    os.mkdir(dirname)
    return dirname

if __name__ == "__main__":
        
#删除数组里的*号并记录该位置
    data = get_device_name()
    now = datetime.now()
    stime = int(time.time())
    print("开始执行:")

    #设定一个方法，兼容旧和新代码
    if "type" in data.keys():
        tp = data["type"]
        if tp == "new":
            sort_arr = data["sort"]
            video_dict = data["dict"]
            speech_video = data["speech_video"]

            key = data["key"]
            dirname = mkdir(key)
            for sort in sort_arr:
                uuid = "".join(map(str, sort))
                mk.new_doprocess(sort,speech_video,video_dict,uuid,dirname)
            etime = int(time.time())
            print("执行完毕,用时："+str(etime-stime)+"秒\n")
        else:
            sort_arr = data["sort"]
            video_dict = data["dict"]
            speech_video = data["speech_video"]
            key = data["key"]
            dirname = mkdir(key)
            for sort in sort_arr:
                uuid = "".join(map(str, sort))
                mk.doprocess(sort,speech_video,video_dict,uuid,dirname)
            etime = int(time.time())
            print("执行完毕,用时："+str(etime-stime)+"秒\n")

