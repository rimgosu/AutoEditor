from rembg import remove
import cv2
import os
import sys
import shutil
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from yolov5.detect_quest import * 

def what_quest(video, target_time, output_path, user):
    if user == 'rimgosu' or user == 'matsuri' or user == 'shadybunny' or user == 'duckdragon':
        # Open the video file
        videocv = cv2.VideoCapture(video)

        # Set the target time for the screenshot
        time = target_time  # in seconds
        size = 0
        xsize = 0
        ysize = 0
        x = [421+xsize-size, 808+xsize-size, 1195+xsize-size]
        y = 219+ysize-size
        w, h = 291-xsize + size*2, 585-ysize + size*2


        for i in range(3):
            # Set the video to the target time
            videocv.set(cv2.CAP_PROP_POS_MSEC, time*1000)
            # Read the frame at the target time
            success, frame = videocv.read()
            # Read the frame at the target time
            if success:

                # Crop the frame to the target area
                frame = frame[y:y+h, x[i]:x[i]+w]

                # Save the screenshot
                cv2.imwrite(output_path + "/quest" + str(i)+".png", frame)

            # Release the video capture object
        videocv.release()
    if user == 'beterbabbit':
        # Open the video file
        videocv = cv2.VideoCapture(video)

        # Set the target time for the screenshot
        time = target_time  # in seconds
        size = 0
        xsize = 0
        ysize = 0
        x = [409+xsize-size, 804+xsize-size, 1197+xsize-size]
        y = 223+ysize-size
        w, h = 291-xsize + size*2, 585-ysize + size*2


        for i in range(3):
            # Set the video to the target time
            videocv.set(cv2.CAP_PROP_POS_MSEC, time*1000)
            # Read the frame at the target time
            success, frame = videocv.read()
            # Read the frame at the target time
            if success:

                # Crop the frame to the target area
                frame = frame[y:y+h, x[i]:x[i]+w]

                # Save the screenshot
                cv2.imwrite(output_path + "/quest" + str(i)+".png", frame)

            # Release the video capture object
        videocv.release()

def what_quest2(video, target_time, output_path, user):
    # Open the video file
    videocv = cv2.VideoCapture(video)

    # Set the target time for the screenshot
    time = target_time  # in seconds

    x = [310, 700, 1085]
    y = 120
    w, h = 500, 800

    for i in range(3):
        # Set the video to the target time
        videocv.set(cv2.CAP_PROP_POS_MSEC, time*1000)
        # Read the frame at the target time
        success, frame = videocv.read()
        # Read the frame at the target time
        if success:

            # Crop the frame to the target area
            frame = frame[y:y+h, x[i]:x[i]+w]

            # Save the screenshot
            cv2.imwrite(output_path.rstrip('/quest') + "/questlarge/large_quest" + str(i)+".png", frame)

        # Release the video capture object
    videocv.release()

def detect_quest(video, target_time, output_path, user):
    directory_path = output_path

    files = os.listdir(directory_path)
    largefiles = os.listdir(directory_path.rstrip('quest/') + "/questlarge")
    if os.path.exists(directory_path):
        for file in files:
            file_path = os.path.join(directory_path, file)
            os.remove(file_path)
    if os.path.exists(directory_path.rstrip('quest/') + "/questlarge"):
        for file in largefiles:
            file_path = os.path.join(directory_path.rstrip('quest/') + "/questlarge", file)
            os.remove(file_path)

    what_quest2(video, target_time, output_path, user)
    what_quest(video, target_time, output_path, user)
    if os.path.exists(ROOT / 'runs/qdetect'):
        shutil.rmtree(ROOT / 'runs/qdetect')
    runq(weights=ROOT / 'models/quest_recognize_ver2.pt', source=output_path.rstrip('quest/') + "/questlarge" , save_txt = True, conf_thres=0.5, project=ROOT / 'runs/qdetect', name='exp')

if __name__ == "__main__":
    current_path = os.path.dirname(__file__)
    current_path = os.path.join(current_path, os.pardir)
    detect_quest(current_path + '/inputvideo/' +'bater.mp4', 368, current_path + '/pysrc/quest/', user ='beterbabbit')