# Dependencies
import os 
import csv
import moment 
import random 
from datetime import datetime
csv_path=('resources', '//Users/sabalemma/Python/Resources/HW3budget_data_1.csv')
total_num_months = 42
current_date = moment.date("01-01-2018", "M-D-YYYY")
starting_date = current_date.add(months=-num_months)
gain_loss_weights = [0.85, 0.15]
range_revenue = [50000, 1200000]
tracked_months = []
current_month = starting_date
revenues = []
for x in range(0, num_months + 1):
    current_month = current_month.add(month=1)
    current_month_string = current_month.date.strftime("%b-%Y")
    tracked_months.append(current_month_string)
    random_revenue = random.randrange(range_revenue[0], range_revenue[1])
    revenues = revenues + [random_revenue]
neg_months = int(num_months * gain_loss_weight[1]
for x in range(neg_months):
    revenues[x] = -1 * revenues[x]
random.shuffle(revenues)
fin_data = zip(tracked_months, revenues)
file_output_name = "/Users/sabalemma/Python/Resources/pybankO.csv"
output_path=os.path.join('output', '/Users/sabalemma/Python/Resources/pybankO.csv')
print(fin_data)
with open(file_output_name, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Date", "Revenue"])
    writer.writerows(fin_data)

