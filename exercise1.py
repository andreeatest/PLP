from operator import itemgetter
with open('passwd.txt') as f:
    d=[]
    for i in f:
        b={}
        a = i.split(':*:')
        b['name']=a[0]
        b['id']=a[1].split(':')[0]

        d.append(b)

    newl= sorted(d, key=itemgetter('name'))

    print(d)
    print(newl)

()