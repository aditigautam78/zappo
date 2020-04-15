import json
import pandas as pd
from web.preprocessor.trp import Document
from web.preprocessor.utils import update_column_headers, convert_form_to_dict
from web.preprocessor.orders import Order
from web.preprocessor.orderitems import OrderitemsDF
pd.set_option('max_columns', 12)

def processDocument(doc):
    for page in doc.pages:
    #     print("PAGE\n====================")
    #     for line in page.lines:
    #         print("Line: {}--{}".format(line.text, ' '))
    #         for word in line.words:
    #             print("Word: {}--{}".format(word.text, ' '))
    #     for table in page.tables:
    #         print("TABLE\n====================")
    #         for r, row in enumerate(table.rows):
    #             for c, cell in enumerate(row.cells):
    #                 print("Table[{}][{}] = {}-{}".format(r, c, cell.text, ' '))
    #     print("Form (key/values)\n====================")
    #     print('*'*20)
    #     for field in page.form.fields:
    #         k = ""
    #         v = ""
    #         if(field.key):
    #             k = field.key.text
    #         if(field.value):
    #             v = field.value.text
    #         print("Field: Key: {}, Value: {}".format(k,v))

    #     #Get field by key
    #     key = "Phone Number:"
    #     print("\nGet field by key ({}):\n====================".format(key))
    #     f = page.form.getFieldByKey(key)
    #     if(f):
    #         print("Field: Key: {}, Value: {}".format(f.key.text, f.value.text))


        #Search field by key
        # key = "CUSTOMER ACCOUNT NO."

        # fields = page.form.searchFieldsByKey(key)
        # print(page.form)
        # for field in fields:
        #     print("Field: Key: {}, Value: {}".format(field.key, field.value))

        # Turning invoice line items into a DF
        for table in page.tables:
            try:
                orderitems = OrderitemsDF()
                orderitems.set_orderitems_dataframe(table)
                df = orderitems.TableDataFrame
                if len(df) == 0:
                    continue
                orderitems.convert_DF_to_Orderitem_objs()

                return orderitems._TableDataFrame.to_dict()
            except KeyError:
                break

        # order = Order()
        # order.set_order_values(page)

        # df = pd.DataFrame([[cell.text for cell in row.cells] for row in page.tables[0].rows])
        # orders_df = update_column_headers(df)
        # print(orders_df.head())
        # print(orders_df.columns)
        # print([line.text for line in page.lines])
        # print(orders_df.head())
        return 






