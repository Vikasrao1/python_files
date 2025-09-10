# working with spreadsheet CSV files
import csv
data = open('example.csv', encoding= 'utf-8')
# csv reader
csv_data = csv.reader(data)

#reformat into a python object list of lists
data_lines = list(csv_data)
print(data_lines[0])
print(len(data_lines))
for line in data_lines[:5]:                        # extract rows
    print(line)
print(data_lines[10][3])                           # extract email from rows

all_emails=[]
for line in data_lines[1:]:
    all_emails.append(line[3])                     # take email column 
    print(all_emails)

full_names=[]
for line in data_lines[1:]:
    full_names.append(line[1]+'' +line[2])         # concatenate 
print(full_names)

#write to a csv
file_to_output = open('to_save_file.csv', mode='w', newline='')
csv_writer = csv.writer(file_to_output, delimiter=',')
result = csv_writer.writerow(['a', 'b', 'c']) 
file_to_output.close()
print(result)