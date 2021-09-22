from PyPDF2 import PdfFileReader, PdfFileWriter
import argparse

def crop_pdf(pdf_path):
    with open(pdf_path, "rb") as in_f:
        input = PdfFileReader(in_f)
        output = PdfFileWriter()

        for i in range(input.getNumPages()):
            page = input.getPage(i)
            page.cropBox.upperRight = (page.mediaBox.getUpperRight_x()/2, page.mediaBox.getUpperRight_y())
            output.addPage(page)

        output_file_name = in_f.name.replace('.pdf', '_cropped_version.pdf')
        with open(output_file_name, "wb") as out_f:
            output.write(out_f)
        return output_file_name

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Crop Pdf each page into half vertically')
    parser.add_argument('pdf_path', type=str, help='Pdf source path')
    args = parser.parse_args()

    output_file_name = crop_pdf(args.pdf_path)
    print('Finish: ', output_file_name)

