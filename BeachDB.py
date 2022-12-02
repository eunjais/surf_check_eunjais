import csv, sys

class BeachDB:

    # constructor
    def __init__(self, data = []):
        self.db_beaches = self.__read_ca_beaches_csv()

    # get beaches
    def get_beaches(self):
        return self.db_beaches

    
    # search beach name from db list
    def search_beaches(self, beach_name):
        result = []
        # if beach name is not supplied
        if not beach_name or beach_name == '':
            return result
        # convert all strings to lowercase
        search_text = beach_name.lower()
        for line in self.db_beaches:
            record_name = line['beach_name'].lower()
            # append to result list if matches
            if record_name.find(search_text) != -1:
                result.append(line)
        return result

    # get all ca beaches from csv
    def __read_ca_beaches_csv(self):
        data = []
        try:
            with open('ca_beaches.csv', encoding='utf-8') as ca_beaches_csv:
                csv_lines = csv.DictReader(ca_beaches_csv)
                for lines in csv_lines:
                    data.append(lines)
        except Exception as e:
            print(str(e))
            sys.exit(1)
        return data
