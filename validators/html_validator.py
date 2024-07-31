from bs4 import BeautifulSoup
import html5lib

class HTMLValidator:
    def __init__(self):
        self.errors = []

    def validate(self, html_file):
        try:
            with open(html_file, 'r') as f:
                html_content = f.read()
            soup = BeautifulSoup(html_content, 'html5lib')
        except html5lib.html5lib.HTMLParserError as e:
            self.errors.append({"error": str(e), "type": "HTMLParserError"})
        except Exception as e:
            self.errors.append({"error": str(e), "type": "GeneralException"})

    def get_errors(self):
        return self.errors