import argparse
import re
import string

import fasttext
import nltk
import numpy as np
from tensorflow.keras.models import load_model


class SATDDetector:
    """
    Self-admitted technical debt verifier
    """

    def __init__(self, weight_file, word_embedding_file):
        # Load the model and its weights
        print('Loading model {}...'.format(weight_file))
        self._model = load_model(weight_file)
        self._size_of_input = self._model.layers[0].get_output_at(0).get_shape()[1]

        # Load the FastText word embeddings
        self._word_embedding = fasttext.load_model(word_embedding_file)
        self._word_embedding_cache = {}

        # Initialize the tokenizer and punctuation settings
        self._tokenizer_words = nltk.TweetTokenizer()

        # Set up label configurations
        label_num = self._model.layers[-1].get_output_at(0).get_shape()[-1]
        self._labels = ['SATD', 'non-SATD']
        self._padding = '<pad>'

    def comment_pre_processing(self, comment):
        """
        Pre-process comment

        :param comment:
        :return:
        """
        # Remove comment delimiters and convert to lowercase
        comment = re.sub('(//)|(/\\*)|(\\*/)', '', comment).lower()
        # Tokenize comment into sentences and words
        tokens_sentences = [self._tokenizer_words.tokenize(t) for t in nltk.sent_tokenize(comment)]
        tokens = [word for t in tokens_sentences for word in t]
        return tokens

    def prepare_comments(self, comment):
        """
        Prepare comments for machine learning model

        :return:
        """
        # Pre-process the comment
        pre_stripped = self.comment_pre_processing(comment)

        # Pad or truncate the comment based on the input size
        if len(pre_stripped) > self._size_of_input:
            new_sentence = pre_stripped[:self._size_of_input]
        else:
            num_padding = self._size_of_input - len(pre_stripped)
            new_sentence = pre_stripped + [self._padding] * num_padding

        # Convert words to word embeddings
        x_test = []
        for word in new_sentence:
            if word not in self._word_embedding_cache:
                word_embed = self._word_embedding[word]
                self._word_embedding_cache[word] = word_embed
                x_test.append(word_embed)
            else:
                x_test.append(self._word_embedding_cache[word])
        return np.array([x_test])

    def classify_prob_comment(self, comment):
        """
        Classify a single comment

        :param comment:
        """
        # Prepare the comment for classification
        input_x = self.prepare_comments(comment)
        # Make predictions using the model
        y_pred = self._model.predict(input_x)
        y_pred_bool = np.argmax(y_pred, axis=1)

        # Print the prediction results
        print('Text: {}'.format(comment))
        print('Predicted label: {}\n'.format(self._labels[y_pred_bool[0]]))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--weight_file", type=str, default="")
    parser.add_argument("--word_embedding_file", type=str, default="")
    args = parser.parse_args()

    v = SATDDetector(args.weight_file, args.word_embedding_file)
    v.classify_prob_comment('to make their code more readable. I would like to see something like this in the API.')
    v.classify_prob_comment('cluster service : add a cluster service based on JGroups Raft')
    v.classify_prob_comment('Would you be able to build an unit test of this sample code so we can take that and add '
                            'to the tests of camel-cxf and work on a fix.')
    v.classify_prob_comment('I\'m raising a new Jira for this.')
    v.classify_prob_comment('We also need to update the mail wiki page with this feature.')
    v.classify_prob_comment('Fix pom.xml files to support nexus based release process')
    v.classify_prob_comment('The component docs are in adoc files with the source code - the wiki is dead so don\'t '
                            'update there. Make sure to fix/update in adoc, and if you want you can do wiki too. '
                            'But wiki only changes will be lost in the future when wiki is discarded completely')


if __name__ == '__main__':
    main()
