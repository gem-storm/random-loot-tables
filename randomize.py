import json
from os import listdir
from random import choice


data_path = input(
    "Paste the path to the default datapack's loot_tables\\blocks folder:\n> "
).replace('"', "")
# reminder to add exceptions for sheep and village chests


def random_tables(path):
    loot_tables = []
    for filename in listdir(path):  # loop through items in path
        fullname = f"{path}\\{filename}"  # listdir() only returns filename, must add to the path
        with open(fullname, "r") as the_file:
            loot_tables.append(
                str(json.load(the_file)).replace("'", '"')
            )  # append the info from file to loot_tables

    for filename in listdir(path):
        rand_table = choice(loot_tables)  # get random loot table
        loot_tables.remove(rand_table)  # remove the chosen loot table from loot_tables
        fullname = path + filename  # join path with filename
        with open(fullname, "w") as the_file:
            the_file.write(rand_table)  # replace everything in file with rand_table


random_tables(data_path)
