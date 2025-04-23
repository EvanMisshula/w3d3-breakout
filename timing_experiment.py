import time
import random
import tracemalloc
from sort_utils import quick_sort, merge_sort

def run_experiment(sort_func, data, label):
    start = time.time()
    tracemalloc.start()
    sort_func(data[:])  # avoid modifying the original list
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end = time.time()
    print(f"{label}: time={end - start:.4f}s, peak memory={peak / 1024:.1f} KB")

if __name__ == "__main__":
    lst = random.sample(range(1000), 500)
    sorted_lst = sorted(lst)
    reverse_lst = sorted(lst, reverse=True)

    print("Quick Sort:")
    run_experiment(quick_sort, lst, "Random")
    run_experiment(quick_sort, sorted_lst, "Sorted")
    run_experiment(quick_sort, reverse_lst, "Reverse")

    print("\nMerge Sort:")
    run_experiment(merge_sort, lst, "Random")
    run_experiment(merge_sort, sorted_lst, "Sorted")
    run_experiment(merge_sort, reverse_lst, "Reverse")
