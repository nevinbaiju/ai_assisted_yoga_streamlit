import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, RTCConfiguration, WebRtcMode, create_mix_track, create_process_track
from streamlit_server_state import server_state, server_state_lock

import av
import cv2
import numpy as np
import math
import json

from pose_estimator import PoseEstimator
from _callbacks import *

from typing import List, Literal


with open('poses.json') as jsonfile:
    pose_dict = json.load(jsonfile)
poses = list(pose_dict.keys())

with server_state_lock["webrtc_contexts"]:
    if "webrtc_contexts" not in server_state:
        server_state["webrtc_contexts"] = []

with server_state_lock["mix_track"]:
    if "mix_track" not in server_state:
        server_state["mix_track"] = create_mix_track(
            kind="video", mixer_callback=mixer_callback, key="mix"
        )

mix_track = server_state["mix_track"]
self_ctx = webrtc_streamer(
        key="self",
        mode=WebRtcMode.SENDRECV,
        media_stream_constraints={"video": True, "audio": False},
        source_video_track=mix_track,
        sendback_audio=False,
    )

self_process_track = None
if self_ctx.input_video_track:
    self_process_track = create_process_track(
        input_track=self_ctx.input_video_track,
        processor_factory=VideoProcessor,
    )
    mix_track.add_input_track(self_process_track)

    pose = st.radio(
        "Select transform type",
        poses,
        key="filter1-type",
    )
    self_process_track.processor.pe.set_reference_angle(pose)