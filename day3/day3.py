file = open('day3.in', 'r')
diagnostics = file.readlines()

width = len(diagnostics[0]) - 1

print(f"diagnostics - {len(diagnostics)}")
print(f"width - {width}")

sums = [0 for i in range(width)]

def most_common_bit(subdiagnostics, n):
    bit_sum = 0

    for subdiagnostic in subdiagnostics:
        bit_sum += 1 if subdiagnostic[n] == "1" else 0

    return "1" if bit_sum >= len(subdiagnostics) - bit_sum else "0"

def least_common_bit(subdiagnostics, n):
    bit_sum = 0

    for subdiagnostic in subdiagnostics:
        bit_sum += 1 if subdiagnostic[n] == "1" else 0

    return "1" if bit_sum < len(subdiagnostics) - bit_sum else "0"


print(f"sums - {sums}")

for diagnostic in diagnostics:
    for i in range(width):
        sums[i] += 1 if diagnostic[i] == "1" else 0

print(f"sums - {sums}")

gamma = int(''.join(["1" if sum_ > len(diagnostics) / 2 else "0" for sum_ in sums]), 2)
epsilon = int(''.join(["1" if sum_ < len(diagnostics) / 2 else "0" for sum_ in sums]), 2)

print(f"gamma - {gamma}")  # 349
print(f"gamma - {epsilon}")  # 3746
print(f"result - {gamma * epsilon}")  # 1307354

oxygen_diagnostics = diagnostics

for i in range(width):
    most_common = most_common_bit(oxygen_diagnostics, i)

    oxygen_diagnostics = list(filter(lambda x: x[i] == most_common, oxygen_diagnostics))

print(f"oxygen_diagnostics - {oxygen_diagnostics}")

scrubber_diagnostics = diagnostics

for i in range(width):
    most_common = least_common_bit(scrubber_diagnostics, i)

    scrubber_diagnostics = list(filter(lambda x: x[i] == most_common, scrubber_diagnostics))

    if len(scrubber_diagnostics) == 1:
        break

print(f"scrubber_diagnostics - {scrubber_diagnostics}")

oxygen = int(oxygen_diagnostics[0].strip(), 2)
scrubber = int(scrubber_diagnostics[0].strip(), 2)

print(f"oxygen - {oxygen}")
print(f"scrubber - {scrubber}")
print(f"result - {oxygen * scrubber}")
