from service import Service
from data_loader import DataLoader as Loader

services = [Service(name='loader', endpoint='/loader', action=Loader().start, cache={})]

for s in services:
    s.start()
