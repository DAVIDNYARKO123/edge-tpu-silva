import time

try:
    from PIL import Image
except ModuleNotFoundError:
    # Handle the missing module
    print(
        "\033[93mWarning: 'PIL' module not found. Continuing without image processing support.\033[0m"
    )


import cv2
import numpy as np

try:
    from pycoral.adapters import common, detect
    from pycoral.utils.dataset import read_label_file
    from pycoral.utils.edgetpu import make_interpreter
except ModuleNotFoundError:
    # Handle the missing module
    print(
        "\033[93mWarning: 'pycoral' module not found. Continuing without Coral TPU functionality.\033[0m"
    )


def draw_objects(frame, objs, labels):
    """Draws the bounding box and label for each object on the frame using cv2.

    Args:
        frame (list): Image frame to process
        objs (list): Objects to dram on frame
        labels (str): Objects label

    Returns:
        List: Image frame
    """
    for obj in objs:
        bbox = obj.bbox
        cv2.rectangle(
            frame, (bbox.xmin, bbox.ymin), (bbox.xmax, bbox.ymax), (0, 0, 255), 2
        )
        label_text = "{}: {:.2f}".format(labels.get(obj.id, obj.id), obj.score)
        cv2.putText(
            frame,
            label_text,
            (bbox.xmin + 10, bbox.ymin + 20),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 0, 255),
            2,
        )
    return frame


def process_detection(
    model_path: str,
    input_path: str,
    labels_path: str,
    threshold: int = 0.4,
    verbose: bool = True,
    get_outputs: bool = False
):
    """Run object detection with with edge-tpu-silva

    Args:
        model_path (str): Define a .tflite model
        input_path (str): File path of image/video to process | Camera(0|1|2)
        labels_path (str): File path of labels file
        threshold (int, optional): Threshold for detected objects. Defaults to 0.4.
        verbose (bool, optional): Display prints to terminal. Defaults to True.
        get_outputs (bool, optional): Get a generator object of frame and its detection information.

    Yields:
        (Gen): frame, objs_lst
    """
    try:
        input_path = int(input_path)
        print("Reaching camera feed")
    except ValueError as e:
        print("Reaching an image or video from path")

    is_image = input_path.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp"))

    if is_image:
        image = Image.open(input_path)
        cap = None
    else:
        # Video or camera capture
        cap = cv2.VideoCapture(input_path)
        image = None

    labels = read_label_file(labels_path) if labels_path else {}
    interpreter = make_interpreter(model_path)
    interpreter.allocate_tensors()

    frame_count = 0
    start_time = time.time()

    while True:
        if not is_image:
            ret, frame = cap.read()
            if not ret:
                break
            # Convert the frame to RGB (PyCoral expects RGB images)
            image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        _, scale = common.set_resized_input(
            interpreter, image.size, lambda size: image.resize(size, Image.LANCZOS)
        )

        start = time.perf_counter()
        interpreter.invoke()
        inference_time = time.perf_counter() - start
        objs = detect.get_objects(interpreter, threshold, scale)

        frame_count += 1
        elapsed_time = time.time() - start_time

        fps = frame_count / elapsed_time

        if verbose:
            print("\n\n----INFERENCE TIME----")
            print("%.2f ms" % (inference_time * 1000))
            print("FPS: {:.2f}".format(fps))

        if verbose:
            print("\n-------RESULTS--------")

        if verbose:
            if not objs:
                print("No objects detected")

        objs_lst = []
        if verbose:
            if objs:
                for obj in objs:

                    print(labels.get(obj.id, obj.id))
                    print("  id:    ", obj.id)
                    print("  score: ", obj.score)
                    print("  bbox:  ", obj.bbox)
                    ol = {
                        "id": obj.id,
                        "label": labels.get(obj.id, obj.id),
                        "score": obj.score,
                        "bbox": obj.bbox,
                    }
                    objs_lst.append(ol)

        # Draw bounding boxes and FPS on the frame
        frame = np.array(image)
        draw_objects(frame, objs, labels)

        # Display FPS on the frame
        cv2.putText(
            frame,
            "FPS: {:.2f}".format(fps),
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
            cv2.LINE_AA,
        )

        # Display the frame with OpenCV
        cv2.imshow("Object Detection", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

        if get_outputs:
            # Yield the processed frame
            yield frame, objs_lst

        # Break the loop if any key is pressed for image files
        if is_image and cv2.waitKey(0) != -1:
            break

        # Break the loop if 'esc' key is pressed for video or camera
        if not is_image and cv2.waitKey(1) == 27:
            break

    if not is_image:
        cap.release()
    cv2.destroyAllWindows()
