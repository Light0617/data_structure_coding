# python3
from heapq import *
class JobQueue:
    def read_data(self):
        # self.num_workers, m = map(int, raw_input().split())
        # self.jobs = list(map(int, raw_input().split()))

        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i]) 

    def assign_jobs(self):
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)

        pq = []
        for i, job in enumerate(self.jobs[:self.num_workers]):
          self.start_times[i] = 0
          self.assigned_workers[i] = i
          finish_time, worker = self.start_times[i] + job, self.assigned_workers[i]
          heappush(pq, [finish_time, worker])

        for i in range(self.num_workers, len(self.jobs)):
          job = self.jobs[i]

          finish_job_time, finish_job_worker = heappop(pq)
          self.start_times[i] = finish_job_time
          self.assigned_workers[i] = finish_job_worker
          finish_time, worker = self.start_times[i] + job, self.assigned_workers[i]
          heappush(pq, [finish_time, worker])

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

