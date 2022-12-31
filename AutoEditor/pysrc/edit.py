"""
1. open premiere pro
2. ctrl+o
3. 'C:/Users/newny/Desktop/PythonWorkspace/chapter/inputvideo/xmlcache/' + video_list
4. enter
5. ctrl+a
6. ctrl+d
7. ctrl+shift+d
8. ctrl+m
9. some shift tab
10. current_path + "/inputvideo/export/edited" + video_list
11. enter
12. some tab
13. enter
"""

import subprocess
import pyautogui
import time
import os
import psutil
import clipboard
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from yolov5.detect_encoding import * 
from pysrc.scr_detect import *

def kill_process(process):
    for proc in psutil.process_iter():
        if proc.name() == process:
            proc.kill()
def check_hangul():
    pyautogui.write("hangul")
    time.sleep(0.2)
    pyautogui.keyDown('ctrl')
    pyautogui.press('a')
    time.sleep(0.1)
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')
    time.sleep(0.1)
    res = clipboard.paste()
    print(res)
    time.sleep(0.1)
    if res == "hangul":
        print('한영키: 영문')
    else:
        print('한영키: 한글')
        pyautogui.press('hangul')
        time.sleep(0.1)
def run_autoPremiere(
    current_path,
    video,
    ex
):
    exposition1 = (508,202)
    exposition2 = (1858,988)
    premiere_path = r'C:\Program Files\Adobe\Adobe Premiere Pro 2023\Adobe Premiere Pro.exe'
    xml_path = current_path + r"\inputvideo\xmlcache" +"\\" + video[:-4] + '.xml'
    ex_file = ex +  '\\' + video[:-4] + "edited.mp4"
    ex_file.replace("/", "\\")
    print(ex_file)
    if os.path.exists(ex_file):
        os.remove(ex_file)
    kill_process('Opencapture.exe')
    kill_process('chrome.exe')
    kill_process('explorer.exe')
    kill_process("Adobe Premiere Pro.exe")   
    kill_process("PotPlayer64.exe")   
    kill_process("notepad.exe")

    subprocess.Popen(premiere_path)
    time.sleep(12)
    pyautogui.keyDown('ctrl') 
    pyautogui.press('o')
    pyautogui.keyUp('ctrl')
    time.sleep(0.5)
    check_hangul()
    pyautogui.write(xml_path) 
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('alt')
    time.sleep(0.2)
    pyautogui.press('space')
    time.sleep(0.2)
    pyautogui.press('x')
    time.sleep(1)
    pyautogui.keyDown('shift')
    pyautogui.press('3')
    pyautogui.keyUp('shift')
    time.sleep(1)
    pyautogui.keyDown('ctrl') 
    pyautogui.keyDown('shift')
    pyautogui.press('i')  
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('shift')
    time.sleep(0.5)
    pyautogui.keyDown('ctrl') 
    pyautogui.keyDown('shift')
    pyautogui.press('x')  
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('shift')
    time.sleep(0.5)
    pyautogui.keyDown('ctrl')
    pyautogui.press('a')
    pyautogui.keyUp('ctrl')
    time.sleep(0.5)
    pyautogui.keyDown('shift')
    pyautogui.press('d')
    pyautogui.keyUp('shift')
    time.sleep(0.5)
    pyautogui.keyDown('ctrl') 
    pyautogui.keyDown('shift')
    pyautogui.press('d')  
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('shift')
    time.sleep(0.5)
    pyautogui.keyDown('ctrl')
    pyautogui.press('m')
    pyautogui.keyUp('ctrl')
    time.sleep(3)
    pyautogui.click(exposition1)
    time.sleep(0.5)
    pyautogui.write(ex_file) 
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.click(exposition2)
    scr_path = current_path + "/yolov5/data/encodingimage/"
    scr_detect('encoding', current_path, scr_path, 'models/encoding.pt', 'runs/edetect')
    kill_process("Adobe Premiere Pro.exe")     

if __name__=="__main__":
    current_path = os.path.dirname(__file__)
    current_path = os.path.join(current_path, os.pardir)
    video_list = os.listdir(current_path + "/inputvideo/")
    video_list = [file for file in video_list if file.endswith(".mp4")]
    export_path = current_path + r'\inputvideo\export'
    run_autoPremiere(current_path,video_list[0],export_path)