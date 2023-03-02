import uiautomator2 as u2
import os,time
import uiautomator2 as u2
from multiprocessing import Process,Queue
import tiktok as tk

def get_devices_serials():
    devices_list = []
    fd = os.popen("adb devices")
    devices_list_src = fd.readlines()
    fd.close()
    for device in devices_list_src:
        if "device\n" in device:
            device = device.replace("\tdevice\n","")
            devices_list.append(device)
    return devices_list
    
def worker( serial ):
    os.system("python -m uiautomator2 init  --serial %s"%serial)
    d = u2.connect(serial)
    print(d.info)
    d.app_start("com.zhiliaoapp.musically")
    t = tk.Tiktok()
    t.startVideo(d)

    
if __name__ == "__main__":
    process_list = []
    serial_list = get_devices_serials()
    for index in range( len(serial_list) ):
        p = Process( target=worker, args=( serial_list[index],  ) )
        p.start()
        process_list.append(p)
    for p in process_list:
        p.join()
    print("all task done!")