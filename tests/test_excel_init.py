import unittest
import openpyxl as xl
class TestExcelInit(unittest.TestCase):
    def test_excel_init(self):
        wb = xl.Workbook()
        ws = wb.active
        ws['A1'] = 10
        wb.save("test.xlsx")

if __name__ == "__main__":
    unittest.main()