class Contact:
    def __init__(self, name, phone, email = ''):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return "Name : {}  Phone : {} Email : {}".format(\
            self.name, self.phone, self.email)

    def match(self, pattern):
        return pattern.lower() in self.name.lower() 
         
        
if __name__ == '__main__':
    c1 = Contact('abc', '99999999')
    c2 = Contact('pqr', '99999999', 'abc@abc.com')
    
    print(c1);print(c2)
    
    print(c1.match('pq'))
    print(c1.match('ABCD'))
    print(c1.match('ab'))
    print(c1.match('AB'))
    print(c1.match('ABC'))
    print(c2.match('ABC'))