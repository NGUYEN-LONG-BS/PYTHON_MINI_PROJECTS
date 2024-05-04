path='E:\QLSV.txt'

def save (line):
    try:
        f=open(path, 'a', encoding='utf8')
        f.writelines (line)
        f.writelines ('\n')
        f.close()
    except:
        pass

def read():
    SV=[]
    try:
        f = open(path, 'r', encoding='utf8')
        for i in f:
            data=i.strip()
            arr=data.split('-')
            sv.append(arr)
        f.close()
    except:
        pass
    return SV