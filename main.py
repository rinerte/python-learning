# multiprocessing =

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count+=1

def main():
    start = time.perf_counter()

    # a = Process(target=counter, args=(1_000_000_000,))
    # a.start()
    # b = Process(target=counter, args=(1_000_000_000,))
    # b.start()
    # a = Process(target=counter, args=(5_00_000_000,))
    # a.start()
    # b = Process(target=counter, args=(5_00_000_000,))
    # b.start()
    a = Process(target=counter, args=(250_000_000,))
    a.start()
    b = Process(target=counter, args=(250_000_000,))
    b.start()
    c = Process(target=counter, args=(250_000_000,))
    c.start()
    d = Process(target=counter, args=(250_000_000,))
    d.start()

    a.join()
    b.join()
    c.join()
    d.join()

    print("finished in: ",time.perf_counter()-start)
    print(cpu_count())


if __name__ == '__main__':
    main()


