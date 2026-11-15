class Document:
    def __init__(self, title: str, content: str, pages: int) -> None: 
        self.__title: str = title
        self.__content = content
        self.__pages = pages

    def get_title(self) -> str:
        return self.__title

    def get_content(self) -> str:
        return self.__content

    def get_pages(self) -> int:
        return self.__pages

#Printer class (depends on Document)
class Printer:
    def __init__(self, printer_name: str, printer_type: str) -> None:
        self.__printer_name : str = printer_name
        self.__printer_type : str = printer_type

    def print_document(self, document: Document) -> None:
        #Printer USES Document object temporarily through method parameter
        #After printing, Printer doesnot keep the Document

        print(f"\n{'='*10}")
        print(f"Printer: {self.__printer_name} ({self.__printer_type})")
        print(f"\n{'='*10}")
        print(f"Printing Document: {document.get_title()}")
        print(f"Total Pages : {document.get_pages()}")
        print(f"\nContent:")
        print(f"{document.get_content()}")
        print(f"\n{'='*10}")
        print("Printing Completed!\n")

    def get_printer_info(self) -> str:
        return f"{self.__printer_name} - {self.__printer_type}"

doc1 : Document = Document(
    title= "Python Tutorial",
    content = "This is a beginner's guide to Python Programming...",
    pages=20
)

doc2 : Document = Document(
    title= "LLD Notes", content="Low Level Design important concepts...", pages=10
)

office_printer : Printer = Printer("HP Laserjet", "Laser Printer")

office_printer.print_document(doc1)
office_printer.print_document(doc2)

"""
==========
Printer: HP Laserjet (Laser Printer)

==========
Printing Document: Python Tutorial
Total Pages : 20

Content:
This is a beginner's guide to Python Programming...

==========
Printing Completed!


==========
Printer: HP Laserjet (Laser Printer)

==========
Printing Document: LLD Notes
Total Pages : 10

Content:
Low Level Design important concepts...

==========
Printing Completed!
"""

# Important - Printer doesn't store the documents! 
# Documents still exist independently
print(f"Document 1 still exists: {doc1.get_title()}")
print(f"Document 2 still exists: {doc2.get_title()}")
# Document 1 still exists: Python Tutorial
# Document 2 still exists: LLD Notes