import argparse
from typing import Tuple, Union

from .silva.silva_classify import process_classification
from .silva.silva_detect import process_detection
from .silva.silva_segment import process_segmentation


def parse_imgsz(value: str) -> Union[int, Tuple[int, int]]:
    try:
        # Try to parse as integer
        return int(value)
    except ValueError:
        try:
            # Try to parse as tuple
            values = map(int, value.split(","))
            return tuple(values)
        except ValueError:
            # If both attempts fail, raise an error
            raise argparse.ArgumentTypeError(
                "Invalid value for imgsz. It should be an integer or a tuple of two integers."
            )


def parse_classes(value: str) -> list[int]:
    try:
        # Try to parse as a list of integers
        return [int(x) for x in value.split(",")]
    except ValueError:
        raise argparse.ArgumentTypeError(
            "Invalid value for classes. It should be a comma-separated list of integers."
        )


def silvatpu():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "-p",
        "--process",
        default=None,
        type=str,
        help="Process type to perform. ('cls' | 'det' | 'seg') ",
    )
    parser.add_argument(
        "-m", "--model", default=None, type=str, help="File path of .tflite file"
    )
    parser.add_argument(
        "-i",
        "--input",
        default=None,
        type=str,
        help="File path of image/video to process | Camera(0|1|2)",
    )
    parser.add_argument(
        "-z",
        "--imgsz",
        type=parse_imgsz,
        default=None,
        help="Defines the image size for inference. Can be a single integer 640 for square resizing or a (height, width) tuple. This should be same as what was used to export the YOLO model.",
    )
    parser.add_argument(
        "-t",
        "--threshold",
        type=float,
        default=0.45,
        help="Threshold for detected objects",
    )
    parser.add_argument(
        "-v", "--verbose", type=bool, default=True, help="Display prints to terminal"
    )
    parser.add_argument(
        "-s", "--show", type=bool, default=False, help="Display frame with detection"
    )
    parser.add_argument(
        "-c",
        "--classes",
        type=parse_classes,
        default=None,
        help="Filters predictions to a set of class IDs. Only detections belonging to the specified classes will be returned",
    )

    args = parser.parse_args()

    if args.process == "det":
        outs = process_detection(
            model_path=args.model,
            input_path=args.input,
            imgsz=args.imgsz,
            threshold=args.threshold,
            verbose=args.verbose,
            show=args.show,
            classes=args.classes,
        )

        for _, _, _ in outs:
            pass

    elif args.process == "cls":
        outs = process_classification(
            model_path=args.model,
            input_path=args.input,
            imgsz=args.imgsz,
            threshold=args.threshold,
            verbose=args.verbose,
            show=args.show,
            classes=args.classes,
        )

        for _, _, _ in outs:
            pass

    elif args.process == "seg":
        outs = process_segmentation(
            model_path=args.model,
            input_path=args.input,
            imgsz=args.imgsz,
            threshold=args.threshold,
            verbose=args.verbose,
            show=args.show,
            classes=args.classes,
        )

        for _, _, _ in outs:
            pass

    else:
        message = (
            "\nCommands:\n\n"
            "--Check system and setup instruction(s):\n"
            "   run:    \033[94msilvatpu-sys\033[0m\n\n"
            "--Perform object detection:\n"
            "   run:    \033[94msilvatpu -p det -m path/to/model.tflite -i path/to/input/video.mp4 -l path/to/labels.txt -t 0.5 -v True -s True\033[0m\n\n"
            "--Install Linux/Debian setup:\n"
            "   run:    \033[94msilvatpu-linux-setup\033[0m\n\n"
        )
        print(f"{message}")
