import random

def intersect(list1, list2):
    return {el for el in list1} & {el for el in list2}

def generate():
    generated = list()
    for i in range(random.randint(1,1000)):
        generated.append(random.randint(-500,500))
    return generated

def main():
    a = generate()
    b = generate()
    section = intersect(a,b)
    #format print to list
    print( [int for int in section] )
    
main()