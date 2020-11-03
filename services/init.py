from service import Service
from data_loader import DataLoader as Loader

services = [
    Service(name='loader',
            endpoint='/loader',
            cache={},
            action=Loader(cache={}).start)
]

for s in services:
    s.start()
