import os
from collections import OrderedDict
import csv
import argparse

#packet_analyzer class can red and analyze websites visited
class packet_analyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        csv_file  =open(file_path,'r')
        self.csv_reader = csv.DictReader(csv_file)
        self.freq_dict = {

        }
        self.duration_dict = {

        }

        self.freq_dict = {

        }

        #for row in csv_reader:
            #print(type(row))
         #   print(row)

    def get_freq_dict(self):
            self.freq_dict.clear()
            for row in self.csv_reader:
                if row["Address B"] not in self.freq_dict:
                    self.freq_dict[row["Address B"]] = 1
                else:
                    self.freq_dict[row["Address B"]] += 1
            

    def get_duration_dict(self):
            self.duration_dict.clear()
            for row in self.csv_reader:
                if row["Duration"] not in self.freq_dict:
                    self.duration_dict[row["Address B"]] = row["Duration"]
                else:
                    self.duration_dict[row["Address B"]] += row["Duration"]
            

    def get_3_most_freq_ip(self):
            #v = list(self.freq_dict.values())
            #k = list(self.freq_dict.keys())
            #return k[v.index(max(v))]
            self.freq_value_to_ip = {

            }
            for keys in self.freq_dict:
                self.freq_value_to_ip[self.freq_dict[keys]] = keys
            
        
    def get_3_most_duration_ip(self):
            #v = list(self.duration_dict.values())
            #k = list(self.duration_dict.keys())
            #return k[v.index(max(v))]
            self.duration_value_to_ip = {

            }
            for keys in self.duration_dict:
                self.duration_value_to_ip[self.duration_dict[keys]] = keys
            

              
    def update_duration_dict(self,entry_new):
            if entry_new in self.duration_dict:
                self.duration_dict[entry_new["Address B"]]+=entry_new["Duration"]
            
            else:
                self.duration_dict[entry_new["Address B"]]=entry_new["Duration"]
        
    def update_freq_dict(self,entry_new):
            if entry_new in self.freq_dict:
                self.freq_dict[entry_new["Address B"]]+=1
            
            else:
                self.freq_dict[entry_new["Address B"]]=1

        

#main function for getting the output
    
if __name__=="__main__":
    analyzer  = packet_analyzer('tcp_udp.csv')
    parser  = argparse.ArgumentParser()
    parser.add_argument("--kind", help="it depicts most frequent website or most duration website")

    args = parser.parse_args()
    print(type(args.kind))
    
    if args.kind=="0":
        print("The 3 with maximum duration of transmission will be printed")
        analyzer.get_duration_dict()
        analyzer.get_3_most_duration_ip()
        curr_list = list(reversed(sorted(analyzer.duration_value_to_ip.keys())))
        print("IP Address                 Duration")
        print("-----------------------------------")
        for i in range(3):
            curr_duration = curr_list[i]
            curr_ip = analyzer.duration_value_to_ip[curr_duration]
            print(str(curr_ip)+"                 "+ str(curr_duration)) 
        #print(analyzer.get_most_duration_ip())
    
    else:
        print("The 3 with max frequency in CSV file will be printed")
        analyzer.get_freq_dict()
        analyzer.get_3_most_freq_ip()
        curr_list = list(reversed(sorted(analyzer.freq_value_to_ip.keys())))
        print("IP Address                 Frequency")
        print("-----------------------------------")
        #As we donot want to consider private connections and top most frequency is of our private connection so instead of i --> i+1
        for i in range(3):
            curr_freq = curr_list[i+1]
            curr_ip = analyzer.freq_value_to_ip[curr_freq]
            print(str(curr_ip)+"                 "+ str(curr_freq)) 
        #print(analyzer.get_most_freq_ip())
    
    
    