def binarySearch(numlist, find, low, high):
	if high >= low:
		mid = (high + low)//2
		if numlist[mid] == find:
			return mid
		elif numlist[mid] < find:
			return binarySearch(numlist, find, mid + 1, high)
		else:
			return binarySearch(numlist, find, low, mid-1)
	else:
		return -1

def getData():
	arr = list(map(int,input("Enter elements in ascending order(ex 1,2,3): ").strip().split(',')))
	a=int(input("Enter the number to be found:(KEY) "))
	return arr,a

def main():
	print("Binary Search:-")
	numlist, find = getData()
	result = binarySearch(numlist, find, 0, len(numlist)-1)
	if result != -1:
		print(f"Element found at {result+1}th position")
	else:
		print("Element not found")

if __name__ == "__main__":
	main()