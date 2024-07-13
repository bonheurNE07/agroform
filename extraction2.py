import json
import re
import cv2
import pytesseract

def ocr_image(image_path):
    # Read the image
    cv2_image = cv2.imread(image_path)

    # Preprocessing
    gray_image = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2GRAY)
    binary_image = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY)[1]
    denoised_image = cv2.medianBlur(binary_image, 7)

    # OCR
    image_text = pytesseract.image_to_string(denoised_image, config='--psm 6')
    print(image_text)
    # Extract relevant data using regular expressions
    name = re.search(r'Amazina / Names\n(.+)', image_text)
    birth_date = re.search(r'ltariki yavutseho / Date of Birth\n(.+)', image_text)
    sex = re.search(r'igitsina/ Sex Aho Yatangiwe / Place of \ssue\n(.+)', image_text)
    national_id = re.search(r'Indangamuntu / National ID No\n(.+)', image_text)

    data = {
        "names": name.group(1) if name else "",
        "Date of Birth": birth_date.group(1) if birth_date else "",
        "sex": sex.group(1) if sex else "",
        "National ID No": national_id.group(1) if national_id else ""
    }

    json_dataset = json.dumps(data, indent=4)
    return json_dataset

image_path = "D:/professional/capture/image2.jpg"
results = ocr_image(image_path)
print(results)
