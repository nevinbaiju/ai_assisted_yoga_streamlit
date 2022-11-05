import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, RTCConfiguration

import av

from pose_estimator import PoseEstimator

pe = PoseEstimator(window_size=8, smoothing_function='savgol')

class VideoProcessor(VideoProcessorBase):
    def __init__(self):
        self.style = 'color'    
    
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        print("Image", type(img))
        pose_coords = pe.get_pose_coords(img)
        if pose_coords:
            annotated_img = pe.get_annotated_image(img, pose_coords)
            angles = pe.get_angles(pose_coords)
            st.subheader(f'{angles}')
        else:
            annotated_img = img
        return av.VideoFrame.from_ndarray(annotated_img)
        
webrtc_streamer(key="vpf", video_processor_factory=VideoProcessor)

