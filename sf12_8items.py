
import pandas as pd
from score_calculator.sf12_score import SF12Score
import csv
import pandas as pd


file_path = 'examples/example.csv'

score_instance = SF12Score(file_path)
answers = score_instance.load_answers()
# Sample data for 3 respondents
data = pd.DataFrame({
    'GH1':  [5, 3, 2, 1],
    'PF02': [2, 1, 3, 3],
    'PF04': [1, 2, 2, 3],
    'RP2':  [1, 2, 1, 2],
    'RP3':  [2, 1, 1, 2],
    'RE2':  [1, 2, 2, 2],
    'RE3':  [2, 1, 1, 2],
    'BP2':  [3, 4, 2, 1],
    'MH3':  [4, 5, 6, 1],
    'VT2':  [3, 2, 5, 1],
    'MH4':  [2, 3, 1, 6],
    'SF2':  [1, 3, 4, 5]
})


# Iterate in dataframe and convert to a map 
answers.columns = [col.upper() for col in answers.columns]
data = answers.to_dict(orient='records')
print(data)
avg_psc = 0
avg_mcs = 0
f_data = []
for d in data:
    d = pd.DataFrame(d, index=[0])
    d = d.to_dict(orient='records')[0]
    print(d)
    (PCS, MCS, DOMS) = score_instance.sf12_v2(d)
    print (PCS, MCS)
    avg_mcs += MCS
    avg_psc += PCS
    DOMS['PCS'] = PCS
    DOMS['MCS'] = MCS
    f_data.append(DOMS)

print("Average PCS: ", avg_psc/len(data))
print("Average MCS: ", avg_mcs/len(data))


filename = "_ex1.csv"

with open(filename, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=f_data[0].keys())

    writer.writeheader()

    writer.writerows(f_data)

print(f"CSV file '{filename}' created successfully!")
