import json
que = { }

res = 0

num=1

b = open("questions.txt",'r')
que = json.load(b)
b.close()

name = input("Enter your name: ")

for i in que.keys():
    
    print("Question",num , ": ", i)
    a = input("The answer is ")
    
    if a == que[i]:
      res = res + 1
     
    num = num + 1


result={name:res}
m = open("result.txt",'w')
result = json.dump(result,m)
m.close()