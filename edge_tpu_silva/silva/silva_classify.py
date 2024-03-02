import time
from typing import Tuple, Union

import cv2
from ultralytics import YOLO


def process_classification(
    model_path: str,
    input_path: str,
    imgsz: Union[int, Tuple[int, int]],
    threshold: int = 0.4,
    verbose: bool = True,
    show: bool = False,
    classes: list[int] = None,
):
    """Run object detection with with edge-tpu-silva

    Args:
        model_path (str): Define a .tflite model
        input_path (str): File path of image/video to process | Camera(0|1|2).
        imgsz (Union[int, Tuple[int, int]]): Defines the image size for inference. Can be a single integer 640 for square resizing or a (height, width) tuple. This should be same as what was used to export the YOLO model.
        threshold (int, optional): Threshold for detected objects. Defaults to 0.4.
        verbose (bool, optional): Display prints to terminal. Defaults to True.
        show (bool, optional): Display frame with detection. Defaults to False.
        classes (list[int], optional): Filters predictions to a set of class IDs. Only detections belonging to the specified classes will be returned. Defaults to None.

    Yields:
        (Gen): frame, objs_lst, fps
    """

    # Load a model
    model = YOLO(
        model=model_path, task="classify", verbose=False
    )  # Load a official model or custom model

    # Run Prediction
    outs = model.predict(
        source=input_path,
        conf=threshold,
        imgsz=imgsz,
        verbose=False,
        stream=True,
        show=show,
        classes=classes,
    )

    frame_count = 0
    start_time = time.time()
    for out in outs:
        img = out.orig_img
        probs = out.probs
        labels = out.names

        top5_id = probs.top5
        top5conf = probs.top5conf
        top5label = [labels[key] for key in top5_id if key in labels]

        objs_lst = {"top5_id": top5_id, "top5conf": top5conf, "top5label": top5label}
        if verbose:
            print("\n\n-------RESULTS--------")
            print("  top5_id:    ", top5_id)
            print("  top5conf: ", top5conf)
            print("  top5label: ", top5label)

        frame_count += 1
        elapsed_time = time.time() - start_time
        fps = frame_count / elapsed_time

        if verbose:
            print("----INFERENCE TIME----")
            print("FPS: {:.2f}".format(fps))

        yield img, objs_lst, fps

        # Break the loop if 'esc' key is pressed for video or camera
        if cv2.waitKey(1) == 27:
            break
