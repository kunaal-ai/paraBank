from playwright.sync_api import Page

class HomePage:

    def __init__(self, page:Page) -> None:
        self.page = page
    
    def load(self):
        self.page.goto("https://parabank.parasoft.com/parabank/index.htm")
    
