# get the pose data
import mediapipe as mp 
import cv2
import numpy as np
p_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

pose = mp_pose.Pose(
        static_image_mode=False,
        model_complexity=2,
        enable_segmentation=False,
        min_detection_confidence=0.5)

def imageReader(IMGFile = None):
    if IMGFile == None:
        print("No input")
        return None
    elif IMGFile != None:
        return cv2.imread(IMGFile)
        
    
def GetPoseDataFromVideo(videoFile = None):
    '''
    return a list of dicts
    '''
    if videoFile == None:
        print("No Input")
        return None
    cap = cv2.VideoCapture(videoFile)
    #视频属性
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #获取原视频的宽
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) #获取原视频的搞
    fps = int(cap.get(cv2.CAP_PROP_FPS)) #帧率
    fourcc = int(cap.get(cv2.CAP_PROP_FOURCC)) #视频的编码
    n = 0 #总的帧数
    data_list = [] #每个时刻的数据
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            n += 1
            data_list.append(GetPoseDataFromPicture(image = frame))
            print("第{}帧处理完成".format(n),end=', ')
            try:
                len(data_list[-1])
                print("发现有效坐标")
            except Exception as e:
                print("但未发现有效坐标")
        else:
            cap.release()
    return data_list,n
    
def GetPoseDataFromPicture(image = None,imageFile = None):
    '''
    return a dict  
    '''
    if image.all() == None:
        image = imageReader(imageFile)
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_pose = mp.solutions.pose
    BG_COLOR = (192, 192, 192) # gray
    data = {}
    # Convert the BGR image to RGB before processing.
    results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    
    if results.pose_world_landmarks == None:
        return None
    data = results.pose_world_landmarks.landmark
    #print(results.pose_world_landmarks .landmark)
    return data
    """
    The 33 pose landmarks.
        NOSE = 0
        LEFT_EYE_INNER = 1
        LEFT_EYE = 2
        LEFT_EYE_OUTER = 3
        RIGHT_EYE_INNER = 4
        RIGHT_EYE = 5
        RIGHT_EYE_OUTER = 6
        LEFT_EAR = 7
        RIGHT_EAR = 8
        MOUTH_LEFT = 9
        MOUTH_RIGHT = 10
        LEFT_SHOULDER = 11
        RIGHT_SHOULDER = 12
        LEFT_ELBOW = 13
        RIGHT_ELBOW = 14
        LEFT_WRIST = 15
        RIGHT_WRIST = 16
        LEFT_PINKY = 17
        RIGHT_PINKY = 18
        LEFT_INDEX = 19
        RIGHT_INDEX = 20
        LEFT_THUMB = 21
        RIGHT_THUMB = 22
        LEFT_HIP = 23
        RIGHT_HIP = 24
        LEFT_KNEE = 25
        RIGHT_KNEE = 26
        LEFT_ANKLE = 27
        RIGHT_ANKLE = 28
        LEFT_HEEL = 29
        RIGHT_HEEL = 30
        LEFT_FOOT_INDEX = 31
        RIGHT_FOOT_INDEX = 32
        """