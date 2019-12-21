class Reversing:
    sent = ""
    vowels = ['a','e','i','o','u',]
    def __init__(self,sentence):
        self.sent = sentence
    def reverse(self):
        lst = self.sent.split()
        lst.reverse()
        return lst  
    def vowelCount(self):
        lst = self.sent.split()
        dict = {}
        for i in range(len(lst)):
            count=0
            mystr = lst[i]
            mystr = mystr.lower()
            for item in mystr:
                if item in self.vowels:
                    count+=1
            dict[mystr] = count 
        sortedDict = sorted(dict.items(),key=lambda x: x[1],reverse=True)
        return sortedDict
obj = Reversing('I am here because of you')
#print(obj.reverse())
print(obj.vowelCount())
