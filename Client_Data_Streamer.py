import pandas as pd
from datetime import datetime
from datetime import timedelta
import requests
import time
import random

# class for data_generation


def data_generation():
    surr_id = random.randint(1, 3)
    speed = random.randint(20, 260)
    date = datetime.today().strftime("%Y-%m-%d")
    time = datetime.now().isoformat()

    return [surr_id, speed, date, time]


if __name__ == '__main__':
    REST_API_URL = env.PBI_URL

    while True:
        data_raw = []
        for i in range(1):
            row = data_generation()
            print(row[2])
            data_raw.append(row)
            print("Raw data - ", data_raw)

        # set the header record
        HEADER = ["surr_id", "speed", "date", "time"]

        data_df = pd.DataFrame(data_raw, columns=HEADER)
        data_json = bytes(data_df.to_json(orient='records'), encoding='utf-8')
        print("JSON dataset", data_json)

        # Post the data on the Power BI API
        r = requests.post(REST_API_URL, data_json)
        pastebin_url = r.status_code
        print("response status:", pastebin_url)

        print("Data posted in Power BI API")
        time.sleep(2)
