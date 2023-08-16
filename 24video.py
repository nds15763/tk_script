import ffm_video as ff
import json
import os
from datetime import datetime
import sys
import msvcrt
import time

#读取配置文件data.json
def get_device_name():
    #读取本地的tmp.json文件
    with open('data.json', encoding='utf-8') as f:
        data = json.load(f)
        return  data

#删除数组里的*号并记录该位置
def get_pos(): 
    for i in range(len(arr)):
        if arr[i] == "0":
            star_pos = i
            arr.pop(i)
            return star_pos
        
def set_pos(tmp,star_pos):
    tmp.insert(star_pos, "0")
    return tmp


def permutations(arr, position, end,have_zero,tp):
    if position == end:
        tmp = arr.copy()
        if have_zero:
            tmp = set_pos(tmp,star_pos)
        #uuid是最后排序的内容，需要把tmp数组的所有内容拼成一个字符串，然后*号变成数字1
        uuid = "".join(tmp)
        ff.doprocess(tmp,speech_video,video_dict,uuid,dirname,tp)
        print(tmp)
        return 
 
    for index in range(position, end):
        arr[index], arr[position] = arr[position], arr[index]
        permutations(arr, position+1, end,have_zero,tp) 
        arr[index], arr[position] = arr[position], arr[index]

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
    datalist = get_device_name()
    now = datetime.now()
    stime = int(time.time())
    print("开始执行:")
    for key in datalist:
        data = datalist[key]
        arr = data["sort"]
        video_dict = data["dict"]
        speech_video = data["speech_video"]
        tp = ""
        try:
            tp = data["tp"]
        except:
            print("缺少tp字段，tp:LR:左右，TB:上下")
        #判断是否有0
        star_pos = 0

        have_zero = False
        if "0" in arr:
            have_zero = True
            print("获取0的位置")
            star_pos = get_pos()
            
        dirname = mkdir(key)   
        permutations(arr, 0, len(arr),have_zero,tp)
    etime = int(time.time())
    print("执行完毕,用时："+str(etime-stime)+"秒\n")


    print("请按任意键退出~")
    ord(msvcrt.getch())