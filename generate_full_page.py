# import os
# from PIL import Image
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# from PyPDF2 import PdfReader, PdfWriter

# # Define file paths and settings
# qr_images_dir = './images/'  # Folder containing QR code images
# template_front3_path = './templates/coupons_template_front_a4.pdf'  # Front template for 3 QR codes
# template_back3_path = './templates/coupons_template_back_a4.pdf'  # Back template for 3 QR codes
# template_front2_path = './templates/coupons_template_front2.pdf'  # Front template for 2 QR codes
# template_back2_path = './templates/coupons_template_back2.pdf'  # Back template for 2 QR codes
# template_front1_path = './templates/coupon_template_front.pdf'  # Front template for 1 QR code
# template_back1_path = './templates/coupon_template_back.pdf'  # Back template for 1 QR code
# output_dir = './output/'  # Folder to save the generated PDFs

# # Ensure output directory exists
# os.makedirs(output_dir, exist_ok=True)

# # Function to create a new PDF page with QR images on the front and back template
# def create_pdf_with_qrs(qr_image_paths, output_pdf_path, template_front, template_back):
#     # Create a temporary PDF with the QR code images using ReportLab
#     qr_temp_pdf_path = './qr_temp.pdf'
#     c = canvas.Canvas(qr_temp_pdf_path, pagesize=letter)

#     # Define coordinates for the QR code placement
#     qr_coords = [(425.5, 65), (425.5, 345), (425.5, 625)]  # 3 slots vertically

#     # Loop to place QR codes on the front template
#     for idx, qr_image_path in enumerate(qr_image_paths):
#         if idx < 3:  # Ensure we are only placing 3 QR codes on the front
#             qr_x, qr_y = qr_coords[idx]
#             qr_width = 145
#             qr_height = 145
#             c.drawImage(qr_image_path, qr_x, qr_y, width=qr_width, height=qr_height)

#     c.save()

#     # Read the appropriate templates
#     reader_front = PdfReader(template_front)
#     reader_back = PdfReader(template_back)
#     qr_reader = PdfReader(qr_temp_pdf_path)

#     # Create a PDF writer to write the final document
#     writer = PdfWriter()

#     # Get the first page (front) and second page (back)
#     template_page1 = reader_front.pages[0]
#     template_page2 = reader_back.pages[0]

#     # Merge the QR codes onto the front page
#     template_page1.merge_page(qr_reader.pages[0])

#     # Add the front and back pages to the writer
#     writer.add_page(template_page1)
#     writer.add_page(template_page2)

#     # Write the final output PDF
#     with open(output_pdf_path, 'wb') as f:
#         writer.write(f)

#     # Clean up the temporary QR PDF
#     os.remove(qr_temp_pdf_path)

# # Function to divide QR images into chunks of 3
# def chunk_qr_images(qr_images):
#     return [qr_images[i:i + 3] for i in range(0, len(qr_images), 3)]

# # Loop through the QR code images and create PDFs
# def process_qr_images():
#     qr_images = [os.path.join(qr_images_dir, qr_image_name) for qr_image_name in os.listdir(qr_images_dir) if qr_image_name.endswith(('.png', '.jpg'))]
#     qr_images = sorted(qr_images)  # Ensure order, if needed

#     # Divide QR images into chunks of 3
#     qr_chunks = chunk_qr_images(qr_images)

#     # Iterate over the chunks and create PDFs for each chunk
#     for i, qr_chunk in enumerate(qr_chunks):
#         num_qrs = len(qr_chunk)

#         # Select the appropriate front and back templates based on the number of QR codes
#         if num_qrs == 3:
#             template_front = template_front3_path
#             template_back = template_back3_path
#         elif num_qrs == 2:
#             template_front = template_front2_path
#             template_back = template_back2_path
#         else:
#             template_front = template_front1_path
#             template_back = template_back1_path

#         output_pdf_path = os.path.join(output_dir, f'output_{i + 1}.pdf')

#         try:
#             # Create PDF with the QR code chunk
#             create_pdf_with_qrs(qr_chunk, output_pdf_path, template_front, template_back)
#             print(f"Generated: {output_pdf_path}")
#         except Exception as e:
#             print(f"Failed to generate PDF for chunk {i + 1}: {e}")

# if __name__ == "__main__":
#     process_qr_images()
#     print("PDFs generation completed.")


# import os
# from PIL import Image
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# from PyPDF2 import PdfReader, PdfWriter

