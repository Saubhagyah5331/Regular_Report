# Create an iterator that returns the first n even numbers.


class even_num():
    def __init__(self, start, end):
        self.current = start if start % 2 == 0 else start + 1
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        print_ev_num = self.current
        self.current +=2
        return print_ev_num
        

even = even_num(1,4)

for i in even:
    print(i)