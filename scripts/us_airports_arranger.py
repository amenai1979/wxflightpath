import json


us_with_state = {}
states = set()
fields_without_state = []

with open("../data/airports.json","r") as us_input:
    us_all_dict = json.load(us_input)
    for key in us_all_dict.keys():
        if us_all_dict[key]["country"]=="US":
            us_with_state[key]={y: us_all_dict[key][y] for y in ["lat","long","name","state"]}
            states.add(us_with_state[key]["state"])
            if us_with_state[key]["state"]=="":
                us_with_state[key]["state"]="other"
    replaced_set = {'other' if item == '' else item for item in states}

"""
for state in replaced_set:
    perstate_airfield_dict={}
    for key in us_with_state.keys():
        if us_with_state[key]["state"]==state:
            perstate_airfield_dict[key]=us_with_state[key]
    with open(f"../data/airports.US.{state}.json","w") as perstate_airfield_file:
        json.dump(perstate_airfield_dict,perstate_airfield_file,indent=4)
"""
print(sorted(replaced_set))
#print(fields_without_state)



