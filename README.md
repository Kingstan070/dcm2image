Here’s a README file for your DICOM to image conversion program, complete with an installation guide and an example. I've added some emojis to make it more engaging!

---

# 🖼️ DICOM to Image Converter

This program converts DICOM (.dcm) files into PNG images while preserving the directory structure. It supports both single-slice and multi-slice DICOM images and provides options for image resizing.

## 📦 Installation

To get started, you need to install the necessary packages. You can either install them manually or use the provided Conda environment YAML file.

### Option 1: Manual Installation

Make sure you have Python installed on your system. You can install the required packages using `pip`:

```bash
pip install pydicom numpy Pillow
```

### Option 2: Using Conda Environment YAML

If you have a Conda environment YAML file in your folder, you can set up the environment as follows:

1. Navigate to the directory where the YAML file is located.
2. Run the following command:

```bash
conda env create -f environment.yml
```

Replace `environment.yml` with the name of your YAML file.

## 🚀 How to Use

1. **Prepare your DICOM files:** Place your DICOM files in a folder structure of your choice.
2. **Set the input and output directories:** Modify the `input_folder` and `output_directory` variables in the code to specify where your DICOM files are located and where you want to save the converted images.
3. **Run the program:** Execute the script, and it will process all `.dcm` files in the specified input folder and its subdirectories, saving the images in the same structure in the output directory.

### Example Usage

Here’s a snippet demonstrating how to set the input and output directories:

```python
# Example usage
input_folder = r"SampleData"  # Path to the folder containing .dcm files
output_directory = r'output_image'   # Path where converted images will be saved

# Convert all DICOM files in the specified folder
dcm_to_images(input_folder, output_directory, target_size=(720, 720))  # Adjust the target size as needed
```

## 📂 Directory Structure

The program will preserve the folder structure of your DICOM files. For example:

```
\new_60_70_dataset
│
├── Subfolder1
│   ├── image1.dcm
│   └── image2.dcm
│
├── Subfolder2
│   ├── Subsubfolder1
│   │   ├── image3.dcm
│   └── image4.dcm
```

After running the program, the output will be saved as:

```
\output_image
│
├── Subfolder1
│   ├── image1_slice_1.png
│   └── image2_slice_1.png
│
├── Subfolder2
│   ├── Subsubfolder1
│   │   ├── image3_slice_1.png
│   └── image4.png
```

## 💡 Notes

- Make sure you have the necessary permissions to read the DICOM files and write to the output directory.
- The program applies a windowing technique to enhance contrast in the images.

## 📧 Contact

For any questions or suggestions, please feel free to reach out:

- Email: tallwinkingstan@gmail.com
- GitHub: [Kingstan070](https://github.com/Kingstan070)