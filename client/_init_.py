import csv
# import novaclient
# from novaclient import client
import os
header = ['VM', 'IsAlive', 'Space']
# import psycopg2
# from psycopg2.extras import LogicalReplicationConnection

with open('central_repository.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)

HOST_UP = False if os.system("ping -c 1 " + "10.0.0.220") != 0 else True
HOST_UP = False if os.system("ping -c 1 " + "10.0.0.125") != 0 else True
HOST_UP = False if os.system("ping -c 1 " + "192.168.100.66") != 0 else True
HOST_UP = False if os.system("ping -c 1 " + "10.0.0.17") != 0 else True

print(HOST_UP)
#for instance in client.
#    print(instance.name)
#    print(instance.addresses)
#    print(instance.status)


