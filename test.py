import subprocess

video1 = 'videos/c278334375d34d60aafb44249d93b08b.mp4'
video2 = 'videos/501fb1b11e78457a8ea6bcc1e360700a.mp4'

output1 = 'videos/c278334375d34d60aafb44249d93b08b_output.mp4'
output2 = 'videos/501fb1b11e78457a8ea6bcc1e360700a_output.mp4'

# 处理第一个视频
cmd = ['ffprobe', '-v', 'error', '-select_streams', 'v:0',
       '-show_entries', 'stream=codec_name', '-of', 'default=nokey=1:noprint_wrappers=1', video1]

result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
codec_name = result.stdout.decode('utf-8').strip()

if codec_name not in ['h264', 'h265']:
  cmd = f'ffmpeg -i {video1} -c:v libx264 -crf 23 -c:a copy {output1}' 
  subprocess.call(cmd, shell=True)
else:
  cmd = f'ffmpeg -i {video1} -c:v copy -tag:v h264 {output1}'
  subprocess.call(cmd, shell=True)  

# 处理第二个视频  
cmd = ['ffprobe', '-v', 'error', '-select_streams', 'v:0',
       '-show_entries', 'stream=codec_name', '-of', 'default=nokey=1:noprint_wrappers=1', video2]

result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
codec_name = result.stdout.decode('utf-8').strip()

if codec_name not in ['h264', 'h265']:
  cmd = f'ffmpeg -i {video2} -c:v libx264 -crf 23 -c:a copy {output2}'
  subprocess.call(cmd, shell=True)
else: 
  cmd = f'ffmpeg -i {video2} -c:v copy -tag:v h264 {output2}'
  subprocess.call(cmd, shell=True)

# 拼接视频  
cmd = f'ffmpeg -i "video" -c copy -vsync vfr output.mp4'
subprocess.call(cmd, shell=True)

print('视频处理完成!')  