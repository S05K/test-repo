'''Recursion Code'''
i=1
def hello():
    global i
    if i==6:
        return
    print("hello-world")
    i=i+1
    hello()

hello()