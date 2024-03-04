import time,os,random,sys

i = "*" *50
a = random.randint(1000,9999)
b = "ok"
c = "error"
d = "nomber only"
d = f"""┌─[inter this code]
└──╼ $  {a} """
for char in d:
    time.sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()
print ("\n"+i)
raf = int(input("\n inter: "))
print ()
print (i)
if a == raf: 
  print (b)
else: 
  print (c)