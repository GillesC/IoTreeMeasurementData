import os
import pandas as pd
import json

dir_path = os.path.dirname(os.path.realpath(__file__))

def _to_csv(file_name):
    path = os.path.join(dir_path, file_name+".json")
    print("Converting {}".format(path))

    

    with open(path) as json_file:
        data = json.load(json_file)

        
        measurements = []
        for serie in data["results"]:
            for thing in serie["series"]:
                df_values = pd.DataFrame(
                    thing["values"], columns=thing["columns"])
                measurements.append(df_values)
        
        df = pd.DataFrame(columns=data["results"][0]["series"][0]["columns"])
        df = df.append(measurements, ignore_index=True)
        path_out = os.path.join(dir_path, file_name+".csv")
        print("to {}".format(path_out))
        df.to_csv(path_out, index=False)

# r=root, d=directories, f = files
for r, d, f in os.walk(dir_path):
    for file in f:
        if '.json' in file:
            file_name = os.path.splitext(file)[0]
            _to_csv(file_name)

