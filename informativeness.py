import pandas as pd
from collections import Counter
import csv
import numpy as np
import pprint
import json

pp = pprint.PrettyPrinter(indent=4)

def write_data(arrayed,name):
    with open(name,mode="w",encoding="utf-8",newline="") as f:
        writer = csv.writer(f)
        writer.writerows(arrayed)

def import_dictionary(name):
    dictionary_csv = list(csv.reader(open(name)))
    word_dict={}
    for line in dictionary_csv:
        arr = line
        word = arr[0]
        val = int(arr[1])
        word_dict[word] = val
    return word_dict

word_dict = import_dictionary("hsp_voc.csv")

df = pd.read_csv("./exp200_full_unfilt_02-12-2020.csv",encoding="utf-8")


r_data = [["verb1","prop1","verb2","prop2","verb2_id","trial"]]
matdata = [["verb1","prop1","verb2","prop2"]]


verb_pairs = ["build","stack","turn","twist","spin","shake","put",'hold',"hit",'fall',"drop","throw","touch","point","cut","saw","push","press","reach","grab","give","take","drive","move","pick",'place']
verb_dict = {}
trial_dict = {}
#print(verb_pairs)
#print(df["guess"])
#counte = 0
for verb in verb_pairs:
    #print("\t"+verb)
    trials = df.loc[df["guess"]==verb]["trial"].values
    for trial in trials:
        guesses = df.loc[df["trial"]==trial]["guess"].values
        guesses = Counter(guesses)
        guesses.pop(np.nan,None)
        amt= sum(guesses.values())
        #print(guesses)
        if amt >4:
            #print(trial)
            #counte +=1
            trial_dict[trial] = guesses
            #print(guesses)
            #print(list(guesses.keys())[0])
            if guesses[verb] != amt:
                #print(list(guesses.most_common(2)[0]))
                second_v = list(guesses.most_common(2)[0])[0]
                second_count = list(guesses.most_common(2)[0])[1]
                if second_v == verb:
                    second_v = list(guesses.most_common(2)[1])[0]
                    second_count = list(guesses.most_common(2)[1])[1]
            else:
                second_v = "N/A"
                second_count = 0
            #print(guesses.values())
            #print(max(guesses,key=lambda key: guesses[key]))
            #print(verb, guesses[verb]/amt)
            #print(second_v,second_count/amt)
            #print(guesses)
            #print(guesses.count(verb))
            if guesses[verb]/amt > 1:
                print(trial)
                print(guesses)
                print(guesses[verb])
                print(amt)
            r_data.append([verb, guesses[verb]/amt,second_v,second_count/amt,word_dict[second_v],trial])
            matdata.append([word_dict[verb], guesses[verb]/amt,word_dict[second_v],second_count/amt])

            if verb not in verb_dict:
                verb_dict[verb] = {"A":[],"B":[],"C":[]}

            if guesses[verb]/amt >= 0.66 and second_count/amt <= 0.33:
                verb_dict[verb]["A"].append([verb, guesses[verb]/amt,second_v,second_count/amt,word_dict[second_v],trial])

            elif guesses[verb]/amt < 0.33 and second_count/amt <= 0.66:
                verb_dict[verb]["B"].append([verb, guesses[verb]/amt,second_v,second_count/amt,word_dict[second_v],trial])

            elif guesses[verb]/amt >= 0.33 and second_count/amt >= 0.33 and guesses[verb]/amt < 0.66 and second_count/amt <0.66:
                verb_dict[verb]["C"].append([verb, guesses[verb]/amt,second_v,second_count/amt,word_dict[second_v],trial])

            #print()
    #print()

with open("type_ABC_vids.json","w") as json_file:
    json.dump(verb_dict,json_file)

#write_data(r_data,"r-data_12-2.csv")
#write_data(matdata,"mat-data_12-2.csv")
