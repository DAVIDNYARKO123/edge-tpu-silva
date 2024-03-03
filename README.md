<p align="center">
  <img src="asset/images/edge-tpu-silva-banner.jpg" alt="edge-tpu-silva">
</p>

### The power of [`Coral Edge TPU`](https://coral.ai/docs/accelerator/get-started/#requirements) and [`Ultralytics`](https://docs.ultralytics.com/) all in one place: [`edge-tpu-silva`](https://pypi.org/project/edge-tpu-silva/).

**edge-tpu-silva** is a Python package that simplifies the installation of the Coral TPU USB dependency and ensures compatibility with PyCoral and Ultralytics. This package empowers object `detection`, `segmentation` and `classification` capabilities on various edge devices.


## [Installation](#)


### Step 1: Install edge-tpu-silva

To install **edge-tpu-silva**, use the following pip command in a specified python environment:

```bash
pip install edge-tpu-silva

```


### Step 2: Run Setup Command

### [System Compatibility](#)

This table provides an overview of the compatibility of the system with different devices and operating systems.

|                       | Compatibility     | Setup Command             |
| --------------------- | ------------------ | ------------------------- |
| Raspberry Pi 5        | ✔                  | silvatpu-linux-setup      |
| Raspberry Pi 4        | ✔                  | silvatpu-linux-setup      |
| Raspberry Pi 3        | ✔                  | silvatpu-linux-setup      |
| Jetson Nano           | ✔                  | silvatpu-linux-setup      |
| x86-64                | ✔                  | silvatpu-linux-setup      |
| Armv7 (32-bit)        | ✔                  | silvatpu-linux-setup      |
| Armv8 (64-bit)        | ✔                  | silvatpu-linux-setup      |
| Windows               | ❌                 |                           |
| macOS                 | ❌                 |                           |

In order to configure setup tools for your system, run the setup command in the terminal after step 1 is completed.

Example: If you are on a Raspberry Pi 5, run below command in the terminal following step 1.

```bash
silvatpu-linux-setup
```

## Usage

### [Object Detection Process](#)

To perform object detection using the `process_detection` function, you can follow this example:

```python
from edge_tpu_silva import process_detection

# Example Usage with Required Parameters
model_path = 'path/to/your/model.tflite'
input_path = 'path/to/your/input/video.mp4'
imgsz = 240

# Run the object detection process
outs = process_detection(model_path, input_path, imgsz)

for _, _, _ in outs:
  pass
```

### Running `process_detection` in the Terminal: Using the Entry Point "silvatpu"

To perform object detection with the `process_detection` function from the command line, you can use the user-friendly entry point `silvatpu`. Here's an example command:

```bash
silvatpu -p det -m path/to/model.tflite -i path/to/input/video.mp4 -z 240 -t 0.5 -v True
```

### [Object Segmentation Process](#)

To perform object segmentation using the `process_segmentation` function, you can follow this example:

```python
from edge_tpu_silva import process_segmentation

# Example Usage with Required Parameters
model_path = 'path/to/your/model.tflite'
input_path = 'path/to/your/input/video.mp4'
imgsz = 192


# Run the object segmentation process
outs = process_segmentation(model_path, input_path, imgsz)

for _, _, _ in outs:
  pass
```

### Running `process_segmentation` in the Terminal: Using the Entry Point "silvatpu"

To perform object segmentation with the `process_segmentation` function from the command line, you can use the user-friendly entry point `silvatpu`. Here's an example command:

```bash
silvatpu -p seg -m path/to/model.tflite -i path/to/input/video.mp4 -z 192 -t 0.5 -v True
```


### Process `detection`, `segmentation` and `classification` Function Parameters

| Parameter      | Description                                        | Default Value |
| --------------- | -------------------------------------------------- | ------------- |
| `model_path`    | Path to the object segmentation model.             | \-            |
| `input_path`    | File path of image/video to process (Camera(0\|1\|2)). | \-           |
| `imgsz`         | Defines the image size for inference.  | \-             |
| `threshold`     | Threshold for detected objects.                    | `0.4`         |
| `verbose`       | Display prints to the terminal.                    | `True`        |
| `show`          | Display frame with segmentation.                   | `False`       |
| `classes`       | Filters predictions to a set of class IDs. | `None`            |

## Dependencies

    Coral TPU USB drivers
    PyCoral
    Ultralytics

## Contribution
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

Python Package Index Maintainer(s) (c) [2024] [David Nyarko](https://github.com/DAVIDNYARKO123)

