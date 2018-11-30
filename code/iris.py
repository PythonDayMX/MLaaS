# ===============================================================
# Author: Rodolfo Ferro
# Email: ferro@cimat.mx
# Twitter: @FerroRodolfo
#
# ABOUT COPYING OR USING PARTIAL INFORMATION:
# This script was originally created by Rodolfo Ferro, for
# his workshop in PythonDay Mexico 2018 at CUCEA in Gdl, Mx.
# Any explicit usage of this script or its contents is granted
# according to the license provided and its conditions.
# ===============================================================

# -*- coding: utf-8 -*-

from sklearn.datasets import load_iris
from sklearn import tree
import graphviz


def iris_classifier(verbose=False):
    """Basic Decision Tree Classifier for Iris problem.

    Based on: http://scikit-learn.org/stable/modules/tree.html
    """

    # Load dataset:
    # TODO

    # Build and train classifier:
    # TODO: Build classifier
    # TODO: Train classifier

    # Visualize model:
    if verbose:
        dot_data = tree.export_graphviz(clf, out_file=None,
                                        feature_names=iris.feature_names,
                                        class_names=iris.target_names,
                                        filled=True, rounded=True,
                                        special_characters=True)
        graph = graphviz.Source(dot_data)
        graph.render("iris")
    return clf


if __name__ == '__main__':
    iris_classifier(verbose=True)
