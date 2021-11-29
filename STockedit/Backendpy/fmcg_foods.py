# -*- coding: utf-8 -*-
"""FMCG_Foods.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yFm70qdThFmUkCyHLn0h4s1pEySXA_a9

#Sector: FMCG-Foods
"""



from bs4 import BeautifulSoup
import requests
import pandas as pd
import json 
def fmcgfoods():
  def fmcgtob(stockname,url1,url2):


    stock_name=stockname
    url = url1

    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(url).text

    # Parse HTML code for the entire site
    soup = BeautifulSoup(html_content, "lxml")
    # print(soup)

    mc = soup.find_all("div", attrs={"class": "oview_table"})
    # print("Number of tables on site: ",len(mc))

    data = dict()
    for tb in mc[:4]:
        body = tb.find_all("tr")
        for i in body:
            vals = i.find_all("td")
            title = vals[0].text.strip()
            try:
                value = float(vals[1].text.replace(',',''))
            except ValueError:
                value = vals[1].text.replace(',','')
            data[title] = value
    # print(data)



    excel_data=pd.read_csv(r"C:\Users\mohil\OneDrive\Desktop\STOCKS_new.csv")
    excel_data.drop(columns=['Name (largecap alpha.csv)', 'Ticker (largecap alpha.csv)'],inplace=True)
    # excel_data.head(10)

    avg_price=round((data['Open']+data['Previous Close'])/2,2)
    shareholding=round((data['Mkt Cap (Rs. Cr.)']/avg_price),2)
    shareholding

    parameters_dict = dict()
    def scrape_indicators(urls):
        for url in urls:
            html_content = requests.get(url).text

            # Parse HTML code for the entire site
            soup = BeautifulSoup(html_content, "lxml")
            stonks = soup.find_all("div", attrs={"id": "standalone-new"})

            body = stonks[0].find_all("tr")

            indicator_dict = dict()

            for record in body:
                indicator = record.find_all("td")[0].text.upper()
                temp_indicator_values = []
                try:
                    for table_data in (record.find_all('td')[1:-1]):
                        temp_indicator_values.append(
                            float(table_data.text.replace(',', '')))
                except ValueError:
                    continue
                indicator_dict[indicator] = temp_indicator_values

            parameters_dict.update(indicator_dict)

        yield(url, parameters_dict)


        
    urls=url2
    # urls = ["https://www.moneycontrol.com/financials/godfreyphillipsindia/balance-sheetVI/GPI#GPI","https://www.moneycontrol.com/financials/godfreyphillipsindia/profit-lossVI/GPI#GPI","https://www.moneycontrol.com/financials/godfreyphillipsindia/cash-flowVI/GPI#GPI","https://www.moneycontrol.com/financials/godfreyphillipsindia/ratiosVI/GPI#GPI"]


    for request_url, indicator_data in scrape_indicators(urls):
        # print(request_url)
        # print(indicator_data)
        #print()
        print()

    if(data['Mkt Cap (Rs. Cr.)']<20000.00 and data['Mkt Cap (Rs. Cr.)']>5000.00):
      cap="Mid Cap"
    elif (data['Mkt Cap (Rs. Cr.)']>20000.00):
      cap="Large Cap"
    else:
      cap="Small Cap"
    

    pepoints=0



    ##Indicator 1: Reserves & Surplus
    # print(indicator_data['RESERVES AND SURPLUS'])
    rands_list=[]
    count_reserves=0
    for i in range(len(indicator_data['RESERVES AND SURPLUS'])-1,0,-1):
      if(indicator_data['RESERVES AND SURPLUS'][i-1]-indicator_data['RESERVES AND SURPLUS'][i]>0):
        rands_list.append(round(((indicator_data['RESERVES AND SURPLUS'][i-1]-indicator_data['RESERVES AND SURPLUS'][i])/indicator_data['RESERVES AND SURPLUS'][i])*100,2))
        # print(indicator_data['RESERVES AND SURPLUS'][i])
        count_reserves=count_reserves+20
        pepoints+=1
        # print(indicator_data['RESERVES AND SURPLUS'][i-1] , "-" , indicator_data['RESERVES AND SURPLUS'][i],"=", round(indicator_data['RESERVES AND SURPLUS'][i-1]-indicator_data['RESERVES AND SURPLUS'][i],2))
      else:
        rands_list.append(round(((indicator_data['RESERVES AND SURPLUS'][i-1]-indicator_data['RESERVES AND SURPLUS'][i])/indicator_data['RESERVES AND SURPLUS'][i])*100,2))
        # print(indicator_data['RESERVES AND SURPLUS'][i])
        count_reserves=count_reserves-20
        pepoints-=1
        # print(indicator_data['RESERVES AND SURPLUS'][i-1],"-",indicator_data['RESERVES AND SURPLUS'][i],"=", round(indicator_data['RESERVES AND SURPLUS'][i-1]-indicator_data['RESERVES AND SURPLUS'][i],2))

    rands_list=rands_list[::-1]

    for i in range(len(indicator_data['RESERVES AND SURPLUS'])-1,-1,-1):
        if(indicator_data['RESERVES AND SURPLUS'][i]<0):
          count_reserves-=20
          pepoints-=1

    # print(count_reserves)
    # print(rands_list)

    ##Indicator 2: Revenue From Operations Gross
    count_revenuefromop=0
    revenue_list=[]
    # print(indicator_data['REVENUE FROM OPERATIONS [GROSS]'])
    for i in range(len(indicator_data['REVENUE FROM OPERATIONS [GROSS]'])-1,0,-1):
      if(indicator_data['REVENUE FROM OPERATIONS [GROSS]'][i-1]-indicator_data['REVENUE FROM OPERATIONS [GROSS]'][i]>0):
        revenue_list.append(round(((indicator_data['REVENUE FROM OPERATIONS [GROSS]'][i-1]-indicator_data['REVENUE FROM OPERATIONS [GROSS]'][i])/indicator_data['REVENUE FROM OPERATIONS [GROSS]'][i])*100,2))
        count_revenuefromop=count_revenuefromop+10
        # print(indicator_data['REVENUE FROM OPERATIONS [GROSS]'][i-1] , "-" , indicator_data['REVENUE FROM OPERATIONS [GROSS]'][i],"=", round(indicator_data['REVENUE FROM OPERATIONS [GROSS]'][i-1]-indicator_data['REVENUE FROM OPERATIONS [GROSS]'][i],2))
      else:
        revenue_list.append(round(((indicator_data['REVENUE FROM OPERATIONS [GROSS]'][i-1]-indicator_data['REVENUE FROM OPERATIONS [GROSS]'][i])/indicator_data['REVENUE FROM OPERATIONS [GROSS]'][i])*100,2))
        count_revenuefromop=count_revenuefromop-10
        # print(indicator_data['REVENUE FROM OPERATIONS [GROSS]'][i-1],"-",indicator_data['REVENUE FROM OPERATIONS [GROSS]'][i],"=",round(indicator_data['REVENUE FROM OPERATIONS [GROSS]'][i-1]-indicator_data['REVENUE FROM OPERATIONS [GROSS]'][i],2))

    revenue_list=revenue_list[::-1]

    for i in range(len(indicator_data['REVENUE FROM OPERATIONS [GROSS]'])-1,-1,-1):
        if(indicator_data['REVENUE FROM OPERATIONS [GROSS]'][i]<0):
          count_revenuefromop-=15


    # print(count_revenuefromop)
    # print(revenue_list)





    ##Indicator 3: Profit/Loss for the period
    count_profitloss=0
    profit_list=[]
    # print(indicator_data['PROFIT/LOSS FOR THE PERIOD'])
    for i in range(len(indicator_data['PROFIT/LOSS FOR THE PERIOD'])-1,0,-1):
      if(indicator_data['PROFIT/LOSS FOR THE PERIOD'][i-1]-indicator_data['PROFIT/LOSS FOR THE PERIOD'][i]>0):
        profit_list.append(round(((indicator_data['PROFIT/LOSS FOR THE PERIOD'][i-1]-indicator_data['PROFIT/LOSS FOR THE PERIOD'][i])/indicator_data['PROFIT/LOSS FOR THE PERIOD'][i])*100,2))
        count_profitloss=count_profitloss+10
        # print(indicator_data['PROFIT/LOSS FOR THE PERIOD'][i-1] , "-" , indicator_data['PROFIT/LOSS FOR THE PERIOD'][i],"=", round(indicator_data['PROFIT/LOSS FOR THE PERIOD'][i-1]-indicator_data['PROFIT/LOSS FOR THE PERIOD'][i],2))
      else:
        profit_list.append(round(((indicator_data['PROFIT/LOSS FOR THE PERIOD'][i-1]-indicator_data['PROFIT/LOSS FOR THE PERIOD'][i])/indicator_data['PROFIT/LOSS FOR THE PERIOD'][i])*100,2))
        count_profitloss=count_profitloss-10
        # print(indicator_data['PROFIT/LOSS FOR THE PERIOD'][i-1],"-",indicator_data['PROFIT/LOSS FOR THE PERIOD'][i],"=",round(indicator_data['PROFIT/LOSS FOR THE PERIOD'][i-1]-indicator_data['PROFIT/LOSS FOR THE PERIOD'][i],2))

    profit_list=profit_list[::-1]

    for i in range(len(indicator_data['PROFIT/LOSS FOR THE PERIOD'])-1,-1,-1):
        if(indicator_data['PROFIT/LOSS FOR THE PERIOD'][i]<0):
          count_profitloss-=15

    # print(count_profitloss)
    # print(profit_list)

    # print(pepoints)

    ##Indicator 4: ROCE

    count_roce=0
    # print(indicator_data['RETURN ON CAPITAL EMPLOYED (%)'])
    for i in range(len(indicator_data['RETURN ON CAPITAL EMPLOYED (%)'])-1,0,-1):
      if(indicator_data['RETURN ON CAPITAL EMPLOYED (%)'][i-1]-indicator_data['RETURN ON CAPITAL EMPLOYED (%)'][i]>-1):
        count_roce+=10
        # print(indicator_data['RETURN ON CAPITAL EMPLOYED (%)'][i-1] , "-" , indicator_data['RETURN ON CAPITAL EMPLOYED (%)'][i],"=", round(indicator_data['RETURN ON CAPITAL EMPLOYED (%)'][i-1]-indicator_data['RETURN ON CAPITAL EMPLOYED (%)'][i],2))
      else:
        count_roce-=10
        # print(indicator_data['RETURN ON CAPITAL EMPLOYED (%)'][i-1],"-",indicator_data['RETURN ON CAPITAL EMPLOYED (%)'][i],"=",round(indicator_data['RETURN ON CAPITAL EMPLOYED (%)'][i-1]-indicator_data['RETURN ON CAPITAL EMPLOYED (%)'][i],2))

    for i in range(len(indicator_data['RETURN ON CAPITAL EMPLOYED (%)'])-1,-1,-1):
        if(indicator_data['RETURN ON CAPITAL EMPLOYED (%)'][i]<10):
          count_roce-=15
          pepoints-=1
        else:
          if(indicator_data['RETURN ON CAPITAL EMPLOYED (%)'][i]>10):
            count_roce+=15
            pepoints+=1


    for i in range(len(indicator_data['RETURN ON CAPITAL EMPLOYED (%)'])-1,-1,-1):
        if(indicator_data['RETURN ON CAPITAL EMPLOYED (%)'][i]<0):
          count_roce-=25

    roce_ind=indicator_data['RETURN ON CAPITAL EMPLOYED (%)'][0]


    # print(count_roce)

    # print(pepoints)

    ##Indicator 5: Inventory Turnover Ratio
    count_ito=0
    # print(indicator_data['INVENTORY TURNOVER RATIO (X)'])
    for i in range(len(indicator_data['INVENTORY TURNOVER RATIO (X)'])-1,0,-1):
      if(indicator_data['INVENTORY TURNOVER RATIO (X)'][i-1]-indicator_data['INVENTORY TURNOVER RATIO (X)'][i]>0):
        count_ito+=20
        pepoints+=1
        # print(indicator_data['INVENTORY TURNOVER RATIO (X)'][i-1] , "-" , indicator_data['INVENTORY TURNOVER RATIO (X)'][i],"=", round(indicator_data['INVENTORY TURNOVER RATIO (X)'][i-1]-indicator_data['INVENTORY TURNOVER RATIO (X)'][i],2))
      else:
        count_ito-=10
        pepoints-=1
        # print(indicator_data['INVENTORY TURNOVER RATIO (X)'][i-1],"-",indicator_data['INVENTORY TURNOVER RATIO (X)'][i],"=",round(indicator_data['INVENTORY TURNOVER RATIO (X)'][i-1]-indicator_data['INVENTORY TURNOVER RATIO (X)'][i],2))
    # print(count_ito)

    # pepoints

    ##Indicator 6: Reserves & Surplus/Equity Share Capital
    # print(indicator_data['RESERVES AND SURPLUS'])
    # print(indicator_data['TOTAL SHARE CAPITAL'])
    #print()
    rsesc_list=[]
    for i in range(len(indicator_data['RESERVES AND SURPLUS'])-1,-1,-1):
            # print(indicator_data['RESERVES AND SURPLUS'][i])
            # print(indicator_data['RESERVES AND SURPLUS'][i] , "/" , indicator_data['TOTAL SHARE CAPITAL'][i],"=", round((indicator_data['RESERVES AND SURPLUS'][i]/indicator_data['TOTAL SHARE CAPITAL'][i]),2))
            rsesc_list.append(round(indicator_data['RESERVES AND SURPLUS'][i]/indicator_data['TOTAL SHARE CAPITAL'][i],2))

    #print()
    rsesc_list=rsesc_list[::-1]
    # print(rsesc_list)
    #print()
    count_rec=0
    for i in range(len(rsesc_list)-1,0,-1):
      if(rsesc_list[i-1]-rsesc_list[i]>0):
        count_rec+=20
        pepoints+=1
        # print(rsesc_list[i-1] , "-" , rsesc_list[i],"=", round(rsesc_list[i-1]-rsesc_list[i],2))
      else:
        count_rec-=10
        pepoints-=1
        # print(rsesc_list[i-1],"-",rsesc_list[i],"=",round(rsesc_list[i-1]-rsesc_list[i],2))


    for i in range(len(rsesc_list)-1,-1,-1):
        if(rsesc_list[i]<10):
          count_rec-=15

    for i in range(len(rsesc_list)-1,-1,-1):
        if(rsesc_list[i]<0):
          count_rec-=20


    # print(rsesc_list)
    # print(count_rec)



    # pepoints





    ## Indicator 7: Trade Receivables in Current Assets
    # print(indicator_data['TOTAL CURRENT ASSETS'])
    # print(indicator_data['TRADE RECEIVABLES'])

    trade_list=[]
    bonus=0
    for i in range(len(indicator_data['TOTAL CURRENT ASSETS'])-1,-1,-1):
              # print(indicator_data['TOTAL CURRENT ASSETS'][i] , "/" , indicator_data['TRADE RECEIVABLES'][i],"=", round((indicator_data['TOTAL CURRENT ASSETS'][i]/indicator_data['TRADE RECEIVABLES'][i]),2))
              if(round((indicator_data['TOTAL CURRENT ASSETS'][i]/indicator_data['TRADE RECEIVABLES'][i]),2)<50.00):
                bonus+=10
              else:
                bonus-=5
    # print(bonus)

    # print(pepoints)

    ## Indicator 8: Earnings Before Interest Tax

    indicator_data['PBIT MARGIN (%)']
    count_ebit=0
    # print(indicator_data['PBIT MARGIN (%)'])
    for i in range(len(indicator_data['PBIT MARGIN (%)'])-1,0,-1):
      if(indicator_data['PBIT MARGIN (%)'][i-1]-indicator_data['PBIT MARGIN (%)'][i]>0):
        count_ebit+=10
        pepoints+=1
        # print(indicator_data['PBIT MARGIN (%)'][i-1] , "-" , indicator_data['PBIT MARGIN (%)'][i],"=", round(indicator_data['PBIT MARGIN (%)'][i-1]-indicator_data['PBIT MARGIN (%)'][i],2))
      else:
        count_ebit-=5
        pepoints+=1
        # print(indicator_data['PBIT MARGIN (%)'][i-1],"-",indicator_data['PBIT MARGIN (%)'][i],"=",round(indicator_data['PBIT MARGIN (%)'][i-1]-indicator_data['PBIT MARGIN (%)'][i],2))

    for i in range(len(indicator_data['PBIT MARGIN (%)'])-1,-1,-1):
        if(indicator_data['PBIT MARGIN (%)'][i]<0):
          count_ebit-=20


    # print(count_ebit)

    # print(pepoints)

    ## Indicator 9: Debt To Equity Ratio

    count_debt=0
    # print(indicator_data["TOTAL DEBT/EQUITY (X)"])

    for i in range(len(indicator_data['TOTAL DEBT/EQUITY (X)'])-1,0,-1):
      if(indicator_data['TOTAL DEBT/EQUITY (X)'][i-1]-indicator_data['TOTAL DEBT/EQUITY (X)'][i]>0):
        count_debt+=10
        # print(indicator_data['TOTAL DEBT/EQUITY (X)'][i-1] , "-" , indicator_data['TOTAL DEBT/EQUITY (X)'][i],"=", round(indicator_data['TOTAL DEBT/EQUITY (X)'][i-1]-indicator_data['TOTAL DEBT/EQUITY (X)'][i],2))
      elif (indicator_data['TOTAL DEBT/EQUITY (X)'][i-1]-indicator_data['TOTAL DEBT/EQUITY (X)'][i]==0):
            count_debt+=10
      else:
        count_debt-=5
        # print(indicator_data['TOTAL DEBT/EQUITY (X)'][i-1],"-",indicator_data['TOTAL DEBT/EQUITY (X)'][i],"=",round(indicator_data['TOTAL DEBT/EQUITY (X)'][i-1]-indicator_data['TOTAL DEBT/EQUITY (X)'][i],2))
      
    for i in range(len(indicator_data['TOTAL DEBT/EQUITY (X)'])-1,-1,-1):
        if(indicator_data['TOTAL DEBT/EQUITY (X)'][i]>2):
          count_debt-=15
          pepoints-=1
        else:
          count_debt+=15
          pepoints+=1

    for i in range(len(indicator_data['TOTAL DEBT/EQUITY (X)'])-1,-1,-1):
        if(indicator_data['TOTAL DEBT/EQUITY (X)'][i]<0):
          count_debt-=20


    # print(count_debt)

    # pepoints

    ## Indicator 10: Current Ratio
    indicator_data['CURRENT RATIO (X)']

    count_currentratio=0
    # print(indicator_data["CURRENT RATIO (X)"])

    for i in range(len(indicator_data['CURRENT RATIO (X)'])-1,0,-1):
      if(indicator_data['CURRENT RATIO (X)'][i-1]-indicator_data['CURRENT RATIO (X)'][i]>0):
        count_currentratio+=10
        # print(indicator_data['CURRENT RATIO (X)'][i-1] , "-" , indicator_data['CURRENT RATIO (X)'][i],"=", round(indicator_data['CURRENT RATIO (X)'][i-1]-indicator_data['CURRENT RATIO (X)'][i],2))
      elif ((indicator_data['CURRENT RATIO (X)'][i-1]-indicator_data['CURRENT RATIO (X)'][i])==0):
            count_currentratio+=10
      else:
        count_currentratio-=5
        # print(indicator_data['CURRENT RATIO (X)'][i-1],"-",indicator_data['CURRENT RATIO (X)'][i],"=",round(indicator_data['CURRENT RATIO (X)'][i-1]-indicator_data['CURRENT RATIO (X)'][i],2))

    for i in range(len(indicator_data['CURRENT RATIO (X)'])-1,-1,-1):
        if(indicator_data['CURRENT RATIO (X)'][i]<2):
          # print(indicator_data['CURRENT RATIO (X)'][i])
          count_currentratio-=10
          pepoints=pepoints-0.5
        elif (indicator_data['CURRENT RATIO (X)'][i]<1):
          count_currentratio-=20
          pepoints=pepoints-1
        else:
          count_currentratio+=10
          pepoints+=1


    # print(count_currentratio)

    # pepoints

    ##Indicator 11: Net Cashflow From Operating Activities
    count_netcashflow=0
    cashflow_list=[]
    # print(indicator_data['NET CASHFLOW FROM OPERATING ACTIVITIES'])
    for i in range(len(indicator_data['NET CASHFLOW FROM OPERATING ACTIVITIES'])-1,0,-1):
      if(indicator_data['NET CASHFLOW FROM OPERATING ACTIVITIES'][i-1]-indicator_data['NET CASHFLOW FROM OPERATING ACTIVITIES'][i]>0):
        cashflow_list.append(round(((indicator_data['NET CASHFLOW FROM OPERATING ACTIVITIES'][i-1]-indicator_data['NET CASHFLOW FROM OPERATING ACTIVITIES'][i])/indicator_data['NET CASHFLOW FROM OPERATING ACTIVITIES'][i])*100,2))
        count_netcashflow=count_netcashflow+10
        pepoints+=1
        # print(indicator_data['NET CASHFLOW FROM OPERATING ACTIVITIES'][i-1] , "-" , indicator_data['NET CASHFLOW FROM OPERATING ACTIVITIES'][i],"=", round(indicator_data['NET CASHFLOW FROM OPERATING ACTIVITIES'][i-1]-indicator_data['NET CASHFLOW FROM OPERATING ACTIVITIES'][i],2))
      else:
        cashflow_list.append(round(((indicator_data['NET CASHFLOW FROM OPERATING ACTIVITIES'][i-1]-indicator_data['NET CASHFLOW FROM OPERATING ACTIVITIES'][i])/indicator_data['NET CASHFLOW FROM OPERATING ACTIVITIES'][i])*100,2))
        count_netcashflow=count_netcashflow-10
        pepoints-=1
        # print(indicator_data['NET CASHFLOW FROM OPERATING ACTIVITIES'][i-1],"-",indicator_data['NET CASHFLOW FROM OPERATING ACTIVITIES'][i],"=",round(indicator_data['NET CASHFLOW FROM OPERATING ACTIVITIES'][i-1]-indicator_data['NET CASHFLOW FROM OPERATING ACTIVITIES'][i],2))

    cashflow_list=cashflow_list[::-1]

    for i in range(len(indicator_data['NET CASHFLOW FROM OPERATING ACTIVITIES'])-1,-1,-1):
        if(indicator_data['NET CASHFLOW FROM OPERATING ACTIVITIES'][i]<0):
          count_netcashflow-=15

    # print(count_netcashflow)
    # print(cashflow_list)

    ##Indicator 12: Free cash Flow
    stock_position=None
    stock_data=excel_data.values.tolist()
    stock_data
    for i in stock_data:
      for j in i:
        j=str(j)
        if(stock_name in j):
          # print(j.index(i))
          stock_position=stock_data.index(i)
          # print(j)
          break
          
    # print(stock_position)

    freecash_list=[]
    for i in range(5):
      freecash_list.append(stock_data[stock_position][i])
    # print(freecash_list)

    count_freecash=0
    for i in range(1,len(freecash_list)):
      if(freecash_list[i]-freecash_list[i-1]>0):
        # print(freecash_list[i],"-",freecash_list[i-1],"=",freecash_list[i]-freecash_list[i-1])
        count_freecash+=20
        pepoints+=1
      else:
        # print(freecash_list[i],"-",freecash_list[i-1],"=",freecash_list[i]-freecash_list[i-1])
        count_freecash-=10
        pepoints-=1

    for i in range(0,len(freecash_list)):
      if(freecash_list[i]<0):
        count_freecash-=20
        pepoints-=1

    # print(count_freecash)

    ##Indicator 13: Pledged shares
    for i in stock_data:
      for j in i:
        j=str(j)
        if(stock_name in j):
          # print(j.index(i))
          stock_position=stock_data.index(i)
          # print(j)
          break

    pledged_shares=stock_data[stock_position][15]
    # print(pledged_shares)
    stock_name=stock_data[stock_position][5]
    count_pshares=1
    if(pledged_shares>0):
      pepoints-=1
      count_pshares=count_pshares*-10
    else:
      pepoints+=1
      count_pshares=count_pshares*10

    ##Entities: Alpha & Beta
    alpha=round(stock_data[stock_position][9],2)
    # print("Alpha",alpha)
    beta=round(stock_data[stock_position][10],2)
    # print("Beta",beta)
    divy=data['Dividend Yield']
    # print("Dividend Yield",divy)

    cagr=stock_data[stock_position][8]
    # print("CAGR:", cagr)

    # pepoints

    ##Indicator 14: PE Ratio
    st_pe=data['TTM PE']
    se_pe=data['Sector PE']
    # print("Stock PE", st_pe)
    # print("Sector PE",se_pe)
    count_pe=1
    if(data['TTM PE']=="--"):
        count_pe=pepoints*12
    elif(data['TTM PE']<data['Sector PE']):
      count_pe=pepoints*15
    else:
      count_pe=pepoints*10

    # print(count_pe)



    #Predicting Target Price 
    flag=0
    target_price=None
    entry_price=None
    # int(indicator_data['ENTERPRISE VALUE (CR.)'])
    # print(indicator_data['EV/EBITDA (X)'])
    #print()

    ebitda_list=[]
    for i in range(len(indicator_data['ENTERPRISE VALUE (CR.)'])-1,-1,-1):
            if(indicator_data['ENTERPRISE VALUE (CR.)'][i]==0):

              flag=1
              break

            # print(indicator_data['ENTERPRISE VALUE (CR.)'][i] , "/" , indicator_data['EV/EBITDA (X)'][i],"=", round((indicator_data['ENTERPRISE VALUE (CR.)'][i]/indicator_data['EV/EBITDA (X)'][i]),2))
            ebitda_list.append(round(indicator_data['ENTERPRISE VALUE (CR.)'][i]/indicator_data['EV/EBITDA (X)'][i],2))
    if(flag==0):

      #print()
      ebitda_list=ebitda_list[::-1]

      # print(ebitda_list)
      growth_ebitda=[]
      for i in range(len(ebitda_list)-1,0,-1):
        # print(ebitda_list[i-1],"-",ebitda_list[i],"=",round(ebitda_list[i-1]-ebitda_list[i],2), "   ",round((ebitda_list[i-1]-ebitda_list[i])/ebitda_list[i]*100,2))
        growth_ebitda.append(round((ebitda_list[i-1]-ebitda_list[i])/ebitda_list[i]*100,2))

      #print()
      growth_ebitda=growth_ebitda[::-1]

      # print(growth_ebitda)
      #print()
      grow=0
      for i in range(len(growth_ebitda)-1):
        grow=grow+growth_ebitda[i]

      growth=round(grow/3,2)
      # print("Growth for last three years:", growth)
      #print()
      # print(ebitda_list[0])
      pred_ebitda=round(((100+growth)*ebitda_list[0])/100,2)

      # print("Predicted Ebitda:",pred_ebitda)


      #print()
      forecasted_ev= round(pred_ebitda*indicator_data['EV/EBITDA (X)'][0],2)

      #print()
      forecasted_ev=forecasted_ev-indicator_data['LONG TERM BORROWINGS'][0]
      forecasted_ev

      # print("Forecasted EV:",forecasted_ev)
      #print()
      target_price=round(forecasted_ev/shareholding,2)
      # print("Target Price:", target_price)

      entry_price=round(target_price*0.75,2)
      # print("Good Buy Price:",entry_price)

    points=bonus+count_currentratio+count_debt+count_ebit+count_ito+count_profitloss+count_rec+count_reserves+count_revenuefromop+count_roce+count_netcashflow+count_pe+count_freecash+count_pshares
    final_list=[]
    positives=[]
    if(beta>0 and beta<1.5):
      positives.append(" {} is {} times volatile than the market, low risk stock".format(stock_name,beta))
    if(count_reserves>60):
      positives.append(" Reserves And Surplus for {} are significantly increasing.".format(stock_name))
    if(count_revenuefromop>40):
      positives.append(" Constant increase in Revenue for {}.".format(stock_name))
    if(count_profitloss>40):
      positives.append(" Increasing Profits for {}.".format(stock_name))
    if(count_roce>90):
      positives.append(" {} is performing very well on ROCE indicator.".format(stock_name))
    if(count_ito>80):
        positives.append(" {} is outperforming it's previous cycle.".format(stock_name))
    if(count_freecash>80):
      positives.append(" {} has free cash flow over the years.".format(stock_name))
    if(st_pe!= "--"):
      if(st_pe<se_pe and pepoints >24):
        positives.append(" {} has PE ratio less than the industry PE, can be a steal deal".format(stock_name))
    


    

    negatives=[]
    if(count_freecash<0):
      negatives.append(" Free Cash Flow problems for {}.".format(stock_name))
    if(pledged_shares>5):
      negatives.append(" {} has pledged shares.".format(stock_name))
    if(count_reserves<0):
      negatives.append(" Reserves and Surplus are continously decreasing for {}.".format(stock_name))
    if(count_revenuefromop<0):
      negatives.append(" Decreasing revenues for {}.".format(stock_name))
    if(count_debt<30):
      negatives.append("{} has high debts over the years.".format(stock_name))
    if(beta>1.5):
      negatives.append(" {} is {} times volatile than the market, high risk stock".format(stock_name,beta))
    if(roce_ind<10):
      negatives.append(" {} has low return on capital".format(stock_name,beta))


    final_list.append(stock_name)
    final_list.append(divy)
    final_list.append(cagr)
    final_list.append(target_price)
    final_list.append(cap)
    final_list.append(roce_ind)
    final_list.append(points)
    final_list.append(positives)
    final_list.append(negatives)
    
    return final_list

  table=[]
  url_list=[]
  url_list=[[["Nestle"],["https://www.moneycontrol.com/india/stockpricequote/foodprocessing/nestleindia/NI"],["https://www.moneycontrol.com/financials/nestleindia/balance-sheetVI/NI#NI","https://www.moneycontrol.com/financials/nestleindia/profit-lossVI/NI#NI","https://www.moneycontrol.com/financials/nestleindia/cash-flowVI/NI#NI","https://www.moneycontrol.com/financials/nestleindia/ratiosVI/NI#NI"]],
            [["Britannia"],["https://www.moneycontrol.com/india/stockpricequote/foodprocessing/britanniaindustries/BI"],["https://www.moneycontrol.com/financials/britanniaindustries/balance-sheetVI/BI#BI","https://www.moneycontrol.com/financials/britanniaindustries/cash-flowVI/BI#BI","https://www.moneycontrol.com/financials/britanniaindustries/ratiosVI/BI#BI", " https://www.moneycontrol.com/financials/britanniaindustries/profit-lossVI/BI#BI"]],
            [['Hatsun'],["https://www.moneycontrol.com/india/stockpricequote/foodprocessing/hatsunagroproducts/HAP"],['https://www.moneycontrol.com/financials/hatsunagroproducts/balance-sheetVI/HAP#HAP','https://www.moneycontrol.com/financials/hatsunagroproducts/cash-flowVI/HAP#HAP','https://www.moneycontrol.com/financials/hatsunagroproducts/ratiosVI/HAP#HAP','https://www.moneycontrol.com/financials/hatsunagroproducts/profit-lossVI/HAP#HAP']],
            [["ZYDUSWELL"],['https://www.moneycontrol.com/india/stockpricequote/vanaspatioils/zyduswellness/ZW01'],['https://www.moneycontrol.com/financials/zyduswellness/balance-sheetVI/ZW01#ZW01','https://www.moneycontrol.com/financials/zyduswellness/cash-flowVI/ZW01#ZW01','https://www.moneycontrol.com/financials/zyduswellness/ratiosVI/ZW01#ZW01','https://www.moneycontrol.com/financials/zyduswellness/profit-lossVI/ZW01#ZW01']],
            [["Hindustan Foods Ltd"],['https://www.moneycontrol.com/india/stockpricequote/foodprocessing/hindustanfoods/HFL'],['https://www.moneycontrol.com/financials/hindustanfoods/balance-sheetVI/HFL#HFL','https://www.moneycontrol.com/financials/hindustanfoods/profit-lossVI/HFL#HFL','https://www.moneycontrol.com/financials/hindustanfoods/cash-flowVI/HFL#HFL','https://www.moneycontrol.com/financials/hindustanfoods/ratiosVI/HFL#HFL']],
            [['DODLA'],['https://www.moneycontrol.com/india/stockpricequote/consumerfood/dodladairy/DD01'],['https://www.moneycontrol.com/financials/dodladairy/balance-sheetVI/DD01#DD01','https://www.moneycontrol.com/financials/dodladairy/profit-lossVI/DD01#DD01','https://www.moneycontrol.com/financials/dodladairy/cash-flowVI/DD01#DD01','https://www.moneycontrol.com/financials/dodladairy/ratiosVI/DD01#DD01']]]


  for i in range(len(url_list)):
    list_input=[]
    for j in url_list[i]:
      list_input.append(j)
    stockname=list_input[0][0]
    url1=list_input[1][0]
    url2=list_input[2]
    # print(stockname,url1,url2)
    final_list=fmcgtob(stockname,url1,url2)
    table.append(final_list)
  df=pd.DataFrame(table,columns=['stock_name','divy','cagr','target_price','cap','roce_ind','points','positives','negatives'])
  df.sort_values(by='points', ascending=False,inplace=True)
  stock=[]
  stock=df.values.tolist()
  with open("foods_stock.txt","w") as fmcgdata:
    stock_json=json.dumps(stock)
    fmcgdata.write(stock_json)
  return stock

import datetime
from datetime import datetime


def function_foods():
  currentDay = datetime.now().day
  currentMonth = datetime.now().month

  if(currentMonth in [11,2,5,8] and currentDay==20):
    result=fmcgfoods()
    return result
  else:
    try:
      data_file = open("foods_stock.txt","r")
      list_stock = data_file.read()
      list_stock = json.loads(list_stock)

    except FileNotFoundError:
      
      list_stock = fmcgfoods()
    return list_stock

