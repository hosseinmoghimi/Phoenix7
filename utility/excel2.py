import pandas as pd
class Excel():
    def __init__(self,origin_file_name=None,origin_file=None,*args, **kwargs):
        if origin_file_name is not None:
            df = pd.read_excel(origin_file_name)
        if origin_file is not None:
            df = pd.read_excel(origin_file)
        print(df)
        # self.sheets=[]
        # self.origin_file_name=origin_file_name
        # self.sheet_counter=0

        # if self.origin_file_name is None:
        #     self.work_book = Workbook()
        #     for sheet in self.sheets:
        #         self.work_book.create_sheet(sheet.sheet_name)
        # else:
        #     REPORT_ROOT=os.path.join(STATIC_ROOT,'report')
        #     filename =os.path.join(REPORT_ROOT,self.origin_file_name)   
        #     # filename =os.path.join(STATIC_ROOT,self.origin_file_name)      
        #     self.work_book = load_workbook(filename = filename)
            
    def to_data_table(self):
        pass
