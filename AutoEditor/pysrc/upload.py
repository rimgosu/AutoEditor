"""
1. 크롬 실행
2. 유저 선택
3. 만들기로 동영상 업로드 버튼 클릭
4. export 동영상 하나 불러오기
5. 재생목록 선택
6. 수익창출 선택 x
7. 가장 먼 달 클릭 및 예약
8. 크롬 종료
"""
import subprocess
import pyautogui
import time
import os
import random
import clipboard

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
def upload_youtube(current_path, video_list):
    for i in range(len(video_list)):
        export_path = current_path + r'\inputvideo\export'+ '\\' + video_list[i].rstrip('.mp4') + "edited.mp4"
        subprocess.Popen(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
        time.sleep(1)
        check_hangul()
        pyautogui.write("youtube.com")
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.press('F11')
        time.sleep(3)
        duration02 = random.uniform(0.2,0.5)
        duration05 = random.uniform(0.5,1)
        duration10 = random.uniform(1,1.5)
        duration15 = random.uniform(1.5,2)
        duration30 = random.uniform(3,3.5)
        duration50 = random.uniform(5,6)
        smalldurpath =random.uniform(2,2)
        durpath = random.uniform(10,10)
        pyautogui.click(1733+durpath, 33+durpath)
        time.sleep(duration05)
        pyautogui.click(1632+durpath, 82+durpath)
        time.sleep(duration15)
        pyautogui.click(958+durpath, 473+durpath)
        time.sleep(duration05)
        pyautogui.write(export_path)
        time.sleep(duration05)
        pyautogui.press('enter')
        time.sleep(duration30)
        pyautogui.click(779+durpath, 143+durpath)
        time.sleep(duration05)
        pyautogui.click(723+durpath, 315+durpath)
        time.sleep(duration05)
        pyautogui.click(611+smalldurpath, 310+smalldurpath)
        time.sleep(duration05)
        pyautogui.click(814+durpath, 408+durpath)
        time.sleep(duration05)
        pyautogui.click(884+durpath, 152+durpath)
        time.sleep(duration05)
        pyautogui.click(965+durpath, 555+durpath)
        time.sleep(duration02)
        pyautogui.scroll(-2000)
        time.sleep(duration02)
        pyautogui.click(602+durpath, 933+durpath)
        time.sleep(duration10)
        pyautogui.click(1166+durpath, 322+durpath)
        time.sleep(duration50)
        pyautogui.click(1401+durpath, 1004+durpath)
        time.sleep(duration02)
        pyautogui.click(1401+durpath, 1004+durpath)
        time.sleep(duration02)
        pyautogui.click(1401+durpath, 1004+durpath)
        time.sleep(duration02)
        pyautogui.click(1401+durpath, 1004+durpath)

if __name__ == "__main__":
    current_path = os.path.dirname(__file__)
    current_path = os.path.join(current_path, os.pardir)
    video_list = os.listdir(current_path + "/inputvideo/")
    video_list = [file for file in video_list if file.endswith(".mp4")]
    upload_youtube(current_path, video_list)