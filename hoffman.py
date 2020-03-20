
olds = "abccabbdhfkdhfkkksjskdjkkbb"
s = "abccabbdhfkdhfkkksjskdjkkbb"

def compress(s):
	hashmap = {}
	for i in s:
		if i not in hashmap:
			hashmap[i] = 1
		else:
			hashmap[i] += 1

	hashmap = {k: v for k, v in sorted(hashmap.items(), reverse=True, key=lambda item: item[1])}
	print(hashmap)
	binaryhash = {}
	count = 1
	for k in hashmap:
		hashmap[k] = count
		count += 1
	for k in hashmap:
		hashmap[k] = "{0:b}".format(hashmap[k])
	lastLength = len(list(hashmap.values())[-1])

	for k in hashmap:
		hashmap[k] = hashmap[k].zfill(lastLength)

	for k in hashmap.keys():
		s = s.replace(k, hashmap[k])
	return s


print('size of string before compression: ' + str(len(olds) * 8))
s = compress(s)
print('size after compression: ' + str(len(s)))