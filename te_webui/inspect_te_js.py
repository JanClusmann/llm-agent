import ujson

def read_json(file_path: str):
    "Read a JSON file."
    with open(file_path, "r") as f:
        data = ujson.load(f)
    return data

reranked_trials_reloaded = read_json("/home/jeff/Downloads/ranked_trials.json")
example_trial = reranked_trials_reloaded[1]

print(example_trial["nctId"])
criteria = example_trial["structured_criteria"]
for k, nested_criteria in criteria.items():
    for term, criteria in nested_criteria.items():
        logic = criteria[0]
        real_criteria = criteria[1]
        assert isinstance(real_criteria, list), f"Real criteria must be a list, but is of type {type(real_criteria)}"
        print(logic)
        for item in real_criteria:
            if isinstance(item, str):
                print("<CHECKBOX>", item)               # add a checkbox here
            elif isinstance(item, list):
                for subitem in item:
                    print("          ", "<CHECKBOX>", subitem)   # add a checkbox here
                print("     ", "<GLOBAL_CHECKBOX>", "is the overall criterion met?")
            else:
                raise ValueError(f"Unknown criterion type: {type(item)}")
            print()