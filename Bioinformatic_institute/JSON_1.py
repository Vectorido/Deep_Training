import json

student_1 = {
    'first_name': 'Greg',
    'last_name': 'Dean',
    'scores': [70, 80, 90],
    'description': 'Good job, Greg',
    'certificate': True,
}

student_2 = {
    'first_name': 'Sean',
    'last_name': 'Gone',
    'scores': [80, 80.2, 80],
    'description': 'Well Done, Sean Gone',
    'certificate': True,

}

data = [student_1, student_2]

data_json = json.dumps(data, indent=4, sort_keys=True)
data_again = json.loads(data_json)
print(sum(data_again[0]["scores"]))

with open("students.json", "r") as f:
    data_again = json.load(f)
    print(sum(data_again[1]["scores"]))

# with open("students.json", "w") as f:
#      json.dump(data, f, indent=4, sort_keys=True)