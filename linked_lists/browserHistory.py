class Node:
    def __init__(self,url):
        self.url = url
        self.prev = None
        self.next = None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.currentTab = Node(homepage)

    def visit(self, url: str) -> None:
        newTab = Node(url)
        self.currentTab.next = newTab
        newTab.prev = self.currentTab
        self.currentTab = newTab

    def back(self, steps: int) -> str:
        temp = self.currentTab
        while steps > 0 and temp.prev != None:
            temp = temp.prev
            steps-=1
        self.currentTab = temp
        return temp.url

    def forward(self, steps: int) -> str:
        temp = self.currentTab
        while steps > 0 and temp.next != None:
            temp = temp.next
            steps-=1
        self.currentTab = temp
        return temp.url