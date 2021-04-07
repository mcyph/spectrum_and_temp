import csv
import time
import datetime
from collections import deque

import as7265x_spectral_data
import bme280_temp_humidity_data
#import ccs811_air_quality_data

SLEEP_SECONDS = 0
IN_MEMORY_CACHE = 6*60
FLUSH_TO_DISK_EVERY = 3


def get_values_key(values):
    return '_'.join([str(y) for y in values[:-1]])


open_files = {}
csv_writers = {}
most_recent_queues = {}
num_times = [0]


def get_last_values():
    out = {}
    for k in most_recent_queues:
        out[k] = [most_recent_queues[k][0]]
    return out


def get_time_series():
    out = {}
    for k in most_recent_queues:
        out[k] = list(most_recent_queues[k])
    return out


def poll():
    values_dict = {
        "spectral_raw": as7265x_spectral_data.get_raw_values(),
        "spectral_calibrated": as7265x_spectral_data.get_calibrated_values(),
        "temp_humidity": bme280_temp_humidity_data.get_values(),
        #"air_quality": ccs811_air_quality_data.get_values()
    }

    for key, values in values_dict.items():
        if key not in open_files:
            # Open the file for the CSV out
            f = open_files[key] = open(f'{key}.csv', 'a', encoding='utf-8')

            # Open the CSV dict writer, adding a header if the file is new
            csv_writers[key] = csv.DictWriter(f, fieldnames=['datetime']+[
                get_values_key(i_values) for i_values in values
            ])
            if not f.tell():
                csv_writers[key].writeheader()

            # Add a most recent queue to allow in-memory reading from the API
            most_recent_queues[key] = deque(maxlen=IN_MEMORY_CACHE)

        # Write to the CSV file
        csv_writer = csv_writers[key]
        write_me = {'datetime': datetime.datetime.now().isoformat()}
        write_me.update({
            get_values_key(i_values): str(i_values[-1])
            for i_values in values
        })
        csv_writer.writerow(write_me)
        most_recent_queues[key].appendleft(write_me)

    time.sleep(SLEEP_SECONDS)
    num_times[0] += 1

    if num_times[0] % FLUSH_TO_DISK_EVERY == 0:
        for f in open_files.values():
            f.flush()


if __name__ == '__main__':
    while True:
        poll()
