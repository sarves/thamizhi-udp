# ThamizhiUDp: Universal Dependency Parser for Tamil
## Home page: http://nlp-tools.uom.lk/thamizhi-udp/

ThamizhiUDp is a neural-based dependency parser, which provides a complete pipeline for the dependency parsing of the Tamil language text using Universal Dependency formalism. We have considered the phases of the dependency parsing pipeline and identified tools and resources in each of these phases to improve the accuracy and to tackle data scarcity.

ThamizhiUDp uses Stanza for tokenisation and lemmatisation, ThamizhiPOSt and ThamizhiMorph for generating Part of Speech (POS) and Morphological annotations, and uuparser with multilingual training for dependency parsing.

Our dependency parser ThamizhiUDp was trained using multilingual data. It shows a Labelled Assigned Score (LAS) of 62.39, 4 points higher than the current best achieved for Tamil dependency parsing. 

## Cite us
Sarveswaran, K, Gihan Dias, 2020, December. "ThamizhiUDp: A Dependency Parser for Tamil". In Proceedings of the 17th International Conference on Natural Language Processing (ICON-2020), IIT Patna, India [Accepted].

# How to use

## Setting up ThamizhiUDp:
You need to have Python 3.0. In addition, install the following tools and libraries (These commands are for Debian based distribution, you can find the similar ones for other Linux distributions & Windows over the web):
```
pip3 install stanza
sudo apt install foma
pip3 install cython
pip3 install uuparser
```
[Download this compressed file](http://nlp-tools.uom.lk/thamizhi-udp/thamizhi-pos-morph-ud-parsers.zip) , and uncompressed it. You should be able to see the following scipts: thamizhi-post.py, thamizhi-morph.py, thamizhi-pos-morph.py, parse.sh, and the following two folders: models and thamizhiudp


1. **POS Tagging: ThamizhiPOSt:**
```
python3 thamizhi-post.py "input-file"
```
where "input-file" is the text file you want to POS tag. (there should not be any empty lines in the file) . This will generate a file called pos-tagged.txt. For more information about POS tagging, visit ThamizhiPOSt

2. **Morphological Tagging: ThamizhiMorph:**
```
python3 thamizhi-morph.py "input-file"
```
where "input-file" is the text file you want to POS tag. (there should not be any empty lines in the file) . This will generate a file called morph-tagged.txt. For more information about Morphological tagging, visit ThamizhiMorph

3. **POS-Morphology aligned Tagging: ThamizhiPOSt & ThamizhiMorph:**
```
python3 thamizhi-pos-morph.py "input-file"
```
where "input-file" is the text file you want to POS-Morphology aligned tags. (there should not be any empty lines in the file) . This will generate a file called pos-morph-aligned.txt.

4. **Dependency Parsing: ThamizhiUDp:**
```
./parse.sh "input-file"
```
where "input-file" is the text file . Currently, this file has to be in CoNLL format, you can have an "_" as a placeholder for dependency lable. Soon we will make a sophesticated script using which you can easily parse raw text. This script will generate a file called dependency-parsed.txt.

### Acknowledgment
This research was supported by the Accelerating Higher Education Expansion and Development (AHEAD) Operation of the Ministry of Higher Education, Sri Lanka funded by the World Bank.

*How can I improve this, write to me please!*

