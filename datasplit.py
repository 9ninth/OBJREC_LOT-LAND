import os
import shutil
from sklearn.model_selection import train_test_split

# Define the path to the images and annotations
data_path = 'C:\\Users\\juani\\Downloads\\data'

# Define the paths to the training, validation, and test directories
train_path = 'C:\\Users\\juani\\Downloads\\data\\train'
val_path = 'C:\\Users\\juani\\Downloads\\data\\val'
test_path = 'C:\\Users\\juani\\Downloads\\data\\test'

for path in [train_path, val_path, test_path]:
    os.makedirs(path, exist_ok=True)

all_image_files = [f for f in os.listdir(data_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

train_files, test_val_files = train_test_split(all_image_files, test_size=0.3, random_state=42)

val_files, test_files = train_test_split(test_val_files, test_size=0.5, random_state=42)

def copy_files(files, source_dir, target_dir):
    for file in files:

        source_image_path = os.path.join(source_dir, file)

        shutil.copy2(source_image_path, target_dir)


        annotation_file = os.path.splitext(file)[0] + '.txt'

        source_annotation_path = os.path.join(source_dir, annotation_file)

        if os.path.exists(source_annotation_path):

            shutil.copy2(source_annotation_path, target_dir)


copy_files(train_files, data_path, train_path)
copy_files(val_files, data_path, val_path)
copy_files(test_files, data_path, test_path)

print("Dataset successfully split into train, val, and test sets!")
