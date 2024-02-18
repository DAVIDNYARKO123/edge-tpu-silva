import argparse

from .deps.detect import process_detection


def silvatpu():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "-p",
        "--process",
        required=True,
        type=str,
        help="Process type to perform. ('cls' | 'det' | 'seg') ",
    )
    parser.add_argument(
        "-m", "--model", required=True, type=str, help="File path of .tflite file"
    )
    parser.add_argument(
        "-i",
        "--input",
        required=True,
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
            args.model, args.input, args.labels, args.threshold, args.verbose
        )
