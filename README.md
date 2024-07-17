<img width="772" alt="image" src="https://github.com/rimgosu/AutoEditor/assets/120752098/76e70b67-517e-401b-b145-06830ca16f9d">

# AutoEditor

- 편집할 때 반복되는 부분이 많아 만들게 된 저의 첫 코딩 작품입니다.
- 30분 길이의 원본 영상을 넣으면 10분 내외의 영상으로 편집해주고 유튜브에 자동으로 업로드를 합니다.
- 자동으로 기물을 인식하여 시청자에게 유의미한 정보를 제공해줍니다.
- _**92%**_ 의 시청자님들의 긍정적인 반응을 이끌어 냈습니다.

![image](https://github.com/rimgosu/AutoEditor/assets/120752098/98e56e45-ed01-4316-ad6d-689eb8a3f3a2)

## 사용된 기술
- AutoEditor는 **Python**으로 제작되었습니다.
- **OpenCV, yolov5, FFMPEG, moviepy** 라이브러리를 사용해 영상을 분석합니다.
- yolov5를 활용하여 이미지 분석을 하였습니다. **3493개**의 이미지 데이터 학습하여 38개 종류를 구분합니다.
- 분석된 영상을 ElementTree XML API를 이용해 **.xml** 파일로 영상 정보를 담습니다.
- NVIDIA 그래픽 카드를 사용하면 **CUDA**를 이용해 더 빠른 작업을 할 수 있습니다.

## 영상 활용처

- 다음 유튜브에서 자동 편집 프로그램을 사용중입니다.

  - 림고수 유튜브 : <https://www.youtube.com/@user-cd6ij7ym4u/videos>
  - Matsuri 유튜브 : <https://www.youtube.com/@matsurihs>
  - 덕드래곤 유튜브 : <https://www.youtube.com/@duckdragon_>


## 사용

### 기본 세팅
- 기본적으로 이 프로그램은 원본 영상을 분석해 Premier Pro만 읽을 수 있는 .xml 파일 형태로 만들어주는 프로그램입니다. 따라서 _Premier Pro 2020 버전 이상_ 이 있어야합니다.
- Yolov5, FFMPEG, OpenCV, pyautogui, ElementTree, moviepy, numpy, shutil 등 pip install을 통해 설치해주세요.
- pyautogui로 Premier Pro를 실행하여 .xml 파일을 읽습니다. Premier Pro의 단축키 설정은 _기본값_ 이어야 합니다.
- premiere_path = r'C:\Program Files\Adobe\Adobe Premiere Pro 2023\Adobe Premiere Pro.exe'의 경로를 _Premier Pro가 설치되어있는 절대경로_ 로 변경해주세요.

### 사용 방법

<ol start="1" data-sourcepos="45:1-46:0" dir="auto">
<li data-sourcepos="45:1-46:0"><strong>게임 한 판</strong>의 영상을 다음 경로로 영상을 넣어주세요: <br><code>예: /AutoEditor/inputvideo/rimgosu 영상.mp4</code></li>

<details>
<summary>주의사항 보기/접기</summary>

 - **.mp4 영상만 허용됩니다.**
 - 영상의 이름은 **'rimgosu', 'matsuri', 'duckdragon' 중 하나를 포함** 해야 정상적으로 동작합니다.
     - ex : `matsuri test.mp4`
 - 여러 영상을 넣어도 정상 동작합니다.
 - export : 편집이 완전히 완료된 영상이 export 폴더에 담깁니다.
 - xmlcache : 분석이 완료된 영상이 .xml 파일로 저장됩니다.
 - wait : 자유롭게 활용해도 되는 여분 폴더입니다. 저는 주로 오류가 나는 영상들을 보관해두었다가 코드를 수정하는 데 사용하는 폴더였습니다.
 - Premier Pro가 실행되는 도중 다른 작업을 하면 오류가 발생할 수 있습니다.

</details>
</ol>
   
<ol start="2" data-sourcepos="45:1-46:0" dir="auto">
<li data-sourcepos="45:1-46:0"><code>/AutoEditor/runAutoEditor.py</code>를 실행해주세요.</li>

<details>
<summary>파라미터 보기/접기</summary>

```
run_autoEditor(    
        current_path,
        video_list,
        input_path,
        exf_path,
        framerate=3,
        res=1/3,
        FRchange=True,
        yoloDetect=True,
        changeXml=True,
        Premiere=True,
        screenshot=True,
        uploadYotube=False, #only False on real running
        display_newminion=True,
        newminion_patchday='_230831',
        shutdown=False
    )
```
</details>

<details>
<summary>파라미터 자세한 설명 보기/접기</summary>

- _runAutoEditor.py 코드 맨 아랫줄_ 에서 각종 설정을 변경할 수 있습니다.
- `FRchange, yoloDetect, changeXml` : **디버그를 위해 필요한 파라미터**이므로 반드시 True로 설정해두어야합니다.
- `framerate` : framerate = 3이 의미하는 것은 1초당 3번의 프레임을 분석하겠다는 뜻입니다. 5로 설정하면 더 정밀한 영상 분석이 가능하나 더 오래걸립니다.
- `res` : ffmpeg로 영상을 얼마나 더 축소할지 정합니다. res를 1로 정하면 원본 영상 그대로를 분석하고, res가 1/3이면 640px*480px 영상으로 만들어 분석합니다.
- `uploadYotube` : 자동으로 영상 업로드를 해주나, 유튜브 정책상 자동으로 올리면 밴을 먹을 수도 있을 것 같아 사용하진 않았습니다.
- `screenshot` : 가끔 전투 페이즈와 고용페이즈를 헷갈리는 경우가 있습니다. 그 때 openCV를 활용하여 처음부터 전투페이즈와 고용 페이즈를 구분하는 스크린샷을 찍습니다.
- `display_newminion` : 기물 정보를 자동으로 표시해줄지에 대한 설정입니다.
- `newminion_patchday` : 새로운 패치가 진행되면 폴더에 새로운 이미지를 추가해주어야합니다. 그 폴더의 이름을 적습니다.
- `shutdown` : 편집이 모두 완료되면 컴퓨터를 끕니다.

</details>
</ol>

3. `/AutoEditor/inputvideo/export` 폴더에서 편집된 영상을 확인하세요


