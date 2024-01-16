## Random-Loot-Tables
Randomizes Minecraft block's loot tables. **This isn't meant to work for entities or chest loot.**

It'll create a datapack, here's how it works:

```
data pack folder structure:
        loot_tables (folder):
            blocks (folder):
                example_item1.json
                example_item2.json
                example_item3.json
                ...

code explanation:
        - makes a list of all info from json
        files in loot_tables\blocks
        - gets a random file's info from the list
        - replace all info in the json files with
        the random file info we got above
```

## Usage
- Go to the [default minecraft datapack repo](https://github.com/PixiGeko/Minecraft-default-data/), select the branch for whatever version of minecraft you're using, click the green `Code` button and `Download ZIP`.
- Unzip the datapack
- Download and run [randomize.py](/randomize.py) with python
- Paste the path to `<default-datapack>\data\minecraft\loot_tables\blocks` when prompted.
- Done!

Apply it like any other Minecraft datapack.
