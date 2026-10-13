class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])
    
    def __add__(self, other):
        result = []

        for i in range(self.rows):
            rows = []
            
            for j in range(self.cols):
                rows.append(self.data[i][j] + other.data[i][j])
                
            result.append(rows)
        return Matrix(result)
      
    
    def __sub__(self, other):
        result = []
        
        for i in range(self.rows):
            rows = []
            
            for j in range(self.cols):
                rows.append(self.data[i][j] - other.data[i][j])
            
            result.append(rows)
        return Matrix(result)

    def __mul__(self, scalar):
        result = []
    
        for i in range(self.rows):
            rows = []
        
            for j in range(self.cols):
                rows.append(self.data[i][j] * scalar)
            
            result.append(rows)
    
        return Matrix(result) 

    def __matmul__(self, other):
        result = []
        
        for i in range(self.rows):
            rows = []
            
            for j in range(other.cols):
                total = 0
                
                for k in range(self.cols):
                    total += self.data[i][k] * other.data[k][j]
                
                rows.append(total)
            result.append(rows)
        return Matrix(result)         
    

A = Matrix([
    [1, 2],
    [3, 4]
])

B = Matrix([
    [5, 6],
    [7, 8]
])

# print(A.rows)
# print(A.cols)
# print((A + B) .data)
# print((A - B) .data)
# print(C.data)

# print((A @ B).data)