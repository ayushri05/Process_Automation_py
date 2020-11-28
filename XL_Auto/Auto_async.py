import signal
import sys
import asyncio
import aiohttp
from aiohttp import ClientSession, TCPConnector
import json
import csv
from collections import namedtuple
import time
# import pandas as pd
import requests
import settings as s

# load_dotenv()

if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

header = {
    'apiAccessKeyId': s.apiAccessKeyId,
    'apiSecretAccessKey': s.apiSecretAccessKey,
    'Content-type': s.Content_type
}
payload = {}
Config = namedtuple('Config', ['concurrency', 'duration', 'timeout'])
# df = pd.DataFrame()
# loop = asyncio.get_event_loop()

# client = aiohttp.ClientSession(loop=loop, headers=header)


async def get_json(client, url):
   # client = aiohttp.ClientSession(loop=loop, headers=header)
    async with client.get(url) as response:
        print(response.status)
        report = await response.json()
        repid = report["response"]["reports"][0]["id"]
        return repid
        # report_res = report["response"]
        # report_rep = report_res["reports"]
        # reportid = report_rep[0]["id"]


async def post_json(client, url):
    async with client.post(url, data=payload) as response:
        # response.headers['Content-Type'] = 'application/json'
        print(response.status)
        report = await response.json()
        return report["response"]["reportRunId"]


async def get_json_exp(client, url):
    # async with client.get(url) as response:
    response = await client.get(url)
    print(response.status)
    time.sleep(20)
    return await response.text()

    # print(response.status)
    # print(response.text.encode('utf8'))
    # report = response.content_disposition.filename
    # report = await response.text(encoding='utf16')
    # with open('blank.csv', 'w') as csv_file:
    #    writer = csv.DictWriter(csv_file, delimiter='\t')
    #   writer.writerow(report)

    # async with client.get(url) as response:
    # reader = aiohttp.MultipartReader.from_response(response)
   # response = await client.get(url).text
   # result = await response

   # return response

    # response = client.get(url)

    # report = response.splitlines()


async def write_result(result):
    # with open('new.txt', 'w') as txt_file:
    #   txt_file.write(result)
    # writer = csv.writer(txt_file)
    # writer.writerow(in_reader)
    # with open(txt_file, "r") as in_text:
    #   in_reader = csv.reader(in_text, delimiter='\t')
    # print(in_reader)
    with open('blank.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for row in result:
            writer.writerow(row)
    # for row in in_reader:
    #   writer.writerow(row)
    # records = result.splitlines()
    # with open('blank.csv', 'w') as csv_file:
 #   csv_file.write(result)
    # writer = csv.writer(csv_file)
    # writer.writerow(result.text)

    # for row in records:


async def get_reddit_top(config, loop):

    # client_ser = aiohttp.ClientSession(loop=loop, headers=header)
    async with ClientSession(loop=loop, headers=header) as client:
        rep_id = await get_json(client, "https://zconnectsandbox.zuora.com/api/rest/v1/reports/search?query=test%20report")
        print(rep_id)

    async with ClientSession(loop=loop, headers=header) as client_r:
        run_reportid = await post_json(client_r, "https://zconnectsandbox.zuora.com/api/rest/v1/reports/"+rep_id+"/reportrun?viewType=Detail")
        print(run_reportid)

    time.sleep(10)

    url_e = "https://zconnectsandbox.zuora.com/api/rest/v1/reportruns/export/" + \
        run_reportid+"?pivoted=true"

    async with ClientSession(loop=loop, headers=header) as client_e:
        response = await get_json_exp(client_e, url_e)
        print(response)
    time.sleep(10)
    # print(response.status())
    # print(run_reportid)

    # response = requests.request("GET", url, headers=header, data=payload)
    # report = reponse.text.encode('utf8')

    with open("test.txt", "w", encoding='utf8') as myfile:
        # report = await response.text()
        time.sleep(5)
        myfile.write(response)

    with open('test.txt', 'r') as infile, open('RatePlanCharge.csv', 'w', newline='') as outfile:
        in_reader = csv.reader(infile, delimiter='\t')
        writer = csv.writer(outfile)
        # csv_file.write(in_reader)
        for row in in_reader:
            writer.writerow(row)

    # writer = csv.writer(csvFile, delimiter='\t')

    # for row in new_data:
    #   writer.writerow(row)
    # f = open('new_yahoo.csv', 'w', newline='', encoding='utf8')
    # f.write(response.text())
    # writer = csv.writer(f)
    # for line in response.iter_lines():
    #   writer.writerow(line.decode('utf-8').split('\t'))
    # async with ClientSession(loop=loop, headers=header) as client_e:
    #   result = await get_json_exp(client_e, "https://zconnectsandbox.zuora.com/api/rest/v1/reportruns/export/"+run_reportid+"?pivoted=true")

    print(response)
    # await write_result(result)
    return
    # report = response.json()
    # report_res = report["response"]
    # report_rep = report_res["reports"]
    # reportid = report_rep[0]["id"]
    # return await reportid


async def get_exp_rep(config, loop):
    # client_run = aiohttp.ClientSession(loop=loop, headers=header)
 #   connector = TCPConnector(limit=config.concurrency)
    async with ClientSession(loop=loop, headers=header) as client:

        run_reportid = await post_json(client, "https://zconnectsandbox.zuora.com/api/rest/v1/reports/" +
                                       reportid+"/reportrun?viewType=Summary")

        return run_reportid
    # print(reportid)
  #  async with ClientSession(loop=loop, headers=header) as client_r:
    #     run_reportid = await post_json(client_r, "https://zconnectsandbox.zuora.com/api/rest/v1/reports/" +
    #                                   reportid+"/reportrun?viewType=Summary")

    # report = response_run.json()
    # report_ru_res = report["response"]
    # run_reportid = report_res["reportRunId"]
    # reportid = report_rep[0]["id"]
    # return await reportid

    # print(run_reportid + '\n')

    # return await run_reportid


async def main():
    return await asyncio.gather()


def session_met(concurrency, duration, timeout):
    config = Config(concurrency=concurrency,
                    duration=duration, timeout=timeout)

    loop = asyncio.get_event_loop()

    # print('Running test on {url}'.format(url=config.url))
    try:
        # reportid = await asyncio.Future()
        # reportid = asyncio.ensure_future(get_reddit_top(config, loop))
        # reportid = asyncio.ensure_future(
        #    session_met_ser(concurrency, duration, timeout))
        # run_reportid = asyncio.ensure_future(get_reddit_top(config, loop))
        tasks = asyncio.ensure_future(get_reddit_top(config, loop))
        loop.run_until_complete(tasks)
        # print(run_reportid)
 #   loop.run_until_complete(get_run_rep(reportid, config, loop))

    except:
        pass
    finally:
        loop.close()


# print('Stopped')

# asyncio.ensure_future(get_run_rep(client))

session_met(concurrency=1000,
            duration=1000,
            timeout=1000)


"""
if __name__ == '__main__':
    session_met(
        url='http://127.0.0.1:8888/asdf',
        concurrency=1000,
        duration=1000,
        timeout=1000
    ) """
#   loop.stop()
# client.close()
#  sys.exit(0)


# reportid = asyncio.ensure_future(get_reddit_top())
# run_reportid = asyncio.ensure_future(get_run_rep('reportid'))
# asyncio.ensure_future(get_reddit_top('compsci', client))
# loop.run_until_complete(session_met())
# loop.run_forever
# await session.close()
# signal.signal(signal.SIGINT, signal_handler)
# loop.close()
