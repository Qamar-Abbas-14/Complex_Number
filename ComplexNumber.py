
class ComplexNumber(object):
    def __init__(self,real,img):
        self.img_part=img
        self.real_part=real

    def __str__(self):
        self.complex_number= str(self.real_part) +'+'+'j'+str(self.img_part)
        return self.complex_number

    def __repr__(self):
        mytuple=f"ComplexNumber({self.real_part},{self.img_part})"
        return mytuple




if __name__=='__main__':
    num1=ComplexNumber(2,3)
    s=str(num1)
    print(s)
    

