import numpy as np
import scipy
from PIL import Image


image = Image.open("/Users/amitomer/Desktop/Projects/Graphics/eifel.jpeg")
image = image.convert('L')
image_matrix = np.array(image)

row  = image_matrix.shape[0]
col  = image_matrix.shape[1]


for i in range(row):
    
    for j in range(col):
        if j+1 >= col:
            if i+1 >= row:
                break
            current_error = 255 - image_matrix[i][j] if image_matrix[i][j] > 127 else image_matrix[i][j]
            op = 'sub' if image_matrix[i][j] > 127 else 'add'
            if op == 'sub':
                image_matrix[i][j] = 255
                current_value = image_matrix[i+1][j]
                image_matrix[i+1][j] = max(0,current_value - current_error)
            else:
                image_matrix[i][j] = 0
                current_value = image_matrix[i+1][j]
                image_matrix[i+1][j] = min(255,current_value + current_error)
        elif i+1 >= row:
            if j+1 >= row:
                break
            current_error = 255 - image_matrix[i][j] if image_matrix[i][j] > 127 else image_matrix[i][j]
            op = 'sub' if image_matrix[i][j] > 127 else 'add'
            if op == 'sub':
                image_matrix[i][j] = 255
                current_value = image_matrix[i][j+1]
                image_matrix[i][j+1] = max(0,current_value - current_error)
            else:
                image_matrix[i][j] = 0
                image_matrix[i][j+1] = min(255,image_matrix[i][j+1] + current_error)
        else:
            current_error = 255 - image_matrix[i][j] if image_matrix[i][j] > 127 else image_matrix[i][j]
            op = 'sub' if image_matrix[i][j] > 127 else 'add'
            if op == 'sub':
                image_matrix[i][j] = 255
                image_matrix[i][j+1] = max(0,image_matrix[i][j+1] - current_error/3)
                image_matrix[i+1][j] = max(0,image_matrix[i+1][j] - current_error/3)
                image_matrix[i+1][j+1] = max(0,image_matrix[i+1][j+1] - current_error/3)
            else:
                image_matrix[i][j] = 0
                current_value = image_matrix[i][j+1]
                current_value2 = image_matrix[i+1][j]
                current_value3 = image_matrix[i+1][j+1]
                image_matrix[i][j+1] = min(255,current_value + current_error/3)
                image_matrix[i+1][j] = min(255,current_value2 + current_error/3)
                image_matrix[i+1][j+1] = min(255,current_value3 + current_error/3)

print(image_matrix)
out_image = Image.fromarray(image_matrix)
out_image.save('eifel_dif.jpeg')