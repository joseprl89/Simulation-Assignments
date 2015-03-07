
class Random:
    
    a = 17
    c = 19
    
    def __init__(self, seed, m=2**32):
        self.seed = seed
        self.m = m
        
    def nextInt(self):
        self.seed = ( Random.a * self.seed + Random.c ) % self.m
        return self.seed