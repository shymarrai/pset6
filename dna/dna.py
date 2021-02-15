import sys
import csv

DNA_AGATC = "AGATC"
DNA_AATG = "AATG"
DNA_TATC = "TATC"


def main():
    base, dna_sequence = verify_args()
    sequence = read_sequence(dna_sequence)
    people = read_people(base)
    dna = compare_sequences(sequence)
    person = lookup_people(people, dna)

    if person:
        print(person["name"])
    else:
        print("No match")


def compare_sequences(sequence):
    return {
        DNA_AGATC: counting_dna(sequence, DNA_AGATC),
        DNA_AATG: counting_dna(sequence, DNA_AATG),
        DNA_TATC: counting_dna(sequence, DNA_TATC),
    }


def verify_args():
    if len(sys.argv) != 3:  # check for entreance of datas
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)
    return sys.argv[1], sys.argv[2]

# Load sequences


def read_sequence(sequence):
    with open(sequence, "r") as sequence_file:
        return sequence_file.read()
# switch database
# read cells and csv file and load database


def read_people(base):
    people = []
    with open(base, "r") as dna_file:
        reader = csv.DictReader(dna_file)
        for row in reader:
            people.append({
                "name": row["name"],
                DNA_AGATC: int(row[DNA_AGATC]),
                DNA_AATG: int(row[DNA_AATG]),
                DNA_TATC: int(row[DNA_TATC]),
            })
    return people


def lookup_people(people, dna):
    for person in people:
        if person[DNA_AGATC] == dna[DNA_AGATC]\
                and person[DNA_AATG] == dna[DNA_AATG]\
                and person[DNA_TATC] == dna[DNA_TATC]:

            return person


def counting_dna(sequence, dna_str):
    max_group_dna = 0
    while True:
        index = sequence.find(dna_str)

        if index >= 0:
            dna_sequence = sequence[index:]
            dna_groups, group_len = calculate_group(dna_sequence, dna_str)
            max_group_dna = max(max_group_dna, dna_groups)
            sequence = dna_sequence[group_len:]

        else:
            break

    return max_group_dna


def calculate_group(dna_sequence, dna_str):
    dna_groups = 0
    group_len = len(dna_str)
    while dna_sequence.find(dna_str) == 0:
        dna_groups += 1
        dna_sequence = dna_sequence[group_len:]

    return dna_groups, dna_groups * group_len


main()