def sex(data):
   features = data["features"]
   
   sex_map = {"male": 0, "female": 1}
   features["Sex"] = sex_map.get(features["Sex"], 2)


def embarked(data):
   features = data["features"]

   embarked_map = {"C": 0, "Q": 1, "S": 2, "U":3}
   features["Embarked"] = embarked_map.get(features["Embarked"], 3)

def name(data):
    features = data["features"]

    name_prefix = features["Name"].lower()
    if "mr" in name_prefix:
        features["Name"] = 0
    elif "mrs" in name_prefix:
        features["Name"] = 1
    elif "miss" in name_prefix:
        features["Name"] = 2
    else:
        features["Name"] = 3