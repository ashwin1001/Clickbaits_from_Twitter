import json
if __name__ == "__main__":
    f1=open('data.jsonl','w')
    f=open('instances.jsonl','r')
    f2=open('truth.jsonl','r')
    i=1
    while i<=2459:
        str1=f.readline()
        str2=f2.readline()

        s1=json.loads(str1)
        s2=json.loads(str2)
        data={'id':s1['id'],'postText':s1['postText'],'truthClass':s2['truthClass']}
        newstr=json.dumps(data)
        f1.write(newstr)
        f1.write("\n")
        #f1.write("\n")

        i+=1
    print s2['truthClass']
