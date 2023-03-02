import uiautomator2 as u2
import multiprocessing as np
import subprocess
import time
import tiktok as tk

def getphonelist():  # 获取手机设备
    cmd = r'adb devices'  # % apk_file
    pr = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    pr.wait()  # 不会马上返回输出的命令，需要等待
    out = pr.stdout.readlines()  # out = pr.stdout.read().decode("UTF-8")
    devices = []
    for i in (out)[1:-1]:
        device = str(i).split("\\")[0].split("'")[-1]
        devices.append(device)
    return devices  # 手机设备列表

def test_xxx(i):  #执行用例
    d = u2.connect(getphonelist()[int(i)])  # d = u2.connect('192.168.1.117')#  uiautomator2 连接手机
    MultiDevice(d)

def MultiDevice( d):  # 功能执行
    t = tk.Tiktok()
    t.startVideo(d)

def main():#多进程

    for i in range(len(getphonelist())):  #有几个设备起几个进程
        p = np.Process(target=test_xxx, args=(str(i)))
        p.start()


if __name__ == '__main__':
    main()
