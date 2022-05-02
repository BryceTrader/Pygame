#!/bin/bash

template="from BaseComponent import BaseComponent

class $1(BaseComponent):
    def __init__(self, $2) -> None:
        super().__init__($1)
        self.$2 = $2
        
    def __repr__(self):
        return f'$1({self.name}, {self.$2})'"

touch $1.py
echo -e "$template" > $1.py
code $1.py