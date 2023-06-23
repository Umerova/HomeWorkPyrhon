def calculate(*args):
    avg = sum(args) / len(args)
    above_avg = [x for x in args if x > avg]
    return avg, above_avg
