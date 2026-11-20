#We'll define and execute all classes directly here

from abc import ABC, abstractmethod

class DataParser(ABC) : 
    # _method(self) = Protected Method - Current class's object can use methods & inheriting class can also use this method.

    def _open(self): 
        print("Opening the file")

    def _close(self) : 
        print("Closing the file")

    @abstractmethod
    def _dataParser(self): pass
        
    def _parse_template(self):
        self._open()
        # logic for parsing - depends on respective inheriting classes's parse()
        self._dataParser() 
        self._close()

class CSVParser(DataParser):
    def _dataParser(self):
        print("Parsing CSV File")

csv_parser = CSVParser()
csv_parser._parse_template()
# Opening the file
# Parsing CSV File
# Closing the file

# Now if we need to add more parsers, we can simply inherit the Abstract Class and implement method

class JSONParser(DataParser):
    def _dataParser(self):
        print("Parsing JSON File")

json_parser = JSONParser()
json_parser._parse_template()
# Opening the file
# Parsing JSON File
# Closing the file