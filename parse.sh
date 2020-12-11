cp $1 thamizhiudp/data-dir/UD_Tamil-TTB/ta_ttb-ud-dev.conllu
uuparser --predict --outdir thamizhiudp/output-dir --modeldir thamizhiudp/ta_ttb --datadir thamizhiudp/data-dir --testfile thamizhiudp/data-dir/UD_Tamil-TTB/ta_ttb-ud-dev.conllu --include "ta_ttb" --multiling
cp thamizhiudp/output-dir/ta_ttb/ta_ttb.conllu ud-tagged.txt
