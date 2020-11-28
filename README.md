# Process_Automation_py
The process to automate Shipment flow using Python script.

The project is created with the purpose of automating the complete Shipment flow. 
The file 'main.py' import all the files in order to automate the complete flow sequentially.
The flow includes - 

1.Fetching data from Zuora -
The data is extracted using Zconnect APIs. This Automation is completed using 'Auto_async.py' file. The program is developed using various Python libraries like - asyncio, aiohttp, sys etc.

2.Processing the data in our local system
The extracted data pasted into the target file. Target file contain various formulas, filters and Macros. This automation is done using 'XL_Automatic.py' file. The program is developed using various Python libraries like - openpyxl , codecs, and csv.

3.Filter out required information which needs to be shared for order delivery. Then Run macros for creating final files.
Two separate sheets created for transfering to delivery team(a text file) and uploading back to Zconnect(a csv file) respectively. The required data is seprated out using macros. This is done using 'Run_macros.py' file. 
The program is developed using various Python libraries like - os, win32com etc.

4.Transfer the required data to respective delivery team securely using Secure File transfer protocol.
In this step, the text file created in above step is uploaded to the target server of delivery team. This is completed using 'sftp_fileShare.py' file.
This is developed using Python library -'pysftp'

5.Update the order status in the Zuora system using Workflows.
Now the data present in our system is updated with the correct status. This is achieved using UI Automation using Selenium webdriver. 
This section is developed using mainly 2 Python libraries - Selenium webdriver and win32api

