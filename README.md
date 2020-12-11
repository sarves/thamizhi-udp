# thamizhi-udp: Universal Dependency Parser for Tamil language

ThamizhiUDp is a neural-based dependency parser, which provides a complete pipeline for the dependency parsing of the Tamil language text using Universal Dependency formalism. We have considered the phases of the dependency parsing pipeline and identified tools and resources in each of these phases to improve the accuracy and to tackle data scarcity.
ThamizhiUDp uses Stanza for tokenisation and lemmatisation, ThamizhiPOSt and ThamizhiMorph for generating Part of Speech (POS) and Morphological annotations, and uuparser with multilingual training for dependency parsing.
Our dependency parser ThamizhiUDp was trained using multilingual data. It shows a Labelled Assigned Score (LAS) of 62.39, 4 points higher than the current best achieved for Tamil dependency parsing. 
