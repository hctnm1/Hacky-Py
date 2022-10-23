from abc import ABC, abstractmethod 
import pandas as p
class CGPA(ABC):
    @abstractmethod
    def get_marks(self): 
        pass
    @abstractmethod
    def cal_GPA(self):
        pass
    @abstractmethod
    def getGPA(self):
        pass
    @abstractmethod
    def cal_CGPA(self):
        pass
    @abstractmethod
    def getCGPA(self):
        pass
class Student_A(CGPA):
    def get_marks(self,m1,m2,m3): 
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def cal_GPA(self,GPA1=0,GPA2=0,GPA3=0,g=0,g2=0,g3=0):
        if (self.m1>=85) or(self.m1 == 85):
            self.g = "A"
            self.GPA1 = 4
        elif (self.m1>=70) or(self.m1 == 70):
            self.g = "B"         
            self.GPA1 = 3
        elif (self.m1>=55) or(self.m1 == 55):
            self.g = "C"        
            self.GPA1= 2
        elif (self.m1>=40) or(self.m1 == 40):
            self.g = "D"          
            self.GPA1 = 1
        elif (self.m1>=0) or(self.m1 == 0):
            self.g = "F"
            self.GPA1 = 0
        if (self.m2>=85)or(self.m2 == 85):
            self.g2 = "A"
            self.GPA2 = 4
        elif (self.m2>=70) or(self.m2 == 70):
            self.g2 = "B"         
            self.GPA2 = 3
        elif (self.m2>=55) or(self.m2 == 55):
            self.g2 = "C"         
            self.GPA2 = 2
        elif (self.m2>=40) or(self.m2 == 40):
            self.g2 = "D"
            self.GPA2= 1
        elif (self.m2>=0) or(self.m2 == 0):
            self.g2 = "F"
            self.GPA2 = 0
        if (self.m3>=85) or(self.m3 == 85):
            self.g3 = "A"        
            self.GPA3 = 4
        elif (self.m3>=70) or(self.m3 == 70):
            self.g3 = "B"         
            self.GPA3 = 3
        elif (self.m3>=55) or(self.m3 == 55):
            self.g3 = "C"
            self.GPA3 = 2
        elif (self.m3>=40) or(self.m3 == 40):
            self.g3 = "D"          
            self.GPA3 = 1
        elif (self.m3>=0) or(self.m3 == 0):
            self.g3 = "F" 
            self.GPA3 = 0
        else:
            print("Nothing")
    def getGPA(self):
        dict1={
            "MARK":[self.m1,self.m2,self.m3],
            "GRADE":[self.g,self.g2,self.g3],
            "GPA":[self.GPA1,self.GPA2,self.GPA3]
        }
        d=p.DataFrame(dict1)
        d.index+=1
        print("Student A:")
        display(d)
    def cal_CGPA(self,CGPA= 0 ):
        Add  = self.GPA1 + self.GPA2 +self.GPA3
        self.CGPA = Add // 3
    def getCGPA(self):
        print(f"CGPA : {self.CGPA}")
class Student_B(CGPA):
    def get_marks(self,m1,m2,m3,m4,m5): 
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.m5 = m5
    def cal_GPA(self,GPA1=0,GPA2=0,GPA3=0,GPA4=0,GPA5=0,g=0,g2=0,g3=0,g4=0,g5=0):
        if (self.m1>=85) or(self.m1 == 85):
            self.g = "A"            
            self.GPA1 = 4
        elif (self.m1>=70) or(self.m1 == 70):
            self.g = "B"           
            self.GPA1 = 3
        elif (self.m1>=55) or(self.m1 == 55):
            self.g = "C"       
            self.GPA1= 2
        elif (self.m1>=40) or(self.m1 == 40):
            self.g = "D"          
            self.GPA1 = 1
        elif (self.m1>=0) or(self.m1 == 0):
            self.g = "F"
            self.GPA1 = 0
        if (self.m2>=85)or(self.m2 == 85):
            self.g2 = "A"           
            self.GPA2 = 4
        elif (self.m2>=70) or(self.m2 == 70):
            self.g2 = "B"  
            self.GPA2 = 3
        elif (self.m2>=55) or(self.m2 == 55):
            self.g2 = "C"
            self.GPA2 = 2
        elif (self.m2>=40) or(self.m2 == 40):
            self.g2 = "D"
            self.GPA2= 1
        elif (self.m2>=0) or(self.m2 == 0):
            self.g2 = "F"
            self.GPA2 = 0
        if (self.m3>=85) or(self.m3 == 85):
            self.g3 = "A"
            self.GPA3 = 4
        elif (self.m3>=70) or(self.m3 == 70):
            self.g3 = "B"
            self.GPA3 = 3
        elif (self.m3>=55) or(self.m3 == 55):
            self.g3 = "C"
            self.GPA3 = 2
        elif (self.m3>=40) or(self.m3 == 40):
            self.g3 = "D"
            self.GPA3 = 1
        elif (self.m3>=0) or(self.m3 == 0):
            self.g3 = "F" 
            self.GPA3 = 0
        if (self.m4>=85) or(self.m4 == 85):
            self.g4 = "A"
            self.GPA4 = 4
        elif (self.m4>=70) or(self.m4 == 70):
            self.g4 = "B"
          
            self.GPA4 = 3
        elif (self.m4>=55) or(self.m4 == 55):
            self.g4 = "C"
            self.GPA4 = 2
        elif (self.m4>=40) or(self.m4 == 40):
            self.g4 = "D"
          
            self.GPA4 = 1
        elif (self.m4>=0) or(self.m4 == 0):
            self.g4 = "F" 
            self.GPA4 = 0
        if (self.m5>=85) or(self.m5 == 85):
            self.g5 = "A"
            self.GPA5 = 4
        elif (self.m5>=70) or(self.m5 == 70):
            self.g5 = "B"
          
            self.GPA5 = 3
        elif (self.m5>=55) or(self.m5 == 55):
            self.g5 = "C"
            self.GPA5 = 2
        elif (self.m5>=40) or(self.m5 == 40):
            self.g5 = "D"
          
            self.GPA5 = 1
        elif (self.m5>=0) or(self.m5 == 0):
            self.g5 = "F" 
            self.GPA5 = 0
        
        else:
            print("Nothing")
    def getGPA(self):
        dict1={
            "MARK":[self.m1,self.m2,self.m3,self.m4,self.m5],
            "GRADE":[self.g,self.g2,self.g3,self.g4,self.g5],
            "GPA":[self.GPA1,self.GPA2,self.GPA3,self.GPA4,self.GPA5]
        }
        d=p.DataFrame(dict1)
        d.index+=1
        print("Student B:")
        display(d)
    def cal_CGPA(self,CGPA= 0 ):
        Add  = self.GPA1 + self.GPA2 +self.GPA3 +self.GPA4 +self.GPA5
        self.CGPA = Add / 5
    def getCGPA(self):
        print(f"CGPA : {self.CGPA}")
st1=Student_A()



st1.get_marks(65,89,44)
st1.cal_GPA()
st1.getGPA()
st1.cal_CGPA()
st1.getCGPA()
st2=Student_B()
st2.get_marks(70,90,85,60,60)
st2.cal_GPA()
st2.getGPA()
st2.cal_CGPA()
st2.getCGPA()
