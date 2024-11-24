import csv

def check_and_save_csv(input_file_path, output_file_path, output_urgent):
    try:
        with open(input_file_path, mode='r', encoding='utf-8') as input_file:
            csv_reader = csv.reader(input_file)
            with open(output_file_path, mode='w', encoding='utf-8') as output_file, \
                 open(output_urgent, mode='w', encoding='utf-8') as output_urgent_file:
                csv_writer = csv.writer(output_file)
                csv_writer_urgent = csv.writer(output_urgent_file)

                for row in csv_reader:
                    if any('urgent' in entry.lower() for entry in row):
                        csv_writer_urgent.writerow(row)
                    elif all(len(entry) <= 7000 for entry in row):
                        csv_writer.writerow(row)
                    else:
                        print(f"Skipped spam row: {row[:5]}...")  # Log truncated row
    except Exception as e:
        print(f"Error processing CSV files: {e}")
