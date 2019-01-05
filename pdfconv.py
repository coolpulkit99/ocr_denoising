from pdf2jpg import pdf2jpg
inputpath = r"test.pdf"
outputpath = r"convertedpdf"

result = pdf2jpg.convert_pdf2jpg(inputpath, outputpath, pages="ALL")
print(result)
