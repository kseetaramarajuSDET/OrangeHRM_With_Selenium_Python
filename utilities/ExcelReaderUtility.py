import openpyxl
import os


class ExcelReader:
    @staticmethod
    def get_data_from_excel(file_name, sheet_name):
        """
        Reads data rows from a specific Excel sheet and returns a list of tuples.
        Excludes the header row automatically.
        """
        # Build the exact absolute path to the test data file
        # Assumes your data file sits inside a 'testData' folder at project root
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "test-data", file_name))

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Excel data sheet not found at path: {file_path}")

        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook[sheet_name]

        data_list = []

        # Iterate over all rows starting from row 2 to completely skip the headers
        for row in sheet.iter_rows(min_row=2, values_only=True):
            # Ensure the row isn't empty before adding it to our test data pool
            if any(row):
                data_list.append(row)

        return data_list
