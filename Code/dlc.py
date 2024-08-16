import deeplabcut
from pathlib import Path

HERE = Path(__file__).parent
path_to_pupil_to_hyponogram_data = Path("/home/james/Code/Pupil-to-Hypnogram/Pupil-to-hypnogram-data")
path_video = HERE.parent / "data" / "eyeCamleft.mj2"

path_config_file = path_to_pupil_to_hyponogram_data /  "Intermediate/DLC/DLC-Kobayashi-2021-07-19/config.yaml"

deeplabcut.analyze_videos(
    path_config_file, [str(path_video)], videotype="mj2", save_as_csv=True
)
