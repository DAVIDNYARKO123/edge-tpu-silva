from edge_tpu_silva import process_detection

# Example Usage with Required Parameters
model_path = 'path/to/your/model.tflite'
input_path = 'path/to/your/input/video.mp4'
labels_path = 'path/to/your/labels.txt'

# Run the object detection process
process_detection(model_path, input_path, labels_path)