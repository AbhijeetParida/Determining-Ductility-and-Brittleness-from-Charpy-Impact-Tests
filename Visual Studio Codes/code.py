import cv2
import os

def select_brittle_fracture(binary_mask):
    # Find contours
    contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Check if any contours are found
    if contours:
        # Iterate over contours
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 100:  # Adjust the minimum area threshold as needed
                cv2.drawContours(binary_mask, [contour], -1, (255, 255, 255), -1)  # Mark as brittle fracture
    else:
        print("No contours found.")

# Specify the folder path containing the images
folder_path = "C:/Users/bibdh/V-6 steel axles"

# Get a list of all files in the folder
image_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg', '.png', '.tiff'))]

# Create/open a text file to store the results
output_file = open(os.path.join(folder_path, 'output.txt'), 'w')

# Iterate through the list of image files
for image_file in image_files:
    image_path = os.path.join(folder_path, image_file)
    
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Failed to read image: {image_file}")
        continue
    
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Thresholding to obtain binary mask
    _, binary_mask = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    
    # Select brittle fracture areas
    select_brittle_fracture(binary_mask)
    
    # Calculate ductile and brittle percentages
    total_pixels = binary_mask.shape[0] * binary_mask.shape[1]
    brittle_pixels = cv2.countNonZero(binary_mask)
    ductile_pixels = total_pixels - brittle_pixels
    ductile_percentage = (ductile_pixels / total_pixels) * 100
    brittle_percentage = (brittle_pixels / total_pixels) * 100
    
    # Write the results to the output file
    output_file.write(f"Image: {image_file}\n")
    output_file.write(f"Ductility Percentage: {ductile_percentage:.2f}%\n")
    output_file.write(f"Brittleness Percentage: {brittle_percentage:.2f}%\n\n")

# Close the output file
output_file.close()