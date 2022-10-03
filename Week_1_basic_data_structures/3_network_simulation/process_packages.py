# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []
        self.queue = []

    def process(self, request):
        # Check for any already processed packets, remove from queue
        if self.queue:
            next_up = self.queue[0]
            while next_up <= request.arrived_at:
                self.queue.pop(0)
                if self.queue:
                    next_up = self.queue[0]
                else:
                    next_up = float("inf")

        # Check if buffer is empty after removing any previous; if yes, process packet immediately, add to queue
        if len(self.queue) == 0:
            finishing_time = request.arrived_at + request.time_to_process
            self.finish_time.append(finishing_time)
            self.queue.append(finishing_time)
            return Response(False, request.arrived_at)

        # Check if buffer is full; if yes, packet gets dropped
        if len(self.queue) == self.size:
            return Response(True, -1)

        # Add new packet to end of queue
        end_of_queue = self.queue[-1]
        new_queue_end = end_of_queue + request.time_to_process
        self.queue.append(new_queue_end)
        self.finish_time.append(new_queue_end)

        return Response(False, end_of_queue)


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
