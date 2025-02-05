from typing import List


def findAntinode(location: List[int], pairLocation: List[int], diff: List[int],
                 map: List[List[int]], uniqueAntinodes: set):
    possibleLocation1 = [location[0] + diff[0], location[1] + diff[1]]
    possibleLocation2 = [location[0] - diff[0], location[1] - diff[1]]
    antinode = possibleLocation1 if possibleLocation1[0] != pairLocation[0] else possibleLocation2
    if 0 <= antinode[0] < len(map) and 0 <= antinode[1] < len(map[0]):
        uniqueAntinodes.add(str(antinode))


def findAntinode2(location: List[int], pairLocation: List[int], diff: List[int],
                  map: List[List[int]], uniqueAntinodes: set):
    uniqueAntinodes.add(str(location))

    possibleLocation1 = [location[0] + diff[0], location[1] + diff[1]]
    possibleLocation2 = [location[0] - diff[0], location[1] - diff[1]]
    if possibleLocation1[0] != pairLocation[0]:
        while 0 <= possibleLocation1[0] < len(map) and 0 <= possibleLocation1[1] < len(map[0]):
            uniqueAntinodes.add(str(possibleLocation1))
            possibleLocation1[0] += diff[0]
            possibleLocation1[1] += diff[1]
    else:
        while 0 <= possibleLocation2[0] < len(map) and 0 <= possibleLocation2[1] < len(map[0]):
            uniqueAntinodes.add(str(possibleLocation2))
            possibleLocation2[0] -= diff[0]
            possibleLocation2[1] -= diff[1]


def findUniqueAntinodes(map: List[List[int]], frequencyLocations: dict) -> int:
    uniqueAntinodes = set()
    for locations in frequencyLocations.values():
        for i in range(len(locations)):
            for j in range(i + 1, len(locations)):
                diff = [locations[i][0] - locations[j][0],
                        locations[i][1] - locations[j][1]]
                # findAntinode(locations[i], locations[j],
                #              diff, map, uniqueAntinodes)
                # findAntinode(locations[j], locations[i],
                #              diff, map, uniqueAntinodes)
                findAntinode2(locations[i], locations[j],
                              diff, map, uniqueAntinodes)
                findAntinode2(locations[j], locations[i],
                              diff, map, uniqueAntinodes)
    return len(uniqueAntinodes)


def findUniqueAntinodeLocations() -> int:
    map = []
    frequencyLocations = dict()

    with open(r'd:\adventofcode\day8.txt', 'r') as f:
        lines = f.readlines()

        for i in range(len(lines)):
            row = lines[i].strip()
            col = []
            for j in range(len(row)):
                col.append(row[j])
                if row[j] != ".":
                    frequency = row[j]
                    if frequency not in frequencyLocations:
                        frequencyLocations[frequency] = []
                    frequencyLocations[frequency].append([i, j])
            map.append(col)

    return findUniqueAntinodes(map, frequencyLocations)


def main():
    print(findUniqueAntinodeLocations())


if __name__ == "__main__":
    main()
