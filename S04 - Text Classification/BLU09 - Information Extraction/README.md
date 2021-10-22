# BLU09 - Information Extraction

## What is in this BLU?

This big learning unit continues the text classification specialization. Now that you know how to process text and extract meaningful features, it will be shown how you can prepare these features so you can actually use them for whatever challenge you are facing, as text classification, for example.

We will focus on how to go from a huge set of features to a more tractable dataset, which is more useful for the modelling of our problem.

If you are able to solve this BLU, you are equipped with one more set of tools to succeed in the following hackathon :)

## How to go through this BLU

By now you should already know the process by heart, nevertheless here it is:
1. Follow the [Learning Unit Workflow](https://github.com/LDSSA/batch5-students#learning-unit-workflow) to setup your environment.
1. Go through the Learning Notebooks (there's two of them).
1. Do the Exercise notebook, and submit it on [the portal](https://portal.lisbondatascience.org), as usual.

## "I need help understanding something"

You can and should ask for help, be it about Learning Notebooks, Exercises, or anything else. Please checkout the [How to Ask for Help](https://ldssa.github.io/wiki/Starters%20Academy%20(LDSSA)/How-to-ask-for-and-give-help/), and remember not to share code when asking for help about the exercises! 

## "I think I've found a bug"

This repo is completely open source and is continuously improving over time. When you spot a mistake, please check whether it has been detected in the issues. If it hasn't, please open an issue, explaining in details where it is (e.g. in what notebook, and on what line), and how to reproduce the error. If it is an easy fix, feel free to make a pull request.

## Known issues:

(OSX): Getting an SSL error during this step:

```
python -m spacy download en_core_web_md
```

has happened in the past. Doing the following:

```
/Applications/Python\ 3.7/Install\ Certificates.command
```

should solve it.
