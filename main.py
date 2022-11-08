import random
from madlib1 import mad_lib1
from madlib2 import mad_lib2

def run():
    ran = random.randint(1, 2)
    print(ran)
    if ran == 1:
        print(mad_lib1())
    
    elif ran == 2:
        print(mad_lib2())
    

if __name__ == "__main__":
    run()

# adj = input("Write an adjetive: ")
# verb1 = input("Write a verb: ")
# verb2 = input("Write a verb: ")
# famous_person = input("Write a famous person name: ")


# madlib = f"Computer programming is so {adj}! It makes so excited all the time \
# because I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}"

# print(madlib)