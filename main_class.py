from unicodedata import name


class Student:
    student = ("name", "age", "tracks", "score")
    
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self):
        
        return self.name
    
    def change_age(self):
        
        return self.age
    
    def add_track(self):
        
        return self.tracks

    def get_score(self):
        return self.score
        
Bob = Student(name="Peter", age=26, tracks=["FE","BE"],score=20.90)


print(Bob.change_name())
print(Bob.change_age())
print(Bob.add_track())
print(Bob.get_score())