# # Define file paths and settings
# qr_images_dir = './images/'  # Folder containing QR code images
# template_front3_path = './templates/coupons_template_front_a4.pdf'  # Front template for 3 QR codes
# template_back3_path = './templates/coupons_template_back_a4.pdf'  # Back template for 3 QR codes
# template_front2_path = './templates/coupons_template_front2.pdf'  # Front template for 2 QR codes
# template_back2_path = './templates/coupons_template_back2.pdf'  # Back template for 2 QR codes
# template_front1_path = './templates/coupon_template_front.pdf'  # Front template for 1 QR code
# template_back1_path = './templates/coupon_template_back.pdf'  # Back template for 1 QR code
# output_dir = './output/'  # Folder to save the generated PDFs

# # Ensure output directory exists
# os.makedirs(output_dir, exist_ok=True)

# # Function to create a new PDF page with QR images on the front and back template
# def create_pdf_with_qrs(qr_image_paths, template_front, template_back):
#     # Create a temporary PDF with the QR code images using ReportLab
#     qr_temp_pdf_path = './qr_temp.pdf'
#     c = canvas.Canvas(qr_temp_pdf_path, pagesize=letter)

#     # Define coordinates for the QR code placement
#     qr_coords = [(425.5, 65), (425.5, 345), (425.5, 625)]  # 3 slots vertically

#     # Loop to place QR codes on the front template
#     for idx, qr_image_path in enumerate(qr_image_paths):
#         if idx < 3:  # Ensure we are only placing 3 QR codes on the front
#             qr_x, qr_y = qr_coords[idx]
#             qr_width = 145
#             qr_height = 145
#             c.drawImage(qr_image_path, qr_x, qr_y, width=qr_width, height=qr_height)

#     c.save()

#     # Read the appropriate templates
#     reader_front = PdfReader(template_front)
#     reader_back = PdfReader(template_back)
#     qr_reader = PdfReader(qr_temp_pdf_path)

#     # Create a PDF writer to write the final document
#     writer = PdfWriter()

#     # Get the first page (front) and second page (back)
#     template_page1 = reader_front.pages[0]
#     template_page2 = reader_back.pages[0]

#     # Merge the QR codes onto the front page
#     template_page1.merge_page(qr_reader.pages[0])

#     # Add the front and back pages to the writer
#     writer.add_page(template_page1)
#     writer.add_page(template_page2)

#     # Return the writer instance for later use
#     return writer

# # Function to divide QR images into chunks of 3
# def chunk_qr_images(qr_images):
#     return [qr_images[i:i + 3] for i in range(0, len(qr_images), 3)]

# # Loop through the QR code images and create PDFs
# def process_qr_images():
#     qr_images = [os.path.join(qr_images_dir, qr_image_name) for qr_image_name in os.listdir(qr_images_dir) if qr_image_name.endswith(('.png', '.jpg'))]
#     qr_images = sorted(qr_images)  # Ensure order, if needed

#     # Divide QR images into chunks of 3
#     qr_chunks = chunk_qr_images(qr_images)

#     writer = PdfWriter()

#     # Iterate over the chunks and create PDFs for each chunk
#     for i, qr_chunk in enumerate(qr_chunks):
#         num_qrs = len(qr_chunk)

#         # Select the appropriate front and back templates based on the number of QR codes
#         if num_qrs == 3:
#             template_front = template_front3_path
#             template_back = template_back3_path
#         elif num_qrs == 2:
#             template_front = template_front2_path
#             template_back = template_back2_path
#         else:
#             template_front = template_front1_path
#             template_back = template_back1_path

#         try:
#             # Create PDF with the QR code chunk and add to the final writer
#             chunk_writer = create_pdf_with_qrs(qr_chunk, template_front, template_back)
#             # Add each generated page to the final PDF
#             for page in chunk_writer.pages:
#                 writer.add_page(page)
#             print(f"Added chunk {i + 1} to final PDF.")
#         except Exception as e:
#             print(f"Failed to generate PDF for chunk {i + 1}: {e}")

#     # Save the combined PDF
#     with open('./output/big.pdf', 'wb') as f:
#         writer.write(f)

# if __name__ == "__main__":
#     process_qr_images()
#     print("PDF generation completed.")

import os
import argparse
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter

