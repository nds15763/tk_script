import uiautomator2 as u2
import tiktok as tk

def sInit():
    d = u2.connect('99151FFAZ009WE') # Pixel4 2号
    d.set_new_command_timeout(12000) # 配置accessibility服务的最大空闲时间，超时将自动释放。默认3分钟。
    # d.app_start("TikTok")
    return d

if __name__ == "__main__":
    d = sInit()
    #开始
    t = tk.Tiktok()
    t.startVideo(d)