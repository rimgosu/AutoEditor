"""
0     EMPLOY              0~1 = employ, battle
1     BATTLE
2     DENTED MINION       2~20 = moving detect
3     DENTED CARD
4     DENTED HEROPOWER
5     PUT CARD
6     PUT GOLD CARD
7     TAKE CARD
8     TAKE GOLD CARD
9     COIN
10    WAD OF COINS	
11    BUFF NUMBER
12    MURLOC BUFF
13    DARK BUFF
14    ARTISA BUFF
15    BLOOD JAM
16    SHINING
17    LIGHTNING
18    FREEZE
19    BANG
20    BIG BANG
21    STAR                    battle
22    KELTUZAD                battle
23    JJIGGREGI               battle
24    PYOSI                   discovery
25    SUMGIGI                 discovery
26    SEE HERO INFORMATION    discovery
27    SEE INTERNET            byunsu 
28    DONATION                byunsu
29    SELECT HERO             start
30    GAME END                end
31    LOOK FOR SANGDAE
32    RECONNECTING            byunsu(고용, 전투 확실하지 않을 때)
33    YOG
34    DEMON EAT
35    COOKIE EAT
36    CHOOSE ONE
37    HOMZ
"""
"""
작업해야 할것 두 가지.
2. tinker로 시각화 할 것
3. text 데이터를 신뢰도, 좌표값 모두 받아와서 분석할 것
4. 유튜브 업로드 시 불법 프로그램으로 걸릴 수도 있으니까 rand함수 최대한 많이써서 사람이 하듯이 클릭할 것.
"""

import os
import shutil
import ffmpeg
import math
import numpy as np
import subprocess
from yolov5.detect_modified import *
from moviepy.editor import VideoFileClip
from pysrc.TREE import *
from pysrc.edit import *
from pysrc.upload import *
from pysrc.audio_analysis import *
from pysrc.screenshot_bgremove import *
from pysrc.sendemail import *
from pysrc.cv_templematch import *
from pysrc.user_discrimination import *
def framerate_resolution_change(inputvideo_path, outputvideo_path, framerate, res):
    if os.path.isfile(outputvideo_path):
        pass
    else: 
        stream = ffmpeg.input(inputvideo_path)  # video location
        stream = stream.filter('fps', fps=framerate, round='up')
        stream = stream.filter('scale', width = res, height = res)
        stream = ffmpeg.output(stream, outputvideo_path)
        ffmpeg.run(stream)
# def framerate_resolution_change(inputvideo_path, outputvideo_path, framerate, res):
#     if os.path.isfile(outputvideo_path):
#         pass
#     else:
#         print(res)
#         print(framerate)
#         # FFmpeg 명령을 문자열로 작성
#         ffmpeg_command = [
#             'ffmpeg',  # FFmpeg 실행 파일
#             '-hwaccel', 'cuvid',  # cuvid 하드웨어 가속 옵션 추가
#             # '-c:v', 'h264_cuvid',
#             '-i', inputvideo_path,  # 입력 비디오 파일
#             '-vf', f'fps={framerate},scale={res}:{res}',  # 필터 옵션으로 프레임 속도 및 해상도 변경
#             '-c:v', 'h264_nvenc',  # 출력 비디오 코덱 선택
#             outputvideo_path  # 출력 비디오 파일
#         ]
        
#         # FFmpeg 명령 실행
#         subprocess.run(ffmpeg_command)
def DeleteAllFiles(filePath):
    if os.path.exists(filePath):
        for file in os.scandir(filePath):
            os.remove(file.path)
        return 'Remove All File'
    else:
        return 'Directory Not Found'
def delete_target(dir, extension):
    # specify the directory path
    directory = dir

    # use a for loop to iterate through all files in the directory
    for filename in os.listdir(directory):
        # check if the file is an mp4
        if filename.endswith(extension):
            # build the full file path
            file_path = os.path.join(directory, filename)
            try:
                # delete the file
                os.remove(file_path)
                print(f"{file_path} has been deleted.")
            except Exception as e:
                # print the error message if there is an error
                print(f"Error: {e}")
def frame_to_second(index, fps):
    index_second = [index[i] / fps for i in range(len(index))]
    return np.round(index_second, 1)
def set_list_sort(index):
    index = set(index)
    index = list(index)
    index.sort()
    return index
def trim_edge(_gamestart, _gameend, source_list):
    edge = []
    for j in range(0, _gamestart):
        edge.append(j)
    for j in range(_gameend, 20000):
        edge.append(j)
    for j in edge:
        while j in source_list:
            source_list.remove(j)
    source_list = set_list_sort(source_list)
    return source_list
# 1 dimension list
def check_listlength(index_list, i):
    if len(index_list) == i:
        pass
    else:
        index_list.append('__fail__')
    return index_list
def index_append(return_index, append_index):
    for j in append_index:
        return_index.append(j)
def index_range_append(return_index, _from, _to):
    for j in range(_from, _to):
        return_index.append(j)
def index_remove(return_index, dup_index):
    for j in dup_index:
        while j in return_index:
            return_index.remove(j)
    return return_index
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
def index_exapnd(input_index, minus_constant, plus_constant):
    output_index = []
    for j in input_index:
        for k in range(-minus_constant, plus_constant):
            output_index.append(j+k)
    output_index = set_list_sort(output_index)
    return output_index
def remove_not_between(arr, n, m):
    # (n, m) 사이에 속하는 숫자 추출
    between = [x for x in arr if n <= x <= m]
    return between


