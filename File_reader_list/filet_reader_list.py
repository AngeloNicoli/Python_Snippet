import os

# Load matrix from txt file
def render_image(image_name):
    
    render_matrix = []

    with open("palette\\" + image_name + ".txt", "r") as file:
        i = 0
        for line in file:
            line = line.strip()
            render_matrix.append("#" + line)
            print(render_matrix[i])
            i +=1

    return render_matrix
   

print(render_image("win_palette"))