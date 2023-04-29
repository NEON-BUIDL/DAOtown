import os
import sys
import math
from pathlib import Path

def main():
    if "--head" in sys.argv:
        print("# DAOtown\n")
        print("[![.github/workflows/main.yml](https://github.com/NEON-BUIDL/DAOtown/actions/workflows/main.yml/badge.svg)](https://github.com/NEON-BUIDL/DAOtown/actions/workflows/main.yml) [![](https://dcbadge.vercel.app/api/server/uwuFuB6m)](https://discord.gg/uwuFuB6m)\n")
        print("The wild west of cipherspace, welcome to DAOtown\n")
        print("Demo: https://hyperfy.io/daotown\n")
        print("## About\n")
        print("Howdy! We're building a 3D frontend for the DAO ecosystem. First just gathering assets into a drag and drop pallet that 3D designers can use to mock up (perhaps even collaboratively) concepts with. The buildings will have links to other worlds that link back, forming a 3D [web ring](https://indieweb.org/webring). The signs and NPCs will be interactive elements to learn more about various projects and for bounties. Since they're just glbs, DAOtown can be built across a multitude of different platforms. We're just getting started, lets build!\n")
        print("![image](https://user-images.githubusercontent.com/32600939/235210391-b759c45a-198e-41f3-816d-f4db3b998fd7.png)\n")
        print("[DAOtown](https://opensea.io/assets/ethereum/0x5864a2eef51cee5fdbee8bc4649e6d38a2ff5a97/7) by Perchy")
        print("\n")
        sys.exit(0)

    if len(sys.argv) < 2:
        print("Usage: python table.py directory/")
        sys.exit(1)

    directory = sys.argv[1]
    pairs = {}

    for root, dirs, files in os.walk(directory):
        for glb in files:
            if glb.endswith(".glb"):
                base = Path(glb).stem
                png = Path(root) / (base + ".png")
                if png.exists():
                    pairs[base] = (Path(root) / glb, png)

    count = len(pairs)
    size = int(math.sqrt(count))

    ## Change this later to be based on repo name
    print(f" ## {directory}")
    print("\n")

    print("|", end="")
    for i in range(size):
        print(f" {i + 1} |", end="")
    print()

    print("|", end="")
    for i in range(size):
        print(" --- |", end="")
    print()

    index = 0
    for key, value in pairs.items():
        if index % size == 0:
            print("|", end="")

        glb, png = value
        print(f" [![{key}]({png})]({glb}) |", end="")

        index += 1

        if index % size == 0:
            print()

    print()

if __name__ == "__main__":
    main()

