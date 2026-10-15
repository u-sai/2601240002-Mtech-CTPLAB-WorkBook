from queue import Queue
from threading import Thread, Lock
from multiprocessing import Process, Queue as MPQueue, Lock as MPLock


def thread_producer(queue, lock):
    for i in range(1, 6):
        queue.put(i)
        with lock:
            print("Thread Produced:", i)
    queue.put(None)


def thread_consumer(queue, lock):
    while True:
        item = queue.get()

        if item is None:
            break

        with lock:
            print("Thread Consumed:", item)


def process_producer(queue, lock):
    for i in range(1, 6):
        queue.put(i)
        with lock:
            print("Process Produced:", i, flush=True)
    queue.put(None)


def process_consumer(queue, lock):
    while True:
        item = queue.get()

        if item is None:
            break

        with lock:
            print("Process Consumed:", item, flush=True)


if __name__ == "__main__":

    print("Threading Result")

    thread_queue = Queue()
    thread_lock = Lock()

    producer_thread = Thread(
        target=thread_producer,
        args=(thread_queue, thread_lock)
    )

    consumer_thread = Thread(
        target=thread_consumer,
        args=(thread_queue, thread_lock)
    )

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()

    print("\nMultiprocessing Result")

    process_queue = MPQueue()
    process_lock = MPLock()

    producer_process = Process(
        target=process_producer,
        args=(process_queue, process_lock)
    )

    consumer_process = Process(
        target=process_consumer,
        args=(process_queue, process_lock)
    )

    producer_process.start()
    consumer_process.start()

    producer_process.join()
    consumer_process.join()

    print("Producer-Consumer completed")