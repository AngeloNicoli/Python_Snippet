#import os

# Load matrix from txt file
def render_image(image_name):
    
    render_matrix = []
    for el in range(20):
        render_matrix.append([None]*20)

    with open(image_name + ".txt", "r") as file:
        i = 0
        for line in file:
            line = line.strip()
            #print(file.read())
            # a=file.read()     (NON USARE. LEGGE TUTTO IL FILE IN UNA SOLA VOLTA)
            #print("Divido la linea")
            #print(type(a))
            #print(a)
            render_matrix[i] = line.split(",")
            #print("la linea da scrivere è " + str(render_matrix[i])+ "\n \n \n")
            #print(type(render_matrix[i]))
            #print(render_matrix)
            #print(type(render_matrix[0]))
            i+=1
            #print(i)
            #print("\n \n \n" + str(render_matrix[0]))
            #print("\n \n \n" + str(render_matrix[i]))
            #print(render_matrix)
     
    for el in range(len(render_matrix)):
        for ely in range(len(render_matrix[el])):
            render_matrix[el][ely]= int(render_matrix[el][ely])
            
    return render_matrix
   
