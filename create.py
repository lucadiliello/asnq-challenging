from argparse import ArgumentParser
import csv
import datasets
from tqdm import tqdm


def main(args):
    """ Create ASNQ-challenging dataset. """
    asnq = datasets.load_dataset('asnq')
    split = asnq[args.split]

    filters = None
    if args.filter is not None:
        with open(args.filter) as fi:
            filters = [x.strip() for x in fi.readlines()]

    identities_vocabulary = dict()
    with open(args.output_file, "w") as fo:
        writer = csv.writer(fo, delimiter="\t", quoting=csv.QUOTE_MINIMAL, quotechar='"')

        for example in tqdm(split, total=len(split), desc="Processing..."):
            if filters is not None and example['question'].strip() not in filters:
                continue

            question = example['question']
            sentence = example['sentence']
            label_number = example['sentence_in_long_answer'] * 2 + example['short_answer_in_sentence'] + 1
 
            if label_number == 1:
                continue

            if not question in identities_vocabulary:
                identities_vocabulary[question] = len(identities_vocabulary)

            writer.writerow([identities_vocabulary[question], question, sentence, label_number == 4])


if __name__ == "__main__":

    parser = ArgumentParser()

    parser.add_argument('--split', choices=['train', 'validation'], default='train', type=str, required=False)
    parser.add_argument('--output_file', type=str, required=True)
    parser.add_argument('--filter', type=str, required=False, default=None)

    args = parser.parse_args()
    main(args)
