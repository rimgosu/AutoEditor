import os
import ffmpeg

current_path = os.path.dirname(__file__)

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

if os.path.exists(current_path+'matsuri_test.mp4'):
    DeleteAllFiles(current_path+'matsuri_test.mp4')

framerate_resolution_change(
    'matsuri_test.mp4', 
    'matsuri_test_1f.mp4',
    framerate=1/5,
    res=1/3
    )