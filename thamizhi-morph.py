#this script generate morphological and pos tags using
#thamizhiMorph http://nlp-tools.uom.lk/thamizhi-morph/
#thamizhiPOSt http://nlp-tools.uom.lk/thamizhi-pos/
#Developed by K. Sarveswaran, sarves@cse.mrt.ac.lk
#National Languages Processing Centre, University of Moratuwa, Sri lanka
#version-2020-12-001

import stanza
import sys
import subprocess
import os
import json
import datetime

input_file=str(sys.argv[1]) #input sentence should not have any leading empty lines
morph_tagged_file="morph-tagged.txt"

def isEnglish(text):
        try:
                text.encode(encoding='utf-8').decode('ascii')
        except UnicodeDecodeError:
                return 0
        else:
                return 1


def find_morphemes(word,fsts):

        analyses=[]
        for fst in fsts:
                p1 = subprocess.Popen(["echo", word], stdout=subprocess.PIPE)
                file_name="fsts/"+fst
                p2 = subprocess.Popen(["flookup", file_name], stdin=p1.stdout, stdout=subprocess.PIPE)
                p1.stdout.close()
                output,err = p2.communicate()
                #print(output.decode("utf-8"))

                #1st analysis is broken by new line to tackle cases with multiple analysis
                #then analysis with one output is handled
                #1st each line is broken by tab to find lemma and analysis
                #then those are store in a list and returned back to main

                lines=output.decode("utf-8").strip().split("\n")
                if len(lines) > 1:
                        for line in lines:
                                analysis=line.split("	")
                                if len(analysis) > 1:
                                        if "?" in output.decode("utf-8"):
                                                results=0
                                        else:
                                                #print(analysis[1].strip().split("+"))
                                                analyses.append(analysis[1].strip().split("+"))
                                else:
                                        return 0

                #this is to handle cases with one output, 1st each line is broken by tab to
                #find lemma and analysis
                #then those are store in a list and returned back to main
                analysis=output.decode("utf-8").split("	")
                if len(analysis) > 1:
                        if "?" in output.decode("utf-8"):
                                results=0
                        else:
                                #print(analysis[1].strip().split("+"))
                                analyses.append(analysis[1].strip().split("+"))
                else:
                        return 0
        if analyses :
                return analyses
        else:
                return 0

def guess_morphemes(word,fsts):
        analyses=[]
        for fst in fsts:
                p1 = subprocess.Popen(["echo", word], stdout=subprocess.PIPE)
                file_name="fsts/"+fst
                p2 = subprocess.Popen(["flookup", file_name], stdin=p1.stdout, stdout=subprocess.PIPE)
                p1.stdout.close()
                output,err = p2.communicate()
                #1st analysis is broken by new line to tackle cases with multiple analysis
                #then analysis with one output is handled
                #1st each line is broken by tab to find lemma and analysis
                #then those are store in a list and returned back to main

                lines=output.decode("utf-8").strip().split("\n")
                if len(lines) > 1:
                        for line in lines:
                                analysis=line.split("	")
                                if len(analysis) > 1:
                                        if "?" in output.decode("utf-8"):
                                                results=0
                                        else:
                                                #print(analysis[1].strip().split("+"))
                                                analyses.append(analysis[1].strip().split("+"))
                                else:
                                        return 0

                #this is to handle cases with one output, 1st each line is broken by tab to
                #find lemma and analysis
                #then those are store in a list and returned back to main
                analysis=output.decode("utf-8").split("	")
                if len(analysis) > 1:
                        if "?" in output.decode("utf-8"):
                                results=0
                        else:
                                #print(analysis[1].strip().split("+"))
                                analyses.append(analysis[1].strip().split("+"))
                else:
                        return 0
        if analyses :
                return analyses
        else:
                return 0


#here Stanza models are listed for pos tagging     
config = {
	'processors': 'tokenize', # Comma-separated list of processors to use
	'lang': 'ta', # Language code for the language to build the Pipeline in
	'tokenize_model_path': './models/ta_ttb_tokenizer.pt', 
}
nlp = stanza.Pipeline(**config)

punct_dict = """{".":"period",",":"comma",";":"semi-colon",":":"colon","-":"hyphen","(":"open-bracket",")":"close-bracket"}"""
punct_json = json.loads(punct_dict)

#reading fsts, fsts in fst_list has to be placed in a priority order in which look up should happen
#this needs to be passed to the function using which morphemes are extracted
fsts=[]
f1=open("fsts/fst-list","r")
for line in f1:
        fsts.append(line.strip())
f1.close()

#reading guesser file names, these will be used when a word is not found in fsts
gussers=[]
f1=open("fsts/guesser-list","r")
for line in f1:
        gussers.append(line.strip())
f1.close()


#read data to be passed, and keep it in an array
data_input=[]
f1=open(input_file,"r")
for line in f1:
        data_input.append(line.strip())
f1.close()


#open up a file to write results
morph_tagged=open(morph_tagged_file, 'w')


