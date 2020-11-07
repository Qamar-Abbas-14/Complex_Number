
class ComplexNumber(object):
    def __init__(self,real,img):
        self.img_part=img
        self.real_part=real

    def __str__(self):
        if self.img_part>=0:
            self.complex_number= str(self.real_part) +'+'+'j'+str(self.img_part)
            return self.complex_number
        else:
            self.complex_number= str(self.real_part) +'-'+'j'+(str(self.img_part*(-1)))
            return self.complex_number

    def __repr__(self):
        mytuple=f"ComplexNumber({self.real_part},{self.img_part})"
        return mytuple

    def __add__(self, value):
        if isinstance(value, int):
            obj=ComplexNumber(0,0)
            obj.real_part=self.real_part+value
            obj.img_part=self.img_part
            return obj
        if isinstance(value, ComplexNumber):
            obj=ComplexNumber(0,0)
            obj.real_part=self.real_part+value.real_part
            obj.img_part=self.img_part+value.img_part
            return obj

    def __sub__(self, value):
        if isinstance(value, int):
            obj=ComplexNumber(0,0)
            obj.real_part=self.real_part-value
            obj.img_part=self.img_part
            return obj
        if isinstance(value, ComplexNumber):
            obj=ComplexNumber(0,0)
            obj.real_part=self.real_part-value.real_part
            obj.img_part=self.img_part-value.img_part
            return obj



if __name__=='__main__':
    num1=ComplexNumber(-2,7)
    num2=ComplexNumber(3,4)
    num3=num1+2
    num4=num1+num3
    num5=num1-num2
    print(num3)
    print(repr(num3))
    print(num1)
    print(num4)
    print(num5)
    print(type(num4))

