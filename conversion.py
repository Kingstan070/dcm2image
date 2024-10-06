import os
import pydicom
import numpy as np
from PIL import Image
from tqdm import tqdm

def dcm_to_images(input_folder, output_dir, target_size=(2048, 2048)):
    os.makedirs(output_dir, exist_ok=True)

    dicom_files = []
    for root, dirs, files in os.walk(input_folder):
        for filename in files:
            if filename.endswith('.dcm'):
                dicom_files.append(os.path.join(root, filename))

    with tqdm(total=len(dicom_files), desc='Processing DICOM files') as pbar:
        for dcm_file_path in dicom_files:
            dicom_data = pydicom.dcmread(dcm_file_path)
            pixel_array = dicom_data.pixel_array

            relative_path = os.path.relpath(os.path.dirname(dcm_file_path), input_folder)
            new_subdirectory = os.path.join(output_dir, relative_path)
            os.makedirs(new_subdirectory, exist_ok=True)

            if pixel_array.ndim == 3:
                with tqdm(total=pixel_array.shape[0], desc=f'Processing slices for {os.path.basename(dcm_file_path)}', leave=False) as slice_pbar:
                    for i in range(pixel_array.shape[0]):
                        slice_image = pixel_array[i]

                        window_center = np.mean(slice_image)
                        window_width = np.max(slice_image) - np.min(slice_image)
                        slice_image = np.clip(slice_image, window_center - window_width / 2, window_center + window_width / 2)
                        slice_image = (slice_image - np.min(slice_image)) / (np.max(slice_image) - np.min(slice_image)) * 255
                        slice_image = slice_image.astype(np.uint8)

                        image = Image.fromarray(slice_image)
                        image = image.resize(target_size, Image.LANCZOS)

                        output_filename = os.path.join(new_subdirectory, f"{os.path.splitext(os.path.basename(dcm_file_path))[0]}_slice_{i + 1}.png")
                        image.save(output_filename, format='PNG')
                        slice_pbar.update(1)

            else:
                window_center = np.mean(pixel_array)
                window_width = np.max(pixel_array) - np.min(pixel_array)
                pixel_array = np.clip(pixel_array, window_center - window_width / 2, window_center + window_width / 2)
                pixel_array = (pixel_array - np.min(pixel_array)) / (np.max(pixel_array) - np.min(pixel_array)) * 255
                pixel_array = pixel_array.astype(np.uint8)

                image = Image.fromarray(pixel_array)
                image = image.resize(target_size, Image.LANCZOS)

                output_filename = os.path.join(new_subdirectory, f"{os.path.splitext(os.path.basename(dcm_file_path))[0]}.png")
                image.save(output_filename, format='PNG')

            pbar.update(1)
