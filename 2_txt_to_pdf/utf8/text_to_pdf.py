import os
import chardet
from fpdf import FPDF


# Encoding Conversion Functions
def convert_file_to_utf8(input_file_path, output_file_path):
    """Convert a text file from its original encoding to UTF-8."""
    with open(input_file_path, 'rb') as f:
        raw_data = f.read()
        detected_encoding = chardet.detect(raw_data)['encoding']
        print(f"[INFO] Detected encoding for {input_file_path}: {detected_encoding}")

    with open(input_file_path, 'r', encoding=detected_encoding, errors='replace') as f:
        content = f.read()

    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    # Log the creation of the new UTF-8 file
    print(f"[INFO] Created new UTF-8 file: {output_file_path}")


def convert_files_to_utf8():
    """Convert all .txt files in 'text_files' to UTF-8 and save them in 'utf8'."""
    text_folder = "../text_files"  # Navigate to the 'text_files' folder
    utf8_folder = "./"  # The script is in the 'utf8' folder

    # Ensure output folder exists
    if not os.path.exists(utf8_folder):
        os.makedirs(utf8_folder)

    for filename in os.listdir(text_folder):
        if filename.endswith('.txt'):
            input_path = os.path.join(text_folder, filename)
            output_path = os.path.join(utf8_folder, filename)
            try:
                convert_file_to_utf8(input_path, output_path)
            except Exception as e:
                print(f"[ERROR] Failed to process {filename}: {e}")


# PDF Generation Functions
def create_pdf_with_tabs(input_file, output_file, font_path, tab_width=20):
    """Generate a PDF from a UTF-8 text file with fixed tab spacing."""
    pdf = FPDF()

    # Add the Unicode font
    print(f"[INFO] Using font file: {font_path}")
    if not os.path.exists(font_path):
        raise FileNotFoundError(f"Font file not found: {font_path}")

    pdf.add_font("DejaVu", style="", fname=font_path, uni=True)
    pdf.set_font("DejaVu", size=12)
    pdf.add_page()

    # Read the UTF-8 text file and add its content to the PDF
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            formatted_line = line.replace('\t', ' ' * tab_width)
            pdf.multi_cell(0, 10, txt=formatted_line)

    pdf.output(output_file)
    print(f"[INFO] PDF created: {output_file}")


def generate_pdfs():
    """Generate PDFs for all UTF-8 files in the 'utf8' folder."""
    font_folder = "../dejavu"  # Navigate to the 'dejavu' folder
    font_file = os.path.join(font_folder, "DejaVuSans.ttf")
    pdf_folder = "../pdf"

    # Ensure the PDF folder exists
    if not os.path.exists(pdf_folder):
        os.makedirs(pdf_folder)

    for filename in os.listdir('.'):  # Current folder for input files
        if filename.endswith('.txt'):
            input_file = os.path.join('.', filename)
            output_file = os.path.join(pdf_folder, f"{os.path.splitext(filename)[0]}.pdf")
            try:
                create_pdf_with_tabs(input_file, output_file, font_file)
            except Exception as e:
                print(f"[ERROR] Failed to create PDF for {filename}: {e}")


# Main Execution
if __name__ == "__main__":
    print("[INFO] Converting text files to UTF-8...")
    convert_files_to_utf8()
    print("[INFO] Generating PDFs from UTF-8 files...")
    generate_pdfs()
