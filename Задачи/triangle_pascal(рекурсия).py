def triangle(val):
    triangle = []
    for i in range(val+1):
        triangle.append([1] + [0]*val)
    for i in range(1, val+1):
        for j in range(1, i+1):
            triangle[i][j] = triangle[i-1][j] + triangle[i-1][j-1]
    return triangle[val]
        
    
print(triangle(4))