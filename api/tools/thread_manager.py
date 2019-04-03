"""
File contain a service to manage Threads with a pool
"""

from threading import Thread


class ThreadManager:

    pool = []

    def add_and_run(self, function, *args, **kwarg):
        """
        Add action on the pool and run it
        :param function: The function to exec
        :param args: args for the function
        :param kwarg: kwargs for the function
        """
        print('started!')
        self.free_dead()
        thread = Thread(target=function, args=args, kwargs=kwarg)
        thread.start()
        self.pool.append(thread)

    def free_dead(self):
        """
        Clean the pool the ended threads
        """
        for th in self.pool:
            if th.isAlive() is False:
                self.pool.remove(th)

    def join_all(self):
        """
        Join all thread from the pool
        """
        for th in self.pool:
            th.join()
        self.free_dead()
