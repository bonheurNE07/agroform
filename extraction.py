# importing modules
import json
import re
import numpy as np
import PIL
#from matplotlib import pyplot as plt
import cv2
import pytesseract

def ocr_image(image_path:str):
    # read the file
    image_path = image_path
    cv2_image = cv2.imread(image_path)

    #plot the file 

    #plt.imshow(cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB))
    #plt.show()
    
    # convert the RGB image into a binary imsge
    image = cv2.resize(cv2_image, None, fx=6, fy=6, interpolation=cv2.INTER_CUBIC) # elargit the image
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    image = cv2.threshold(image, 100,255,cv2.THRESH_BINARY)[1]
    image = cv2.medianBlur(image, 7)

    #plot the binary image

    """ plt.imshow(image, cmap='gray',vmin=0,vmax=255)
    plt.show() """

    #extract all the text on the image
    image_text = pytesseract.image_to_string(image)

    #####################
    # SEPARATE ALL DATA #
    #####################

    # EXTRACT NAMES
    name = re.compile(r'\w.+')

    match = re.findall(name, image_text)

    final_data = []
    id_number_found = False
    for index, text in enumerate(match):
        if "Amazina" in text or "Names" in text:
            final_data.append(match[index + 1])
        elif "ltanki" in text or  "yavutseho" in text\
            or "Date" in text or "Birth" in text:
            final_data.append(match[index + 1])
        elif "Igitsina" in text or "Sex" in text or \
            "Aho" in text or "Yatangiwe" in text or \
            "Place" in text or "Issue" in text:
            d = match[index + 1]
            d = d.split(" ")
            # remove and separate data
            if 'F' in d or 'Gore' in d:
                sex = "F"
                if 'F' in d :d.remove('F')
                if 'Gore' in d:d.remove('Gore')

            elif 'M' in d or 'Gabo' in d:
                sex = "M"
                if 'M' in d:d.remove('M')
                if 'Gabo' in d:d.remove('Gabo')
            
            cleaned_d = [item for item in d if item != '/']
            cleaned_data = []
            for t in cleaned_d:
                if len(t) >= 3:
                    cleaned_data.append(t)
            
            final_data.append(sex)
            final_data.append(cleaned_data)

        elif "Indangamuntu" in text or "National" in text\
    or "ID" in text or "No" in text or "Nytrayo" in text or "Signature" in text:
            if "card" not in text:  # Instead of pass, you can use "not in"
                # EXTRACT THE NATIONAL ID NO
                if not id_number_found:
                    dd = match[index + 1]
                    print(f"id fixing {dd}")
                    national_no_re = re.compile(r"\d{1} *\d{4} *\d{1} *\d{7} *\d{1} *\d{2}")
                    national_no = re.search(national_no_re, dd)
                    if national_no:
                        ID = dd[national_no.start():national_no.end()]
                        final_data.append(ID)
                        id_number_found = True
 
    for _ in final_data:
        if None in final_data:
            final_data.remove(None)
        elif "" in final_data:
            final_data.remove("")

    data = {}
    
    if len(final_data) >= 1:
        data["names"] = final_data[0]

    if len(final_data) >= 2:
        data["Date of Birth"] = final_data[1]

    if len(final_data) >= 3:
        data["sex"] = final_data[2]

    if len(final_data) >= 4:
        data["addresses"] = final_data[3]

    if len(final_data) >= 5:
        data["National ID No"] = final_data[4]

    # json_dataset = json.dumps(data, indent=4)
    

    # # save as json file "C:\Users\ST\Documents\SharedScreenshot.jpg"
    # path = f"{final_data[0]}.json"
    # with open(path, 'w') as outfile:
    #     outfile.write(json_dataset)
        
    return data

    

""" image_path = "D:/professional/capture/image2.jpg"
results = ocr_image(image_path)
print(results) """