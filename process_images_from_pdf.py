# STEP 1 
# import libraries 
import fitz 
import io 
from PIL import Image 
import process_images_module

def process_pdf_file(file):
	
    # open the file 
    pdf_file = fitz.open(file) 

    # STEP 3 
    # iterate over PDF pages 
    for page_index in range(len(pdf_file)): 

        # get the page itself 
        page = pdf_file[page_index] 
        image_list = page.get_images() 

        # printing number of images found in this page 
        # if image_list: 
            # print( 
            # 	f"[+] Found a total of {len(image_list)} images in page {page_index}") 
        # else: 
            # print("[!] No images found on page", page_index) 
        for image_index, img in enumerate(page.get_images(), start=1): 

            # get the XREF of the image 
            xref = img[0] 

            # extract the image bytes 
            base_image = pdf_file.extract_image(xref) 
            image_bytes = base_image["image"] 

            # get the image extension 
            image_ext = base_image["ext"] 

        for image_index, img in enumerate(page.get_images(), start=1): 
            print("In For Loop ")
            query = "Can you read or analyse this image"

            # get the XREF of the image 
            xref = img[0] 

            # extract the image bytes 
            base_image = pdf_file.extract_image(xref) 
            
            image_bytes = base_image["image"] 


            image = Image.open(io.BytesIO(image_bytes))
            image_resized = image.resize((image.width // 2, image.height // 2))  
            #print(image_resized)
            image_bytes = base_image["image"]
            return image_bytes
            

