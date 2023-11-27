import requests
def get_data_from_cb(site):
    result = requests.get(site)
    valites = result.json()
    valutes_raw_dict = valites["Valute"]
    #print(valutes_raw_dict)
    for val in valutes_raw_dict:
        print("----------------------")
        print(val)
        print(valutes_raw_dict[val]["Value"])
        print("----------------------")
    pass

def put_data_to_db():
    pass

if __name__ == "__main__":
    cb_site = "https://www.cbr-xml-daily.ru/daily_json.js"
    data = get_data_from_cb(cb_site)

    #put_result = put_data_to_db(data)

