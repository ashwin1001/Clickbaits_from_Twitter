# Clickbaits_from_Twitter
This project was done as a part of course completion of Social Computing Under the Guidance of Prof. Saptarshi Ghosh, Dept. of Computer Science and Engineering IIT Kharagpur.


# SVM clickbait classifier

Data set was taken from the online clickbait challenge.Which was pre-processed and used as per the requirements.
Under the guidance of Abhijnan Chakraborty,Prof. Saptarshi Ghosh ,Dept. of Computer Science engineering,IIT Kharagpur.

### Requirements
1. JDK 1.7 or greater
2. Python modules
  * numpy
  * scipy
  * SocketServer
  * Scikit Learn
  * networkx

### Usage
* Download [Stanford CoreNLP suite](http://stanfordnlp.github.io/CoreNLP/) (ensure Java version compatibility) and extract
* Download python module [stanford_corenlp_pywrapper](https://github.com/brendano/stanford_corenlp_pywrapper)
* Install python module stanford_corenlp_pywrapper following instructions in thier README.md
* In file stanford_server.py, change path to the Stanford CoreNLP suite to where the suite was extracted
* Run Command : python stanford_server.py
* On a *separate Terminal*, run command: python clickbait_classifier.py
* At the prompt, enter the title to be classified, or enter q/Q to exit

### Code
* dataset: This directory contains both clickbait and non-clickbait tweets used to train the classifier
* dependencies : Includes the corpus of hyperbolic words, common ngrams etc.
* vectors: Includes pretrained vectors used for classification
* experiment.py: code used to run certain experiments for the paper (can be ignored)
* stanford_server.py : Exposes Stanford CoreNLP as a service on localhost
* clickbait_classifier.py : The clickbait classifier
* utility.py : Helper functions
