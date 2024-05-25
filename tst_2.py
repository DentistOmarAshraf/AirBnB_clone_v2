#!/usr/bin/python3

from models import *
from models.state import State


all_states = storage.all(State).values()

for state in all_states:
    print(state.cities)
