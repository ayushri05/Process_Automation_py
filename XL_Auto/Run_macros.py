import os
import os.path
import win32com.client as ws


def macro_run():
    if os.path.exists("Excel_Automation_05-10-2020_n.xlsm"):
        #xl = win32com.client.Dispatch('Excel.Application')
        xl = ws.Dispatch("Excel.Application")
        xl.Workbooks.Open(os.path.abspath(
            "Excel_Automation_05-10-2020_n.xlsm"))
    # ActiveSheet.Name = 'process steps'
        xl.Application.Run(
            "Excel_Automation_05-10-2020_n.xlsm!Module1.Copy_to_zuoraencompass")

        xl.Application.Run(
            "Excel_Automation_05-10-2020_n.xlsm!Module1.Save_And_Make_zuoraenc_txt")

        xl.Application.Run(
            "Excel_Automation_05-10-2020_n.xlsm!Module1.Save_And_Make_dl1charge_csv")
        xl.Application.Save()
        xl.Application.Quit()


macro_run()
