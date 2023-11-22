def read_file(readfile):
    f=open(readfile,"r")
    print(f.read())
    f.close()
file=str(input())
read_file(file)