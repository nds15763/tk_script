import subprocess
import os
from datetime import datetime
import cv2

#speech_video:口播视频
#sortlist:排序列表(用作最后命名)
#video_dict:视频字典
#uuid: 本次执行的uuid，也就是abcd的排序字符串
#dirname: 本次执行的文件夹名字

def doprocess(sortlist,speech_video,video_dict,uuid,dirname,tp):

     #创建一个临时文件用来存放拼接视频的文件名
    with open('./videos/tmp_video_'+uuid+'.txt', 'w') as f:
        for i in range(len(sortlist)):
            f.write("file '"+video_dict[sortlist[i]]+"'\n")

    tmptext = './videos/tmp_video_'+uuid+'.txt'
    concatvideo = './'+dirname+"/"+uuid+'_output.mp4'

    final_video = './'+dirname+"/"+"final_"+uuid+'.mp4'
    # 输入视频路径
    videos = []
    for i in range(len(sortlist)):
        videos.append(video_dict[sortlist[i]])
    # 黑底视频参数

    # 拼接静音后视频  
    cmd_concat = './libs/ffmpeg -safe 0 -f concat -i '+tmptext+' -c copy '+concatvideo

    subprocess.call(cmd_concat)

    if tp == "TB":
        # tmpout = './videos/tmpout_'+uuid+'.mp4'
        # #原始战神
        # cmd_tmp_tb = f'ffmpeg -i {concatvideo} -i {"./videos/"+speech_video} \
        # -filter_complex "[1:v]pad=iw*2:ih[a];[a][0:v]overlay=0:h"\
        # -map 1:a {tmpout}'
        # subprocess.call(cmd_tmp_tb)

        # cmd_blurred = f'ffmpeg -i {concatvideo} -i {tmpout}  \
        # -filter_complex "[0:v]boxblur=luma_radius=10:luma_power=1.5[blurred];\
        # [1:v]scale=iw/2:ih/2[scaled];\
        # [blurred][scaled]overlay=x=W/4:y=0[out]" \
        # -map "[out]" -map 1:a {final_video}'
        # subprocess.call(cmd_blurred)

        #融合战神
        cmd_blurred = f'./libs/ffmpeg -i {concatvideo} -i {"./videos/"+speech_video}  \
        -filter_complex "[1:v]pad=iw*1:ih*2[a];[a][0:v]overlay=0:h[c];\
        [0:v]boxblur=luma_radius=10:luma_power=1.5[blurred];\
        [c]scale=iw/2:ih/2[scaled];\
        [blurred][scaled]overlay=x=W/4:y=0[out]" \
        -map "[out]" -map 1:a {final_video}'
        subprocess.call(cmd_blurred)

    else:
        cmd_concat_width = ['./libs/ffmpeg', '-i', concatvideo, '-i', os.path.join("./videos",speech_video), 
            '-filter_complex','[0:v]pad=iw*2:ih*1[a];[a][1:v]overlay=w', 
            '-map', '1:a',final_video
        ]
        subprocess.call(cmd_concat_width)

    # #删除临时文件
    os.remove(tmptext)
    os.remove(concatvideo)