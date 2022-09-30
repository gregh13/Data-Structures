# python3

from collections import namedtuple, deque

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []
        self.deque = deque([])

    def process(self, request):
        # Check for any processed packets, remove from deque
        while self.deque[0] <= request.arrived_at:
            self.deque.popleft()

        # Check if buffer is full; if yes, packet gets dropped
        if len(self.deque) == self.size:
            return Response(True, -1)

        # Check if buffer is empty; if yes, process packet immediately, add to deque
        if len(self.deque) == 0:
            finishing_time = request.arrived_at + request.time_to_process
            self.finish_time.append(finishing_time)
            self.deque.append(finishing_time)
            return Response(False, finishing_time)

        # Add new packet to end of deque
        end_of_deque = self.deque[-1]
        new_deque_end = end_of_deque + request.time_to_process
        self.deque.append(new_deque_end)





        return   # Response(False, -1)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
