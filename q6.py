marks=[78,45,91,33,67,49]
lst=["a","b","c","d","e",'f']
p=0
f=0
for i in range(6):
    k=marks[i]
    if k>45:
        print("PASSED","STUDENT NAME",lst[i],": ",marks[i])
        p+=1
    else:
        print("FAILED","STUDENT NAME",lst[i],": ",marks[i])
        f+=1
print("RATIO OF FAILED TO THE PASSED STUDENT",f/p)