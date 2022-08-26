import math
def sum_com(n1,n2):
    return (n1[0]+n2[0]),(n1[1]+n2[1])

def pro_com(n1,n2):
    real=(n1[0]*n2[0])-(n1[1]*n2[1])
    ima=(n1[0]*n2[1])+(n1[1]*n2[0])
    return (real,ima)

def rest_com(n1,n2):
    return (n1[0]-n2[0]),(n1[1]-n2[1])

def div_com(n1,n2):
     deno=pro_com(n2,(n2[0],(n2[1]*-1)))
     num=pro_com(n1,(n2[0],(n2[1]*-1)))
     return (num[0]/deno[0]),(num[1]/deno[0])

def mod_com(n1):
    return (((n1[0]*2)+(n1[1]*2))*.5)

def conjugado_com(n1):
    return n1[0],(n1[1]*-1)

def conversion(r,a):
    number= math.radians(a)
    x = r * math.cos(number)
    y = r * math.sin(number)
    return (x,y)

def fase_com(n1):
    number=(n1[1]/n1[0])
    return (math.degrees(math.atan(number)))

def main():
    a = (3,4)
    b = (4,5)
    print(sum_com(a,b))


main()