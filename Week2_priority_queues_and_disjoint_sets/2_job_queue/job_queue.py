# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])
def left_child(i):
    return 2*i + 1

def right_child(i):
    return 2*i + 2

def priority_job_queue(n_workers, jobs):
    def change_priority(job):
        # Since min heap, next worker will always be the root
        next_worker = worker_heap[0]

        # Add worker index and start time to results
        result.append(AssignedJob(next_worker[0], next_worker[1]))

        # Add job to worker thread
        next_worker[1] += job

        return

    def sift_down(index, size):
        l_index = left_child(index)
        r_index = right_child(index)
        min_rank, min_time = worker_heap[index][0], worker_heap[index][1]
        l_child_rank, l_child_time = worker_heap[l_index][0], worker_heap[l_index][1]
        r_child_rank, r_child_time = worker_heap[r_index][0], worker_heap[r_index][1]

        if l_index <= size:
            pass

        if r_index <= size:
            pass

        pass

    result = []
    size = n_workers - 1
    worker_heap = [[x, 0] for x in range(n_workers)]

    for job in jobs:
        change_priority(job)
        sift_down(size)


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
