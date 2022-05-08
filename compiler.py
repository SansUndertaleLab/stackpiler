file=open("test.stack","r")
read=file.read()
buildfile=open("test.stacked","w")
if read:
    buildfile.write("\n")
buildfile.write("{")
if read:
    buildfile.write("\n")
    file.close()
    letters="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    numbers="0123456789"
    index=0
    prevtype=""
    name=""
    special="=;+-*/"
    validtokens={"=":"set",";":"endline","+":"add","-":"sub","*":"mul","/":"div"}
    token=[]
    ttype=[]
    while True:
        if read[index] in letters: 
            if prevtype!="name":
                if prevtype=="special":
                    prevtype=validtokens[name]
                token.append(name)
                ttype.append(prevtype)
                name=""
            prevtype="name"
            name+=read[index]
        elif read[index] in numbers:
            if prevtype=="name":
                name+=read[index]
                index+=1
                if index==len(read):
                    if prevtype=="special":
                        prevtype=validtokens[name]
                    token.append(name)
                    ttype.append(prevtype)
                    break
                continue
            if prevtype!="int":
                if prevtype=="special":
                    prevtype=validtokens[name]
                token.append(name)
                ttype.append(prevtype)
                name=""
            prevtype="int"
            name+=read[index]
        elif read[index] in special:
            if prevtype!="special":
                token.append(name)
                ttype.append(prevtype)
                name=""
            prevtype="special"
            name+=read[index]
        index+=1
        if index==len(read):
            if prevtype=="special":
                prevtype=validtokens[name]
            token.append(name)
            ttype.append(prevtype)
            break
    prevline=-1
    line=0
    placed=False
    # +str(value)
    value=0
    for i in zip(ttype[1:],token[1:]):
        if i[1]==";":
            prevline=line
            line+=1
            placed=False
            buildfile.write("\t},\n")
            value=0
        else:
            if not placed:
                placed=True
                buildfile.write("\t"+str(line)+":{\n")
            if i[0]=="int":
                buildfile.write("\t\t"+i[0]+"_"+str(value+1)+": "+i[1]+",\n")
            else:
                buildfile.write("\t\t"+i[0]+"_"+str(value+1)+": \""+i[1]+"\",\n")
            value+=1
buildfile.write("}")
buildfile.close()