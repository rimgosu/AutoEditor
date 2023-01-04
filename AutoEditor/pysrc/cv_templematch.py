import cv2
import os
def vidoescreenshot(video, target_time, output_path):
    videocv = cv2.VideoCapture(video)

    # Set the target time for the screenshot
    time = target_time  # in seconds
    x = 975
    y = 700
    w, h = 300, 300

    # Set the video to the target time
    videocv.set(cv2.CAP_PROP_POS_MSEC, time*1000)
    # Read the frame at the target time
    success, frame = videocv.read()
    # Read the frame at the target time
    if success:

        # Crop the frame to the target area
        frame = frame[y:y+h, x:x+w]

        # Save the screenshot
        cv2.imwrite(output_path + "/hpcheck.png", frame)

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
        print(target_hpimage)
        matched = os.path.basename(target_hpimage)
        print(matched)
        return matched
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
        vidoescreenshot(inputvideo, time + hpindex, hptemp_path)
        for i in hpimg_list:
            target = "\\"+ i
            cutsave_path = hptemp_path + target[:-4] + "_cut.png"
            _targetsave_image(target, [119, 120], [230, 209], 0.621, hpimg_path)
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

if __name__ == "__main__":
    m = find_heropower('mumuri.mp4', 5)
    print(m)