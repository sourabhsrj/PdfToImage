import fitz  # PyMuPDF
from PIL import Image

def pdf_to_images(pdf_path, image_path_template="page_{}.png"):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    for page_number in range(pdf_document.page_count):
        # Get a specific page
        page = pdf_document[page_number]

        # Render the page as a Pixmap
        pixmap = page.get_pixmap()

        # Convert the Pixmap to a Pillow Image
        image = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)

        # Save the image
        image_path = image_path_template.format(page_number + 1)
        image.save(image_path)

    # Close the PDF document
    pdf_document.close()

if __name__ == "__main__":
    # Replace 'your_pdf_file.pdf' with the path to your PDF file
    pdf_file_path = 'anandwan_menu.pdf'

    # Convert PDF to images
    pdf_to_images(pdf_file_path)

    print("PDF to images conversion completed.")
