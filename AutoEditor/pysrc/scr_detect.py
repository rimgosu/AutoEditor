import sys
import os
import pyautogui
import time
import shutil
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from yolov5.detect_encoding import * 

def scr_detect(
    name,
    current_path,
    scr_path,
    pt,
    export_path
    ):
    i=0
    text=[]
    for f in os.listdir(scr_path):
        os.remove(os.path.join(scr_path, f))    

    j=0
    # 15분이 지났는데도 루프를 계속 돌고있을 시, 강제종료
    while j<180:
        scr = scr_path + name + ".png"
        if os.path.exists(scr):
            os.remove(scr)
        pyautogui.screenshot(scr)

        run(weights=ROOT / pt, source=scr_path , save_txt = True, conf_thres=0.5, project=ROOT / export_path, name='exp')
        if len(os.listdir(current_path+ "/yolov5/"+export_path+"/exp/labels")) == 1:
            print(os.listdir(current_path+ "/yolov5/"+export_path+"/exp/labels"))
            text.append(i)
        time.sleep(5)
        if os.path.exists(current_path + "/yolov5/"+export_path+"/"):
            shutil.rmtree(current_path + "/yolov5/"+export_path+"/")
        if len(text) + 1 == i: 
            break
        i += 1
        j += 1

if __name__ == "__main__":
    current_path = os.path.dirname(__file__)
    current_path = os.path.join(current_path, os.pardir)
    video_list = os.listdir(current_path + "/inputvideo/")
    video_list = [file for file in video_list if file.endswith(".mp4")]
    scr_path = current_path + "/yolov5/data/encodingimage/"
    scr_detect('encoding', current_path, scr_path, 'models/encoding.pt', 'runs/edetect')
    
 