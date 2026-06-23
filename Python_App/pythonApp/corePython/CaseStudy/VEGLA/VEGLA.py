import csv
import re
from datetime import datetime
from collections import Counter
class VehicleLogAuditor:

    def __init__(self):
        self.clean_records = []
        self.duplicate_records = []
        self.suspicious_records = []
        self.rejected_records = []



    def validate_vehicle(self, vehicle_no):

        pattern = r"^WB\d{2}[A-Z]{2}\d{4}$"
    
        if re.match(pattern, vehicle_no):
            return True
    
        return False



    def validate_device(self, device):

        pattern = r"^DEV\d{3}$"
    
        if re.match(pattern, device):
            return True
    
        return False



    def validate_time(self, scan_time):

        try:
            datetime.strptime(scan_time,
                              "%d-%m-%Y %H:%M:%S")
            return True
    
        except:
            return False




    def read_file(self, filename):

         with open(filename, "r") as file:
     
             reader = csv.DictReader(file)
     
             for row in reader:
     
                 vehicle = row["vehicle_no"]
                 device = row["security_device"]
                 scan_time = row["scan_time"]
     
                 if not self.validate_vehicle(vehicle):
                     self.rejected_records.append(row)
                     continue
     
                 if not self.validate_device(device):
                     self.rejected_records.append(row)
                     continue
     
                 if not self.validate_time(scan_time):
                     self.rejected_records.append(row)
                     continue
     
                 self.clean_records.append(row)






    def find_duplicates(self):

        checked = []
    
        for record in self.clean_records:
    
            vehicle = record["vehicle_no"]
            scan_type = record["scan_type"]
            device = record["security_device"]
    
            current_time = datetime.strptime(
                record["scan_time"],
                "%d-%m-%Y %H:%M:%S"
            )
    
            duplicate = False
    
            for old_record in checked:
    
                old_time = datetime.strptime(
                    old_record["scan_time"],
                    "%d-%m-%Y %H:%M:%S"
                )
    
                diff = abs(
                    (current_time - old_time).total_seconds()
                )
    
                if (
                    vehicle == old_record["vehicle_no"]
                    and scan_type == old_record["scan_type"]
                    and device == old_record["security_device"]
                    and diff <= 45
                ):
    
                    self.duplicate_records.append(record)
                    duplicate = True
                    break
    
            if not duplicate:
                checked.append(record)




    def find_suspicious(self):

         for i in range(len(self.clean_records)):
     
             for j in range(i + 1,
                            len(self.clean_records)):
     
                 r1 = self.clean_records[i]
                 r2 = self.clean_records[j]
     
                 if r1["vehicle_no"] == r2["vehicle_no"]:
     
                     if r1["gate_code"] != r2["gate_code"]:
     
                         t1 = datetime.strptime(
                             r1["scan_time"],
                             "%d-%m-%Y %H:%M:%S"
                         )
     
                         t2 = datetime.strptime(
                             r2["scan_time"],
                             "%d-%m-%Y %H:%M:%S"
                         )
     
                         minutes = abs(
                             (t1 - t2).total_seconds()
                         ) / 60
     
                         if minutes <= 30:
     
                             self.suspicious_records.append(r2)




    def generate_report(self):
    
        vehicle_count = Counter()
    
        # Count all records
        for record in (
            self.clean_records
            + self.duplicate_records
            + self.suspicious_records
            + self.rejected_records
        ):
            vehicle_count[record["vehicle_no"]] += 1
    
        total_records = (
            len(self.clean_records)
            + len(self.duplicate_records)
            + len(self.suspicious_records)
            + len(self.rejected_records)
        )
    
        with open("audit_summary.txt", "w") as file:
    
            file.write("Vehicle Gate Log Audit Report\n")
            file.write("----------------------------------\n\n")
    
            file.write(f"Total Records : {total_records}\n")
            file.write(f"Clean Records : {len(self.clean_records)}\n")
            file.write(f"Duplicate Records : {len(self.duplicate_records)}\n")
            file.write(f"Suspicious Records : {len(self.suspicious_records)}\n")
            file.write(f"Rejected Records : {len(self.rejected_records)}\n\n")
    
            file.write("Vehicle Wise Summary\n")
            file.write("-------------------------\n")
    
            for vehicle, count in vehicle_count.items():
                file.write(f"{vehicle} : {count} scans\n")
    
        print("audit_summary.txt generated successfully")




    def save_clean_records(self):

         with open("clean_records.csv", "w", newline="") as file:
     
             if self.clean_records:
     
                 writer = csv.DictWriter(
                     file,
                     fieldnames=self.clean_records[0].keys()
                 )
     
                 writer.writeheader()
                 writer.writerows(self.clean_records)
     
         print("clean_records.csv created successfully")


    def save_rejected_records(self):

         with open("rejected_records.csv", "w", newline="") as file:
     
             if self.rejected_records:
     
                 writer = csv.DictWriter(
                     file,
                     fieldnames=self.rejected_records[0].keys()
                 )
     
                 writer.writeheader()
                 writer.writerows(self.rejected_records)
     
         print("rejected_records.csv created successfully")



def main():
    auditor = VehicleLogAuditor()

    auditor.read_file("raw_vehicle_logs.csv")
    
    auditor.find_duplicates()
    
    auditor.find_suspicious()
    
    auditor.generate_report()
    auditor.save_clean_records()
    auditor.save_rejected_records()
if __name__ == "__main__":
    main()