import torch

batch_size = 2 
resize_to = 416
epochs = 10
num_workers = 4
device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
train_dir = '/home/burakzdd/my_workspace/faster-rcnn/data_train'
classes = [
    'prohibitory','danger','mandatory','other'
]
visualize_transformed_images = True
out_dir = '/home/burakzdd/my_workspace/faster-rcnn/models/'
model_name = "model_name"
test_model_name = "model_name"
test_video = "/path_name/"
test_image = ""