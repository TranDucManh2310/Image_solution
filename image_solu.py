import cv2
import numpy as np

def unsharp_mask(image, sigma=1.0, strength=1.5):
    # Làm mờ ảnh
    blurred = cv2.GaussianBlur(image, (0, 0), sigma)
    
    # Tăng cường độ nét bằng cách sử dụng Unsharp Masking
    sharpened = cv2.addWeighted(image, 1.0 + strength, blurred, -strength, 0)
    
    return sharpened

# Đọc ảnh
image_path = "oip-42.jpg"
image = cv2.imread(image_path)

if image is None:
    print(f"Can't read from {image_path}. Please check your image.")
else:
    # Áp dụng Unsharp Masking
    sharpened_image = unsharp_mask(image, sigma=1.0, strength=1.5)

    # Hiển thị hình ảnh gốc và hình ảnh đã làm nét
    cv2.imshow('Original Image', image)
    cv2.imshow('Sharpened Image', sharpened_image)

    # Chờ đợi phím bất kỳ để đóng cửa sổ
    cv2.waitKey(0)
    cv2.destroyAllWindows()