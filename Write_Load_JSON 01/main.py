import load_json
import write_json
import display
import insert_data


Name_list = [0]

function_dict = {
    'Load': load_json.load_data,
    'Save': write_json.save_data,
    'Display': load_json.Display_Data,
    'Insert Data': write_json.Insert_Data
}
Continue_Calculation = 0

while Continue_Calculation == 0:
    # Check if the selected function exists in the dictionary
    selected_function = input("Enter the name of the function you want to execute: ")
    if selected_function in function_dict:
        # Get the function from the dictionary and execute it
        result = function_dict[selected_function]()
        Name_list = result
        print("Function Executed:", selected_function)
    else:
        print("Function not found.")

