import sys
import os

# This line will add to the python list of paths to look for modules the path to the project root
MAIN_PARENT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
if MAIN_PARENT_PATH not in sys.path:
    sys.path.append(MAIN_PARENT_PATH)

import numpy as np
import qsimov as qj
import random as rnd
import sympy as sp
import pathlib

from translator.main_translator import MainTranslator 


parent_folder = MAIN_PARENT_PATH.replace("\\", "/") + "/main/codes/"
filename = "ejemplo.txt"
with open(parent_folder + filename , "r") as file:
    txt = file.read()

result = txt.split("\n")

env = {}
exec(txt, env)


translator = MainTranslator()

print(translator.to_openqasm(env["qc"]))

