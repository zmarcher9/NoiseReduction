import cv2
import numpy as np

# Load the noisy image in COLOR
img = cv2.imread('noisy_image_sample.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Step 1: Apply Median Filter to remove salt-and-pepper noise (works on color images)
# This is excellent for removing random pixel noise while keeping colors
median_filtered = cv2.medianBlur(img, 7)

# Step 2: Apply Bilateral Filter to smooth while preserving edges
# This removes noise while keeping color transitions sharp
bilateral = cv2.bilateralFilter(median_filtered, 9, 75, 75)

# Step 3: Apply Non-local Means Denoising for COLOR images
# This is specifically designed for color image denoising
denoised = cv2.fastNlMeansDenoisingColored(bilateral, None, 
                                           h=10, 
                                           hColor=10,
                                           templateWindowSize=7, 
                                           searchWindowSize=21)

# Step 4: Optional - slight sharpening to restore detail
kernel_sharpen = np.array([[-1,-1,-1],
                           [-1, 9,-1],
                           [-1,-1,-1]]) / 9.0
sharpened = cv2.filter2D(denoised, -1, kernel_sharpen)

# Use denoised or sharpened based on preference
# For cleaner look use 'denoised', for sharper details use 'sharpened'
cleaned = denoised

# Save the final cleaned COLOR image
cv2.imwrite('final_cleaned_document.jpg', cleaned)
cv2.imwrite('final_cleaned_document.png', cleaned)

print("✓ Processing complete!")
print("✓ Color preserved, noise removed")
print("✓ Saved: final_cleaned_document.jpg")
print("✓ Saved: final_cleaned_document.png")

# Display before and after
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

ax1.imshow(img_rgb)
ax1.set_title('Original Noisy Image', fontsize=14, fontweight='bold')
ax1.axis('off')

cleaned_rgb = cv2.cvtColor(cleaned, cv2.COLOR_BGR2RGB)
ax2.imshow(cleaned_rgb)
ax2.set_title('Cleaned Document (Noise Removed)', fontsize=14, fontweight='bold')
ax2.axis('off')

plt.tight_layout()
plt.savefig('before_after_comparison.png', dpi=300, bbox_inches='tight')
plt.show()

print("✓ Saved: before_after_comparison.png")