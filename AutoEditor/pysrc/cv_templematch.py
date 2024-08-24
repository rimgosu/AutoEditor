import cv2
import os
from moviepy.editor import VideoFileClip 
import math
from tqdm import tqdm
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from pysrc.user_discrimination import who

def set_list_sort(index):
    index = set(index)
    index = list(index)
    try:
        index.sort()
    except:
        pass
    return index
def index_exapnd(input_index, minus_constant, plus_constant):
    output_index = []
    for j in input_index:
        for k in range(-minus_constant, plus_constant):
            output_index.append(j+k)
    return output_index
def start_end(index, threshold=1):
    return_index = []
    return_index.append(index[0])
    return_index.append(index[len(index)-1])
    for j in range(len(index)-1):
        if index[j+1] - index[j] <= threshold:
            pass
        else:
            return_index.append(index[j])
            return_index.append(index[j+1])
    return_index = set_list_sort(return_index)
    return return_index
def shrink_index(index, minus_constant, plus_constant):
    idx = []
    for j in range(len(index)):
        if j % 2 == 0:
            idx.append(index[j]+plus_constant)
        else:
            idx.append(index[j]-minus_constant)
    idx = set_list_sort(idx)
    return idx

def DeleteAllFiles(filePath):
    if os.path.exists(filePath):
        for file in os.scandir(filePath):
            os.remove(file.path)
        return 'Remove All File'
    else:
        return 'Directory Not Found'

def vidoescreenshot(video, target_time, output_path, x=975,y=700,w=300,h=300):
    videocv = cv2.VideoCapture(video)

    # Set the target time for the screenshot
    time = target_time  # in seconds

    # Set the video to the target time
    videocv.set(cv2.CAP_PROP_POS_MSEC, time*1000)
    # Read the frame at the target time
    success, frame = videocv.read()
    # Read the frame at the target time
    if success:

        # Crop the frame to the target area
        frame = frame[y:y+h, x:x+w]

        # Save the screenshot
        cv2.imwrite(output_path, frame)

    # Release the video capture object
    videocv.release()
def cut_image(input, m1, m2, mul):
    img = cv2.imread(input, cv2.IMREAD_COLOR)
    roc_img = img[m1[1]:m2[1], m1[0]:m2[0]].copy()
    mul_img = cv2.resize(roc_img, dsize=(0, 0), fx=mul, fy=mul, interpolation=cv2.INTER_AREA)
    return mul_img
def _targetsave_image(img, m1, m2, mul, hpimg_path):
    hpimg = cut_image(hpimg_path + img, m1, m2, mul)
    temp_path = os.path.join(hpimg_path, 'hptemp')
    cutsave_path = temp_path + img[:-4] + "_cut.png"
    cv2.imwrite(cutsave_path, hpimg)
