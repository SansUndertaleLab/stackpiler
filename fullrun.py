def runpy(filename):
    file=open(filename,"r")
    read=file.read()
    file.close()
    exec(read)
runpy("build.py")
runpy("run.py")