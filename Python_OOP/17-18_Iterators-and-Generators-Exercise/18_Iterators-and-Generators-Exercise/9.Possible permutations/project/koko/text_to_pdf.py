import os
from fpdf import FPDF

def create_pdf_with_tabs(input_file, output_file, font_path, tab_width=20):
    """Generate a PDF from a UTF-8 text file with fixed tab spacing."""
    pdf = FPDF()

    # Add the Unicode font
    font_path = os.path.abspath(font_path)
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

def process_files(utf8_folder, pdf_folder, font_folder):
    """Generate PDFs for all UTF-8 files in the specified folder."""
    font_path = os.path.join(font_folder, "DejaVuSans.ttf")

    if not os.path.exists(pdf_folder):
        os.makedirs(pdf_folder)

    for filename in os.listdir(utf8_folder):
        if filename.endswith('.txt'):
            input_file = os.path.join(utf8_folder, filename)
            output_file = os.path.join(pdf_folder, f"{os.path.splitext(filename)[0]}.pdf")
            try:
                create_pdf_with_tabs(input_file, output_file, font_path)
            except Exception as e:
                print(f"[ERROR] Failed to create PDF for {filename}: {e}")

if __name__ == "__main__":
    # Folder paths
    main_folder = os.getcwd()
    utf8_folder = os.path.join(main_folder, 'utf8')
    pdf_folder = os.path.join(main_folder, 'pdf')
    font_folder = os.path.join(main_folder, 'dejavu')

    print(f"[INFO] Generating PDFs from {utf8_folder} to {pdf_folder}")
    process_files(utf8_folder, pdf_folder, font_folder)
