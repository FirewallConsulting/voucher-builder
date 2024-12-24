import os
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter

# Define file paths and settings
qr_images_dir = './images/'  # Folder containing QR code images
template_path = './templates/coupon_template.pdf'  # Your template PDF file
output_dir = './output/'  # Folder to save the generated PDFs

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Function to create a new PDF page with QR image on top of the template
def create_pdf_with_qr(qr_image_path, output_pdf_path):
    # Create a temporary PDF with the QR code image using ReportLab
    qr_temp_pdf_path = './qr_temp.pdf'
    c = canvas.Canvas(qr_temp_pdf_path, pagesize=letter)

    # Set the coordinates for the QR code placement (adjust as needed)
    qr_x = 425.5  # X coordinate to position the QR code
    qr_y = 65  # Y coordinate to position the QR code
    qr_width = 145  # Adjust the width as needed
    qr_height = 145  # Adjust the height as needed

    # Place the QR image on the canvas
    c.drawImage(qr_image_path, qr_x, qr_y, width=qr_width, height=qr_height)
    c.save()

    # Read the template PDF and the temporary QR PDF
    reader = PdfReader(template_path)
    qr_reader = PdfReader(qr_temp_pdf_path)

    # Create a PDF writer to write the final document
    writer = PdfWriter()

    # Get the first and second pages from the template
    template_page1 = reader.pages[0]
    template_page2 = reader.pages[1]

    # Overlay the QR code on the first page from the temporary QR PDF
    template_page1.merge_page(qr_reader.pages[0])

    # Add the modified first page and the second page to the writer
    writer.add_page(template_page1)
    writer.add_page(template_page2)

    # Write the final output PDF
    with open(output_pdf_path, 'wb') as f:
        writer.write(f)

    # Clean up the temporary QR PDF
    os.remove(qr_temp_pdf_path)

# Loop through the QR code images and create PDFs
for i, qr_image_name in enumerate(os.listdir(qr_images_dir)):
    if qr_image_name.endswith('.png') or qr_image_name.endswith('.jpg'):
        qr_image_path = os.path.join(qr_images_dir, qr_image_name)
        output_pdf_path = os.path.join(output_dir, f'output_{i+1}.pdf')
        
        # Create PDF with QR image
        create_pdf_with_qr(qr_image_path, output_pdf_path)

print("PDFs generated successfully!")