def matchimage(capture_image, target_hpimage, threshold):
    target_image = cv2.imread(target_hpimage, cv2.IMREAD_COLOR)
    capture_image = cv2.imread(capture_image, cv2.IMREAD_COLOR)
    h, w, _ = target_image.shape
    res = cv2.matchTemplate(capture_image, target_image, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    if max_val > threshold:
        print(min_val, max_val)
        matched = os.path.basename(target_hpimage)
        return matched

def guess_battles(detect_list, num=10):
    battles = []
    print(detect_list)
    for j in range(len(detect_list)-num):
        summ = 0
        for k in range(j, j+num):
            summ += detect_list[k]
        if summ == 0:
            for k in range(j, j+num):
                battles.append(k)
    battles = set_list_sort(battles)
    return battles

def find_heropower(video, video_second):
    current_path = os.path.join(os.path.dirname(__file__), os.pardir)
    inputvideo_path = os.path.join(current_path, 'inputvideo')
    inputvideo = os.path.join(inputvideo_path, video)

    hpimg_path = os.path.join(current_path, 'pysrc')
    hpimg_path = os.path.join(hpimg_path, 'heropower')
    hptemp_path = os.path.join(hpimg_path, 'hptemp')
    hpimg_list = os.listdir(hpimg_path)
    hpimg_list = [file for file in hpimg_list if file.endswith(".png")]
    time = video_second

    hptest = True
    hpindex = 0
    while hptest:
        vidoescreenshot(inputvideo, time + hpindex, hptemp_path + "/hpcheck.png")
        for i in hpimg_list:
            target = "\\"+ i
            cutsave_path = hptemp_path + target[:-4] + "_cut.png"
            _targetsave_image(target, [134, 118], [246, 207], 0.621, hpimg_path)
            matched = matchimage(hptemp_path + "\\" "hpcheck.png", cutsave_path, threshold=0.85)
            if matched is not None:
                break
        if matched is not None:
            hptest = False
            print('matched!')
        else:
            hptest = True
            hpindex += 5
            print(time + hpindex)
        if hpindex == 100:
            hptest = False

    matched = matched[:-8] + '.png'
    return matched

def find_anomalies(video, video_second):
    current_path = os.path.join(os.path.dirname(__file__), os.pardir)
    inputvideo_path = os.path.join(current_path, 'inputvideo')
    inputvideo = os.path.join(inputvideo_path, video)

    hpimg_path = os.path.join(current_path, 'pysrc')
    hpimg_path = os.path.join(hpimg_path, 'anomalies')
    hptemp_path = os.path.join(hpimg_path, 'hptemp')
    hpimg_list = os.listdir(hpimg_path)
    hpimg_list = [file for file in hpimg_list if file.endswith(".png")]
    time = video_second

    hptest = True
    hpindex = 0
    while hptest:
        vidoescreenshot(inputvideo, time + hpindex, hptemp_path + "/hpcheck.png",1570,370,100,100)
        for i in hpimg_list:
            target = "\\"+ i
            cutsave_path = hptemp_path + target[:-4] + "_cut.png"
            _targetsave_image(target, [142, 118], [236, 210], 0.442, hpimg_path)
            matched = matchimage(hptemp_path + "\\" "hpcheck.png", cutsave_path, threshold=0.75)
            if matched is not None:
                break
        if matched is not None:
            hptest = False
            print('matched!')
        else:
            hptest = True
            hpindex += 5
            print(time + hpindex)
        if hpindex == 100:
            hptest = False

    matched = matched[:-8] + '.png'
    return matched

def find_trinket(video, video_second, grade):
    current_path = os.path.join(os.path.dirname(__file__), os.pardir)
    inputvideo_path = os.path.join(current_path, 'inputvideo')
    inputvideo = os.path.join(inputvideo_path, video)

    hpimg_path = os.path.join(current_path, 'pysrc')
    hpimg_path = os.path.join(hpimg_path, 'trinket')
    hptemp_path = os.path.join(hpimg_path, 'hptemp')
    hpimg_list = os.listdir(hpimg_path)
    hpimg_list = [file for file in hpimg_list if file.endswith(".png")]
    time = video_second

    hptest = True
    hpindex = 0
    while hptest:
        if grade == 0:
            vidoescreenshot(inputvideo, time + hpindex, hptemp_path + "/hpcheck.png",805,855,40,40)
        else:
            vidoescreenshot(inputvideo, time + hpindex, hptemp_path + "/hpcheck.png",728,782,40,40)
        for i in hpimg_list:
            target = "\\"+ i
            cutsave_path = hptemp_path + target[:-4] + "_cut.png"
            _targetsave_image(target, [149, 89], [234, 178], 0.442, hpimg_path)
            matched = matchimage(hptemp_path + "\\" "hpcheck.png", cutsave_path, threshold=0.75)
            if matched is not None:
                break
        if matched is not None:
            hptest = False
            print('matched!')
        else:
            hptest = True
            hpindex += 5
            print(time + hpindex)
        if hpindex == 100:
            hptest = False

    matched = matched[:-8] + '.png'
    return matched

def find_battles_second(video, inputvideo_path, screenshot = True):
    current_path = os.path.join(os.path.dirname(__file__), os.pardir)
    inputvideo = os.path.join(inputvideo_path, video)
    videopy = VideoFileClip(inputvideo)
    total_duration = math.floor(videopy.end)

    battleimg = os.path.join(current_path, 'pysrc')
    battleimg = os.path.join(battleimg, 'image_src')
    battleimg = os.path.join(battleimg, 'battleimg')
    videocapture_path = os.path.join(battleimg, 'videocapture')
    battle_index = []
    if screenshot:
        DeleteAllFiles(videocapture_path)
    for i in range(total_duration):
        if screenshot:
            vidoescreenshot(inputvideo, i, videocapture_path + '/' + str(i) + '.png', x=1481,y=456,w=150,h=75)
        matched = matchimage(battleimg + "/battlekr.png", videocapture_path + '/' + str(i) + '.png', threshold=0.90)
        if matched is None:
            matched = matchimage(battleimg + "/battlejp.png", videocapture_path + '/' + str(i) + '.png', threshold=0.90)
        if matched is None:
            matched = matchimage(battleimg + "/battle.png", videocapture_path + '/' + str(i) + '.png', threshold=0.90)

        if matched:
            battle_index.append(i)
        print(str(i) +':', matched)
    
    battle_index = index_exapnd(battle_index, 15, 15)
    battle_index = set_list_sort(battle_index)
    battle_index = start_end(battle_index)
    battle_index = shrink_index(battle_index, plus_constant=12, minus_constant=14)
    print(battle_index)
    return battle_index

    # 과거: mul = 0.54 
def newminion_cut(patchday='_230315', imagecut_init = True, m1=[118,100], m2=[270,256], mul=0.54):
    current_path = os.path.join(os.path.dirname(__file__), os.pardir)
    
    forcuts_path = os.path.join(current_path, 'pysrc')
    forcuts_path = os.path.join(forcuts_path, 'newminion')
    forcuts_path = os.path.join(forcuts_path, patchday)
    forcuts_path = os.path.join(forcuts_path, 'forcuts')
    forcuts_images = os.listdir(forcuts_path)
    forcuts_images = [file for file in forcuts_images if file.endswith(".png")]

    videocapture_path = os.path.join(current_path, 'pysrc')
    videocapture_path = os.path.join(videocapture_path, 'newminion')
    videocapture_path = os.path.join(videocapture_path, patchday)
    videocapture_path = os.path.join(videocapture_path, 'screenshot_temp')

    cut_completed_path = os.path.join(current_path, 'pysrc')
    cut_completed_path = os.path.join(cut_completed_path, 'newminion')
    cut_completed_path = os.path.join(cut_completed_path, patchday)
    cut_completed_path = os.path.join(cut_completed_path, 'cut_completed')
    
    if imagecut_init:
        for x in forcuts_images:
            cut_img = cut_image(forcuts_path + '/' + x, m1, m2, mul)
            cv2.imwrite(cut_completed_path + '/' + x, cut_img)

def newminion_detect(video, inputvideo_path, second, patchday='_230315', forbrann='False'):
    current_path = os.path.join(os.path.dirname(__file__), os.pardir)
    forcuts_path = os.path.join(current_path, 'pysrc')
    forcuts_path = os.path.join(forcuts_path, 'newminion')
    forcuts_path = os.path.join(forcuts_path, patchday)
    forcuts_path = os.path.join(forcuts_path, 'forcuts')
    forcuts_images = os.listdir(forcuts_path)
    forcuts_images = [file for file in forcuts_images if file.endswith(".png")]

    inputvideo = os.path.join(inputvideo_path, video)
    videocapture_path = os.path.join(current_path, 'pysrc')
    videocapture_path = os.path.join(videocapture_path, 'newminion')
    videocapture_path = os.path.join(videocapture_path, patchday)
    videocapture_path = os.path.join(videocapture_path, 'screenshot_temp')

    cut_completed_path = os.path.join(current_path, 'pysrc')
    cut_completed_path = os.path.join(cut_completed_path, 'newminion')
    cut_completed_path = os.path.join(cut_completed_path, patchday)
    cut_completed_path = os.path.join(cut_completed_path, 'cut_completed')
    cut_completed_images = os.listdir(cut_completed_path)
    cut_completed_images = [file for file in cut_completed_images if file.endswith(".png")]

    match_list = []
    for y in range(3):
        if forbrann == 'True':
            vidoescreenshot(inputvideo, second+y/2, videocapture_path + '/screenshot.png', x=479,y=501,w=969,h=188)
            _thr = 0.70
        elif forbrann == 'False':
            vidoescreenshot(inputvideo, second+y/2, videocapture_path + '/screenshot.png', x=479,y=322,w=969,h=372)
            _thr = 0.70
        for x in cut_completed_images:
            matched = matchimage(videocapture_path + '/screenshot.png', cut_completed_path + '/' + x, threshold=_thr)
            match_list.append(matched)

    match_list = set_list_sort(match_list)
    if forbrann == 'False':
        match_list.remove(None)
    while len(match_list) >= 4:
        del match_list[0]
    print(match_list)
    return match_list

def cutimage_remove(matched_list, patchday='_230315'):
    current_path = os.path.join(os.path.dirname(__file__), os.pardir)
    forcuts_path = os.path.join(current_path, 'pysrc')
    forcuts_path = os.path.join(forcuts_path, 'newminion')
    forcuts_path = os.path.join(forcuts_path, patchday)
    forcuts_path = os.path.join(forcuts_path, 'forcuts')
    forcuts_images = os.listdir(forcuts_path)
    forcuts_images = [file for file in forcuts_images if file.endswith(".png")]

    cut_completed_path = os.path.join(current_path, 'pysrc')
    cut_completed_path = os.path.join(cut_completed_path, 'newminion')
    cut_completed_path = os.path.join(cut_completed_path, patchday)
    cut_completed_path = os.path.join(cut_completed_path, 'cut_completed')

    for x in matched_list:
        exist_image = cut_completed_path + '/' + x
        if os.path.isfile(exist_image):
            os.remove(exist_image)

if __name__ == "__main__":
    # find_battles_second('rimgosu std.mp4')
    video = 'rimgosu homz.mp4'
    inputvideo_path = r'C:\Users\rimgosu\Desktop\ShareFolder\git\AutoEditor\inputvideo'
    second = 752
    newminion_cut()
    for i in range(2):
        newminion_list = newminion_detect(video, inputvideo_path, second)
        cutimage_remove(newminion_list)
    pass