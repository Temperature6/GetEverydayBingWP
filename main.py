import os
import sys
import requests
import time

save_dir = ".\\BingWallpaper"


def GetTime():
    return time.strftime("%Y%m%d", time.localtime())


def GetPic(time_str):
    last_time = time.time()
    rqs = requests.get("https://bingwallpaperimages.azureedge.net/hpimages/Latest/3840x2160/{0}.jpg".format(time_str))
    if rqs.status_code == 200:
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        save_ = "{0}\\{1}.jpg".format(save_dir, time_str)
        pic_file = open(save_, "wb")
        pic_file.write(rqs.content)
        current_time = time.time()
        print("[Success]Download {0} in {1} seconds".format(save_, (round(current_time - last_time, 2))))
    else:
        print("[Fail]Fail to get picture from server, status code is {0}".format(rqs.status_code))
        os.system("pause")
    return


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "-t":
        for i in range(2, len(sys.argv)):
            GetPic(sys.argv[i])
    else:
        GetPic(GetTime())
