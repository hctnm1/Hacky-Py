class weight:
     def __init__(self,gram,kg,tonne):
         self.gram=gram
         self.kg=kg
         self.tonne=tonne
     def __sub__(self,obj):
         if obj.gram> self.gram:
             self.gram +=1000
             self.kg -=1
         if obj.kg>self.kg:
             self.kg +=1000
             self.tonne -=1
         gram=self.gram-obj.gram
         kg=self.kg-obj.kg
         tonne=self.tonne-obj.tonne
         print("[t]tonnes,[gram]gram,[kg]kilograms")
 ob1=weight(9,500,300)
 ob2=weight(6,600,400)
 print(ob1-ob2)
