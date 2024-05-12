import load_json
import write_json


function_dict = {
    'Load': load_json.load_data,
    'Save': write_json.save_data
}

Continue_Calculation = 0

while Continue_Calculation == 0:
    # Check if the selected function exists in the dictionary
    selected_function = input("Enter the name of the function you want to execute: ")
    if selected_function in function_dict:
        # Get the function from the dictionary and execute it
        result = function_dict[selected_function]()
        
        print("Result of", selected_function + ":", result)
    else:
        print("Function not found.")