# Define file paths and settings
qr_images_dir = './images/'  # Folder containing QR code images
template_front3_path = './templates/coupons_template_front_a4.pdf'  # Front template for 3 QR codes
template_back3_path = './templates/coupons_template_back_a4.pdf'  # Back template for 3 QR codes
template_front2_path = './templates/coupons_template_front2.pdf'  # Front template for 2 QR codes
template_back2_path = './templates/coupons_template_back2.pdf'  # Back template for 2 QR codes
template_front1_path = './templates/coupon_template_front.pdf'  # Front template for 1 QR code
template_back1_path = './templates/coupon_template_back.pdf'  # Back template for 1 QR code
output_dir = './output/'  # Folder to save the generated PDFs

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Function to create a new PDF page with QR images on the front and back template
def create_pdf_with_qrs(qr_image_paths, output_pdf_path, template_front, template_back):
    # Create a temporary PDF with the QR code images using ReportLab
    qr_temp_pdf_path = './qr_temp.pdf'
    c = canvas.Canvas(qr_temp_pdf_path, pagesize=letter)

    # Define coordinates for the QR code placement
    qr_coords = [(425.5, 65), (425.5, 345), (425.5, 625)]  # 3 slots vertically

    # Loop to place QR codes on the front template
    for idx, qr_image_path in enumerate(qr_image_paths):
        if idx < 3:  # Ensure we are only placing 3 QR codes on the front
            qr_x, qr_y = qr_coords[idx]
            qr_width = 145
            qr_height = 145
            c.drawImage(qr_image_path, qr_x, qr_y, width=qr_width, height=qr_height)

    c.save()

    # Read the appropriate templates
    reader_front = PdfReader(template_front)
    reader_back = PdfReader(template_back)
    qr_reader = PdfReader(qr_temp_pdf_path)

    # Create a PDF writer to write the final document
    writer = PdfWriter()

    # Get the first page (front) and second page (back)
    template_page1 = reader_front.pages[0]
    template_page2 = reader_back.pages[0]

    # Merge the QR codes onto the front page
    template_page1.merge_page(qr_reader.pages[0])

    # Add the front and back pages to the writer
    writer.add_page(template_page1)
    writer.add_page(template_page2)

    # Write the final output PDF
    with open(output_pdf_path, 'wb') as f:
        writer.write(f)

    # Clean up the temporary QR PDF
    os.remove(qr_temp_pdf_path)

# Function to divide QR images into chunks of 3
def chunk_qr_images(qr_images):
    return [qr_images[i:i + 3] for i in range(0, len(qr_images), 3)]

# Loop through the QR code images and create PDFs
def process_qr_images(save_separate_files=True):
    qr_images = [os.path.join(qr_images_dir, qr_image_name) for qr_image_name in os.listdir(qr_images_dir) if qr_image_name.endswith(('.png', '.jpg'))]
    qr_images = sorted(qr_images)  # Ensure order, if needed

    # Divide QR images into chunks of 3
    qr_chunks = chunk_qr_images(qr_images)

    if save_separate_files:
        # Generate separate PDF files for each chunk
        for i, qr_chunk in enumerate(qr_chunks):
            num_qrs = len(qr_chunk)

            # Select the appropriate front and back templates based on the number of QR codes
            if num_qrs == 3:
                template_front = template_front3_path
                template_back = template_back3_path
            elif num_qrs == 2:
                template_front = template_front2_path
                template_back = template_back2_path
            else:
                template_front = template_front1_path
                template_back = template_back1_path

            output_pdf_path = os.path.join(output_dir, f'output_{i + 1}.pdf')

            try:
                # Create PDF with the QR code chunk
                create_pdf_with_qrs(qr_chunk, output_pdf_path, template_front, template_back)
                print(f"Generated: {output_pdf_path}")
            except Exception as e:
                print(f"Failed to generate PDF for chunk {i + 1}: {e}")
    else:
        # Combine all the QR code chunks into one large PDF
        writer = PdfWriter()

        # Iterate over the chunks and create PDFs for each chunk
        for i, qr_chunk in enumerate(qr_chunks):
            num_qrs = len(qr_chunk)

            # Select the appropriate front and back templates based on the number of QR codes
            if num_qrs == 3:
                template_front = template_front3_path
                template_back = template_back3_path
            elif num_qrs == 2:
                template_front = template_front2_path
                template_back = template_back2_path
            else:
                template_front = template_front1_path
                template_back = template_back1_path

            # Create PDF with the QR code chunk
            created_pdf = create_pdf_with_qrs(qr_chunk, './temp.pdf', template_front, template_back)
            reader = PdfReader('./temp.pdf')

            # Add the front and back pages to the writer
            writer.add_page(reader.pages[0])  # Add the front page
            writer.add_page(reader.pages[1])  # Add the back page

            print(f"Added chunk {i + 1} to the large PDF.")

        # Save the combined PDF
        with open('./output/output_merged.pdf', 'wb') as f:
            writer.write(f)
        print("Combined PDF generated successfully.")

        # Clean up temporary file
        os.remove('./temp.pdf')

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Generate coupon PDFs with QR codes.")
    parser.add_argument('--separate', action='store_true', help="Generate separate PDF files for each chunk")
    parser.add_argument('--combine', action='store_true', help="Generate one combined PDF file")
    args = parser.parse_args()

    if args.separate and args.combine:
        print("Please choose only one option: --separate or --combine")
    elif args.separate:
        process_qr_images(save_separate_files=True)  # Generate separate files
    elif args.combine:
        process_qr_images(save_separate_files=False)  # Generate one large file
    else:
        print("Please specify an option: --separate or --combine")
