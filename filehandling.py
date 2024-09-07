def read():
    f=open("filehandling.txt","r")
    while True:
        s=f.readline()
        if s=='':
            break
        else:
            print(s)
read()