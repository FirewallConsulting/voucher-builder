# QR Code PDF Generator for Foodbasket

This project is designed to generate PDF vouchers with QR codes specifically for **Foodbasket**, a network of grocery stores managed by **Synergy Marketing and Distribution**. The Python script overlays QR codes from the provided images onto a predefined PDF template, generating individual PDFs for each QR code.

## Features

- Load QR code images from a specified directory.
- Overlay each QR code on a predefined PDF template for Foodbasket vouchers.
- Create multiple PDF files, each containing a unique QR code.
- Handles both pages of the template (first page gets the QR code, second page is unchanged).
- Easily configurable for different template layouts or QR code sizes.

## Requirements

- Python 3.x
- `Pillow` (PIL Fork) - For handling image files.
- `ReportLab` - For creating and modifying PDFs.
- `PyPDF2` - For merging PDFs.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/qr-code-pdf-generator.git
   cd qr-code-pdf-generator
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Directory Structure

- **`./images/`**: Place your QR code images (e.g., `.png`, `.jpg`) for Foodbasket here.
- **`./coupon_template.pdf`**: Place your Foodbasket template PDF with an empty space for the QR code.
- **`./output/`**: The script will generate the output PDFs here.

### Running the Script

Once everything is set up, you can run the script to generate PDFs:

```bash
python generate_pdfs.py
```

This will read the QR code images from the `images/` folder, place each one on the Foodbasket template, and save the resulting PDFs to the `output/` folder.

## Configuration

You can modify the following settings in the script to suit your needs:

- **QR code placement**: Adjust the `qr_x`, `qr_y`, `qr_width`, and `qr_height` values in the script to position and resize the QR codes on the template.
- **Template path**: Change the `template_path` variable to the location of your Foodbasket template PDF file.
