import cv2
import pytesseract
import re

def preprocess_image(image_path):
    cv2_image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    binary_image = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return binary_image

def extract_id_card_data(image_path):
    preprocessed_image = preprocess_image(image_path)
    
    extracted_text = pytesseract.image_to_string(preprocessed_image, lang='eng')
    
    return extracted_text

def extract_data_using_regex(text, pattern):
    match = re.search(pattern, text)
    return match.group(1) if match else None

# Replace with the path to your ID card image
image_path = "D:/professional/capture/image2.jpg"

extracted_data = extract_id_card_data(image_path)

# Define regular expression patterns for different data fields
name_pattern = r'Amazina / Names\n(.+)'
birth_date_pattern = r'ltariki yavutseho / Date of Birth\n(.+)'
sex_pattern = r'igitsina/ Sex Aho Yatangiwe / Place of \ssue\n(.+)'
national_id_pattern = r'Indangamuntu / National ID No\n(.+)'

# Extract data using regular expressions
name = extract_data_using_regex(extracted_data, name_pattern)
birth_date = extract_data_using_regex(extracted_data, birth_date_pattern)
sex = extract_data_using_regex(extracted_data, sex_pattern)
national_id = extract_data_using_regex(extracted_data, national_id_pattern)

# Print extracted data
print("Name:", name)
print("Birth Date:", birth_date)
print("Sex:", sex)
print("National ID:", national_id)
