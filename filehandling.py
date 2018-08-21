f=open("demofile.txt","w+")
f.write("Line 1: This is a demo file.\nLine 2: This is a demo file.\nLine 3: this is a Demo file.")
f.close()


f=open("demofile.txt","r+")
str=f.read()

print(str,"\n\n\n\n")
f.close()



f=open("demofile.txt","w")
f.seek(0,2)

f.write("\nNew Line added.")

f.close()


f=open("demofile.txt","r")
print(f.read())
f.close()