d = {"EUR": 1, "USD": 2, "EUR": 3}
print(d)                                        # one EUR, the last value

by_segment_stage = {("retail", 1): 120, ("retail", 2): 15}     # a tuple as the key
print(by_segment_stage[("retail", 2)])

bad = {["retail", 1]: 120}                      # TypeError: a list is unhashable