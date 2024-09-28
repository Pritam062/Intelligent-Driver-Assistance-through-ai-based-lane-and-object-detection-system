import os
import cv2
from lane_detector.detector import DetectLane
from object_detector.detector import DetectObject


class LO_Detector:
    def __init__(self, op_dir=None):
        self.op_dir = op_dir if op_dir else "results"
        self.lane_detector = DetectLane()
        self.obj_detector = DetectObject()
        
    def detect(self, video_path):
        """main pipeline for detecting the lanes, roads, objects from video frames"""
        
        """
        Working:
        1. Capture the video from given video path
        2. Get the width, height, fps of captured video for remaining the constant in output video 
        3. Now iterate over each frame 1 by 1 and perfrom:
            1. Detect Lanes
            2. Detect Objects
            3. Add the output frame in output video
        4. Save the all the output frames/video in directory
        5. return the output video path
        """
        
        # get the name of video
        file_name = os.path.basename(video_path)

        cap = cv2.VideoCapture(video_path)
        
        # return none, if system can't open the file
        if not cap.isOpened():
            raise Exception("Can't open the video.")
        
        
        # prepare the output video    
        original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)
        output_video_path = os.path.join(self.op_dir, file_name)
        fourcc = cv2.VideoWriter_fourcc(*'H264')
        out = cv2.VideoWriter(output_video_path, fourcc, fps, (original_width, original_height))

        # work on each frame
        while cap.isOpened():
            ret, frame = cap.read()
    
            if not ret:
                break
    
            frame = self.lane_detector.detect(frame)
            frame = self.obj_detector.detect(frame)
            out.write(frame)
            
        cap.release()
        out.release()
        cv2.destroyAllWindows()

        return output_video_path