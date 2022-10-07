class Mobile:
    def __init__(self,m):
        self.model=m
        
    def show_model(self,p):
        price=p
        print("Model: ",self.model,"Price: ",price)


realme=Mobile("Redmi 10")
realme=Mobile("samsung")
print(realme.model)
print(realme.model)
realme.show_model(15000)
realme.show_model(25000)
print(id(realme))
print(id(realme))



