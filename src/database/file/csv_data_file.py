import csv
from .data_file import DataFile


class CSVDataFile(DataFile):
    def __output(self, record):
        """
        Inject uuid to record

        :param record: Record
        :return: Injected record
        """
        return {field: record[field_id] for field_id, field in enumerate(self.fields)}

    def load(self):
        with open(self.filename, 'r') as f:
            yield from map(self.__output, csv.reader(f))

    def save(self, data):
        with open(self.filename, 'w') as f:
            writer = csv.writer(f)
            for record in data:
                writer.writerow(record)
