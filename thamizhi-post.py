#this script generate pos tags using
#thamizhiPOSt http://nlp-tools.uom.lk/thamizhi-pos/
#Developed by K. Sarveswaran, sarves@cse.mrt.ac.lk
#National Languages Processing Centre, University of Moratuwa, Sri lanka
#version-2020-12-001

import stanza
import sys
import datetime

f1=open(str(sys.argv[1]),"r")
       
config = {
	'processors': 'tokenize,pos', # Comma-separated list of processors to use
	'lang': 'ta', # Language code for the language to build the Pipeline in
	'tokenize_model_path': './models/ta_ttb_tokenizer.pt', 
	'pos_model_path': './models/ta_amr_tagger.pt',
	'pos_pretrain_path': './models/ta_amr.pretrain.pt',
}
nlp = stanza.Pipeline(**config)
pos_tagged=open("./pos-tagged-sentence.txt","w")
x=f1.read()
doc = nlp(x)


pos_tagged.write("#This is annotated using ThamizhiPOSt. \n \
#Please site us if you are using this data. \n \
#Sarveswaran, K, Gihan Dias, 2020, December. ThamizhiUDp: A Dependency Parser for Tamil. In Proceedings of the 17th International Conference on Natural Language Processing (ICON-2020). \n \
#for more information: http://nlp-tools.uom.lk/thamizhi-pos/ \n \
#Generated on "+ str(datetime.datetime.now()) +" \n")


for sent in doc.sentences :
        for word in sent.words :
                pos_tagged.write("\n" + word.text + "\\" + word.upos+ " ")
pos_tagged.close()
f1.close()
