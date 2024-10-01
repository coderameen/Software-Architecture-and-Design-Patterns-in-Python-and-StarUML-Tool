class DocumentProcessor:
    def process(self):
        self.open_file()
        self.read_data()
        print("File closed")
    
class WordProcessor(DocumentProcessor):
    def open_file(self):
        print("Word opened...")
    def read_data(self):
        print("Reading word..")

class PDFProcessor(DocumentProcessor):
    def open_file(self):
        print("PDF opened..")
    def read_data(self):
        print("Reading PDF...")

#client code
WordProcessor().process()
PDFProcessor().process()