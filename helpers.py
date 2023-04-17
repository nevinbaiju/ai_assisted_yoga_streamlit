import json

def read_poses_json():
    with open('poses.json') as jsonfile:
        pose_dict = json.load(jsonfile)
        poses = list(pose_dict.keys())

    return poses, pose_dict