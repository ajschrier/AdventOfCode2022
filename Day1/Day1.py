demo_input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

def find_calorie_sums(input_list):
    calorie_sums = []
    idx = 0
    calorie_sums.append(0)
    for i in input_list:
        if i != "":
            calorie_sums[idx] += int(i)
        else:
            idx += 1
            calorie_sums.append(0)
    return calorie_sums

def max_calorie_count(input_list):
    calorie_sums = find_calorie_sums(input_list)
    return max(calorie_sums)

def top_three_calorie_count(input_list):
    calorie_sums = find_calorie_sums(input_list)
    calorie_sums.sort(reverse=True)
    return sum(calorie_sums[:3])


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        input_file = f.readlines()
    print([i.strip() for i in input_file])


    print(max_calorie_count([i.strip() for i in input_file]))
    print(top_three_calorie_count([i.strip() for i in input_file]))