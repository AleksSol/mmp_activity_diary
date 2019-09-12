import argparse
import sys


def main(target_len=10):
    def print_dict(d):
        print(f'len: {len(d):<7}memory: {sys.getsizeof(d)}')

    sample_dict = {}

    print(f'\nINITIAL\n')
    print_dict(sample_dict)

    print('\nADD STAGE\n')

    for i in range(target_len):
        sample_dict[i] = i
        print_dict(sample_dict)

    print('\nDELETE STAGE\n')

    for i in range(target_len):
        del sample_dict[i]
        print_dict(sample_dict)

    print('\nADD LAST\n')
    sample_dict[0] = 0
    print_dict(sample_dict)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Dict can became smaller!')
    parser.add_argument('--num', type=int, default=21, help='Number of dict elements')
    args = parser.parse_args()

    main(args.num)
