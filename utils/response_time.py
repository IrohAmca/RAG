from time import perf_counter

class ShowResponseTime:
    def __init__(self, msg: str = None):
        self.msg = msg
    
    def __enter__(self):
        self.start_time = perf_counter()
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        if self.msg:
            print(f"{self.msg} - ", end="")
        print(f"Response Time: {perf_counter()-self.start_time:.5f} seconds")
