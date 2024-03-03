from edge_tpu_silva import process_detection

# Example Usage with Required Parameters
model_path = 'path/to/your/model.tflite'
input_path = 'path/to/your/input/video.mp4'
imgsz = 240

# Run the object detection process
outs = process_detection(model_path, input_path, imgsz)

for _, _, _ in outs:
  pass