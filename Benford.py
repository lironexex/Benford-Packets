import matplotlib.pyplot as plt
import numpy as np
import csv

if __name__ == '__main__':

    heights_single = [0] * 16
    heights_double = [0] * 256

    with open('packets.csv', 'r') as f:
        reader = csv.reader(f)
        amr_csv = list(reader)
        for line in amr_csv:
            if line[0][0] > 'F':
                continue
            heights_double[int(line[0], 16)] += 1
            heights_single[int(line[0][0], 16)] += 1

    print(heights_single)
    print(heights_double)

    # single digit graph
    bar_labels = list(range(0, 16))
    bar_labels = ' '.join(f'{i:01x}' for i in bar_labels)
    bar_labels = bar_labels.upper().split()
    print(bar_labels)
    plt.bar(bar_labels, heights_single, color=['tomato'])
    plt.xlabel('First number in the packet')
    plt.ylabel('Amount of packets who start with the number')
    plt.title("Graph for the first digit in the packet")
    plt.show()

    # two digit graph
    bar_labels = list(range(0, 256))
    bar_labels = ' '.join(f'{i:02x}' for i in bar_labels)
    bar_labels = bar_labels.upper().split()
    print(bar_labels)
    plt.bar(bar_labels, heights_double, color=['tomato'])
    plt.show()
