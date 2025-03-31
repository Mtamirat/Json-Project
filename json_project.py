import json

data = {

    'name': 'john doe',
    'age': 30,
    'city': 'New York,NY',
    'interests': ['golf', 'running', 'videogames'],
    'is_student': True 
    
    }

with open ('data.json','w') as json_file:
    json.dump(data, json_file, indent=4)

print("You have successfully written to data.json")
