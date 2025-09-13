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
    

#def load_image(image_name):
#    Matrix_Rendered = render_image("demofile")
    
    
#Matrix_Rendered = render_image("demofile")
#print(Matrix_Rendered)

def terrain_generator():
    terrain_map = []
    
    terrain_row_01 = [2,2,2,2,2,2,2,2,2,2,6,6,4,4,4,4,4,6,2,2,2]
    terrain_row_02 = [2,2,2,2,2,2,2,2,2,2,6,6,4,4,4,4,4,4,6,2,2]
    terrain_row_03 = [2,2,2,2,2,2,2,2,2,2,6,6,4,4,4,4,4,6,2,2,2]
    terrain_row_04 = [2,2,10,10,10,2,2,2,2,2,2,6,4,4,4,4,6,2,2,2,2]
    terrain_row_05 = [2,2,10,10,10,2,2,2,2,2,2,6,4,4,4,4,4,6,2,2,2]

    terrain_row_06 = [2,2,2,3,2,2,2,2,2,2,6,6,6,6,6,6,6,2,2,2,2]
    terrain_row_07 = [2,2,2,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
    terrain_row_08 = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
    terrain_row_09 = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,8,2,8,2,8,2]
    terrain_row_10 = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,8,8,8,8,8,2]

    terrain_row_11 = [2,2,2,2,2,10,10,10,2,2,2,2,2,2,2,2,8,8,8,2,2]
    terrain_row_12 = [2,2,2,2,2,10,10,10,2,2,2,2,2,2,2,2,8,3,8,2,2]
    terrain_row_13 = [2,2,2,2,2,10,10,10,2,2,2,2,2,2,2,2,8,8,8,2,2]
    terrain_row_14 = [2,2,2,2,2,2,3,2,2,2,2,2,2,2,2,2,8,8,8,2,2]
    terrain_row_15 = [2,2,2,2,2,2,3,2,2,2,2,2,2,2,2,8,8,8,8,8,2]

    terrain_row_16 = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
    terrain_row_17 = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
    terrain_row_18 = [2,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
    terrain_row_19 = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
    terrain_row_20 = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
    
    terrain_map.append(terrain_row_01)
    terrain_map.append(terrain_row_02)
    terrain_map.append(terrain_row_03)
    terrain_map.append(terrain_row_04)
    terrain_map.append(terrain_row_05)

    terrain_map.append(terrain_row_06)
    terrain_map.append(terrain_row_07)
    terrain_map.append(terrain_row_08)
    terrain_map.append(terrain_row_09)
    terrain_map.append(terrain_row_10)

    terrain_map.append(terrain_row_11)
    terrain_map.append(terrain_row_12)
    terrain_map.append(terrain_row_13)
    terrain_map.append(terrain_row_14)
    terrain_map.append(terrain_row_15)

    terrain_map.append(terrain_row_16)
    terrain_map.append(terrain_row_17)
    terrain_map.append(terrain_row_18)
    terrain_map.append(terrain_row_19)
    terrain_map.append(terrain_row_20)
    
    #terrain_map = render_image(2,"demofile")
    return terrain_map
    
    
def sword_generator():
    sword_icon = []
    
    sword_icon_01 = [3,2,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
    
    sword_icon_02 = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
    sword_icon_03 = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
    sword_icon_04 = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
    sword_icon_05 = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]

    sword_icon_06 = [2,2,2,2,2,2,2,2,7,7,7,2,2,2,2,2,2,2,2,2,2]
    sword_icon_07 = [2,2,2,2,2,2,2,2,7,7,7,2,2,2,2,2,2,2,2,2,2]
    sword_icon_08 = [2,2,2,2,2,2,2,2,7,7,7,2,2,2,2,2,2,2,2,2,2]
    sword_icon_09 = [2,2,2,2,2,2,2,2,7,7,7,2,2,2,2,2,2,2,2,2,2]
    sword_icon_10 = [2,2,2,2,2,2,2,2,7,7,7,2,2,2,2,2,2,2,2,2,2]

    sword_icon_11 = [2,2,2,2,2,2,2,2,7,7,7,2,2,2,2,2,2,2,2,2,2]
    sword_icon_12 = [2,2,2,2,2,2,2,2,7,7,7,2,2,2,2,2,2,2,2,2,2]
    sword_icon_13 = [2,2,2,2,2,2,8,8,8,8,8,8,8,2,2,2,2,2,2,2,2]
    sword_icon_14 = [2,2,2,2,2,2,2,2,8,8,8,2,2,2,2,2,2,2,2,2,2]
    sword_icon_15 = [2,2,2,2,2,2,2,2,8,8,8,2,2,2,2,2,2,2,2,2,2]

    sword_icon_16 = [2,2,2,2,2,2,2,2,8,8,8,2,2,2,2,2,2,2,2,2,2]
    sword_icon_17 = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
    sword_icon_18 = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
    sword_icon_19 = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
    sword_icon_20 = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
    
    sword_icon.append(sword_icon_01)
    sword_icon.append(sword_icon_02)
    sword_icon.append(sword_icon_03)
    sword_icon.append(sword_icon_04)
    sword_icon.append(sword_icon_05)

    sword_icon.append(sword_icon_06)
    sword_icon.append(sword_icon_07)
    sword_icon.append(sword_icon_08)
    sword_icon.append(sword_icon_09)
    sword_icon.append(sword_icon_10)

    sword_icon.append(sword_icon_11)
    sword_icon.append(sword_icon_12)
    sword_icon.append(sword_icon_13)
    sword_icon.append(sword_icon_14)
    sword_icon.append(sword_icon_15)

    sword_icon.append(sword_icon_16)
    sword_icon.append(sword_icon_17)
    sword_icon.append(sword_icon_18)
    sword_icon.append(sword_icon_19)
    sword_icon.append(sword_icon_20)
    
    
    return sword_icon
   
