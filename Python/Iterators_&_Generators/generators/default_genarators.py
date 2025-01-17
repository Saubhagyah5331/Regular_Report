# generator function is the special function that returs the iterator object. Instead of return to send the single value, genrator use yield to produce the series over a time.

def gen(a):
    for i in range(1, a):
        yield i
    
for i in gen(5):
    print(i)


#genrators help in the creation of the iterators byy simlyfying the process and using the yield fucntion and yield method.
