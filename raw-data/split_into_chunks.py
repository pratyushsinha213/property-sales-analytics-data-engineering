import csv

def split_large_file_into_chunks(file_path, lines_per_file=20000):
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)

        file_count = 1
        lines = []
        for i, row in enumerate(reader, start=1):
            lines.append(row)
            if i % lines_per_file == 0:
                if file_count < 10:
                    with open(f'data_0{file_count}.csv', 'w', newline='', encoding='utf-8') as chunk_file:
                        writer1 = csv.writer(chunk_file)
                        writer1.writerow(header)
                        writer1.writerows(lines)
                else:
                    with open(f'data_{file_count}.csv', 'w', newline='', encoding='utf-8') as chunk_file:
                        writer2 = csv.writer(chunk_file)
                        writer2.writerow(header)
                        writer2.writerows(lines)
                lines = []
                file_count += 1

        # Write remaining lines
        if lines:
            with open(f'data_{file_count}.csv', 'w', newline='', encoding='utf-8') as chunk_file:
                writer = csv.writer(chunk_file)
                writer.writerow(header)
                writer.writerows(lines)

if __name__ == '__main__':
    split_large_file_into_chunks('./raw-data/global_house_purchase_dataset.csv')