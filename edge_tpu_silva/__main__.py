import argparse

from .deps.check import get_installed_version
from .silva.silva_detect import process_detection


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
        "-l", "--labels", type=str, default=None, help="File path of labels file"
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

    args = parser.parse_args()

    if args.process == "det":
        process_detection(
            model_path=args.model,
            input_path=args.input,
            labels_path=args.labels,
            threshold=args.threshold,
            verbose=args.verbose,
            get_outputs=False,
        )

    elif args.process == "cls":
        edge_tpu_silva_version = get_installed_version("edge-tpu-silva")
        print(f"Object Classification is not available in {edge_tpu_silva_version}")

    elif args.process == "seg":
        edge_tpu_silva_version = get_installed_version("edge-tpu-silva")
        print(f"Object Segmentation is not available in {edge_tpu_silva_version}")

    else:
        message = (
            "\nCommands:\n\n"
            "--Check system and setup instruction(s):\n"
            "   run:    \033[94msilvatpu-sys\033[0m\n\n"
            "--Perform object detection:\n"
            "   run:    \033[94msilvatpu -p det -m path/to/model.tflite -i path/to/input/video.mp4 -l path/to/labels.txt -t 0.5 -v True\033[0m\n\n"
            "--Install Linux/Debian setup:\n"
            "   run:    \033[94msilvatpu-linux-setup\033[0m\n\n"
        )
        print(f"{message}")
