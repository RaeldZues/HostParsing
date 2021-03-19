import pandas as pd
import os

"""
This is the NSRL diffing tool.
This only does one at a time. May need to add in the i.find and loop through all to scale?
This will take two single column files and tell you the non matches between the two
Flow: lines in File 1 compared to lines in File2; if file2 lines do not match print out to csv
"""


def nsrl_diff():
    for file in os.listdir(path):
        print('YOU ARE NOW USING NSRL DIFF')
        print(file)
        filename = eval(file)
        print(filename)
        collected_df = pd.read_csv(file, encoding='iso-8859-1')
        collected_df = collected_df['hash']
        collected_df.to_csv(collected_nsrl % (file.strip('.csv'), file), header='hash')
        # Ensure to set the collectedHashes variable as your unique list of hashes between the system you collected
        collected_hashes = set(line.strip() for line in open(file).readlines())
        pwd = os.getcwd()
        # Ensure this is the sorted unique version of the nsrl list you are comparing against MD5 or SHA1 only the hashes
        with open(r'./nsrl/sorted.txt') as f:
            for line in f:
                if line in collected_hashes:
                    collected_hashes.discard(line.strip())

        # This puts everything in a dataframe for processing afterwords
        df = pd.DataFrame(list(collected_hashes))
        # This is where we take the data and print/export/compare
        df = df.applymap(lambda x: x.split(',')[-1])
        df = df.sort_values(by=0, ascending=True)
        df.to_csv(os.path.join(pwd, './nsrl/output/%s.csv' % ()))

if __name__ == "__main__":
    nsrl_diff()
