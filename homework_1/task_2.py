#Task 2 - Hierarchy

class text:
    def __init__(self, text):    
        self.text = str(text)
    def outp(self):              
        raise NotImplementedError("Subclass must implement abstract method")

class JSON(text):
    def outp(self, tag="text"):
        return "{\""+tag+"\":\""+self.text+"\"}"

class HTML(text):
    def outp(self):
        return "<p>"+self.text+"</p>"

class XML(text):
    def outp(self, tag="text"):
        return "<"+tag+">"+self.text+"</"+tag+">"

class plain(text):
    def outp(self):
        return self.text

class binary(text):
    def outp(self):
        return ' '.join(format(ord(x), 'b') for x in self.text)

text = "bing bing bong"

texts = [JSON(text),
           HTML(text),
           XML(text),
           plain(text),
           binary(text)]

for t in texts:
    print(t.__class__.__name__ + ' : ' + t.outp())
