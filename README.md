<p align="center">
  <img src="https://github.com/DAVIDNYARKO123/edge-tpu-silva/blob/main/asset/images/edge-tpu-silva-banner.jpg" alt="edge-tpu-silva">
</p>

### The power of [`Coral Edge TPU`](https://coral.ai/docs/accelerator/get-started/#requirements) and [`Pycoral`](https://github.com/google-coral/pycoral) all in one place: [`edge-tpu-silva`](https://pypi.org/project/edge-tpu-silva/).

**edge-tpu-silva** is a Python package that simplifies the installation of the Coral TPU USB dependency and ensures compatibility with PyCoral. This package empowers object `detection` capabilities on various edge devices.


## Installation


### Step 1: Install edge-tpu-silva

To install **edge-tpu-silva**, use the following pip command in a specified python environment:

```bash
pip install edge-tpu-silva

```


### Step 2: Run Setup Command


### Raspberry Pi System Setup

In order to configure setup tools for Raspberry Pi, run the following command in the terminal after step 1 is completed:

```bash
setup-pi-tpu
```


| Raspberry Pi Model | Compatibility |
| ------------------- | -------------- |
| Raspberry Pi 3      | ✔              |
| Raspberry Pi 4      | ✔              |
| Raspberry Pi 5      | ✔              |



## Usage

### Object Detection Process

To perform object detection using the `process_detection` function, you can follow this example:

```python
from edge_tpu_silva import process_detection

# Example Usage with Required Parameters
model_path = 'path/to/your/model.tflite'
input_path = 'path/to/your/input/video.mp4'
labels_path = 'path/to/your/labels.txt'

# Run the object detection process
process_detection(model_path, input_path, labels_path)
```

### Running `process_detection` in the Terminal: Using the Entry Point "silvatpu"

To perform object detection with the `process_detection` function from the command line, you can use the user-friendly entry point `silvatpu`. Here's an example command:

```bash
silvatpu -p det -m path/to/model.tflite -i path/to/input/video.mp4 -l path/to/labels.txt -t 0.5 -v True
```


### `process_detection` Function Parameters

| Parameter      | Description                                        | Default Value |
| --------------- | -------------------------------------------------- | ------------- |
| `model_path`    | Path to the object detection model.                | -             |
| `input_path`    | Input video/camera(0|1|2) or Iamge for detection.    | -             |
| `labels_path`   | Path to the labels file for mapping class indices. | -             |
| `threshold`     | Confidence threshold for object detection.         | `0.4`         |
| `verbose`       | Enable/disable verbose output.                     | `True`        |


## Dependencies

    Coral TPU USB drivers
    PyCoral

## Contribution
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

Copyright (c) [2024] [David Nyarko](https://github.com/DAVIDNYARKO123)

This project is licensed under the terms of the MIT License. See the [LICENSE](asset/mit/license) file for details.

