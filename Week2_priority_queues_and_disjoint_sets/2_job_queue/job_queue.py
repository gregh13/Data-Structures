# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def left_child(i):
    # Calculates left child index value
    return 2*i + 1


def right_child(i):
    # Calculates right child index value
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

    def sift_down(index):

        # Set min_index to current parent index
        min_index = index

        # Initialize parent worker info
        min_rank, min_time = worker_heap[index][0], worker_heap[index][1]

        # Calculate child indices
        l_index = left_child(index)
        r_index = right_child(index)

        # Check if left child exists
        if l_index <= size:
            # Initialize child worker info
            l_child_rank, l_child_time = worker_heap[l_index][0], worker_heap[l_index][1]

            # Check if child worker is free before parent
            if l_child_time < min_time:
                # Update min values to left child values
                min_index, min_time, min_rank = l_index, l_child_time, l_child_rank

            # If both free at same time, check rank to determine worker position
            elif l_child_time == min_time:
                # Check rank
                if l_child_rank < min_rank:
                    # Update min values to left child values
                    min_index, min_time, min_rank = l_index, l_child_time, l_child_rank

        # Check if right child exists
        if r_index <= size:
            # Initialize child worker info
            r_child_rank, r_child_time = worker_heap[r_index][0], worker_heap[r_index][1]

            # Perform same checks for right child
            if r_child_time < min_time:
                # Update min values to right child values
                min_index, min_time, min_rank = r_index, r_child_time, r_child_rank

            elif r_child_time == min_time:
                # Check rank
                if r_child_rank < min_rank:
                    # Update min values to right child values
                    min_index, min_time, min_rank = r_index, r_child_time, r_child_rank

        if min_index != index:
            # Swap parent with the min child
            worker_heap[index], worker_heap[min_index] = worker_heap[min_index], worker_heap[index]

            # Sift down again
            sift_down(min_index)

        return

    # Initialize result list and size variable
    result = []
    size = n_workers - 1

    # Initialize 2d array with the worker rank (x) and their starting time (0)
    worker_heap = [[x, 0] for x in range(n_workers)]

    # For each job, grabs next worker (top of worker_heap), changes its priority, then sifts it down.
    for job in jobs:
        change_priority(job)
        sift_down(0)

    return result


def assign_jobs(n_workers, jobs):
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

    # assigned_jobs = assign_jobs(n_workers, jobs)
    # for job in assigned_jobs:
    #     print(job.worker, job.started_at)
    #
    # print("---------------")

    priority_jobs = priority_job_queue(n_workers, jobs)
    for job in priority_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
