![image](https://github.com/rimgosu/AutoEditor/assets/120752098/a6c16f86-0fe8-4456-8112-2abf5d2f40de)

# AutoEditor

- 편집할 때 반복되는 부분이 많아 만들게 된 저의 첫 코딩 작품입니다.
- 30분 길이의 원본 영상을 넣으면 10분 내외의 영상으로 편집해주고 유튜브에 자동으로 업로드를 합니다.
- 자동으로 기물을 인식하여 시청자에게 유의미한 정보를 제공해줍니다.
- 92%의 시청자님들의 긍정적인 반응을 이끌어 냈습니다.

![image](https://github.com/rimgosu/AutoEditor/assets/120752098/98e56e45-ed01-4316-ad6d-689eb8a3f3a2)

## 사용된 기술
- AutoEditor는 Python으로 제작되었습니다.
- OpenCV, Yolov5, FFMPEG, moviepy 라이브러리를 사용해 영상을 분석합니다.
- 분석된 영상을 ElementTree XML API를 이용해 Premier Pro가 읽을 수 있는 형태인 .xml 파일로 영상 정보를 담습니다.
- NVIDIA 그래픽 카드를 사용하면 CUDA를 통해 더 빠른 작업을 할 수 있습니다.

## 사용 방법
- 기본적으로 이 프로그램은 원본 영상을 분석해 Premier Pro만 읽을 수 있는 .xml 파일 형태로 만들어주는 프로그램입니다. 따라서 Premier Pro 20버전 이상을 필요로 합니다.
- Yolov5, FFMPEG, OpenCV, pyautogui, ElementTree, moviepy, numpy, shutil
