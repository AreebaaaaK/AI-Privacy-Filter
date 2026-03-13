import cv2
import pytesseract
from detector import detect_sensitive_data
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_data(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    data = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)
    full_text = pytesseract.image_to_string(gray)

    return img, data, full_text


def blur_regions(img, data, indices):
    for i in indices:
        x = data['left'][i]
        y = data['top'][i]
        w = data['width'][i]
        h = data['height'][i]

        roi = img[y:y+h, x:x+w]
        blurred = cv2.GaussianBlur(roi, (51, 51), 0)
        img[y:y+h, x:x+w] = blurred

    return img


def process_image(image_path, output_path):
    img, data, full_text = extract_text_data(image_path)

    sensitive_indices = detect_sensitive_data(data)

    result_img = blur_regions(img, data, sensitive_indices)

    cv2.imwrite(output_path, result_img)

    return output_path


if __name__ == "__main__":
    input_image = "test.png"
    output_image = "output.png"

    process_image(input_image, output_image)

    print("Privacy filtering complete. Check output.png")