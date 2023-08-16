import random

A = ["a1", "a2", "a3", "a4", "a5"]  
B = ["b1", "b2", "b3"]
C = ["c1", "c2", "c3", "c4"]

video_lengths = {
    "a1": 7.5,
    "a2": 7.5, 
    "a3": 7.5,
    "a4": 7.5,
    "a5": 7.5,
    "b1": 5,  
    "b2": 5,
    "b3": 5,
    "c1": 2.5,
    "c2": 2.5,
    "c3": 2.5,
    "c4": 2.5
}

#后续ABC需要从数据库读取，分2.5，5，7.5三种长度
#video_lengths是视频长度，也需要从数据库读取

#这个目标长度是传入视频的目标长度，挂web上传后计算就好了
target_length = 15

#这个函数是随机选择视频，传入目标长度，返回视频列表
def select_videos(target):
    selected_videos = []
    video_groups = [A, B, C]
    
    while sum(video_lengths[v] for v in selected_videos) < target:
        group = random.choice(video_groups)
        video = random.choice(group)
        
        if video not in selected_videos:
            selected_videos.append(video)

    return selected_videos


#这里每次请求都会有不一样，之后挂web以后会选，生成几个视频，然后返回下载链接
for i in range(5):
    print(select_videos(target_length))


#接入生成视频，上传的是右半边的口播，左半边的视频列表已经拿到了，去数据库里面取相应的视频地址
#然后拼接，生成视频，切掉多余时长的部分，然后最后拼接右半边的视频，左右拼或者上下拼，反正这个代码有了

