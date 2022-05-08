def runpy(filename):
    file=open(filename,"r")
    read=file.read()
    file.close()
    exec(read)
    
print("Compiling...")
runpy("compiler.py")
print("Injecting...")
runpy("injector.py")
print("Done")