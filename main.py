import os
from datetime import datetime
from data_base_tools.database_tools import DataBaseTools


container = []
while True:
    for root, _, file_names in os.walk("test_folder"):
        for file_name in file_names:
            if file_name not in container:
                container.append(file_name)
                for plate_name in container:
                    plate_size = plate_name.split("_")[0]
                    quantity = plate_name.split("_")[1]
                    company = plate_name.split("_")[2]
                    file_name = "_".join(plate_name.split("_")[3:])
                    date_time = datetime.now().strftime("%d-%m-%Y   %H:%M:%S")
                    DataBaseTools().insert_plate_info_in_table(company, plate_size, quantity, file_name, date_time)
                    print(f"{plate_size} {quantity} {company} {file_name} {date_time}")
