import timeit
import time
import random

def insertion_sort(lst):
	for i in range(1, len(lst)):
		key = lst[i]
		j = i-1
		while j >=0 and key < lst[j] :
				lst[j+1] = lst[j]
				j -= 1
		lst[j+1] = key 
	return lst

def merge_sort(arr):
	if len(arr) <= 1:
		return arr

	mid = len(arr) // 2
	left_half = arr[:mid]
	right_half = arr[mid:]

	return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
	merged = []
	left_index = 0
	right_index = 0

	while left_index < len(left) and right_index < len(right):
		if left[left_index] <= right[right_index]:
			merged.append(left[left_index])
			left_index += 1
		else:
			merged.append(right[right_index])
			right_index += 1

	while left_index < len(left):
		merged.append(left[left_index])
		left_index += 1

	while right_index < len(right):
		merged.append(right[right_index])
		right_index += 1

	return merged


def compare_sorting(n):
	timeit_way = False
	if timeit_way: # not recommended
		setup = f"population = list(range({n})); random.shuffle(population)"
		ins_time = timeit.timeit("insertion_sort(population)", setup=setup, globals=globals())
		merge_time = timeit.timeit("merge_sort(population)", setup=setup, globals=globals())
		tim_time = timeit.timeit("sorted(population)", setup=setup, globals=globals())
	else:
		population = list(range(n))
		random.shuffle(population)

		start = time.time()
		insertion_sort(population)
		ins_time = time.time() - start
		start = time.time()
		merge_sort(population)
		merge_time = time.time() - start
		start = time.time()
		sorted(population)
		tim_time = time.time() - start

	return ins_time, merge_time, tim_time

times = compare_sorting(10000)
times = [t * 1000 for t in times]
print(f"Insertion sort time: {times[0]:.6f} ms\nMerge sort time: {times[1]:.6f} ms\nTimsort time: {times[2]:.6f} ms")