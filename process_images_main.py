import base64
import requests
import process_images_module
import process_images_from_pdf


# Path to your image
#path = "D:\\Amrita\\CellStrat\\processing_images\\pdfs\\Fourth.pdf"
path = "D:\\Amrita\\CellStrat\\processing_images\\images\\First.png"

query="What is written in image"

if process_images_module.is_pdf_file(path):
  image_bytes= process_images_from_pdf.process_pdf_file(path)
  response = process_images_module.process_images_from_pdf(image_bytes,query)
else:
  response = process_images_module.process_images(path,query)
print(response.content)


