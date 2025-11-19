def can_distribute(jobs, workers, limit, idx=0):
    if idx == len(jobs):
        return True
    
    visited = set()
    for i in range(len(workers)):
        if workers[i] + jobs[idx] <= limit and workers[i] not in visited:
            workers[i] += jobs[idx]
            if can_distribute(jobs, workers, limit, idx + 1):
                return True
            workers[i] -= jobs[idx]
            visited.add(workers[i])
        
        if workers[i] == 0:
            break
    return False

def binary_search_min_time(jobs, k):
    jobs.sort(reverse=True)
    low, high = max(jobs), sum(jobs)
    while low < high:
        mid = (low + high) // 2
        workers = [0] * k
        if can_distribute(jobs, workers, mid):
            high = mid
        else:
            low = mid + 1
    return low

raw_input = input("Enter jobs and number of workers : ")
job_str, k_str = raw_input.strip().split('/')
jobs = list(map(int, job_str.strip().split()))
k = int(k_str.strip())

result = binary_search_min_time(jobs, k)
print(f"Minimum time to complete jobs with {k} workers is {result}")
