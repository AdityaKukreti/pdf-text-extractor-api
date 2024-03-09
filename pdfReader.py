from pypdf import PdfReader


class PDFReader:

    def __init__(self):
        pass

    def getText(self,filename):
        reader = PdfReader(filename)
        pageCount = len(reader.pages)
        text = ""
        for pageNumber in range(pageCount):
            text += reader.pages[pageNumber].extract_text()
        # text = ""
        return text
    

        