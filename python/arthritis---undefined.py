# phekb, 2024.

import sys, csv, re

codes = [{"code":"716.4","system":"ICD9 Diagnosis"},{"code":"716.48","system":"ICD9 Diagnosis"},{"code":"7.165","system":"ICD9 Diagnosis"},{"code":"716.8","system":"ICD9 Diagnosis"},{"code":"716.88","system":"ICD9 Diagnosis"},{"code":"716.89","system":"ICD9 Diagnosis"},{"code":"7.169","system":"ICD9 Diagnosis"},{"code":"719","system":"ICD9 Diagnosis"},{"code":"719.08","system":"ICD9 Diagnosis"},{"code":"719.49","system":"ICD9 Diagnosis"},{"code":"7.196","system":"ICD9 Diagnosis"},{"code":"719.8","system":"ICD9 Diagnosis"},{"code":"719.88","system":"ICD9 Diagnosis"},{"code":"719.89","system":"ICD9 Diagnosis"},{"code":"7.199","system":"ICD9 Diagnosis"},{"code":"V13.4","system":"ICD9 Diagnosis"},{"code":"M12.80","system":"ICD9 Diagnosis"},{"code":"M12.88","system":"ICD9 Diagnosis"},{"code":"M12.89","system":"ICD9 Diagnosis"},{"code":"M13.0","system":"ICD9 Diagnosis"},{"code":"M25.40","system":"ICD9 Diagnosis"},{"code":"M25.48","system":"ICD9 Diagnosis"},{"code":"M25.50","system":"ICD9 Diagnosis"},{"code":"M25.9","system":"ICD9 Diagnosis"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('arthritis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["arthritis---undefined-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["arthritis---undefined-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["arthritis---undefined-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
