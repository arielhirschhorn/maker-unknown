import json
import requests
import pandas as pd

#display max rows
pd.set_option("display.max_rows", None, "display.max_columns", None)

# Function to format the JSON objects correctly
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

#Function to take JSON objects and turn them into a DF across multiple pages
#This does the first three pages of Unknown makers with 25 results per page.

def get_all_objects():
    data_list = []
    for x in range(0, 75):
        parameters = {"search_api_fulltext": "Unknown",
                      "items_per_page": 25,
                      "page": x
                      }
        response = requests.get("https://risdmuseum.org/api/v1/collection", params=parameters).json()
        for item in response:
            data_list.append(item)

    df = pd.DataFrame()
    for each_dict in data_list:
        new_df = pd.json_normalize(each_dict)
        df = df.append(new_df)
    return df


object_df = get_all_objects()
print("Column fields: ")
print(object_df.columns)


##seeing what cultures have unknown makers and adding up counts
s = object_df.groupby(['culture']).size()

culture_counts = s.to_frame()
print(culture_counts)







