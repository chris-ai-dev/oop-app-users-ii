class Post:
    def __init__(self, name, time, text):
        self.name = name
        self.time = time
        self.text = text 
    
    def __str__(self):
        return f"{self.name}\n{self.time}\n{self.text}"