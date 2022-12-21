import cv2
import os

def what_quest(video, target_time, output_path):
    # Open the video file
    videocv = cv2.VideoCapture(video)

    # Set the target time for the screenshot
    time = target_time  # in seconds

    x = [403, 795, 1179]
    y = 200
    w, h = 320, 620
    for i in range(3):
        # Set the video to the target time
        videocv.set(cv2.CAP_PROP_POS_MSEC, time*1000)

        # Read the frame at the target time
        success, frame = videocv.read()

        # Check if the frame was successfully read
        if success:
            # Crop the frame to the target area
            frame = frame[y:y+h, x[i]:x[i]+w]

            # Save the screenshot
            cv2.imwrite(output_path + "/quest" + str(i)+".jpg", frame)

        # Release the video capture object
    videocv.release()

if __name__ == "__main__":
    what_quest('video.mp4', 489, os.path.dirname(__file__))