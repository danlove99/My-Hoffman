

olds = "abccabbxxxdhfkdhfkkksjskdjkkbb"
s = "abccabbxxxdhfkdhfkkksjskdjkkbb"

class Hoffman:

	def __init__(self, s):
		self.s = s
		self.hashmap = {}
		self.compressed = False
		self.binLength = 0
		self.decompressedStr = ''


	def compress(self):
		
		for i in self.s:
			if i not in self.hashmap:
				self.hashmap[i] = 1
			else:
				self.hashmap[i] += 1

		self.hashmap = {k: v for k, v in sorted(self.hashmap.items(), reverse=True, key=lambda item: item[1])}
		print('hashmap: ' + str(self.hashmap))
		binaryhash = {}
		count = 1
		for k in self.hashmap:
			self.hashmap[k] = count
			count += 1
		for k in self.hashmap:
			self.hashmap[k] = "{0:b}".format(self.hashmap[k])
		lastLength = len(list(self.hashmap.values())[-1])
		self.binLength = lastLength

		for k in self.hashmap:
			self.hashmap[k] = self.hashmap[k].zfill(lastLength)

		for k in self.hashmap.keys():
			self.s = self.s.replace(k, self.hashmap[k])

		self.compressed = True
		return str(self.s)

	def decompress(self):
		if self.compressed:
			parts = [self.s[i:i+self.binLength] for i in range(0, len(self.s), self.binLength)]
			for item in parts:
				for key, value in self.hashmap.items():
					if value == item:
						self.decompressedStr += key
			return self.decompressedStr



print('String before compression: ' + olds)
print('size of string before compression: ' + str(len(olds) * 8))
hoff = Hoffman(s)
s = hoff.compress()
print('String after compression: ' + s)
print('size after compression: ' + str(len(s)))
print('decompressed string: ' + hoff.decompress())