import js2py
file=open("js/build/build-stack.js")
js2py.eval_js(file.read())
file.close()