# Packet_analyzer
This code contains the packet_analyzer class to analyze most frequently visted website by users by monitoring their traffic using wireshark.

# Running the Code
* Python is required for running the code.

* Now put the csv file obtained from wireshark in the same folder as the code and then run the following command:
```javascript
python packet_analyzing.py --filename name_of_the_csv_file --kind 1
```
* Here filename is the argument in which name of the given csv file is to be passed
* Here kind is an argument which when 1 will return most frequent websites.
* Then ip of top 3 frequent websites will be seen on the terminal.
