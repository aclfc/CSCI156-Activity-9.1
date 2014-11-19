__author__ = 'Aidan'
def user(str):
    f = open('user.txt','w+', encoding = 'utf-8')
    c=0
    while str != 'q' and str != 'Q':
        f.write(str+'\n')
        str=input("Next input: ")
        c+=1
    print("Goodbye! Here's your string (",c,"inputs ):")
    f.seek(0)
    for i in range(c):
        print(f.readline().strip())
    f.close()
x=input("First input: ")
user(x)

