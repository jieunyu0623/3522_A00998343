"""
Producer Consumer class for making API calls and storing them into a buffer.
"""
import logging
import threading
import time
from threading import Thread

from Labs.Lab10 import city_processor as cp


class CityOverheadTimeQueue:
    """
    CityOverheadTimeQueue class used to create a buffer that holds the data achieved from the API open source.
    """

    def __init__(self):
        """
        constructs an empty queue and a queue lock for safe accessing to threads.
        """
        self.data_queue = []
        self.access_queue_lock = threading.Lock()

    def put(self, overhead_time: cp.CityOverheadTimes) -> None:
        """
        adds a city proxy with latitude and longitude to the data queue list.
        :param overhead_time: CityOverheadTimes
        :return: None
        """
        with self.access_queue_lock:
            logging.info("Thread starting...")
            logging.info("Acquired lock and added %s to the queue.", overhead_time.city.city_name)
            self.data_queue.append(overhead_time)
            logging.info("Releasing lock...")

    def get(self) -> cp.CityOverheadTimes:
        """
        removes an item from the data queue list. This is FIFO system
        so it removes the first item in the list.
        :return: item
        """
        with self.access_queue_lock:
            item = self.data_queue[0]
            logging.info(print(item))
            logging.info("removing the oldest city from the queue...")
            del self.data_queue[0]
            return item

    def __len__(self) -> int:
        """
        gets the length of the data queue list.
        :return: length of data queue list
        """
        return len(self.data_queue)


class ProducerThread(Thread):
    """
    ProducerThread class used to produce the city data and pass
    to adding/deleting methods in CityOverheadTimeQueue class.
    """

    def __init__(self, cities, queue: CityOverheadTimeQueue):
        """
        constructs a thread with a list of cities and queue.
        :param cities:
        :param queue:
        """
        super().__init__()
        self.cities = cities
        self.queue = queue

    def run(self) -> None:
        """
        passes each city data to ISS Data Request and adds to the data queue list in
        the CityOverheadTimeQueue class.
        :return:
        """
        count = 0
        for city in self.cities:
            city_overhead = cp.ISSDataRequest.get_overhead_pass(city)
            self.queue.put(city_overhead)
            count += 1
            if count % 5 == 0:
                time.sleep(1)

    def delete(self) -> None:
        """
        deletes the oldest data from the queue list.
        :return:
        """
        self.queue.get()


class ConsumerThread(Thread):
    """
    ConsumerThread class used to print the data out.
    """

    def __init__(self, queue: CityOverheadTimeQueue):
        """
        constructs the queue proxy and sets the data incoming status.
        :param queue: CityOverheadTimeQueue
        """
        super().__init__()
        self.queue = queue
        self.data_incoming = True

    def run(self) -> None:
        """
        if the queue list is not empty, remove the last item in the queue and
        if the queue list is empty, await for 0.75 seconds.
        :return: None
        """
        while self.data_incoming is True or len(self.queue) > 0:
            if len(self.queue) > 0:
                print(self.queue.data_queue.pop(0))
                time.sleep(0.5)
            else:
                time.sleep(0.75)


def main():
    """
    thread testing with locks. tests if one thread modifies/accesses the queue at a time.
    :return: None
    """
    cotq = CityOverheadTimeQueue()
    db = cp.CityDatabase("city_locations.xlsx")
    logging.info("Main: Before creating threads")
    start_time = time.time()
    num_of_cities = len(db.city_db)
    p1_thread = ProducerThread(db.city_db[0:3:], cotq)
    p2_thread = ProducerThread(db.city_db[3:5:], cotq)
    p3_thread = ProducerThread(db.city_db[5:2:], cotq)
    c_thread = ConsumerThread(cotq)
    p1_thread.start()
    p2_thread.start()
    p3_thread.start()
    c_thread.start()
    p1_thread.join()
    p2_thread.join()
    p3_thread.join()
    c_thread.data_incoming = False
    c_thread.join()
    duration = time.time() - start_time
    print(f"Downloaded data on {num_of_cities} cities in {duration} seconds.")


if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    main()
