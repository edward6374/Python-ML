class Vector:

    def __init__(self, values):
        self.values = values
        line = 0
        column = 0
        for elem in values:
            line = len(elem)
            column += 1
        self.shape = (line, column)

    def dot(self, vector):
        result = 0.0
        for i, j in zip(self.values, vector.values):
            if len(i) == 1:
                result += i[0] * j[0]
            else:
                for k, l in zip(i, j):
                    result += k * l
        return result

    def T(self):
        count = 0
        result = []
        for elem in self.values:
            if len(elem) == 1:
                if len(result) == 0:
                    result.append(elem)
                else:
                    result[0].append(elem[0])
            else:
                for i in elem:
                    result.append([i])
        self.values = result
        return result

    def __add__(self, vector):
        result = []
        for i,l in zip(self.values, vector.values):
            if len(i) == 1 and len(j) != 1:
				raise TypeError("Vectors are not both of the same type")
            if len(i) == 1:
				print("Here")
				if len(result) == 0:
					result.append(i + j)
				else:
					result[0].append(i + j)
			else:
				for j,k in zip(i, l):
					result.append([j + k])
		print(result)


f = Vector([[0.0], [1.0], [2.0], [3.0]])
v = Vector([[2.0], [1.5], [2.25], [4.0]])
print(f.dot(v))
print(f.T())
print(v.T())
print(f.dot(v))
print(f.values)
print(v.values)
v2 = v + f
print(v2)
