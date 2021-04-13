# asnq-challenging
ASNQ without easy negative answers.

## Description

Original ASNQ dataset, proposed by [TandA](https://github.com/alexa/wqa_tanda) contains many negative pairs that should be really simple to be discovered. In the original paper, the authors state that there are three different types of negative pairs:

- Sentences from the document that are in the long answer but do not contain the annotated short answers. It is possible that these sentences might contain the short answer.
- Sentences from the document that are not in the long answer but contain the short answer string, that is, such occurrence is purely accidental.
- Sentences from the document that are neither in the long answer nor contain the short answer.

We believe that the last category, which is the largest one, contains too many pairs with a very easily-recognizable negative answer. We do not consider those negative pairs.
