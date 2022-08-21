import threading
import time

# Capture the program start time
start_time = time.perf_counter()

thread_pool  = list()
total_delay = 0
duration_from_decorator =0.0

#container with random int(a, b)
delay_index = [8, 15, 18, 12, 19, 7, 8, 16, 16]


#a worker method
def worker(delay: int) -> None:
    #Doing something
    time.sleep(delay)
    print(f"Worker_{delay} took {delay} secs to complete")

#Create worker threads and add them to the thread_pool
for i in range(len(delay_index)):
    _delay = delay_index[i]
    total_delay += _delay
    t = threading.Thread(target=worker,name=f'worker_{_delay}',args=(_delay,))

    thread_pool.append(t)



#start the worker threads
for _thread in thread_pool:
    _thread.start()
    print(f'----- Started {_thread.name}')

#Join the threads
for _thread in thread_pool:
    _thread.join()
    print(f'---------Completed  {_thread.name}')
    print(f'{_thread.name} took {_thread.thread_time()} secs')
    duration_from_decorator += _thread.thread_time()

#capture program execution time
end_time = time.perf_counter()
execution_time = end_time - start_time

#print the stats
print(f'Total execution time : {execution_time} secs')
print(f'Total number of threads: {len(thread_pool)}')
print(f'Average total time: {execution_time / len(thread_pool)}')
