# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 15:32:07 2018

@author: ynebh
"""
import csv

import requests
from lxml import html
from bs4 import BeautifulSoup
r = requests.get("https://csr.gov.in/CSR/search_page.php?query=%25%25%25")
content = r.content
soup = BeautifulSoup(content, "html.parser")
#print(soup.text)

with open ('filename.csv','w') as file:
    column_name = ['Name','CIN','Class','State','Company Type','RoC',\
                   'Sub Category','Listing Status','Year','Average Net Profit',\
                   'CSR Prescribed Expenditure','CSR Spent','Local Area Spent',\
                   'CSR Project(s)','Development Sector(s)',\
                   'State','District','Project Amount Outlay','Amount Spent',\
                   'Mode of Implementation']
    
    writer= csv.DictWriter(file, fieldnames=column_name)
    writer.writeheader()
    for row in soup.find_all('tr'):
        for link in row.find_all('a'):
            href = link.get('href')
            CIN= link.text.strip()
            r = requests.get('https://csr.gov.in/CSR/'+href)
            content = r.content
            profile = BeautifulSoup(content, "html.parser")
            
            Name=profile.find('h2').find('b').text
            csr= {"Name": Name.strip()}
            for field in profile.find('tbody').find_all('tr'):
                csr[field.find('th').text.strip()]=field.find('td').text.strip()
            
            ## Financial year 2014-15
            try:
                colfy =profile.find('div', id='colfy1')
                for field in colfy.find('table', id='employee_data').find_all('tr'):
                    csr[field.find('th').text.strip()]=field.find('td').text.strip()
                for field in colfy.find('table', id='datatable').find('tbody').find_all('tr'):
                    tmpInvest = [i.text.strip() for i in field.find_all('td')]
                    if len(tmpInvest) <=8:
                        break
                    csr['CSR Project(s)'] =tmpInvest[1]
                    csr['Development Sector(s)'] =tmpInvest[2]
                    csr['State'] =tmpInvest[3]
                    csr['District'] =tmpInvest[4]
                    csr['Project Amount Outlay'] =tmpInvest[5]
                    csr['Amount Spent'] =tmpInvest[6]
                    csr['Mode of Implementation'] =tmpInvest[7]
                    csr['Year']=2014-15
                    print(csr)
                    writer.writerow(csr)
            except AttributeError as Attrib:
                print('Continue with no element')
                #print('\n'+str(csr)+'===================\n')
              
            ## Financial year 2015-16
            try:
                colfy =profile.find('div', id='colfy2')
                for field in colfy.find('table', id='employee_data').find_all('tr'):
                    csr[field.find('th').text.strip()]=field.find('td').text.strip()
                for field in colfy.find('table', id='datatable').find('tbody').find_all('tr'):
                    tmpInvest = [i.text.strip() for i in field.find_all('td')]
                    if len(tmpInvest) <=8:
                        break
                    csr['CSR Project(s)'] =tmpInvest[1]
                    csr['Development Sector(s)'] =tmpInvest[2]
                    csr['State'] =tmpInvest[3]
                    csr['District'] =tmpInvest[4]
                    csr['Project Amount Outlay'] =tmpInvest[5]
                    csr['Amount Spent'] =tmpInvest[6]
                    csr['Mode of Implementation'] =tmpInvest[7]
                    csr['Year']=2015-16
                    print(csr)
                    writer.writerow(csr)
            except AttributeError as Attrib:
                print('Continue with no element')
                #print('\n'+str(csr)+'===================\n')
                
                
            ## Financial year 2016-17
            try:
                colfy =profile.find('div', id='colfy3')
                for field in colfy.find('table', id='employee_data').find_all('tr'):
                    csr[field.find('th').text.strip()]=field.find('td').text.strip()
                for field in colfy.find('table', id='datatable').find('tbody').find_all('tr'):
                    tmpInvest = [i.text.strip() for i in field.find_all('td')]
                    if len(tmpInvest) <=8:
                        break
                    csr['CSR Project(s)'] =tmpInvest[1]
                    csr['Development Sector(s)'] =tmpInvest[2]
                    csr['State'] =tmpInvest[3]
                    csr['District'] =tmpInvest[4]
                    csr['Project Amount Outlay'] =tmpInvest[5]
                    csr['Amount Spent'] =tmpInvest[6]
                    csr['Mode of Implementation'] =tmpInvest[7]
                    csr['Year']=2016-17
                    print(csr.encode("utf-8"))
                    writer.writerow(csr)
            except AttributeError as Attrib:
                print('Continue with no element')
                #print('\n'+str(csr)+'===================\n')
        