morph_tagged.write("#POS and Morphology annotations, generated by ThamizhiMorph \n \
#Given text will be 1st tokenised and broken into sentences\
#Output is -tab- separated, and the fields represents the following:\n \
#1. Word sequence number\n\
#2. Given word\n\
#3. POS (identified by ThamizhiMorph)\n\
#4. Lemma (Please keep in ming that sometime guesser might get this wrong)\n\
#5. Morpheme lables, speparated by a '-'\n\
#If there are multiple analysis, all the analysis will be generated in separate lines\n\
#if you want to generate only most appropriate analysis, run the script - thamizhi-morph-pos.py \n\
#-------------------------------\n")
                   

#data_input = filter(lambda x: not x.isspace(), data_input)
for data_unit in data_input:     
        doc = nlp(data_unit.replace("-", " - ").replace("("," ( ").replace(")"," ) "))
        #print(doc.text)
        for sent in doc.sentences :
                #this is to print the sentence text 1st
                morph_tagged.write("\n #sentence or clause = " + sent.text + "\n")
                #initialing word count, this will be reset when start a new sentence
                word_id=1
                #iterate for each word of a sentence
                for word in sent.words :
                        analysis_success=0
                        #All the Puncts are marked here with PUNCT. There are no analysis for PUNCT from ThamizhiMorph
                        if word.text in punct_json:
                                morph_tagged.write(str(word_id) + "\t" + word.text + "\t" + "PUNCT" + "\t"+ word.text + "\t" + punct_json[word.text] + "\n")
                        #All numeric will take default annotations given by the POS tagger
                        elif word.text.isnumeric() :
                                morph_tagged.write(str(word_id) + "\t" + word.text + "\t" +  "NUM" + "\t"+ word.text + "\t" + "NUM" "\n")
                        elif isEnglish(word.text) == 1 :
                                morph_tagged.write(str(word_id) + "\t" + word.text + "_" + "\t" +  "_" + "\t" + "Non-Tamil-Text" + "\n")
                        else:
                                #if a word is found in lexicons
                                analyses = find_morphemes(word.text.strip(),fsts)
                                analysis_success=analyses
                                if analyses != 0 :
                                        for each_analysis in analyses:
                                                lemma=""
                                                lables=""
                                                pos=""                                                
                                                counter=0
                                                #print(len(analyses))
                                                #morph_tagged.write(",".join(each_analysis)+"\n")
                                                for analysis in each_analysis:
                                                        
                                                        #In the analysis, 1st what we get is lemma
                                                        #second would be the POS category
                                                        #3rd would be the analysis
                                                        if counter==0:
                                                                lemma=analysis
                                                        elif counter==1:
                                                                pos=analysis
                                                        else:
                                                                lables=lables+","+analysis
                                                        counter=counter+1
                                                morph_tagged.write(str(word_id) + "\t" + word.text + "\t" + pos + "\t" + lemma + "\t" +  '-'.join(list(set(lables.split(","))))  + "\n")
                                        
                                #if the given word is not found in lexicons, in this cases gussers will be applied
                                else:
                                        #here it is assumed that UPOS is correct, and a guesser is chosen based on the UPOS

                                        gusses = guess_morphemes(word.text.strip(),gussers)
                                        analysis_success=gusses
                                        if gusses != 0 :
                                                for each_guess in gusses:
                                                        counter=0
                                                        lemma=""
                                                        lables=""
                                                        pos=""
                                                        #morph_tagged.write(",".join(each_guess)+"\n")
                                                        for analysis in each_guess:
                                                                
                                                                #print(analysis)
                                                                if counter==0:
                                                                        lemma=analysis
                                                                        
                                                                elif counter==1:
                                                                        pos=analysis
                                                                else:
                                                                        lables=lables+","+analysis
                                                                counter=counter+1
                                                        morph_tagged.write(str(word_id) + "\t" + word.text + "\t" + pos + "\t" + lemma+ "\t" +  '-'.join(list(set(lables.split(","))))  + "\n")
                                        else:
                                                if lables=="":
                                                        lables="_"
                                                morph_tagged.write(str(word_id) + "\t" + word.text + "\t" + "UNKNOWN" + "\t" + "UNKNOWN"+ "\t" +  "UNKNOWN"  + "\n")
                        #morph_tagged.write("\n")                
                        #this is a word counter
                        #if(analysis_success !=0) :
                        word_id=word_id+1
morph_tagged.write("\n \n #This is tagged file was annotated using ThamizhiMorph morphological analyser \
#Please site us if you are using this data. \n \
#Sarveswaran, K, Gihan Dias, 2020, December. ThamizhiUDp: A Dependency Parser for Tamil. In Proceedings of the 17th International Conference on Natural Language Processing (ICON-2020). \n \
#for more information: http://nlp-tools.uom.lk/thamizhi-morph/ \n \
#Generated on "+ str(datetime.datetime.now()) +" \n")
morph_tagged.close()

