
def solve(datastream, marker_length=4):
    for index in range(marker_length, len(datastream) + 1):
        if len(set(datastream[index - marker_length : index])) == marker_length:
            return index


assert solve('bvwbjplbgvbhsrlpgdmjqwftvncz') == 5
assert solve('nppdvjthqldpwncqszvftbrmjlhg') == 6
assert solve('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10
assert solve('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11

assert solve('bvwbjplbgvbhsrlpgdmjqwftvncz', marker_length=14) == 23
assert solve('nppdvjthqldpwncqszvftbrmjlhg', marker_length=14) == 23
assert solve('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', marker_length=14) == 29
assert solve('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', marker_length=14) == 26

with open('advent_of_code_2022/day_6/input.txt') as file:
    datastream = file.readline()
print(solve(datastream))
print(solve(datastream, marker_length=14))