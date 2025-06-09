class Document:
    def show(self): pass

class WordDocument(Document):
    def show(self): print("Word Document")

class PDFDocument(Document):
    def show(self): print("PDF Document")

class DocumentFactory:
    def create(self, type):
        if type == 'word': return WordDocument()
        if type == 'pdf': return PDFDocument()

if __name__ == "__main__":
    factory = DocumentFactory()
    doc = factory.create("pdf")
    doc.show()
