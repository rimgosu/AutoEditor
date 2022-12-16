import os
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import * # __all__
from tkinter import filedialog
from PIL import Image
from runAutoEditor import *

root = Tk()
root.title("AutoEditor")

def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요", \
        filetypes=(("mp4 파일", "*.mp4"), ("모든 파일", "*.*")), \
        initialdir=r"C:\Users\rimgosu\Desktop\ShareFolder\AutoEditor\inputvideo")
    global video_list
    video_list = files
    video_list = [os.path.basename(file) for file in video_list if file.endswith(".mp4")]
    print(video_list)
    for file in files:
        list_file.insert(END, file)
def del_file():
    for index in reversed(list_file.curselection()):
        list_file.delete(index)
def browse_dest_path():
    global choosed_export
    folder_selected = filedialog.askdirectory()
    choosed_export = folder_selected.replace("/", "\\")
    print(choosed_export)
    if folder_selected == "": # 사용자가 취소를 누를 때
        print("폴더 선택 취소")
        return
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, choosed_export)
def start():
    framerate = int(fr_combo.get())
    res = int(int(res_combo.get())/1920)
    if FR_combo.get() == 'True':
        FR_bool = True
    else:
        FR_bool = False
    if yolo_combo.get() == 'True':
        yolo_bool = True
    else:
        yolo_bool = False
    if edit_combo.get() == 'True':
        edit_bool = True
    else:
        edit_bool = False
    if upload_combo.get() == 'True':
        upload_bool = True
    else:
        upload_bool = False

    try:
        current_path = os.path.dirname(__file__)
        if list_file.size() == 0:
            msgbox.showwarning("경고", "동영상 파일을 추가하세요")
            return
        if len(txt_dest_path.get()) == 0:
            msgbox.showwarning("경고", "저장 경로를 선택하세요")
            return
        run_autoEditor(
            current_path,
            video_list,
            choosed_export,
            framerate,
            res,
            FRchange=FR_bool,
            yoloDetect=yolo_bool,
            changeXml=True,
            Premiere=edit_bool,
            uploadYotube=upload_bool
            )
    except:
        current_path= os.path.dirname(__file__)
        choosed_export=os.path.join(current_path,'inputvideo')
        choosed_export= os.path.join(choosed_export, 'export')
        run_autoEditor(
            current_path,
            video_list,
            choosed_export,
            framerate,
            res,
            FRchange=FR_bool,
            yoloDetect=yolo_bool,
            changeXml=True,
            Premiere=edit_bool,
            uploadYotube=upload_bool
            )


current_path = os.path.dirname(__file__)
export_base_path = os.path.join(current_path, 'inputvideo')
export_base_path = os.path.join(export_base_path, 'export')
# 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5) # 간격 띄우기
btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="파일추가", command=add_file)
btn_add_file.pack(side="left")
btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="선택삭제", command=del_file)
btn_del_file.pack(side="right")
# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)
scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")
list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)
# 저장 경로 프레임
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)
txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) # 높이 변경
txt_dest_path.insert(END, export_base_path)
btn_dest_path = Button(path_frame, text="찾아보기", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)
# 옵션 프레임
frame_option = LabelFrame(root, text="옵션")
frame_option.pack(padx=5, pady=5, ipady=5)
#프레임 비교
lbl_width = Label(frame_option, text="프레임 비교", width=8)
lbl_width.grid(row=0, column=0,padx=5,pady=5)
fr_option = [3, 5, 7, 10, 15]
fr_combo = ttk.Combobox(frame_option, state="readonly", values=fr_option, width=10)
fr_combo.current(0)
fr_combo.grid(row=0, column=1,padx=5,pady=5)
#해상도 비교
lbl_space = Label(frame_option, text="해상도 비교", width=8)
lbl_space.grid(row=0, column=2,padx=5,pady=5)
res_option = [1920, 1080, 640, 320]
res_combo = ttk.Combobox(frame_option, state="readonly", values=res_option, width=10)
res_combo.current(2)
res_combo.grid(row=0, column=3,padx=5,pady=5)
# FRchange
lbl_format = Label(frame_option, text="FRchange", width=8)
lbl_format.grid(row=0, column=4,padx=5,pady=5)
FR_option = [True, False]
FR_combo = ttk.Combobox(frame_option, state="readonly", values=FR_option, width=10)
FR_combo.current(0)
FR_combo.grid(row=0, column=5,padx=5,pady=5)
# YoloDetect
lbl_format = Label(frame_option, text="YoloDetect", width=8)
lbl_format.grid(row=1, column=0,padx=5,pady=5)
yolo_option = [True, False]
yolo_combo = ttk.Combobox(frame_option, state="readonly", values=yolo_option, width=10)
yolo_combo.current(0)
yolo_combo.grid(row=1, column=1,padx=5,pady=5)
# AutoPremiere
lbl_format = Label(frame_option, text="AutoEdit", width=8)
lbl_format.grid(row=1, column=2,padx=5,pady=5)
edit_option = [True, False]
edit_combo = ttk.Combobox(frame_option, state="readonly", values=edit_option, width=10)
edit_combo.current(0)
edit_combo.grid(row=1, column=3,padx=5,pady=5)
# AutoUpload
lbl_format = Label(frame_option, text="AutoUpload", width=8)
lbl_format.grid(row=1, column=4,padx=5,pady=5)
upload_option = [True, False]
upload_combo = ttk.Combobox(frame_option, state="readonly", values=upload_option, width=10)
upload_combo.current(1)
upload_combo.grid(row=1, column=5,padx=5,pady=5)
# 진행 상황 Progress Bar
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)
p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)
# 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)
btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)
btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)
root.resizable(False, False)
root.mainloop()