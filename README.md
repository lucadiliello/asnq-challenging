# asnq-challenging
ASNQ without easy negative answers.

## Description

Original ASNQ dataset, proposed by [TandA](https://github.com/alexa/wqa_tanda) contains many negative pairs that should be really simple to be discovered. In the original paper, the authors state that there are three different types of negative pairs:

- Sentences from the document that are in the long answer but do not contain the annotated short answers. It is possible that these sentences might contain the short answer.
- Sentences from the document that are not in the long answer but contain the short answer string, that is, such occurrence is purely accidental.
- Sentences from the document that are neither in the long answer nor contain the short answer.

We believe that the last category, which is the largest one, contains too many pairs with a very easily-recognizable negative answer. We do not consider those negative pairs.


## Create the datasets

By default training and development set are available. In order to obtain both training, validation and test sets we suggest you to use the splits defined by [The Cascade Transformers](https://github.com/alexa/wqa-cascade-transformers). In this case, the original development set will be split in both dev and test sets.

Install required libraries:

```bash
pip install -r requirements.txt
```

Create only training and validation sets with:
```bash
python create.py --split train --output_file output/asnq-challenging-train.tsv
python create.py --split validation --output_file output/asnq-challenging-dev.tsv
```

Create training, validation and test sets as in the `Cascade Transformer` with:
```bash
python create.py --split train --output_file output/asnq-challenging-train.tsv --filter input/filters/unique.train
python create.py --split validation --output_file output/asnq-challenging-dev.tsv --filter input/filters/unique.dev
python create.py --split validation --output_file output/asnq-challenging-test.tsv --filter input/filters/unique.test
```
where `unique.train`, `unique.dev` and `unique.test` are taken from [here](https://github.com/alexa/wqa-cascade-transformers/tree/master/data).
