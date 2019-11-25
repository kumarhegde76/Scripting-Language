from collections import Counter
def word_count(fname):
	with open(fname) as f:
		return Counter(f.read().split())
print("Number of Words in the File :",word_count("Test.txt"))