def run():
    response = {}
    
    filePath = "../data/s3_responses/04eed195-04b7-40bd-a304-2609b8fd2db3.json" # <- First response we worked with
    # filePath = "../data/s3_responses/INV_044_17165_709955_20191106.PDF_0.png.json" # <- PDF response (1 of 4)
    # filePath = "../data/s3_responses/INV_044_17165_709955_20191106.PDF_1.png.json" # <- PDF response (2 of 4)
    # filePath = "../data/s3_responses/INV_044_17165_709955_20191106.PDF_2.png.json" # <- PDF response (3 of 4)
    # NEW RESPONSES
    # filePath = "../data/s3_responses_sysco/20191103_193232.jpg.json"
    # filePath = "../data/s3_responses_sysco/20191103_193336.jpg.json"
    # filePath = "../data/s3_responses_sysco/20191103_193346.jpg.json"
    # filePath = "../data/s3_responses_sysco/20191103_193354.jpg.json"
    # filePath = "../data/s3_responses_sysco/20191103_193403.jpg.json"
    # filePath = "../data/s3_responses_sysco/sysco_test_INV_044_17165_709955_20191106-1.png.json"
    # filePath = "../data/s3_responses_sysco/sysco_test_INV_044_17165_709955_20191106-2.png.json""
    # filePath = "../data/s3_responses_sysco/sysco_test_INV_044_17165_709955_20191106-3.png.json"
    # filePath = "../data/s3_responses_sysco/sysco_test_INV_044_17165_709955_20191106-4.png.json"
    # filePath = "../data/s3_responses_sysco/sysco_test_INV_044_17165_741819_20191130-1.png.json"
    # filePath = "../data/s3_responses_sysco/sysco_test_INV_044_17165_741819_20191130-2.png.json"
    # filePath = "../data/s3_responses_sysco/sysco_test_INV_044_17165_741819_20191130-3.png.json"
    # filePath = "../data/s3_responses_sysco/sysco_test_INV_044_17165_741819_20191130-4.png.json"
    # filePath = "../data/s3_responses_sysco/sysco_test_INV_044_17165_741819_20191130-5.png.json"
    # filePath = "../data/s3_responses_sysco/sysco_test_INV_044_17165_744788_20191203-1.png.json"
    # filePath = "../data/s3_responses_sysco/sysco_test_INV_044_17165_744788_20191203-2.png.json"
    # filePath = "../data/s3_responses_sysco/sysco_test_INV_044_17165_744788_20191203-3.png.json"
    # filePath = "../data/s3_responses_sysco/sysco_test_INV_044_17165_744788_20191203-4.png.json"
    # filePath = "../data/s3_responses_sysco/sysco_test_INV_044_17165_750415_20191206-1.png.json"
    # filePath = "../data/s3_responses_sysco/sysco_test_INV_044_17165_750415_20191206-2.png.json"
    # filePath = "../data/s3_responses_sysco/sysco_test_INV_044_17165_750415_20191206-3.png.json"
    # filePath = "../data/s3_responses_sysco/sysco_test_INV_044_17165_750415_20191206-4.png.json"
    # filePath = "../data/s3_responses_sysco/sysco_test_INV_044_20677_709755_20191106-1.png.json"
    # filePath = "../data/s3_responses_sysco/sysco_test_INV_044_20677_725235_20191119-1.png.json"
    # filePath = "../data/s3_responses_sysco/sysco_test_INV_044_20677_725235_20191119-2.png.json"
    # filePath = "../data/s3_responses_sysco/sysco_test_INV_044_20677_725235_20191119-3.png.json"
    # filePath = "../data/s3_responses_sysco/sysco_test_INV_044_20677_746612_20191204-1.png.json"
    # filePath = "../data/s3_responses_sysco/sysco_test_INV_044_20677_746612_20191204-2.png.json"
    # filePath = "../data/s3_responses_sysco/sysco_test_INV_044_20677_746612_20191204-3.png.json"
    # filePath = "../data/s3_responses_sysco/sysco_test_INV_044_20677_746612_20191204-4.png.json"
    # filePath = "../data/s3_responses_sysco/sysco_test_INV_044_23905_709646_20191106-1.png.json"
    # filePath = "../data/s3_responses_sysco/sysco_test_INV_044_23905_709646_20191106-2.png.json"
    # filePath = "../data/s3_responses_sysco/sysco_test_INV_044_23905_709646_20191106-3.png.json"
    # filePath = "../data/s3_responses_sysco/sysco_test_INV_044_23905_725646_20191119-1.png.json"
    # filePath = "../data/s3_responses_sysco/sysco_test_INV_044_23905_725646_20191119-2.png.json"
    # filePath = "../data/s3_responses_sysco/sysco_test_INV_044_23905_725646_20191119-3.png.json"
    # filePath = "../data/s3_responses_sysco/sysco_test_INV_044_23905_725646_20191119-4.png.json"
    # filePath = "../data/s3_responses_sysco/sysco_test_INV_044_23905_748631_20191205-1.png.json"
    # filePath = "../data/s3_responses_sysco/sysco_test_INV_044_23905_748631_20191205-2.png.json"
    # filePath = "../data/s3_responses_sysco/sysco_test_INV_044_23905_748631_20191205-3.png.json"
    # filePath = "../data/s3_responses_sysco/sysco_test_INV_044_23905_748631_20191205-4.png.json"
    # filePath = "../data/s3_responses_sysco/sysco_test_INV_044_28773_750236_20191206-1.png.json"
    # filePath = "../data/s3_responses_sysco/sysco_test_INV_044_28773_750236_20191206-2.png.json"
    # filePath = "../data/s3_responses_sysco/sysco_test_INV_044_28773_750236_20191206-3.png.json"
    # filePath = "../data/s3_responses_sysco/sysco_test_INV_044_28773_750236_20191206-4.png.json"
    with open(filePath, 'r') as document:
        response = json.loads(document.read())

    doc = Document(response)
    processDocument(doc)

if __name__ == '__main__':
    run()
