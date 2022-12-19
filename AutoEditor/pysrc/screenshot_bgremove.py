from rembg import remove
import cv2
import os
import sys
import shutil
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from yolov5.detect_quest import * 

def what_quest(video, target_time, output_path):
    # Open the video file
    videocv = cv2.VideoCapture(video)

    # Set the target time for the screenshot
    time = target_time  # in seconds

    x = [393, 780, 1169]
    y = 190
    w, h = 350, 650


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
            cv2.imwrite(output_path + "/quest" + str(i)+".jpg", frame)

        # Release the video capture object
    videocv.release()

def what_quest2(video, target_time, output_path):
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
            cv2.imwrite(output_path.rstrip('/quest') + "/questlarge/large_quest" + str(i)+".jpg", frame)

        # Release the video capture object
    videocv.release()


def remove_background(video, target_time, output_path):
    what_quest(video, target_time, output_path)

    for j in range(3):
        input_path = output_path+'quest'+str(j)+'.jpg'
        out_path = output_path+'quest'+str(j)+'_bgremoved.png'

        with open(input_path, 'rb') as i:
            with open(out_path, 'wb') as o:
                input = i.read()
                output = remove(input)
                o.write(output)

def detect_quest(video, target_time, output_path):
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

    what_quest2(video, target_time, output_path)
    remove_background(video, target_time, output_path)
    if os.path.exists(ROOT / 'runs/qdetect'):
        shutil.rmtree(ROOT / 'runs/qdetect')
    runq(weights=ROOT / 'models/quest_recognize.pt', source=output_path.rstrip('quest/') + "/questlarge" , save_txt = True, conf_thres=0.5, project=ROOT / 'runs/qdetect', name='exp')

if __name__ == "__main__":
    current_path = os.path.dirname(__file__)
    current_path = os.path.join(current_path, os.pardir)
    detect_quest(current_path + '/inputvideo/' +'hi.mp4', 377.5, current_path + '/pysrc/quest/')