def run_autoEditor(
    current_path,
    video_list,
    input_path,
    exf_path,
    framerate=3,
    res=1/3,
    FRchange=False,
    yoloDetect=False,
    changeXml=True,
    Premiere=True,
    screenshot=False,
    uploadYotube=True,
    display_newminion=False,
    newminion_patchday='_230127',
    shutdown=False
):
    resolution = int(1920 * res)
    inputvideo_path = []
    FRvideo_path = []
    FRtext_path = []
    videopy = []
    frameend = []
    wav_path = []
    for i in range(len(video_list)):
        inputvideo_path.append(input_path + "/" + video_list[i])
        wav_path.append(current_path+"/pysrc/wav/" + video_list[i][:-4] + ".wav")
        FRvideo_path.append(current_path+"/yolov5/data/videos/" + str(framerate) + "f" + str(resolution) + "r" + video_list[i])
        FRtext_path.append(
            current_path+"/yolov5/runs/detect/exp/labels/" + str(framerate) + "f" + str(resolution) + "r" + video_list[i][:-4]
            )
        videopy.append(VideoFileClip(input_path + "/" + video_list[i]))
        frameend.append(math.floor(videopy[i].end * framerate))

    print('FRtext_path')
    print(FRtext_path)
    print('video_list')
    print(video_list)

    # 1. framerate change
    if FRchange:
        if os.path.exists(current_path+"/yolov5/data/videos/"):
            DeleteAllFiles(current_path+"/yolov5/data/videos/")

        for i in range(len(video_list)):
            framerate_resolution_change(
                inputvideo_path[i], 
                FRvideo_path[i],
                framerate=framerate,
                res=res
                )

    # 2. run yolo
    if yoloDetect:
        if os.path.exists(current_path + "/yolov5/runs/detect/"):
            shutil.rmtree(current_path + "/yolov5/runs/detect/")
        run_detect(weights=ROOT / 'models/train_ver2.pt', source=ROOT / 'data/videos', save_txt = True, save_conf=True, conf_thres=0.25)

    # 3. yolo to list
    lines = [[str(100) for x in range(max(frameend))] for y in range(len(video_list))]
    txt_path = [[str(100) for x in range(max(frameend))] for y in range(len(video_list))]
    line_list = [[[str(100) for z in range(0)] for x in range(max(frameend))] for y in range(len(video_list))]
    yolo_list = [[[str(100) for z in range(0)] for x in range(max(frameend))] for y in range(len(video_list))]
    for i in range(len(video_list)):
        for j in range(max(frameend)):
            txt_path[i][j] = FRtext_path[i] + "_" + str(j) + ".txt"
            if os.path.isfile(txt_path[i][j]):
                with open(txt_path[i][j]) as f:
                    lines[i][j] = f.readlines()
            else:
                lines[i][j] = '-'

    for i in range(len(video_list)):
        for j in range(max(frameend)):
            for k in range(len(lines[i][j])):
                line_list[i][j] = lines[i][j][k].split()
                yolo_list[i][j].append(line_list[i][j])

    # remove exp_path 
    if Premiere:
        if os.path.exists(exf_path):
            delete_target(exf_path, '.mp4')

    indexes = True
    if indexes:
        # 4. indexes
        dented_stop = [[[0 for x in range(0)] for y in range(max(frameend))] for z in range(len(video_list))]
        dented_stop_index = [[0 for x in range(0)] for y in range(len(video_list))]
        dentedcard_stop = [[[0 for x in range(0)] for y in range(max(frameend))] for z in range(len(video_list))]
        dentedcard_stop_index = [[0 for x in range(0)] for y in range(len(video_list))]
        tick_index = [[0 for x in range(0)] for y in range(len(video_list))]

        yolototal_index = [[0 for x in range(0)] for y in range(len(video_list))]
        employ_index = [[0 for x in range(0)] for y in range(len(video_list))]
        battle_index = [[0 for x in range(0)] for y in range(len(video_list))]
        EMOVE_INDEX = [[0 for x in range(0)] for y in range(len(video_list))]
        brann_putcard_index = [[0 for x in range(0)] for y in range(len(video_list))]
        dheropower_index = [[0 for x in range(0)] for y in range(len(video_list))]
        bang_index = [[0 for x in range(0)] for y in range(len(video_list))]
        bigbang_index = [[0 for x in range(0)] for y in range(len(video_list))]
        buffnumber = [[0 for x in range(0)] for y in range(len(video_list))]
        yogg_index = [[0 for x in range(0)] for y in range(len(video_list))]

        star_index = [[0 for x in range(0)] for y in range(len(video_list))]
        kelthuzad_index = [[0 for x in range(0)] for y in range(len(video_list))]
        jjiggregi_index = [[0 for x in range(0)] for y in range(len(video_list))]

        pyosi_index = [[0 for x in range(0)] for y in range(len(video_list))]
        sumgigi_index = [[0 for x in range(0)] for y in range(len(video_list))]
        chooseone_index = [[0 for x in range(0)] for y in range(len(video_list))]
        homz_index = [[0 for x in range(0)] for y in range(len(video_list))]

        SHinform_index = [[0 for x in range(0)] for y in range(len(video_list))]
        SI_index = [[0 for x in range(0)] for y in range(len(video_list))]
        donation_index = [[0 for x in range(0)] for y in range(len(video_list))]

        gamestart_index = [[0 for x in range(0)] for y in range(len(video_list))]
        gameend_index = [[0 for x in range(0)] for y in range(len(video_list))]
        gametogame_index = [[0 for x in range(0)] for y in range(len(video_list))]

        reconnecting_index = [[0 for x in range(0)] for y in range(len(video_list))]
        _3_index = [[0 for x in range(0)] for y in range(len(video_list))]

        # chapter 5
        # game start, game end
        gamestart = []
        gameend = []
        gamestart_constant = 0
        gameend_constant = framerate * 5
        zerotohalf_index = [[0 for x in range(0)] for y in range(len(video_list))]

        # ES, BS index
        ES_constant = framerate * 15
        BS_constant = framerate * 15
        EMPLOY_TO_BATTLE_MIN = framerate * 35
        EMPLOY_TO_BATTLE_MAX = framerate * 105
        ES_index = [[0 for i in range(0)] for j in range(len(video_list))]
        BS_index = [[0 for i in range(0)] for j in range(len(video_list))]
        fix_index = [[0 for i in range(0)] for j in range(len(video_list))]
        fix_house_index = [[0 for i in range(0)] for j in range(len(video_list))]

        # battles
        battle_to_atk_constant = framerate * 4
        battles = [[0 for i in range(0)] for i in range(len(video_list))]

        # EMOVE EXPANSION
        EXPANSION_CONSTANT = int(1.6 * framerate)
        EXPANSION_MINUS_CONSTANT = int(2.1 * framerate)
        
        EMOVE_INDEX_EXPANSION = [[0 for x in range(0)] for y in range(len(video_list))]
        EMOVE_INDEX_REVERSE = [[0 for x in range(0)] for y in range(len(video_list))]

        # star index
        STAR_MINUS_THRESHOLD = int(framerate * 0.5)
        star_constant = framerate * 5
        star_minustar_index = [[0 for x in range(0)] for y in range(len(video_list))]

        # sumgigi pyosi
        BALGYUN_THRESHOLD = int(framerate * 1.5)
        PYOSI_THRESHOLD = int(framerate * 0.5)
        BALGYUNEND_TO_DHEROPOWER_THRESHOLD_PLUS = int(framerate * 2.7) 
        BALGYUNEND_TO_DHEROPOWER_THRESHOLD_MINUS = int(framerate * 1)
        SUMPYO_index = [[0 for i in range(0)] for j in range(len(video_list))]
        SUMPYO_SE_index = [[0 for i in range(0)] for j in range(len(video_list))]
        SUMPYO_SEadj_index = [[0 for i in range(0)] for j in range(len(video_list))]
        balgyun_start = [[0 for i in range(0)] for j in range(len(video_list))]
        balgyun_end = [[0 for i in range(0)] for j in range(len(video_list))]
        pyosi_maxim = [[0 for i in range(0)] for j in range(len(video_list))]
        balgyunend_to_dheropower = [[0 for i in range(0)] for j in range(len(video_list))]

        # SCENE index
        SCENE_INDEX = [[0 for x in range(0)] for y in range(len(video_list))]

        # chapter 6
        # expansions
        EMPLOY_EXPANSION_CONSTANT = int( framerate * 3 )
        YOLOTOTAL_EXPANSION_THRESHOLD = int(1.5 * framerate)

        # dminion
        emove_but_nothing_index = [[0 for x in range(0)] for y in range(len(video_list))]
        NOTHING_THRESHOLD = int(framerate * 0.67)

        # kelthuzad
        kelthuzad_remove_index = [[0 for x in range(0)] for y in range(len(video_list))]
        BS_TURNOVER_THRESHOLD = int(framerate * 1.5)
        EALRY_POINT_THRESHOLD = int(framerate * 5)

        # early point
        early_point1 = [[0 for x in range(0)] for y in range(len(video_list))]
        early_point2 = [[0 for x in range(0)] for y in range(len(video_list))]
        early_point3 = [[0 for x in range(0)] for y in range(len(video_list))]
        early_point4 = [[0 for x in range(0)] for y in range(len(video_list))]

        # gamestart, game end
        HEROSELECT_THRESHOLD = int(framerate * 3)
        HEROSELECT_THRESHOLD_MINUS = int(framerate *1)
        ENDEND_THRESHOLD = int(framerate * 0.5)
        ENDEND_THRESHOLD_MINUS = int(framerate * 10)
        heroselect_index = [[0 for x in range(0)] for y in range(len(video_list))]
        endend_index = [[0 for x in range(0)] for y in range(len(video_list))]

        # reconnecting index
        reconend_index = [[0 for x in range(0)] for y in range(len(video_list))]

        # chapter 8
        # total index
        total_index = [[0 for x in range(0)] for y in range(len(video_list))]
        start_index = [[0 for x in range(0)] for y in range(len(video_list))]
        end_index = [[0 for x in range(0)] for y in range(len(video_list))]
        speak_threshold = []
        speak_threshold_star = []
        speak_threshold_startend = []
        audio = [[0 for x in range(0)] for y in range(len(video_list))]
        audio_speak_index = [[0 for x in range(0)] for y in range(len(video_list))]
        adjusted_start_index1 = [[0 for x in range(0)] for y in range(len(video_list))]
        adjusted_end_index1 = [[0 for x in range(0)] for y in range(len(video_list))]
        adjusted_start_index2 = [[0 for x in range(0)] for y in range(len(video_list))]
        adjusted_end_index2 = [[0 for x in range(0)] for y in range(len(video_list))]
        
        # audio
        DeleteAllFiles(current_path + "/pysrc/wav")
        start_index_second = [[0 for x in range(0)] for y in range(len(video_list))]
        end_index_second = [[0 for x in range(0)] for y in range(len(video_list))]
        start_index_frame = [[0 for x in range(0)] for y in range(len(video_list))]
        end_index_frame = [[0 for x in range(0)] for y in range(len(video_list))]
        rateframe = framerate / 60

        # chapter 12
        email_attatched = []











    for i in range(len(video_list)):
        # tryp
        try:
            user = who(video_list[i])
            print('user:', user)
            # check list length
            gamestart = check_listlength(gamestart, i)
            gameend = check_listlength(gameend, i)
            speak_threshold = check_listlength(speak_threshold, i)
            speak_threshold_star = check_listlength(speak_threshold_star, i)
            speak_threshold_startend = check_listlength(speak_threshold_startend, i)
            for j in range(len(yolo_list[i])):
                for k in range(len(yolo_list[i][j])):
                    if yolo_list[i][j][k][0] != '-' and yolo_list[i][j][k][0] != '2' \
                        and yolo_list[i][j][k][0] != '3'and yolo_list[i][j][k][0] != '26':
                        yolototal_index[i].append(j)
                        yolototal_index[i].sort

            for j in range(len(yolo_list[i])):
                for k in range(len(yolo_list[i][j])):
                    if yolo_list[i][j][k][0] == '2' and 0.47 < float(yolo_list[i][j][k][1]) < 0.57 and 0.15 < float(yolo_list[i][j][k][2]) < 0.25:
                        pass
                    elif yolo_list[i][j][k][0] == '0' or yolo_list[i][j][k][0] == '1' or yolo_list[i][j][k][0] == '4' or yolo_list[i][j][k][0] == '5' or \
                        yolo_list[i][j][k][0] == '6' or yolo_list[i][j][k][0] == '7' or yolo_list[i][j][k][0] == '8' or yolo_list[i][j][k][0] == '9' or \
                        yolo_list[i][j][k][0] == '10' or yolo_list[i][j][k][0] == '11' or yolo_list[i][j][k][0] == '12' or yolo_list[i][j][k][0] == '13' or \
                        yolo_list[i][j][k][0] == '14' or yolo_list[i][j][k][0] == '15' or yolo_list[i][j][k][0] == '16' or yolo_list[i][j][k][0] == '17' or \
                        yolo_list[i][j][k][0] == '18' or yolo_list[i][j][k][0] == '19' or yolo_list[i][j][k][0] == '20' or yolo_list[i][j][k][0] == '21' or \
                        yolo_list[i][j][k][0] == '22' or yolo_list[i][j][k][0] == '23' or yolo_list[i][j][k][0] == '24' or yolo_list[i][j][k][0] == '25' or \
                        yolo_list[i][j][k][0] == '26' or yolo_list[i][j][k][0] == '27' or yolo_list[i][j][k][0] == '28' or yolo_list[i][j][k][0] == '29' or \
                        yolo_list[i][j][k][0] == '30' or yolo_list[i][j][k][0] == '31' or yolo_list[i][j][k][0] == '32' or yolo_list[i][j][k][0] == '33' or \
                        yolo_list[i][j][k][0] == '34' or yolo_list[i][j][k][0] == '35' or yolo_list[i][j][k][0] == '36' or yolo_list[i][j][k][0] == '37':
                        pass
                    else:
                        if yolo_list[i][j][k][0] == '2' and float(yolo_list[i][j][k][5]) > 0.20:
                            dented_stop[i][j].append(yolo_list[i][j][k][1])
                            dented_stop[i][j].append(yolo_list[i][j][k][2])
                            dented_stop[i][j].append(yolo_list[i][j][k][3])
                            dented_stop[i][j].append(yolo_list[i][j][k][4])
                        if yolo_list[i][j][k][0] == '3' and float(yolo_list[i][j][k][5]) > 0.20:
                            dentedcard_stop[i][j].append(yolo_list[i][j][k][1])
                            dentedcard_stop[i][j].append(yolo_list[i][j][k][2])
                            dentedcard_stop[i][j].append(yolo_list[i][j][k][3])
                            dentedcard_stop[i][j].append(yolo_list[i][j][k][4])

            for j in range(len(yolo_list[i])):
                for k in range(len(yolo_list[i][j])):
                    if yolo_list[i][j][k][0] == '0' and 0.43 < float(yolo_list[i][j][k][2]) < 0.49 and float(yolo_list[i][j][k][5]) > 0.87:
                        employ_index[i].append(j)
                        employ_index[i].sort()
                    if yolo_list[i][j][k][0] == '1' and 0.43 < float(yolo_list[i][j][k][2]) < 0.49 and float(yolo_list[i][j][k][5]) > 0.87:
                        battle_index[i].append(j)
                        battle_index[i].sort()
                    if yolo_list[i][j][k][0] == '2' and float(yolo_list[i][j][k][5]) > 0.65:
                        # 1) 배치 두는 거 제한
                        # 2) 가끔 상점에 하수인이 하나만 남으면 dented minion이라고 판단하는 것 제거
                        if 0.50 < float(yolo_list[i][j][k][2]) < 0.67:
                            pass
                        elif 0.49 < float(yolo_list[i][j][k][1]) < 0.51 and 0.36 < float(yolo_list[i][j][k][2]) < 0.37 and \
                            0.06 < float(yolo_list[i][j][k][3]) < 0.08 and 0.15 < float(yolo_list[i][j][k][4]) < 0.18:
                            pass
                        # 3) 4/5번째 하수인
                        elif 0.57 < float(yolo_list[i][j][k][1]) < 0.58 and 0.378 < float(yolo_list[i][j][k][2]) < 0.382 and \
                            0.054 < float(yolo_list[i][j][k][3]) < 0.058 and 0.123 < float(yolo_list[i][j][k][4]) < 0.128:
                            pass
                        # 4) 5/5번째 하수인
                        elif 0.635 < float(yolo_list[i][j][k][1]) < 0.65 and 0.385 < float(yolo_list[i][j][k][2]) < 0.40 and \
                            0.058 < float(yolo_list[i][j][k][3]) < 0.065 and 0.127 < float(yolo_list[i][j][k][4]) < 0.14:
                            pass
                        # 3/6번째 하수인
                        elif 0.45 < float(yolo_list[i][j][k][1]) < 0.50 and 0.37 < float(yolo_list[i][j][k][2]) < 0.41 and \
                            0.06 < float(yolo_list[i][j][k][3]) < 0.07 and 0.12 < float(yolo_list[i][j][k][4]) < 0.155:
                            pass
                        # 상점 하수인 몽땅
                        elif 0.36 < float(yolo_list[i][j][k][2]) < 0.41 and \
                            0.054 < float(yolo_list[i][j][k][3]) < 0.07 and 0.12 < float(yolo_list[i][j][k][4]) < 0.155:
                            if user == 'matsuri':
                                pass
                            else:
                                EMOVE_INDEX[i].append(j)
                                EMOVE_INDEX[i].sort()             
                        else:
                            EMOVE_INDEX[i].append(j)
                            EMOVE_INDEX[i].sort()
                            _3_index[i].append(j)
                            _3_index[i].sort()

                    if yolo_list[i][j][k][0] == '3'and float(yolo_list[i][j][k][5]) > 0.75:
                        EMOVE_INDEX[i].append(j)
                        EMOVE_INDEX[i].sort()
                    if yolo_list[i][j][k][0] == '4':
                        if 0.56 < float(yolo_list[i][j][k][1]) < 0.63 and 0.73 < float(yolo_list[i][j][k][2]) < 0.80 and \
                            0.01 < float(yolo_list[i][j][k][3]) < 0.20 and 0.01 < float(yolo_list[i][j][k][4]) < 0.20:
                            EMOVE_INDEX[i].append(j)
                            EMOVE_INDEX[i].sort()
                            dheropower_index[i].append(j)
                            dheropower_index[i].sort()
                    if yolo_list[i][j][k][0] == '5'and float(yolo_list[i][j][k][5]) > 0.75:
                        EMOVE_INDEX[i].append(j)
                        EMOVE_INDEX[i].sort()
                    if yolo_list[i][j][k][0] == '5'and float(yolo_list[i][j][k][5]) > 0.60:
                        brann_putcard_index[i].append(j)
                        brann_putcard_index[i].sort()

                    if yolo_list[i][j][k][0] == '6':
                        EMOVE_INDEX[i].append(j)
                        EMOVE_INDEX[i].sort()
                    if yolo_list[i][j][k][0] == '7' and float(yolo_list[i][j][k][5]) > 0.80:
                        EMOVE_INDEX[i].append(j)
                        EMOVE_INDEX[i].sort()
                    if yolo_list[i][j][k][0] == '8':
                        EMOVE_INDEX[i].append(j)
                        EMOVE_INDEX[i].sort()
                    if yolo_list[i][j][k][0] == '9' and float(yolo_list[i][j][k][5]) > 0.90:
                        EMOVE_INDEX[i].append(j)
                        EMOVE_INDEX[i].sort()
                    if yolo_list[i][j][k][0] == '10' and float(yolo_list[i][j][k][5]) > 0.80:
                        EMOVE_INDEX[i].append(j)
                        EMOVE_INDEX[i].sort()
                    if yolo_list[i][j][k][0] == '11' and float(yolo_list[i][j][k][5]) > 0.80:
                        buffnumber[i].append(j)
                        buffnumber[i].sort()
                        EMOVE_INDEX[i].append(j)
                        EMOVE_INDEX[i].sort()
                    if yolo_list[i][j][k][0] == '12':
                        EMOVE_INDEX[i].append(j)
                        EMOVE_INDEX[i].sort()
                    if yolo_list[i][j][k][0] == '13' and float(yolo_list[i][j][k][5]) > 0.60:
                        EMOVE_INDEX[i].append(j)
                        EMOVE_INDEX[i].sort()      
                    if yolo_list[i][j][k][0] == '14':
                        EMOVE_INDEX[i].append(j)
                        EMOVE_INDEX[i].sort()
                    if yolo_list[i][j][k][0] == '15':
                        EMOVE_INDEX[i].append(j)
                        EMOVE_INDEX[i].sort()
                    if yolo_list[i][j][k][0] == '16' and float(yolo_list[i][j][k][5]) > 0.75:
                        if 0.40< float(yolo_list[i][j][k][2]) < 0.50 and \
                            float(yolo_list[i][j][k][3]) < 0.10 and \
                                float(yolo_list[i][j][k][4]) < 0.10:
                                pass
                        else: 
                            EMOVE_INDEX[i].append(j)
                            EMOVE_INDEX[i].sort()
                    if yolo_list[i][j][k][0] == '17' and float(yolo_list[i][j][k][5]) > 0.75:
                        EMOVE_INDEX[i].append(j)
                        EMOVE_INDEX[i].sort()
                    if yolo_list[i][j][k][0] == '18':
                        EMOVE_INDEX[i].append(j)
                        EMOVE_INDEX[i].sort()
                    if yolo_list[i][j][k][0] == '19':
                        EMOVE_INDEX[i].append(j)
                        EMOVE_INDEX[i].sort()
                        bang_index[i].append(j)
                    if yolo_list[i][j][k][0] == '20' and float(yolo_list[i][j][k][5]) > 0.72:
                        if float(yolo_list[i][j][k][1]) < 0.60 and float(yolo_list[i][j][k][2]) > 0.45: 
                            if not 0.47 < float(yolo_list[i][j][k][1]) < 0.52 and 0.64 < float(yolo_list[i][j][k][2]) < 0.69 and \
                                0.01 < float(yolo_list[i][j][k][3]) < 0.04 and 0.03 < float(yolo_list[i][j][k][4]) < 0.07:
                                bigbang_index[i].append(j)
                                bigbang_index[i].sort()
                    if yolo_list[i][j][k][0] == '21' and float(yolo_list[i][j][k][5]) > 0.71:
                        star_index[i].append(j)
                        star_index[i].sort()
                    if yolo_list[i][j][k][0] == '22':
                        kelthuzad_index[i].append(j)
                        kelthuzad_index[i].sort()
                    if yolo_list[i][j][k][0] == '23':
                        jjiggregi_index[i].append(j)
                        jjiggregi_index[i].sort()

                    # pyosi, sumgigi
                    if yolo_list[i][j][k][0] == '24':
                        if 0.25 < float(yolo_list[i][j][k][1]) < 0.32 and 0.60 < float(yolo_list[i][j][k][2]) < 0.82 and \
                            0.02 < float(yolo_list[i][j][k][3]) < 0.08 and 0.01 < float(yolo_list[i][j][k][4]) < 0.05:
                            pyosi_index[i].append(j)  #0822 0.3 -> 0.32 / 0.7 -> 0.6
                            pyosi_index[i].sort()
                    if yolo_list[i][j][k][0] == '25':
                        if 0.25 < float(yolo_list[i][j][k][1]) < 0.32 and 0.55 < float(yolo_list[i][j][k][2]) < 0.82 and \
                            0.02 < float(yolo_list[i][j][k][3]) < 0.08 and 0.01 < float(yolo_list[i][j][k][4]) < 0.05:
                            sumgigi_index[i].append(j) #0822 0.3 -> 0.32 / 0.7 -> 0.55
                            sumgigi_index[i].sort()      

                    if yolo_list[i][j][k][0] == '26':
                        SHinform_index[i].append(j)
                        SHinform_index[i].sort()
                    if yolo_list[i][j][k][0] == '27':
                        SI_index[i].append(j)
                        SI_index[i].sort()
                    if yolo_list[i][j][k][0] == '28':
                        donation_index[i].append(j)
                        donation_index[i].sort()

                    if yolo_list[i][j][k][0] == '29':
                        if 0.45 < float(yolo_list[i][j][k][1]) < 0.55 and 0.75 < float(yolo_list[i][j][k][2]) < 0.85 and \
                            0.01 < float(yolo_list[i][j][k][3]) < 0.07 and 0.01 < float(yolo_list[i][j][k][4]) < 0.10:
                            gamestart_index[i].append(j)
                            gamestart_index[i].sort()
                    if yolo_list[i][j][k][0] == '30':
                        if 0.45 < float(yolo_list[i][j][k][1]) < 0.55 and 0.35 < float(yolo_list[i][j][k][2]) < 0.45 and float(yolo_list[i][j][k][5]) > 0.80:
                            gameend_index[i].append(j)
                            gameend_index[i].sort()  

                    if yolo_list[i][j][k][0] == '31':
                        gametogame_index[i].append(j)
                        gametogame_index[i].sort()

                    if yolo_list[i][j][k][0] == '32':
                        if 0.45 < float(yolo_list[i][j][k][1]) < 0.55 and 0.45 < float(yolo_list[i][j][k][2]) < 0.55 and \
                            0.30 < float(yolo_list[i][j][k][3]) < 0.50 and 0.15 < float(yolo_list[i][j][k][4]) < 0.35 and float(yolo_list[i][j][k][5]) > 0.70:
                            reconnecting_index[i].append(j)
                            reconnecting_index[i].sort()     

                    if yolo_list[i][j][k][0] == '33' and float(yolo_list[i][j][k][5]) > 0.70:
                        EMOVE_INDEX[i].append(j)
                        EMOVE_INDEX[i].sort()
                        yogg_index[i].append(j)
                        yogg_index[i].sort()
                    if yolo_list[i][j][k][0] == '34' and float(yolo_list[i][j][k][5]) > 0.70:
                        EMOVE_INDEX[i].append(j)
                        EMOVE_INDEX[i].sort()
                    if yolo_list[i][j][k][0] == '35' and float(yolo_list[i][j][k][5]) > 0.70:
                        EMOVE_INDEX[i].append(j)
                        EMOVE_INDEX[i].sort() 

                    if yolo_list[i][j][k][0] == '36' and float(yolo_list[i][j][k][5]) > 0.50:
                        chooseone_index[i].append(j)
                        chooseone_index[i].sort()
                    if yolo_list[i][j][k][0] == '37' and float(yolo_list[i][j][k][5]) > 0.50:
                        homz_index[i].append(j)
                        homz_index[i].sort() 

            print('_3_index')
            print(_3_index[i])

            print("reconnecting_index[i]")
            print(reconnecting_index[i])

            print("employ_index[i]", video_list[i])
            print(employ_index[i])
            print("battle_index[i]", video_list[i])
            print(battle_index[i])

            print("yolototal_index[i]")
            print(yolototal_index[i])

            print("bang_index[i]")
            print(bang_index[i])

            print("bigbang_index[i]")
            print(bigbang_index[i])
            
            EMOVE_INDEX[i] = set_list_sort(EMOVE_INDEX[i])
            print("EMOVE_INDEX[i]")
            print(EMOVE_INDEX[i])
            print("gameend_index[i]")
            print(gameend_index[i])


            """
            0. ADD GAME START, GAME END
            1. REMOVE NOT EMOVE INDEX
            2. ADD BTE_INDEX
            3. REMOVE STAR_INDEX
            4. 
            """
            # 5. SCENE INDEX
            # 5-0. game start, game end
            for j in range(0, int(frameend[i]/2)):
                zerotohalf_index[i].append(j)
            for j in zerotohalf_index[i]:
                while j in gametogame_index[i]:
                    gametogame_index[i].remove(j)

            print("gametogame_index")
            print(gametogame_index)
            print('gameend_index')
            print(gameend_index[i])

            if len(gameend_index[i]) == 0:
                try:
                    for j in gametogame_index[i]:
                        guess_gameend = j - 7 * framerate
                        gameend_index[i].append(guess_gameend)
                except:
                    pass
            if len(gameend_index[i]) == 0:
                guess_gameend = math.floor(framerate * (videopy[i].end - 7))
                gameend_index[i].append(guess_gameend)

            if len(gamestart_index[i]) == 0:
                gamestart_index[i].append(0)

                
            while max(gamestart_index[i]) > frameend[i] / 2 :
                gamestart_index[i].pop()
            while min(gameend_index[i]) < frameend[i] / 2:
                del gameend_index[i][0]
                if len(gameend_index[i]) == 0:
                    gameend_index[i].append(frameend[i])
                    break

            print(gameend_index[i])

            if len(gamestart_index[i]) != 0:
                gamestart.append(max(gamestart_index[i]) + gamestart_constant)
            else:
                gamestart.append(0)

            if len(gameend_index[i]) == 0 and len(gametogame_index[i]) == 0:
                gameend_index[i].append(frameend[i])
            elif len(gameend_index[i]) == 0 and len(gametogame_index[i]) != 0:
                gameend_index[i].append(min(gametogame_index[i]))
            elif len(gameend_index[i]) != 0:
                gameend.append(max(gameend_index[i]) + gameend_constant)
            else:
                gameend.append(frameend[i])

            print("game start, game end")
            print(gamestart[i])
            print(gameend[i])

            # 5-1. find heropower
            gamestart_second = gamestart[i] / framerate
            try:
                heropower = find_heropower(video_list[i], gamestart_second)
                print('heropower:', heropower)
                hero = what_hero(heropower)
            except:
                heropower = None
                hero = '_0_'        #_2_에서 _0_로변경 23.10.29
            # 5-1-1. find anomalies. #only 변형물
            try:
                gamestart_second = gamestart[i] / framerate
                anomalies = find_anomalies(video_list[i], gamestart_second)
                print('anomalies:',anomalies)    
            except:
                anomalies = False
            # 5-1-2 trim edge
            yolototal_index[i] = trim_edge(gamestart[i], gameend[i], yolototal_index[i])
            employ_index[i] = trim_edge(gamestart[i], gameend[i], employ_index[i])
            battle_index[i] = trim_edge(gamestart[i], gameend[i], battle_index[i])
            bang_index[i] = trim_edge(gamestart[i], gameend[i], bang_index[i])
            bigbang_index[i] = trim_edge(gamestart[i], gameend[i], bigbang_index[i])
            star_index[i] = trim_edge(gamestart[i], gameend[i], star_index[i])
            jjiggregi_index[i] = trim_edge(gamestart[i], gameend[i], jjiggregi_index[i])
            pyosi_index[i] = trim_edge(gamestart[i], gameend[i], pyosi_index[i])
            sumgigi_index[i] = trim_edge(gamestart[i], gameend[i], sumgigi_index[i])
            SHinform_index[i] = trim_edge(gamestart[i], gameend[i], SHinform_index[i])
            SI_index[i] = trim_edge(gamestart[i], gameend[i], SI_index[i])
            donation_index[i] = trim_edge(gamestart[i], gameend[i], donation_index[i])
            reconnecting_index[i] = trim_edge(gamestart[i], gameend[i], reconnecting_index[i])
            EMOVE_INDEX[i] = trim_edge(gamestart[i], gameend[i], EMOVE_INDEX[i])
            star_index[i] = trim_edge(gamestart[i], gameend[i], star_index[i])
            print('reconnecting_index2')
            print(reconnecting_index)

            # 5-2-0. 가끔 battle에서 employ, employ에서 battle 뜨는 문제 해결
            employ_noise = []
            battle_noise = []
            for j in range(1, len(employ_index[i])-1):
                if employ_index[i][j] - employ_index[i][j-1] != 1 and employ_index[i][j+1] - employ_index[i][j] != 1:
                    employ_noise.append(employ_index[i][j])
            for j in range(1, len(battle_index[i])-1):
                if battle_index[i][j] - battle_index[i][j-1] != 1 and battle_index[i][j+1] - battle_index[i][j] != 1:
                    battle_noise.append(battle_index[i][j])
            
            employ_index[i] = index_remove(employ_index[i], employ_noise)
            battle_index[i] = index_remove(battle_index[i], battle_noise)

            # 5-2-1. battle to employ
            ES_index[i].append(employ_index[i][0])
            for j in range(len(employ_index[i])-1):
                if employ_index[i][j+1] - employ_index[i][j] > ES_constant:
                    ES_index[i].append(employ_index[i][j+1])

            BS_index[i].append(battle_index[i][0])
            for j in range(len(battle_index[i])-1):
                if battle_index[i][j+1] - battle_index[i][j] > BS_constant:
                    BS_index[i].append(battle_index[i][j+1])

            print(ES_index[i], gameend[i])
            print("BS_index")
            print(BS_index)
            print("ES_index")
            print(ES_index)

            BEINDEX = 0
            BETRUE = False
            try:
                for j in range(len(BS_index[i])):
                    if ES_index[i][j] < BS_index[i][j] < ES_index[i][j+1]:
                        BEINDEX += 1
                if BEINDEX == len(BS_index[i]):
                    BETRUE = True
            except:
                pass
                
            if BETRUE:
                pass
            else: 
                BS_expand = index_exapnd(BS_index[i], 20 * framerate, 20 * framerate)
                ES_expand = index_exapnd(ES_index[i], 20 * framerate, 20 * framerate)
                cvBE_index = find_battles_second(video_list[i],input_path , screenshot)
                cvBE_index = [j*framerate for j in cvBE_index]
                print('cvBE_index', cvBE_index)
                for j in range(len(cvBE_index)):
                    if j % 2 == 0:
                        if not cvBE_index[j] in BS_expand:
                            BS_index[i].append(cvBE_index[j])
                            BS_index[i] = set_list_sort(BS_index[i])
                    else:
                        if not cvBE_index[j] in ES_expand:
                            ES_index[i].append(cvBE_index[j])
                            ES_index[i] = set_list_sort(ES_index[i])

            # ES, BS 1턴, 마지막턴 없을때 예외처리
            print("BS_index_modified")
            print(BS_index)
            print("ES_index_modified")
            print(ES_index)

            ESmia_1turn = 0
            ESmia_lasturn = 0
            if len(BS_index[i]) == len(ES_index[i]):
                for j in range(len(BS_index[i])):
                    if BS_index[i][j] < ES_index[i][j]:
                        ESmia_1turn += 1
                for j in range(len(BS_index[i])):
                    if BS_index[i][j] > ES_index[i][j]:
                        ESmia_lasturn += 1

            if ESmia_1turn == len(BS_index[i]):
                print('1turn ESmia')
                ES_index[i].append(min(EMOVE_INDEX[i])-2)
                ES_index[i] = set_list_sort(ES_index[i])
            if ESmia_lasturn == len(BS_index[i]):
                print('last turn ESmia')
                ES_index[i].append(max(star_index[i])+8)

            try:
                # ES_index 한 개 없을 경우
                if len(BS_index[i]) == len(ES_index[i]):
                    breaker = False
                    if ES_index[i][0] < BS_index[i][0]:
                        for k in range(BS_index[i][1]- EMPLOY_TO_BATTLE_MAX , BS_index[i][1]- EMPLOY_TO_BATTLE_MIN):
                            fix_index[i].append(k)
                    for j in range(1, len(BS_index[i])):
                        if ES_index[i][j] > BS_index[i][j]:
                            for k in range(BS_index[i][j-1] , BS_index[i][j]):
                                fix_index[i].append(k)
                            breaker = True
                            break
                        if breaker == True:
                            break

                    print('fix_index')
                    print(fix_index)

                    for j in fix_index[i]:
                        for k in SI_index[i]:
                            if j == k:
                                fix_house_index[i].append(k)
                    for j in fix_index[i]:
                        for k in reconnecting_index[i]:
                            if j == k:
                                fix_house_index[i].append(k)

                    print("fix_house_index")
                    print(fix_house_index)
                    ES_index[i].append(max(fix_house_index[i]))
                    ES_index[i].sort()

                # BS_index 한 개 없을 경우
                elif len(BS_index[i]) + 2 == len(ES_index[i]):
                    for j in range(len(BS_index[i])):
                        if BS_index[i][j] > ES_index[i][j+1]:
                            for k in range(ES_index[i][j]+ EMPLOY_TO_BATTLE_MIN , ES_index[i][j] + EMPLOY_TO_BATTLE_MAX):
                                fix_index[i].append(k) 
                    for j in fix_index[i]:
                        for k in SI_index[i]:
                            if j == k:
                                fix_house_index[i].append(k)
                    for j in fix_index[i]:
                        for k in reconnecting_index[i]:
                            if j == k:
                                fix_house_index[i].append(k)
                    print("fix_house_index")
                    print(fix_house_index[i])
                    print(max(fix_house_index[i]))
                    BS_index[i].append(max(fix_house_index[i]))
                    BS_index[i].sort()
            except:
                if len(BS_index[i]) == len(ES_index[i]):
                    for j in BS_index[i]:
                        for k in ES_index[i]:
                            if abs(j-k) < framerate * 5:
                                BS_index[i].remove(j)
                elif len(BS_index[i]) + 2 == len(ES_index[i]):
                    for j in BS_index[i]:
                        for k in ES_index[i]:
                            if abs(j-k) < framerate * 5:
                                ES_index[i].remove(k)

            
            
            print("ES, BS indexes final")
            print(ES_index[i])
            print(BS_index[i])

            print("SI_index")
            print(SI_index[i])

            print("reconnecting_index")
            print(reconnecting_index[i])

            # 5-2-2. battles
            for j in range(len(BS_index[i])):
                for k in range(BS_index[i][j] + battle_to_atk_constant, ES_index[i][j+1]):
                    battles[i].append(k)

            print("battles")
            print(battles[i])

            # 5-3. dented stop & fucking dminions
            print('dented_stop')
            print(dented_stop[i])

            for j in range(len(dented_stop[i])-1):
                if len(dented_stop[i][j]) == 4 and len(dented_stop[i][j+1]) == 4:
                    _x = abs(float(dented_stop[i][j+1][0]) - float(dented_stop[i][j][0]))
                    _y = abs(float(dented_stop[i][j+1][1]) - float(dented_stop[i][j][1]))
                    _w = abs(float(dented_stop[i][j+1][2]) - float(dented_stop[i][j][2]))
                    _h = abs(float(dented_stop[i][j+1][3]) - float(dented_stop[i][j][3]))
                    if _x > 0.01 and _y > 0.01 and _w > 0.01 and _h > 0.01:
                        pass
                    else: 
                        dented_stop_index[i].append(j)
                        dented_stop_index[i].append(j+1)

                if len(dentedcard_stop[i][j]) == 4 and len(dentedcard_stop[i][j+1]) == 4:
                    _x_ = abs(float(dentedcard_stop[i][j+1][0]) - float(dentedcard_stop[i][j][0]))
                    _y_ = abs(float(dentedcard_stop[i][j+1][1]) - float(dentedcard_stop[i][j][1]))
                    _w_ = abs(float(dentedcard_stop[i][j+1][2]) - float(dentedcard_stop[i][j][2]))
                    _h_ = abs(float(dentedcard_stop[i][j+1][3]) - float(dentedcard_stop[i][j][3]))
                    if _x_ > 0.01 and _y_ > 0.01 and _w_ > 0.01 and _h_ > 0.01:
                        pass
                    else: 
                        dentedcard_stop_index[i].append(j)
                        dentedcard_stop_index[i].append(j+1)

            for j in range(len(dented_stop[i])):
                if len(dented_stop[i][j]) == 4 or len(dented_stop[i][j]) == 8:
                    _y = float(dented_stop[i][j][1])
                    _w = float(dented_stop[i][j][2])
                    _h = float(dented_stop[i][j][3])
                    if 0.33 < _y < 0.40 and 0.05 < _w < 0.09 and 0.15 < _h < 0.20:
                        tick_index[i].append(j)

            print('tick_index')
            print(tick_index)
            # 5-3-1. dented start end
            dented_stop_index[i] = set_list_sort(dented_stop_index[i])
            dentedcard_stop_index[i] = set_list_sort(dentedcard_stop_index[i])
            
            try:
                dented_start_end = start_end(dented_stop_index[i])
                remove_dented = []
                for j in range(len(dented_start_end)-1):
                    if j % 2 == 0:
                        if dented_start_end[j+1] - dented_start_end[j] > framerate * 1.5:
                            print(dented_start_end[j+1], dented_start_end[j])
                            for k in range(int(dented_start_end[j] + framerate * 0.5), int(dented_start_end[j+1] - framerate * 0.5)):
                                remove_dented.append(k)
            except:
                print('dented minion is None')
                pass

            try:
                dentedcard_start_end = start_end(dentedcard_stop_index[i])       
                remove_dentedcard = []
                for j in range(len(dentedcard_start_end)-1):
                    if j % 2 == 0:
                        if dentedcard_start_end[j+1] - dentedcard_start_end[j] > framerate * 1.5:
                            print(dentedcard_start_end[j+1], dentedcard_start_end[j])
                            for k in range(int(dentedcard_start_end[j] + framerate * 0.5), int(dentedcard_start_end[j+1] - framerate * 0.5)):
                                remove_dentedcard.append(k)
            except:
                print('dented card is None')
                pass


            # 5-3-3. tick(상점) 삭제
            index_remove(EMOVE_INDEX[i], tick_index[i])

            # 5-3-??. append yogg index
            yogg_index[i] = trim_edge(gamestart[i], gameend[i], yogg_index[i])
            yogg_expand = index_exapnd(yogg_index[i], int(1 * framerate), int(3 * framerate))
            print('yogg_index')
            print(yogg_expand)

            # 5-4-1. trim for shine
            # 5-4-2. trim for last kelthuzad
            EMOVE_INDEX[i] = trim_edge(ES_index[i][0], gameend[i], EMOVE_INDEX[i])
            kelthuzad_index[i] = trim_edge(gamestart[i], BS_index[i][len(BS_index[i])-1], kelthuzad_index[i])
            dheropower_index[i] = trim_edge(ES_index[i][0], gameend[i], dheropower_index[i])

            # 5-4-2. EMOVE INDEX EXPANSION
            for j in EMOVE_INDEX[i]:
                for k in range(-EXPANSION_MINUS_CONSTANT, EXPANSION_CONSTANT):
                    EMOVE_INDEX_EXPANSION[i].append(j+k)

                # dheropower_index add
            for j in dheropower_index[i]:
                for k in range(-EXPANSION_MINUS_CONSTANT, EXPANSION_CONSTANT + int(framerate * 2)):
                    EMOVE_INDEX_EXPANSION[i].append(j+k)
            
            

            EMOVE_INDEX_EXPANSION[i] = set_list_sort(EMOVE_INDEX_EXPANSION[i])
            print(EMOVE_INDEX_EXPANSION[i])

            while min(EMOVE_INDEX_EXPANSION[i]) < 0 :
                del EMOVE_INDEX_EXPANSION[i][0]
            while max(EMOVE_INDEX_EXPANSION[i]) > frameend[i]: 
                EMOVE_INDEX_EXPANSION[i].pop()

            for j in range(frameend[i]):
                if j in EMOVE_INDEX_EXPANSION[i]:
                    pass
                else:
                    EMOVE_INDEX_REVERSE[i].append(j)

            print("EMOVE_INDEX_REVERSE")
            print(EMOVE_INDEX_REVERSE[i])


            # 5-5. star index
            star_index[i] = set_list_sort(star_index[i])
            for j in range(len(star_index[i])-1):
                if star_index[i][j+1]- star_index[i][j] < star_constant:
                    for k in range(star_index[i][j] , star_index[i][j+1]):
                        star_index[i].append(k)
                        star_index[i] = set_list_sort(star_index[i])

            print("star_index")
            print(star_index[i])

            # 5-5-2. 
            star_house_index = [[0 for x in range(0)] for y in range(len(BS_index[i]))]
            for j in range(len(BS_index[i])):
                for k in range(ES_index[i][j+1] - framerate * 9, ES_index[i][j+1]):
                    for l in star_index[i]:
                        if l == k:
                            star_house_index[j].append(k)
            for j in range(len(star_house_index)):
                if len(star_house_index[j]) != 0:
                    for k in range(min(star_house_index[j]), max(star_house_index[j]) - STAR_MINUS_THRESHOLD):
                        star_minustar_index[i].append(k)

            # 5-6. SUMGIGI PYOSI
            if heropower == '_2_professor.png':
                FINEADJUSTMENT_THRESHOLD = 1.1
            else:
                FINEADJUSTMENT_THRESHOLD = int(framerate * 1.5)

            for j in sumgigi_index[i]:
                SUMPYO_index[i].append(j)
            for j in pyosi_index[i]:
                SUMPYO_index[i].append(j)
            for j in chooseone_index[i]:
                SUMPYO_index[i].append(j)
            for j in homz_index[i]:
                SUMPYO_index[i].append(j)
            
            SUMPYO_index[i] = set_list_sort(SUMPYO_index[i])
            print("SUMPYO_index")
            print(SUMPYO_index)
            
            try:
                SUMPYO_SE_index[i].append(SUMPYO_index[i][0])
                for j in range(len(SUMPYO_index[i])-1):
                    if SUMPYO_index[i][j+1] - SUMPYO_index[i][j] < FINEADJUSTMENT_THRESHOLD:
                        for k in range(SUMPYO_index[i][j], SUMPYO_index[i][j+1]):
                            for l in SHinform_index[i]:
                                if k == l:
                                    pass
                    else:
                        SUMPYO_SE_index[i].append(SUMPYO_index[i][j])
                        SUMPYO_SE_index[i].append(SUMPYO_index[i][j+1])
                SUMPYO_SE_index[i].append(SUMPYO_index[i][len(SUMPYO_index[i])-1]) 

                for j in range(len(SUMPYO_SE_index[i])-1):
                    if SUMPYO_SE_index[i][j+1] - SUMPYO_SE_index[i][j] < BALGYUN_THRESHOLD:
                        for k in range(SUMPYO_SE_index[i][j] +1, SUMPYO_SE_index[i][j+1]):
                            for l in SHinform_index[i]:
                                if k == l:
                                    SUMPYO_SEadj_index[i].append(k)

                SUMPYO_SE_index_dup = [x for j, x in enumerate(SUMPYO_SE_index[i]) if j != SUMPYO_SE_index[i].index(x)]
                print('SUMPYO_SE_index')
                print(SUMPYO_SE_index)
                print('SUMPYO_SE_index_dup')
                print(SUMPYO_SE_index_dup)
                print('SUMPYO_SEadj_index')
                print(SUMPYO_SEadj_index)

                for j in SUMPYO_SEadj_index[i]:
                    if j not in SUMPYO_SE_index_dup:
                        while j in SUMPYO_SE_index[i]:
                            SUMPYO_SE_index[i].remove(j)
                    else:
                        if j in SUMPYO_SE_index[i]:
                            SUMPYO_SE_index[i].remove(j)

                for j in range(len(SUMPYO_SE_index[i])):
                    if j % 2 == 0:
                        balgyun_start[i].append(SUMPYO_SE_index[i][j])
                    else:
                        balgyun_end[i].append(SUMPYO_SE_index[i][j])

                print(balgyun_start)
                print(balgyun_end)
                print(pyosi_index)

                pyosi_house_index = [[0 for x in range(0)] for y in range(len(balgyun_start[i]))]
                for j in range(len(balgyun_start[i])):
                    for k in range(balgyun_start[i][j], balgyun_end[i][j]):
                        for l in pyosi_index[i]:
                            if l == k:
                                pyosi_house_index[j].append(k)

                print("pyosi_house_index")
                print(pyosi_house_index)

                for j in range(len(pyosi_house_index)):
                    if len(pyosi_house_index[j]) > framerate:
                        for k in range(min(pyosi_house_index[j])+ PYOSI_THRESHOLD, max(pyosi_house_index[j]) - PYOSI_THRESHOLD):
                            pyosi_maxim[i].append(k)
                for j in range(len(balgyun_end[i])):
                    for k in range(balgyun_end[i][j]-BALGYUNEND_TO_DHEROPOWER_THRESHOLD_PLUS, balgyun_end[i][j]+BALGYUNEND_TO_DHEROPOWER_THRESHOLD_PLUS):
                        balgyunend_to_dheropower[i].append(k)
            except:
                print('발견 갯수: 0')
                pass

            # 5-7. find brann
            newminion_cut(patchday='_brann')
            _brann_list = []
            battle_brann = []
            _sum_brann = []
            for j in range(len(BS_index[i])):
                sec = (BS_index[i][j] + 3 * framerate) / framerate
                sec_frame = int( sec * 60 )
                _brann_list = newminion_detect(video_list[i], input_path, sec, patchday='_brann', forbrann='True')
                if '_brann_.png' in _brann_list:
                    battle_brann.append('brann_is_here')
                else:
                    battle_brann.append('-')
            
            print('battle_brann', battle_brann)
            print('brann_putcard_index',brann_putcard_index[i])

            brann_putcard_index[i] = trim_edge(gamestart[i], gameend[i], brann_putcard_index[i])
            for j in range(len(battle_brann)-1):
                if battle_brann[j] == '-':
                    pass
                else:
                    _split_brann = remove_not_between(brann_putcard_index[i], ES_index[i][j], ES_index[i][j+2])
                    print(_split_brann)
                    print(brann_putcard_index[i])
                    _sum_brann += _split_brann

            _sum_brann = index_exapnd(_sum_brann, int(1 * framerate), int(3 * framerate))

            
            print('sum_brann', _sum_brann)

            # 6. merge to SCENE INDEX
            index_range_append(SCENE_INDEX[i], gamestart[i], gameend[i])
            index_remove(SCENE_INDEX[i], EMOVE_INDEX_REVERSE[i])
            index_append(SCENE_INDEX[i], battles[i])
            index_remove(SCENE_INDEX[i], star_minustar_index[i])
            index_remove(SCENE_INDEX[i], pyosi_maxim[i])
                # yogg_add
                # sum_brann_add
            index_append(SCENE_INDEX[i], yogg_expand)
            index_append(SCENE_INDEX[i], _sum_brann)
            SCENE_INDEX[i] = set_list_sort(SCENE_INDEX[i])

            # 6-2. employ expansion
            for j in range(1,len(ES_index[i])):
                for k in range(ES_index[i][j]- EMPLOY_EXPANSION_CONSTANT, ES_index[i][j] + EMPLOY_EXPANSION_CONSTANT):
                    SCENE_INDEX[i].append(k)

            # 6-?. balgyunend_to_dheropower
            for j in balgyunend_to_dheropower[i]:
                SCENE_INDEX[i].append(j)
                SCENE_INDEX[i] = set_list_sort(SCENE_INDEX[i])

            # 6-3-0. keltuzhad 
            print('kelthuzad_index')
            print(kelthuzad_index)
            kelthuzad_house_index = [[0 for x in range(0)] for y in range(len(BS_index[i]))]
            for j in range(len(BS_index[i])):
                for k in range(BS_index[i][j], ES_index[i][j+1]):
                    for l in kelthuzad_index[i]:
                        if l == k:
                            kelthuzad_house_index[j].append(k)

            print("kelthuzad_house_index")
            print(kelthuzad_house_index)

            not_display_minion = []
            for j in range(len(kelthuzad_house_index)):
                if len(kelthuzad_house_index[j]) > 3 * framerate:
                    not_display_minion.append(j)
                    if len(star_house_index[j]) != 0:
                        for k in range(BS_index[i][j]+ BS_TURNOVER_THRESHOLD, max(star_house_index[j]) - STAR_MINUS_THRESHOLD):
                            kelthuzad_remove_index[i].append(k)
                    else: 
                        for k in range(BS_index[i][j]+ BS_TURNOVER_THRESHOLD, ES_index[i][j+1] - int(2.5 * framerate)):
                            kelthuzad_remove_index[i].append(k)

            for j in kelthuzad_remove_index[i]:
                while j in SCENE_INDEX[i]:
                    SCENE_INDEX[i].remove(j)

            """
            employ: 1턴 / 2턴 삭제
            battle: 1턴 / 2턴 / 3턴 / 4턴 스킵
            """
            # 6-3-1. early point
            # 1턴
            hero = '_0_'
            if hero == '_0_':
                if len(star_house_index[0]) != 0:
                    for j in range(BS_index[i][0], max(star_house_index[0])-STAR_MINUS_THRESHOLD):
                        early_point3[i].append(j)
                else:
                    for j in range(BS_index[i][0], ES_index[i][1]):
                        early_point3[i].append(j)
            else:
                for j in range(ES_index[i][0]-EALRY_POINT_THRESHOLD, ES_index[i][1]):
                    early_point1[i].append(j)
            # 2턴
            if hero == '_0_' or hero == '_1_':
                if len(star_house_index[1]) != 0:
                    for j in range(BS_index[i][1], max(star_house_index[1])-STAR_MINUS_THRESHOLD):
                        early_point3[i].append(j)
                else:
                    for j in range(BS_index[i][1], ES_index[i][2]):
                        early_point3[i].append(j)
            else:
                for j in range(ES_index[i][1], ES_index[i][2]):
                    early_point2[i].append(j)
            # 3턴
            if len(star_house_index[2]) != 0:
                for j in range(BS_index[i][2], max(star_house_index[2])-STAR_MINUS_THRESHOLD):
                    early_point3[i].append(j)
            else:
                for j in range(BS_index[i][2], ES_index[i][3]):
                    early_point3[i].append(j)
            # 4턴
            if len(star_house_index[3]) != 0:
                for j in range(BS_index[i][3], max(star_house_index[3])-STAR_MINUS_THRESHOLD):
                    early_point4[i].append(j)
            else:
                for j in range(BS_index[i][3], ES_index[i][4]):
                    early_point4[i].append(j)

            # 6-3-2. early point remove

            SCENE_INDEX[i] = index_remove(SCENE_INDEX[i], early_point1[i])
            SCENE_INDEX[i] = index_remove(SCENE_INDEX[i], early_point2[i])
            SCENE_INDEX[i] = index_remove(SCENE_INDEX[i], early_point3[i])
            SCENE_INDEX[i] = index_remove(SCENE_INDEX[i], early_point4[i])

            # 6-4. game_start / game end
            for j in range(gamestart[i]-HEROSELECT_THRESHOLD_MINUS, gamestart[i]+HEROSELECT_THRESHOLD):
                heroselect_index[i].append(j)
            for j in range(gameend[i]-ENDEND_THRESHOLD_MINUS, gameend[i]+ENDEND_THRESHOLD):
                endend_index[i].append(j)

            # 6-4-2. game_start / game end to scene
            for j in heroselect_index[i]:
                SCENE_INDEX[i].append(j)
                SCENE_INDEX[i] = set_list_sort(SCENE_INDEX[i])
            for j in endend_index[i]:
                SCENE_INDEX[i].append(j)
                SCENE_INDEX[i] = set_list_sort(SCENE_INDEX[i])

            # 6-4-3. game_start / game_end fuck
            for j in range(0, gamestart[i]-HEROSELECT_THRESHOLD_MINUS):
                while j in SCENE_INDEX[i]:
                    SCENE_INDEX[i].remove(j)
            for j in range(gameend[i]+ENDEND_THRESHOLD, frameend[i]):
                while j in SCENE_INDEX[i]:
                    SCENE_INDEX[i].remove(j)


            # 6-5. reconnect
            if len(reconnecting_index[i]) != 0:
                for j in range(len(reconnecting_index[i])-1):
                    if reconnecting_index[i][j+1] - reconnecting_index[i][j] > framerate * 15:
                        reconend_index[i].append(reconnecting_index[i][j+1])
                reconend_index[i].append(reconnecting_index[i][len(reconnecting_index[i])-1])
            
            print('reconend_index')
            print(reconend_index)

            # 6-5-2. add scene
            for j in range(len(reconend_index[i])):
                for k in range(reconend_index[i][j] - framerate, reconend_index[i][j] + framerate):
                    SCENE_INDEX[i].append(k)

            SCENE_INDEX[i] = set_list_sort(SCENE_INDEX[i])

            # 6-6. remove dented_stop
            try:
                SCENE_INDEX[i] = index_remove(SCENE_INDEX[i], remove_dented)
            except:
                pass
            try:
                SCENE_INDEX[i] = index_remove(SCENE_INDEX[i], remove_dentedcard)
            except:
                pass


            # 8-1. total index
            # chapter 8
            # start index, end index
            total_index[i].append(SCENE_INDEX[i][0])
            for j in range(len(SCENE_INDEX[i])-1):
                if SCENE_INDEX[i][j+1] - SCENE_INDEX[i][j] != 1:
                    total_index[i].append(SCENE_INDEX[i][j])
                    total_index[i].append(SCENE_INDEX[i][j+1])
            total_index[i].append(SCENE_INDEX[i][len(SCENE_INDEX[i])-1])

            # 8-2. start, end index
            for j in range(len(total_index[i])):
                if j % 2 == 0:
                    start_index[i].append(total_index[i][j])
                else:
                    end_index[i].append(total_index[i][j])

            print(start_index[i])
            print(end_index[i])

            # trinket 0822
            trinket = []
            trinketframe = []
            grade = 0
            print(balgyunend_to_dheropower[i])
        
            for j in range(len(balgyunend_to_dheropower[i])-1):
                print(balgyunend_to_dheropower[i][j] + 1, balgyunend_to_dheropower[i][j+1])
                if balgyunend_to_dheropower[i][j] + 1 != balgyunend_to_dheropower[i][j+1]:
                    if grade < 2:
                        try:
                            trinket.append(find_trinket(video_list[i], balgyunend_to_dheropower[i][j]/framerate,grade))
                            trinketframe.append(int((balgyunend_to_dheropower[i][j]+6)/rateframe))
                            print('trinket',trinket)
                            print('trinketframe',trinketframe)
                            grade = grade + 1    
                        except:
                            print('trinket_False')
            
        
            # 9-1. video sound threshold
            mp4_to_wav(inputvideo_path[i], wav_path[i])
            mv = max_volume(wav_path[i], math.floor(framerate * videopy[i].end))
            audio[i] = mv
            
            print("audio")
            print(audio)

            audio_copy = audio[i].copy()
            print(audio_copy)
            audio_copy.sort()
            print(audio_copy)
            t = 1.01
            for x in range(200):
                t += 1 / 100
                print(t)
                print(audio_copy[int(len(audio_copy)/t)])
            if user == 'rimgosu':
                speak_threshold.append(audio_copy[int(len(audio_copy)/1.3)])
            elif user == 'duckdragon':
                speak_threshold.append(audio_copy[int(len(audio_copy)/1.3)])
            elif user == 'zanyang':
                speak_threshold.append(audio_copy[int(len(audio_copy)/1.3)])
            elif user == 'matsuri':
                speak_threshold.append(audio_copy[int(len(audio_copy)/1.4)])
            elif user == 'sunbacon':
                speak_threshold.append(audio_copy[int(len(audio_copy)/1.54)])
            elif user == 'shadybunny':
                speak_threshold.append(audio_copy[int(len(audio_copy)/1.57)])

            if user == 'rimgosu' or user == 'duckdragon' or user == 'zanyang' or user == 'shadybunny' or user == 'sunbacon':
                speak_threshold_star.append(audio_copy[int(len(audio_copy)/1.1)])
            elif user == 'matsuri':
                speak_threshold_star.append(audio_copy[int(len(audio_copy)/1.02)])
            print(speak_threshold)
            speak_threshold_startend.append(audio_copy[int(len(audio_copy)/1.05)])
            print("speak_threshold[i]")
            print(speak_threshold[i])
            print("speak_threshold_star[i]")
            print(speak_threshold_star[i])
            print('start_End_threshod', speak_threshold_startend)

            # 9-2. speak adjust
            for j in range(len(audio[i])):
                if j in star_index[i]:
                    if audio[i][j] > speak_threshold_star[i]:
                        audio_speak_index[i].append(j)
                elif gamestart[i] - 10 * framerate < j < gamestart[i] + 10 * framerate:
                    if audio[i][j] > speak_threshold_startend[i]:
                        audio_speak_index[i].append(j)
                elif gameend[i] - 10 * framerate < j < gameend[i] + 10 * framerate:
                    if audio[i][j] > speak_threshold_startend[i]:
                        audio_speak_index[i].append(j)
                else:
                    if audio[i][j] > speak_threshold[i]:
                        audio_speak_index[i].append(j)

            print('audio_speak_index', audio_speak_index)
            

            for j in range(len(start_index[i])):
                while start_index[i][j] in audio_speak_index[i]:
                    start_index[i][j] -= 1       

            for j in range(len(end_index[i])):
                    while end_index[i][j] in audio_speak_index[i]:
                        end_index[i][j] += 1

            for j in range(len(start_index[i])):
                if start_index[i][j] >= end_index[i][j]:
                    pass
                else:
                    adjusted_start_index1[i].append(start_index[i][j])
                    adjusted_end_index1[i].append(end_index[i][j])
            
            adjusted_start_index2[i].append(adjusted_start_index1[i][0])
            for j in range(len(adjusted_start_index1[i])-1):
                if adjusted_end_index1[i][j] >= adjusted_start_index1[i][j+1]:
                    pass
                else:
                    adjusted_start_index2[i].append(adjusted_start_index1[i][j+1])
                    adjusted_end_index2[i].append(adjusted_end_index1[i][j])
            adjusted_end_index2[i].append(adjusted_end_index1[i][len(adjusted_end_index1[i])-1])

            print("adjusted_start_index1[i], adjusted_end_index1[i]")
            print(adjusted_start_index1[i], adjusted_end_index1[i])
            print("adjusted_start_index2[i], adjusted_end_index2[i]")
            print(adjusted_start_index2[i], adjusted_end_index2[i])

            # 9-3. frame to second

            start_index_second[i] = frame_to_second(adjusted_start_index2[i], framerate)
            end_index_second[i] = frame_to_second(adjusted_end_index2[i], framerate)
            start_index_frame[i] = frame_to_second(adjusted_start_index2[i], rateframe)
            end_index_frame[i] = frame_to_second(adjusted_end_index2[i], rateframe)
            print(start_index_frame[i])
            print(end_index_frame[i])

            # 10-1. detect newminions
            # 5턴 이후 전투부터 보여줄 예정임.
            # 본인 heropower는 컷한 이미지를 삭제해서 중복으로 정보가 뜨는 것을 방지 *0510 주석처리
            newminion_cut(patchday=newminion_patchday)
            # hpcut_path = os.path.join(current_path, 'pysrc')
            # hpcut_path = os.path.join(hpcut_path, 'newminion')
            # hpcut_path = os.path.join(hpcut_path, newminion_patchday)
            # hpcut_path = os.path.join(hpcut_path, 'cut_completed')
            # hpcut_path = os.path.join(hpcut_path, heropower[:-4]+'_buddy.png')
            # os.remove(hpcut_path)
            
            newminion_forxml = []
            newminion_list = []
            if display_newminion:
                for j in range(len(BS_index[i])-4):
                    if j+4 in not_display_minion:
                        pass
                    else:
                        sec = (BS_index[i][j+4] + 3 * framerate) / framerate
                        sec_frame = int( sec * 60 )
                        newminion_list = newminion_detect(video_list[i], input_path, sec, patchday=newminion_patchday, forbrann='False')
                        cutimage_remove(newminion_list,patchday=newminion_patchday)
                        while not len(newminion_list) == 3:
                            newminion_list.append('-')
                        newminion_forxml.append(sec_frame)
                        for k in newminion_list:
                            newminion_forxml.append(k)
            
            print('newminion_forxml', newminion_forxml)

            
            

            # 11. export xml
            print(heropower)
            if changeXml:
                run_tree(
                    current_path,
                    input_path,
                    exf_path,
                    video_list[i], 
                    60, 
                    start_index_frame[i], 
                    end_index_frame[i],
                    heropower,
                    newminion_forxml,
                    newminion_patchday,
                    anomalies,
                    trinket,
                    trinketframe
                    )

            # 12. xml to encoding
            if Premiere:
                run_autoPremiere(current_path, video_list[i], exf_path)

            # 13. done - email inform!
            email_attatched.append(video_list[i] + ' done!')
        except:
            email_attatched.append(video_list[i] + ' failed!')
    










    if Premiere:
        Bool = True
        after_treatment(input_path, exf_path, current_path, Bool)
        Bool = False
        after_treatment(input_path, exf_path, current_path, Bool)
        Bool = True
        after_treatment(input_path, exf_path, current_path, Bool)

        try:
            email_attatched.append('=====================')
            email_attatched.append('export success videos')
            email_attatched.append('=====================')
            export_video_list = os.listdir(exf_path)
            export_video_list = [file for file in export_video_list if file.endswith(".mp4")]
            for x in export_video_list:
                email_attatched.append(x)
        except:
            pass
            

    #send_email(email_attatched)

    # 11. upload youtube
    if uploadYotube:
        upload_youtube(current_path, video_list)
    
    # 12. shutdown
    if shutdown:
        command = f"cmd /k shutdown -s -t 3"
        cmd = subprocess.Popen(command, creationflags=subprocess.CREATE_NEW_CONSOLE)

if __name__=="__main__":
    current_path = os.path.dirname(__file__)
    input_path= os.path.join(current_path, 'inputvideo')
    video_list = os.listdir(input_path)
    video_list = [file for file in video_list if file.endswith(".mp4")]
    print(video_list)
    exf_Dpath = os.path.join(current_path, 'inputvideo')
    exf_path = os.path.join(exf_Dpath, 'export')
    run_autoEditor(    
        current_path,
        video_list,
        input_path,
        exf_path,
        framerate=3,
        res=1/3,
        FRchange=True,
        yoloDetect=True,#
        changeXml=True,
        Premiere=True,#
        screenshot=True,
        uploadYotube=False, #only False on real running
        display_newminion=True,
        newminion_patchday='_240821',
        shutdown=True
    )
    