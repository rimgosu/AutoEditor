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
from yolov5.detect_modified import *
from moviepy.editor import VideoFileClip
from pysrc.TREE import *
from pysrc.edit import *
from pysrc.upload import *
from pysrc.audio_analysis import *
from pysrc.screenshot_bgremove import *
from pysrc.sendemail import *
def framerate_resolution_change(inputvideo_path, outputvideo_path, framerate, res):
    if os.path.isfile(outputvideo_path):
        pass
    else:
        stream = ffmpeg.input(inputvideo_path)  # video location
        stream = stream.filter('fps', fps=framerate, round='up')
        stream = stream.filter('scale', width = res, height = res)
        stream = ffmpeg.output(stream, outputvideo_path)
        ffmpeg.run(stream)
def DeleteAllFiles(filePath):
    if os.path.exists(filePath):
        for file in os.scandir(filePath):
            os.remove(file.path)
        return 'Remove All File'
    else:
        return 'Directory Not Found'
def frame_to_second(index, fps):
    index_second = [index[i] / fps for i in range(len(index))]
    return np.round(index_second, 1)

def run_autoEditor(
    current_path,
    video_list,
    ex,
    framerate=3,
    res=1/3,
    user='rimgosu',
    FRchange=False,
    yoloDetect=False,
    changeXml=True,
    Premiere=True,
    uploadYotube=True
):
    print("user",user)
    resolution = int(1920 * res)
    inputvideo_path = []
    FRvideo_path = []
    FRtext_path = []
    videopy = []
    frameend = []
    wav_path = []
    for i in range(len(video_list)):
        inputvideo_path.append(current_path+"/inputvideo/" + video_list[i])
        wav_path.append(current_path+"/pysrc/wav/" + video_list[i].rstrip(".mp4") + ".wav")
        FRvideo_path.append(current_path+"/yolov5/data/videos/" + str(framerate) + "f" + str(resolution) + "r" + video_list[i])
        FRtext_path.append(
            current_path+"/yolov5/runs/detect/exp/labels/" + str(framerate) + "f" + str(resolution) + "r" + video_list[i]
            .rstrip('.mp4')
            )
        videopy.append(VideoFileClip(current_path+"/inputvideo/" + video_list[i]))
        frameend.append(math.floor(videopy[i].end * framerate))


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
        run_detect(weights=ROOT / 'models/final.pt', source=ROOT / 'data/videos', save_txt = True, save_conf=True, conf_thres=0.5)

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

    # 4. indexes
    yolototal_index = [[0 for x in range(0)] for y in range(len(video_list))]
    employ_index = [[0 for x in range(0)] for y in range(len(video_list))]
    battle_index = [[0 for x in range(0)] for y in range(len(video_list))]
    EMOVE_INDEX = [[0 for x in range(0)] for y in range(len(video_list))]
    dminion_index = [[0 for x in range(0)] for y in range(len(video_list))]
    bang_index = [[0 for x in range(0)] for y in range(len(video_list))]
    bigbang_index = [[0 for x in range(0)] for y in range(len(video_list))]

    star_index = [[0 for x in range(0)] for y in range(len(video_list))]
    kelthuzad_index = [[0 for x in range(0)] for y in range(len(video_list))]
    jjiggregi_index = [[0 for x in range(0)] for y in range(len(video_list))]
    pyosi_index = [[0 for x in range(0)] for y in range(len(video_list))]
    sumgigi_index = [[0 for x in range(0)] for y in range(len(video_list))]

    SHinform_index = [[0 for x in range(0)] for y in range(len(video_list))]
    SI_index = [[0 for x in range(0)] for y in range(len(video_list))]
    donation_index = [[0 for x in range(0)] for y in range(len(video_list))]

    gamestart_index = [[0 for x in range(0)] for y in range(len(video_list))]
    gameend_index = [[0 for x in range(0)] for y in range(len(video_list))]
    gametogame_index = [[0 for x in range(0)] for y in range(len(video_list))]

    reconnecting_index = [[0 for x in range(0)] for y in range(len(video_list))]

    # chapter 5
    # game start, game end
    gamestart = []
    gameend = []
    gamestart_constant = 0
    gameend_constant = framerate * 5
    zerotohalf_index = [[0 for x in range(0)] for y in range(len(video_list))]

    # ES, BS index
    ES_constant = framerate * 30
    BS_constant = framerate * 30
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
    BALGYUN_THRESHOLD = int(framerate * 10)
    FINEADJUSTMENT_THRESHOLD = int(framerate * 2)
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
    EMPLOY_EXPANSION_CONSTANT = int( framerate * 1.5 )
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
    # chapter 7
    # quest select, end
    quest_select_frame = []
    questimg_end_frame = []

    # chapter 8
    # total index
    total_index = [[0 for x in range(0)] for y in range(len(video_list))]
    start_index = [[0 for x in range(0)] for y in range(len(video_list))]
    end_index = [[0 for x in range(0)] for y in range(len(video_list))]
    speak_threshold = []
    speak_threshold_star = []
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

    # chapter 10
    # quest start, end frame
    quest_start_frame = []
    quest_end_frame = []

    # chapter 12
    email_attatched = []

    for i in range(len(video_list)):
        for j in range(len(yolo_list[i])):
            for k in range(len(yolo_list[i][j])):
                if yolo_list[i][j][k][0] != '-' and yolo_list[i][j][k][0] != '2' \
                    and yolo_list[i][j][k][0] != '3'and yolo_list[i][j][k][0] != '26':
                    yolototal_index[i].append(j)
                    yolototal_index[i].sort
                elif yolo_list[i][j][k][0] == '2' and float(yolo_list[i][j][k][5]) > 0.79:
                    # for emoticon
                    if not 0.05 < float(yolo_list[i][j][k][3]) < 0.06 and 0.1 < float(yolo_list[i][j][k][4]) < 0.115:
                        dminion_index[i].append(j)
                        dminion_index[i].sort()
                elif yolo_list[i][j][k][0] == '3' and float(yolo_list[i][j][k][5]) > 0.5:
                    dminion_index[i].append(j)
                    dminion_index[i].sort()

        for j in range(len(yolo_list[i])):
            for k in range(len(yolo_list[i][j])):
                if yolo_list[i][j][k][0] == '0' and float(yolo_list[i][j][k][5]) > 0.90:
                    employ_index[i].append(j)
                    employ_index[i].sort()
                if yolo_list[i][j][k][0] == '1' and float(yolo_list[i][j][k][5]) > 0.90:
                    battle_index[i].append(j)
                    battle_index[i].sort()

                if yolo_list[i][j][k][0] == '2' and float(yolo_list[i][j][k][5]) > 0.70:
                    # 배치 두는 거 제한
                    if not 0.50 < float(yolo_list[i][j][k][2]) < 0.67:
                        # 가끔 상점에 하수인이 하나만 남으면 dented minion이라고 판단하는 것 제거
                        if not 0.49 < float(yolo_list[i][j][k][1]) < 0.51 and 0.36 < float(yolo_list[i][j][k][2]) < 0.37 and \
                            0.06 < float(yolo_list[i][j][k][3]) < 0.08 and 0.15 < float(yolo_list[i][j][k][4]) < 0.18:
                            EMOVE_INDEX[i].append(j)
                            EMOVE_INDEX[i].sort()

                if yolo_list[i][j][k][0] == '3'and float(yolo_list[i][j][k][5]) > 0.75:
                    EMOVE_INDEX[i].append(j)
                    EMOVE_INDEX[i].sort()
                if yolo_list[i][j][k][0] == '4'and float(yolo_list[i][j][k][5]) > 0.75:
                    EMOVE_INDEX[i].append(j)
                    EMOVE_INDEX[i].sort()
                if yolo_list[i][j][k][0] == '5':
                    EMOVE_INDEX[i].append(j)
                    EMOVE_INDEX[i].sort()
                if yolo_list[i][j][k][0] == '6':
                    EMOVE_INDEX[i].append(j)
                    EMOVE_INDEX[i].sort()
                if yolo_list[i][j][k][0] == '7' and float(yolo_list[i][j][k][5]) > 0.80:
                    EMOVE_INDEX[i].append(j)
                    EMOVE_INDEX[i].sort()
                if yolo_list[i][j][k][0] == '8':
                    EMOVE_INDEX[i].append(j)
                    EMOVE_INDEX[i].sort()
                if yolo_list[i][j][k][0] == '9' and float(yolo_list[i][j][k][5]) > 0.80:
                    EMOVE_INDEX[i].append(j)
                    EMOVE_INDEX[i].sort()
                if yolo_list[i][j][k][0] == '10'and float(yolo_list[i][j][k][5]) > 0.80:
                    EMOVE_INDEX[i].append(j)
                    EMOVE_INDEX[i].sort()
                if yolo_list[i][j][k][0] == '11'and float(yolo_list[i][j][k][5]) > 0.80:
                    EMOVE_INDEX[i].append(j)
                    EMOVE_INDEX[i].sort()
                if yolo_list[i][j][k][0] == '12':
                    EMOVE_INDEX[i].append(j)
                    EMOVE_INDEX[i].sort()
                if yolo_list[i][j][k][0] == '13':
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
                        bigbang_index[i].append(j)
                        bigbang_index[i].sort()
                if yolo_list[i][j][k][0] == '21' and float(yolo_list[i][j][k][5]) > 0.70:
                    star_index[i].append(j)
                    star_index[i].sort()
                if yolo_list[i][j][k][0] == '22':
                    kelthuzad_index[i].append(j)
                    kelthuzad_index[i].sort()
                if yolo_list[i][j][k][0] == '23':
                    jjiggregi_index[i].append(j)
                    jjiggregi_index[i].sort()

                if yolo_list[i][j][k][0] == '24':
                    pyosi_index[i].append(j)
                    pyosi_index[i].sort()
                if yolo_list[i][j][k][0] == '25':
                    sumgigi_index[i].append(j)
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
                    gamestart_index[i].append(j)
                    gamestart_index[i].sort()
                if yolo_list[i][j][k][0] == '30':
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

        print("reconnecting_index[i]")
        print(reconnecting_index[i])

        print("employ_index[i]", video_list[i])
        print(employ_index[i])
        print("battle_index[i]", video_list[i])
        print(battle_index[i])

        print("yolototal_index[i]")
        print(yolototal_index[i])
        print("dminion_index[i]")
        print(dminion_index[i])

        print("bang_index[i]")
        print(bang_index[i])

        print("bigbang_index[i]")
        print(bigbang_index[i])

        EMOVE_INDEX[i] = set(EMOVE_INDEX[i])
        EMOVE_INDEX[i] = list(EMOVE_INDEX[i])

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
        # 5-1. game start, game end
        for j in range(0, int(frameend[i]/2)):
            zerotohalf_index[i].append(j)
        for j in zerotohalf_index[i]:
            while j in gametogame_index[i]:
                gametogame_index[i].remove(j)

        print("gametogame_index")
        print(gametogame_index)

        if len(gameend_index[i]) == 0:
            for j in gametogame_index[i]:
                gameend_index[i].append(j)

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

        print('length')
        print(len(gameend_index[i]))
        print(len(gametogame_index[i]))

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

        # 5-2-1. battle to employ

        ES_index[i].append(employ_index[i][0])
        for j in range(len(employ_index[i])-1):
            if employ_index[i][j+1] - employ_index[i][j] > ES_constant:
                ES_index[i].append(employ_index[i][j+1])

        BS_index[i].append(battle_index[i][0])
        for j in range(len(battle_index[i])-1):
            if battle_index[i][j+1] - battle_index[i][j] > BS_constant:
                BS_index[i].append(battle_index[i][j+1])

        while max(ES_index[i]) > gameend[i]:
            ES_index[i].pop()
        while max(BS_index[i]) > gameend[i]:
            BS_index[i].pop()
        while min(ES_index[i]) < gamestart[i]:
            del ES_index[i][0]
        while min(BS_index[i]) < gamestart[i]:
            del BS_index[i][0]

        if BS_index[i][len(BS_index[i])-1] > ES_index[i][len(ES_index[i])-1]:
            ES_index[i].append(gameend[i])
        
        # ES_index 한 개 없을 경우
        if len(BS_index[i]) == len(ES_index[i]):
            for j in range(len(BS_index[i])-1):
                if ES_index[i][j] < BS_index[i][j]:
                    for k in range(BS_index[i][j+1]- EMPLOY_TO_BATTLE_MAX , BS_index[i][j+1]- EMPLOY_TO_BATTLE_MIN):
                        fix_index[i].append(k)
            for j in fix_index[i]:
                for k in SI_index[i]:
                    if j == k:
                        fix_house_index[i].append(k)
            for j in fix_index[i]:
                for k in reconnecting_index[i]:
                    if j == k:
                        fix_house_index[i].append(k)
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
        

        print("ES, BS indexes")
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

        # 5-3-2. EMOVE INDEX EXPANSION

        for j in EMOVE_INDEX[i]:
            for k in range(-EXPANSION_MINUS_CONSTANT, EXPANSION_CONSTANT):
                EMOVE_INDEX_EXPANSION[i].append(j+k)

        EMOVE_INDEX_EXPANSION[i] = set(EMOVE_INDEX_EXPANSION[i])
        EMOVE_INDEX_EXPANSION[i] = list(EMOVE_INDEX_EXPANSION[i])
        EMOVE_INDEX_EXPANSION[i].sort()

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


        # 5-4. star index
        star_index[i] = set(star_index[i])
        star_index[i] = list(star_index[i])
        star_index[i].sort()

        for j in range(len(star_index[i])-1):
            if star_index[i][j+1]- star_index[i][j] < star_constant:
                for k in range(star_index[i][j] , star_index[i][j+1]):
                    star_index[i].append(k)
                    star_index[i] = set(star_index[i])
                    star_index[i] = list(star_index[i])
                    star_index[i].sort()

        print("star_index")
        print(star_index[i])

        # 5-4-2. 
        star_house_index = [[0 for x in range(0)] for y in range(len(BS_index[i]))]
        for j in range(len(BS_index[i])):
            for k in range(BS_index[i][j], ES_index[i][j+1]):
                for l in star_index[i]:
                    if l == k:
                        star_house_index[j].append(k)
        for j in range(len(star_house_index)):
            if len(star_house_index[j]) != 0:
                for k in range(min(star_house_index[j]), max(star_house_index[j]) - STAR_MINUS_THRESHOLD):
                    star_minustar_index[i].append(k)

        # 5-5. SUMGIGI PYOSI
        for j in sumgigi_index[i]:
            SUMPYO_index[i].append(j)

        for j in pyosi_index[i]:
            SUMPYO_index[i].append(j)
            SUMPYO_index[i].sort()
        
        SUMPYO_index[i] = set(SUMPYO_index[i])
        SUMPYO_index[i] = list(SUMPYO_index[i])
        SUMPYO_index[i].sort()

        print("SUMPYO_index")
        print(SUMPYO_index)

        SUMPYO_SE_index[i].append(SUMPYO_index[i][0])
        for j in range(len(SUMPYO_index[i])-1):
            if SUMPYO_index[i][j+1] - SUMPYO_index[i][j] < FINEADJUSTMENT_THRESHOLD:
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


        # 6. merge to SCENE INDEX
        for j in range(gamestart[i], gameend[i]):
            SCENE_INDEX[i].append(j)

        for j in EMOVE_INDEX_REVERSE[i]:
            while j in SCENE_INDEX[i]:
                SCENE_INDEX[i].remove(j)

        for j in battles[i]:
            SCENE_INDEX[i].append(j)
            SCENE_INDEX[i] = set(SCENE_INDEX[i])
            SCENE_INDEX[i] = list(SCENE_INDEX[i])
            SCENE_INDEX[i].sort()

        for j in star_minustar_index[i]:
            while j in SCENE_INDEX[i]:
                SCENE_INDEX[i].remove(j)

        for j in pyosi_maxim[i]:
            while j in SCENE_INDEX[i]:
                SCENE_INDEX[i].remove(j)

        # 6-2. employ expansion
        for j in range(1,len(ES_index[i])):
            for k in range(ES_index[i][j]- EMPLOY_EXPANSION_CONSTANT, ES_index[i][j] + EMPLOY_EXPANSION_CONSTANT):
                SCENE_INDEX[i].append(k)

        # 6-?. balgyunend_to_dheropower
        for j in balgyunend_to_dheropower[i]:
            SCENE_INDEX[i].append(j)
            SCENE_INDEX[i] = set(SCENE_INDEX[i])
            SCENE_INDEX[i] = list(SCENE_INDEX[i])
            SCENE_INDEX[i].sort()

        # 6-??-1. dminion fuck nothing
        dminion_dup = [x for y, x in enumerate(dminion_index[i]) if y != dminion_index[i].index(x)]
        for j in dminion_dup:
            while j in dminion_index[i]:
                dminion_index[i].remove(j)
        print("dminion_index dup removed")
        print(dminion_index[i])    

        for j in range(len(yolototal_index[i])):
            for k in range(yolototal_index[i][j]-YOLOTOTAL_EXPANSION_THRESHOLD, yolototal_index[i][j]+YOLOTOTAL_EXPANSION_THRESHOLD):
                yolototal_index[i].append(k)
        yolototal_index[i] = set(yolototal_index[i])
        yolototal_index[i] = list(yolototal_index[i])
        yolototal_index[i].sort()

        for j in yolototal_index[i]:
            while j in dminion_index[i]:
                dminion_index[i].remove(j)
        print("dminion_index yolototal removed")
        print(dminion_index[i])  

        for j in range(len(BS_index[i])):
            for k in range(BS_index[i][j], ES_index[i][j+1]):
                if k in dminion_index[i]:
                    dminion_index[i].remove(k)
        dminion_index[i].sort()
        dminion_dup2 = [x for y, x in enumerate(dminion_index[i]) if y != dminion_index[i].index(x)]
        for j in dminion_dup2:
            while j in dminion_index[i]:
                dminion_index[i].remove(j)
        print("dminion_index pretreated done")
        print(dminion_index[i])  

        # 6-??-2. remove sequential dminion
        for j in range(len(dminion_index[i])-1):
            if dminion_index[i][j+1] - dminion_index[i][j] == 1:
                emove_but_nothing_index[i].append(dminion_index[i][j])
                emove_but_nothing_index[i].append(dminion_index[i][j+1])
        emove_but_nothing_index[i] = set(emove_but_nothing_index[i])
        emove_but_nothing_index[i] = list(emove_but_nothing_index[i])
        emove_but_nothing_index[i].sort()

        if len(emove_but_nothing_index[i]) > int(framerate * 0.5):
            but_nothing_start_index = []
            but_nothing_start_index.append(emove_but_nothing_index[i][0])
            for j in range(len(emove_but_nothing_index[i]) - 1):
                if emove_but_nothing_index[i][j+1] - emove_but_nothing_index[i][j] != 1:
                    but_nothing_start_index.append(emove_but_nothing_index[i][j])
                    but_nothing_start_index.append(emove_but_nothing_index[i][j+1])
            but_nothing_start_index.append(emove_but_nothing_index[i][len(emove_but_nothing_index[i])-1])

            for j in range(len(but_nothing_start_index)):
                if j % 2 == 0:
                    for k in range(but_nothing_start_index[j] + NOTHING_THRESHOLD, but_nothing_start_index[j+1] - NOTHING_THRESHOLD):
                        while k in SCENE_INDEX[i]:
                            SCENE_INDEX[i].remove(k)
            
            print("emove_but_nothing_index")
            print(emove_but_nothing_index)
            print("but_nothing_start_index")
            print(but_nothing_start_index)

        # 6-3-0. keltuzhad 
        kelthuzad_house_index = [[0 for x in range(0)] for y in range(len(BS_index[i]))]
        for j in range(len(BS_index[i])):
            for k in range(BS_index[i][j], ES_index[i][j+1]):
                for l in kelthuzad_index[i]:
                    if l == k:
                        kelthuzad_house_index[j].append(k)

        print("kelthuzad_house_index")
        print(kelthuzad_house_index[i])
        star_house_index = [[0 for x in range(0)] for y in range(len(BS_index[i]))]
        for j in range(len(BS_index[i])):
            for k in range(BS_index[i][j] + BS_TURNOVER_THRESHOLD, ES_index[i][j+1]):
                for l in star_index[i]:
                    if l == k:
                        star_house_index[j].append(k)

        for j in range(len(kelthuzad_house_index[i])):
            if len(kelthuzad_house_index[j]) > 5 * framerate:
                for k in range(BS_index[i][j]+ BS_TURNOVER_THRESHOLD, max(star_house_index[j]) - STAR_MINUS_THRESHOLD):
                    kelthuzad_remove_index[i].append(k)

        for j in kelthuzad_remove_index[i]:
            while j in SCENE_INDEX[i]:
                SCENE_INDEX[i].remove(j)

        """
        employ: 1턴 / 2턴 삭제
        battle: 1턴 / 2턴 / 3턴 / 4턴 스킵
        """
        # 6-3-1. early point
        star_house_index = [[0 for x in range(0)] for y in range(len(BS_index[i]))]
        for j in range(len(BS_index[i])):
            for k in range(BS_index[i][j], ES_index[i][j+1]):
                for l in star_index[i]:
                    if l == k:
                        star_house_index[j].append(k)

        print("star_house_index")
        print(star_house_index[i])

        for j in range(ES_index[i][0]-EALRY_POINT_THRESHOLD, ES_index[i][1]):
            early_point1[i].append(j)
        for j in range(ES_index[i][1], ES_index[i][2]):
            early_point2[i].append(j)
        if len(star_house_index[2]) != 0:
            for j in range(BS_index[i][2], max(star_house_index[2])-STAR_MINUS_THRESHOLD):
                early_point3[i].append(j)
        else:
            for j in range(BS_index[i][2], ES_index[i][3]):
                early_point3[i].append(j)
        if len(star_house_index[3]) != 0:
            for j in range(BS_index[i][3], max(star_house_index[3])-STAR_MINUS_THRESHOLD):
                early_point4[i].append(j)
        else:
            for j in range(BS_index[i][3], ES_index[i][4]):
                early_point4[i].append(j)

        # 6-3-2. early point remove
        for j in early_point1[i]:
            while j in SCENE_INDEX[i]:
                SCENE_INDEX[i].remove(j)
        for j in early_point2[i]:
            while j in SCENE_INDEX[i]:
                SCENE_INDEX[i].remove(j)
        for j in early_point3[i]:
            while j in SCENE_INDEX[i]:
                SCENE_INDEX[i].remove(j)
        for j in early_point4[i]:
            while j in SCENE_INDEX[i]:
                SCENE_INDEX[i].remove(j)

        # 6-4. game_start / game end
        for j in range(gamestart[i]-HEROSELECT_THRESHOLD_MINUS, gamestart[i]+HEROSELECT_THRESHOLD):
            heroselect_index[i].append(j)
        for j in range(gameend[i]-ENDEND_THRESHOLD_MINUS, gameend[i]+ENDEND_THRESHOLD):
            endend_index[i].append(j)

        # 6-4-2. game_start / game end to scene
        for j in heroselect_index[i]:
            SCENE_INDEX[i].append(j)
            SCENE_INDEX[i] = set(SCENE_INDEX[i])
            SCENE_INDEX[i] = list(SCENE_INDEX[i])
            SCENE_INDEX[i].sort()
        for j in endend_index[i]:
            SCENE_INDEX[i].append(j)
            SCENE_INDEX[i] = set(SCENE_INDEX[i])
            SCENE_INDEX[i] = list(SCENE_INDEX[i])
            SCENE_INDEX[i].sort()

        # 6-4-3. game_start / game_end fuck
        for j in range(0, gamestart[i]-HEROSELECT_THRESHOLD_MINUS):
            while j in SCENE_INDEX[i]:
                SCENE_INDEX[i].remove(j)
        for j in range(gameend[i]+ENDEND_THRESHOLD, frameend[i]):
            while j in SCENE_INDEX[i]:
                SCENE_INDEX[i].remove(j)


        # 6-5. reconnect
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

        SCENE_INDEX[i] = set(SCENE_INDEX[i])
        SCENE_INDEX[i] = list(SCENE_INDEX[i])
        SCENE_INDEX[i].sort()

        # 7-1. quest recognize
        balgyun_house_index = [[0 for x in range(0)] for y in range(len(balgyun_start[i]))]
        for j in range(len(balgyun_start[i])):
            for k in range(balgyun_start[i][j], balgyun_end[i][j]):
                for l in SUMPYO_index[i]:
                    if l == k:
                        balgyun_house_index[j].append(k)

        print('balgyun_house_index')
        print(balgyun_house_index)
        
        breaker = False
        for j in range(len(balgyun_house_index)):
            for k in range(len(balgyun_house_index[j])):
                if ES_index[i][3] < min(balgyun_house_index[j]) < BS_index[i][3] \
                    and ES_index[i][3] < max(balgyun_house_index[j]) < BS_index[i][3]:
                    quest_select = (max(balgyun_house_index[j])) / framerate 
                    print(quest_select)
                    breaker = True
                    break
            if breaker == True:
                break

        if user != 'seseisei':
            quest_detect_sum = 0
            while True:
                detect_quest(current_path + '/inputvideo/' + video_list[i], quest_select, current_path + '/pysrc/quest/', user)
                quest_label = os.listdir(current_path + '/yolov5/runs/qdetect/exp/labels/')
                quest_select += framerate * 1/10
                print("quest_select")
                print(quest_select)
                print('quest_label')
                print(quest_label)
                quest_detect_sum += 1
                if len(quest_label) == 1:
                    break
                if quest_detect_sum == framerate * 16:
                    break

        for j in range(3):
            if os.path.exists(current_path + '/yolov5/runs/qdetect/exp/labels/large_quest' + str(j) + '.txt'):
                quest_image = current_path + '/pysrc/quest/quest' + str(j) + '.png'
                quest_copy_image = current_path + '/pysrc/image_src/' + video_list[i].rstrip('.mp4') + '_quest.png'
                shutil.copy(quest_image, quest_copy_image)
                break
        
        quest_select_frame.append(quest_select * 60)
        print("quest_select_frame")
        print(quest_select_frame)

        # 7-2. quest image duration
        if len(bigbang_index[i]) != 0:
            questimg_end_frame.append(int(min(bigbang_index[i])*60/framerate))
        elif len(bigbang_index[i]) == 0:
            bang_avg = max(bang_index[i])/2 + min(bang_index[i])/2
            first_bang = []
            for j in range(int(bang_avg)):
                first_bang.append(j)
            for j in first_bang:
                while j in bang_index[i]:
                    bang_index[i].remove(j)
            questimg_end_frame.append(int(min(bang_index[i])*60/framerate))


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
        speak_threshold.append(audio_copy[int(len(audio_copy)/1.3)])
        speak_threshold_star.append(audio_copy[int(len(audio_copy)/1.1)])
        print(speak_threshold)

        print("speak_threshold[i]")
        print(speak_threshold[i])
        print("speak_threshold_star[i]")
        print(speak_threshold_star[i])

        # 9-2. speak adjust
        for j in range(len(audio[i])):
            if j in star_index[i]:
                if audio[i][j] > speak_threshold_star[i]:
                    audio_speak_index[i].append(j)
            else:
                if audio[i][j] > speak_threshold[i]:
                    audio_speak_index[i].append(j)

        for j in range(len(start_index[i])):
                while start_index[i][j] in audio_speak_index[i]:
                    start_index[i][j] -= 1


        for j in range(len(audio[i])):
            if j in star_index[i]:
                if audio[i][j] > speak_threshold_star[i]:
                    audio_speak_index[i].append(j)
            else:
                if audio[i][j] > speak_threshold[i]:
                    audio_speak_index[i].append(j)                

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

        # 9-1. frame to second

        start_index_second[i] = frame_to_second(adjusted_start_index2[i], framerate)
        end_index_second[i] = frame_to_second(adjusted_end_index2[i], framerate)
        start_index_frame[i] = frame_to_second(adjusted_start_index2[i], rateframe)
        end_index_frame[i] = frame_to_second(adjusted_end_index2[i], rateframe)
        print(start_index_frame[i])
        print(end_index_frame[i])

        # 10-0. quest frame in
        qduration = 0
        for j in range(len(start_index_frame[i])-1):
            if start_index_frame[i][j] < quest_select_frame[i] < end_index_frame[i][j]:
                quest_start_frame.append(qduration + quest_select_frame[i] - start_index_frame[i][j])
                break
            elif end_index_frame[i][j] < quest_select_frame[i] < start_index_frame[i][j+1]:
                quest_start_frame.append(qduration + quest_select_frame[i] - end_index_frame[i][j])
                break
            qduration += end_index_frame[i][j] - start_index_frame[i][j]
            print(qduration)
            print(start_index_frame[i][j])
            print(end_index_frame[i][j])
            print(quest_select_frame[i])
        eduration = 0
        for j in range(len(start_index_frame[i])-1):
            if start_index_frame[i][j] < questimg_end_frame[i] < end_index_frame[i][j]:
                quest_end_frame.append(eduration + questimg_end_frame[i] - start_index_frame[i][j])
                break
            elif end_index_frame[i][j] < questimg_end_frame[i] < start_index_frame[i][j+1]:
                quest_end_frame.append(eduration + questimg_end_frame[i] - end_index_frame[i][j])
                break
            eduration += end_index_frame[i][j] - start_index_frame[i][j]

        print('quest_start_frame[i]')
        print(quest_start_frame[i])
        print('quest_end_frame[i]')
        print(quest_end_frame[i])

        # 10. export xml
        if changeXml:
            run_tree(current_path, video_list[i], 60, start_index_frame[i], end_index_frame[i], quest_start_frame[i], quest_end_frame[i])

        # 11. xml to encoding
        if Premiere:
            run_autoPremiere(current_path, video_list[i], exf)

        # 12. done - email inform!
        email_attatched.append(video_list[i] + ' done!')
        
    send_email(email_attatched)

    # 11. upload youtube
    if uploadYotube:
        upload_youtube(current_path, video_list)

if __name__=="__main__":
    user_list = ['rimgosu', 'xqn', 'matsuri', 'beterbabbit', 'seseisei']
    current_path = os.path.dirname(__file__)
    print(current_path)
    video_list = os.listdir(current_path + "/inputvideo/")
    video_list = [file for file in video_list if file.endswith(".mp4")]
    print(video_list)
    exf = os.path.join(current_path, 'inputvideo')
    exf = os.path.join(exf, 'export')
    run_autoEditor(    
        current_path,
        video_list,
        exf,
        framerate=5,
        res=1/3,
        user='rimgosu',
        FRchange=False ,
        yoloDetect=False,
        changeXml=True,
        Premiere=True,
        uploadYotube=False
    )
    