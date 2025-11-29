# NoiseReduction
Image Denoising & Cleaning Pipeline (OpenCV)

This project implements a multi-stage color image denoising and enhancement pipeline using OpenCV and NumPy. It is designed to remove heavy noise (including salt-and-pepper noise) from scanned documents or photographs while preserving color and edge detail.

The script reads a noisy image, applies multiple filtering techniques, optionally sharpens the result, saves the cleaned output, and generates a side-by-side comparison image.

Features

Removes salt-and-pepper noise using Median Filtering

Preserves edges and color transitions using Bilateral Filtering

Performs advanced color denoising using Non-Local Means

Optional image sharpening for restored detail

Automatically saves:

Final cleaned image (JPG + PNG)

Before/after comparison image

Displays visual results using Matplotlib

Technologies Used

Python 3.x

OpenCV (cv2)

NumPy

Matplotlib

Installation

Install the required dependencies:

pip install opencv-python numpy matplotlib

Project Structure
.
├── noisy_image_sample.jpg      # Input image (required)
├── main.py                     # Denoising script
├── final_cleaned_document.jpg  # Output image (auto-generated)
├── final_cleaned_document.png  # Output image (auto-generated)
└── before_after_comparison.png # Comparison output (auto-generated)

How It Works (Processing Pipeline)

Load Image (Color)

Reads the noisy image in full RGB color.

Median Filter

Removes salt-and-pepper noise while preserving major edges.

Bilateral Filter

Smooths the image while maintaining sharp edges and color boundaries.

Non-Local Means Denoising

Advanced color-aware noise reduction for high-quality cleanup.

Optional Sharpening

Restores fine details after denoising.

Export & Visualization

Saves cleaned images and a before/after comparison.

Usage

Place your noisy input image in the project folder and name it:

noisy_image_sample.jpg


Run the script:

python main.py


Outputs will be saved automatically:

final_cleaned_document.jpg

final_cleaned_document.png

before_after_comparison.png

Output Example

Original noisy image

Cleaned image (noise removed, colors preserved)

Side-by-side comparison saved as a high-resolution PNG

Customization

You can tune denoising strength by editing these values:

cv2.medianBlur(img, 7)
cv2.bilateralFilter(median_filtered, 9, 75, 75)
cv2.fastNlMeansDenoisingColored(
    bilateral, None,
    h=10,
    hColor=10,
    templateWindowSize=7,
    searchWindowSize=21
)


Increase values for stronger noise removal, decrease for more detail preservation.

Use Cases

Scanned document cleanup

Historical photo restoration

Noisy camera images

Preprocessing for OCR systems

Image enhancement for datasets

License

This project is free to use for educational and personal projects.
