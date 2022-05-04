import csv
import numpy as np
import pandas as pd
import requests

from os.path import exists


def parse_koda(token_id, response_json):

    koda = {
        "token_id": token_id,
        "image": response_json['image']
    }
    attributes = response_json['attributes']

    for attribute in attributes:

        koda[attribute['trait_type']] = attribute['value']

    return koda

def run():

    filename = "../seeds/otherdeed/kodas.csv"

    with open(filename, "a") as kodas_file:

        writer = csv.writer(kodas_file)
        if not exists(filename):
            header = ['token_id', 'image', 'head', 'eyes', 'core', 'clothing', 'weapon']
            writer.writerow(header)

        for token_id in np.arange(0, 10000):

            print (token_id)

            response = requests.get('https://api.otherside.xyz/kodas/{}'.format(token_id))
            if response.status_code == 200:
                response_json = response.json()
                koda = parse_koda(token_id, response_json)

                row = [
                    koda['token_id'],
                    koda['image'],
                    koda.get('Head', None),
                    koda.get('Eyes', None),
                    koda.get('Core', None),
                    koda.get('Clothing', None),
                    koda.get('Weapon', None)
                ]
                writer.writerow(row)

run()