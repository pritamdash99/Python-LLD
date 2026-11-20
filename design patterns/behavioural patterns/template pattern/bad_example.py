class CSVParser:

    def openFile(self):
        print("Opening a file")

    def closeFile(self):
            print("Close a file")

    def parse(self):
         self.openFile()

         #Specific Logic for parsing CSV
         print("Parsing CSV File")
         self.closeFile()

class JsonParser:

    def openFile(self):
        print("Opening a file")

    def closeFile(self):
            print("Close a file")
            
    def parse(self):
         self.openFile()

         #Specific Logic for parsing JSON
         print("Parsing JSON File")
         self.closeFile()


csv = CSVParser()
csv.parse()
# Opening a file
# Parsing CSV File
# Close a file

json = JsonParser()
json.parse()
# Opening a file
# Parsing JSON File
# Close a file

#ISSUE - 
#  1. As mentioned in doc, you'll have  to duplicate everything for every new parser.
#  2. If Opening / Closing has to make changes, you'll have to manually change all Parser's open/close code.
