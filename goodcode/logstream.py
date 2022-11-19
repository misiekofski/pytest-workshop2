import json
import os
import random
from time import sleep, time

from faker import Faker

fake = Faker()


def generate_log():
    log = json.dumps({
        'timestamp': time(),
        'user': os.environ.get('USERNAME'),
        'DEVICE_ID': fake.numerify(text='rossmann-pl-%##'),
        'MB_SENT': fake.random_element(elements=(1, 2, 3, 5, 7, 11)),
        'log': fake.json(data_columns={'Message': 'paragraph'}, num_rows=1)
    }, sort_keys=True, indent=4)
    print(log)


def stream_logs():
    while True:
        generate_log()
        sleep(random.randint(0, 3))


if __name__ == "__main__":
    stream_logs()
