from nmigen import *
from nmigen.back.pysim import *
    
class Counter:
    def __init__(self):
        self.count = Signal(4)
    
    def elaborate(self, platform):
        m = Module()
    
        m.d.sync += self.count.eq(self.count + 1)
    
        return m
    
if __name__ == "__main__":
    counter = Counter()
    fragment = Fragment.get(counter, platform=None)
    
    with open("counter.vcd", "w") as vcd_file:
        with Simulator(fragment, vcd_file=vcd_file) as sim:
    
            def counter_test():
                for i in range(20):
                    print("count =", (yield counter.count))
                    yield Tick()
    
            sim.add_clock(1e-6)
            sim.add_process(counter_test)
            sim.run()
