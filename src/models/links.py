class LinkManager:

    def __init__(self):
        self.links = []

    def add(self, link):
        self.links.append(link)

    def remove(self, link):
        self.links.remove(link)

    def clear(self):
        self.links.clear()

    def get_all(self):
        return self.links