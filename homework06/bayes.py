from collections import defaultdict
from copy import deepcopy
import itertools
import math
import operator
from collections import Counter


class NaiveBayesClassifier:
    def __init__(self, alpha):
        if not (alpha <= 1.0 and alpha > 0.0):
            raise ValueError("Smoothing parameter must be between 0.0 and 1.0")
        self.priors = []
        self.alpha = alpha
        self.doc_count = 0
        self.unique_words = []
        self.words_per_class = []
        self.class_lengths = []
        self.word_probs = []

    def fit(self, X, y):
        """ Fit Naive Bayes classifier according to X, y. """
        if not X or not y or not (len(X) == len(y)):
            raise ValueError("The training set is either unmarked or empty.")
        self.doc_count = len(X)
        self.priors = Counter(y)
        for e in self.priors:
            self.priors[e] /= len(y)
        self.unique_words = [i.split(" ") for i in X]
        self.unique_words = list(itertools.chain.from_iterable(self.unique_words))
        self.unique_words = sorted(list(set(self.unique_words)))
        self.words_per_class = defaultdict(defaultdict)
        self.class_lengths = defaultdict(int)
        for i, string in enumerate(X):
            words = string.split(" ")
            c = y[i]
            self.class_lengths[c] += len(words)
            for word in words:
                if not word in self.words_per_class.keys():
                    self.words_per_class[word] = {
                        key: value for (key, value) in zip(list(set(y)), [0 for _ in list(set(y))])
                    }
                self.words_per_class[word][c] += 1
        self.word_probs = deepcopy(self.words_per_class)
        for word, value in self.word_probs.items():
            for c, _ in value.items():
                self.word_probs[word][c] = (self.word_probs[word][c] + self.alpha) / (
                    self.class_lengths[c] + self.alpha * len(self.unique_words)
                )
        return

    def predict(self, X):
        """ Perform classification on an array of test vectors X. """
        if (
            not self.priors
            or not self.doc_count
            or not self.unique_words
            or not self.words_per_class
            or not self.class_lengths
            or not self.word_probs
        ):
            raise ValueError("The model is untrained")
        labels = []
        for document in X:
            words = document.split(" ")
            probabilities = defaultdict(int)
            for c in self.class_lengths.keys():
                word_probs_sum = []
                for word in words:
                    if word in self.unique_words:
                        word_probs_sum.append(math.log(self.word_probs[word][c]))
                word_probs_sum = sum(word_probs_sum)
                probabilities[c] = math.log(self.priors[c]) + word_probs_sum
            predicted_label = max(probabilities.items(), key=operator.itemgetter(1))[0]
            labels.append(predicted_label)
        return labels

    def score(self, X_test, y_test):
        """ Returns the mean accuracy on the given test data and labels. """
        predicted = self.predict(X_test)
        class_accuracies = defaultdict(float)
        for c in list(set(y_test)):
            if y_test.count(c):
                true_positives = sum(
                    [1 for i, e in enumerate(predicted) if e == c and y_test[i] == c]
                )
                false_negatives = sum(
                    [1 for i, e in enumerate(predicted) if e != c and y_test[i] == c]
                )
                class_accuracies[c] = true_positives / (true_positives + false_negatives)
        score = sum([i for i in class_accuracies.values()]) / len(list(set(y_test)))
        return score
