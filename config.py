
class Validate:
	def __init__(self):
		pass

	def check(self, msg):
		self.message = msg
		count = 0
		flag = True
		inappropriate_words = ['hai', 'hello']
		words = self.message.split()
		temp = [self.message]
		for word in words:
			for inappropriate_word in inappropriate_words:
				if(word == inappropriate_word):
					if(flag):
						temp.append(temp[count].replace(word,"xxx"))
						count += 1
					else:
						return(False)
		return(temp[len(temp)-1])