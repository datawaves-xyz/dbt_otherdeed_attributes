import csv
import numpy as np
import pandas as pd
import requests
import sys

from os.path import exists
from requests.adapters import HTTPAdapter, Retry

def parse_land(token_id, response_json):

    koda = {
        "token_id": token_id,
        "image": response_json['image']
    }
    attributes = response_json['attributes']

    for attribute in attributes:

        koda[attribute['trait_type']] = attribute['value']

    return koda


def run():
    start = int(sys.argv[1])
    end = int(sys.argv[2])

    s = requests.Session()
    retries = Retry(total=6,
                    backoff_factor=0.1,
                    status_forcelist=[ 500, 502, 503, 504 ])

    s.mount('https://', HTTPAdapter(max_retries=retries))
    s.mount('http://', HTTPAdapter(max_retries=retries))

    filename = "../seeds/lands.csv.{0}_{1}".format(start, end)

    with open(filename, "a") as f:

        writer = csv.writer(f)
        if not exists(filename):
            header = ['token_id', 'image', 'category', 'sediment', 'sediment_tier', 'environment', 'environment_tier',
                'eastern', 'eastern_tier', 'southern', 'southern_tier', 'western', 'western_tier', 'northern', 'northern_tier',
                'artifact', 'plot', 'koda'
            ]
            writer.writerow(header)

        for token_id in np.arange(start, end):

            print (token_id)

            response = s.get('https://api.otherside.xyz/lands/{}'.format(token_id))
            if response.status_code == 200:
                response_json = response.json()
                land = parse_land(token_id, response_json)

                row = [
                    land['token_id'],
                    land['image'],
                    land.get('Category', None),
                    land.get('Sediment', None),
                    land.get('Sediment Tier', None),
                    land.get('Environment', None),
                    land.get('Environment Tier', None),
                    land.get('Eastern Resource', None),
                    land.get('Eastern Resource Tier', None),
                    land.get('Southern Resource', None),
                    land.get('Southern Resource Tier', None),
                    land.get('Western Resource', None),
                    land.get('Western Resource Tier', None),
                    land.get('Northern Resource', None),
                    land.get('Northern Resource Tier', None),
                    land.get('Artifact', None),
                    land.get('Plot', None),
                    land.get('Koda', None)
                ]
                writer.writerow(row)

run()