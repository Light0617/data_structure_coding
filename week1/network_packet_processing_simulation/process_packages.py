# python3
import sys
class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time

class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time_ = []

    def Process(self, request):
        while self.finish_time_ and self.finish_time_[0] <= request.arrival_time:
            self.finish_time_.pop(0)
        if len(self.finish_time_) >= self.size:
            # full
            return Response(True, -1)
        else:
            cur_start_time = self.finish_time_[-1] if len(self.finish_time_) > 0 else request.arrival_time
            cur_finish_time = cur_start_time + request.process_time
            self.finish_time_.append(cur_finish_time)
            return Response(False, cur_start_time)

def ReadRequests(count):
    requests = []
    for i in range(count):
        #  for testing
        #  arrival_time, process_time = map(int, raw_input().strip().split())
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests

def ProcessRequests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.Process(request))
    return responses

def PrintResponses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)

if __name__ == "__main__":
    size, count = map(int, input().strip().split())
    # for testing
    # size, count = map(int, raw_input().strip().split())
    requests = ReadRequests(count)

    buffer = Buffer(size)
    responses = ProcessRequests(requests, buffer)

    PrintResponses(responses)
