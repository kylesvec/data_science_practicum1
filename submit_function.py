import requests
import json
import pandas as pd
from flatten_json import flatten
from tkinter import *

def submit():
    df=[]
    addy = entry.get()
    print('Wallet Address: ' + addy)
    api_key = '' #Insert valid DeBank API key
    
    data = requests.get(
        'https://pro-openapi.debank.com/v1/user/all_complex_protocol_list?id=' + addy,
            headers={'accept':'application/json','AccessKey':api_key})
    
    info = json.loads(data.content)
    if len(info)>0:
        for i in info:
            temp = flatten(i)
            df_temp = pd.DataFrame([temp])
            df_temp['Address'] = addy
            df.append(df_temp)
        
    df_final = pd.concat(df)       
    df_final.to_csv('debank_data_test.csv')   

    print(df_final)
    
    df_new = df_final[['Address','id','chain','name','tvl',
    'portfolio_item_list_0_name','portfolio_item_list_0_detail_types_0',
    'portfolio_item_list_0_detail_supply_token_list_0_amount',
    'portfolio_item_list_0_detail_supply_token_list_0_optimized_symbol',
    'portfolio_item_list_0_detail_supply_token_list_0_protocol_id',
    'portfolio_item_list_0_pool_adapter_id',
    
    'portfolio_item_list_0_detail_supply_token_list_1_amount',
    'portfolio_item_list_0_detail_supply_token_list_1_optimized_symbol',
    'portfolio_item_list_0_detail_supply_token_list_1_protocol_id',
    
    'portfolio_item_list_0_detail_supply_token_list_2_amount',
    'portfolio_item_list_0_detail_supply_token_list_2_optimized_symbol',
    'portfolio_item_list_0_detail_supply_token_list_2_protocol_id',
    
    'portfolio_item_list_0_detail_supply_token_list_3_amount',
    'portfolio_item_list_0_detail_supply_token_list_3_optimized_symbol',
    'portfolio_item_list_0_detail_supply_token_list_3_protocol_id',
    
    #'portfolio_item_list_0_detail_supply_token_list_4_amount',
    #'portfolio_item_list_0_detail_supply_token_list_4_optimized_symbol',
    #'portfolio_item_list_0_detail_supply_token_list_4_protocol_id',
    
    #'portfolio_item_list_0_detail_supply_token_list_5_amount',
    #'portfolio_item_list_0_detail_supply_token_list_5_optimized_symbol',
    #'portfolio_item_list_0_detail_supply_token_list_5_protocol_id',
    
    #portfolio_item_list_1
    'portfolio_item_list_1_name',
    'portfolio_item_list_1_detail_supply_token_list_0_amount',
    'portfolio_item_list_1_detail_supply_token_list_0_optimized_symbol',
    'portfolio_item_list_1_detail_supply_token_list_0_protocol_id',
    'portfolio_item_list_1_pool_adapter_id',
    
    'portfolio_item_list_1_detail_supply_token_list_1_amount',
    'portfolio_item_list_1_detail_supply_token_list_1_optimized_symbol',
    'portfolio_item_list_1_detail_supply_token_list_1_protocol_id',
    
    #'portfolio_item_list_1_detail_supply_token_list_2_amount',
    #'portfolio_item_list_1_detail_supply_token_list_2_optimized_symbol',
    #'portfolio_item_list_1_detail_supply_token_list_2_protocol_id',
    
    #portfolio_item_list_2
    'portfolio_item_list_2_name',
    'portfolio_item_list_2_detail_supply_token_list_0_amount',
    'portfolio_item_list_2_detail_supply_token_list_0_optimized_symbol',
    'portfolio_item_list_2_detail_supply_token_list_0_protocol_id',
    'portfolio_item_list_2_pool_adapter_id',
    
    'portfolio_item_list_2_detail_supply_token_list_1_amount',
    'portfolio_item_list_2_detail_supply_token_list_1_optimized_symbol',
    'portfolio_item_list_2_detail_supply_token_list_1_protocol_id',
    
    #'portfolio_item_list_2_detail_supply_token_list_2_amount',
    #'portfolio_item_list_2_detail_supply_token_list_2_optimized_symbol',
    #'portfolio_item_list_2_detail_supply_token_list_2_protocol_id',
    
    #portfolio_item_list_3
    'portfolio_item_list_3_name',
    'portfolio_item_list_3_detail_supply_token_list_0_amount',
    'portfolio_item_list_3_detail_supply_token_list_0_optimized_symbol',
    'portfolio_item_list_3_detail_supply_token_list_0_protocol_id',
    'portfolio_item_list_3_pool_adapter_id',
    
    'portfolio_item_list_3_detail_supply_token_list_1_amount',
    'portfolio_item_list_3_detail_supply_token_list_1_optimized_symbol',
    'portfolio_item_list_3_detail_supply_token_list_1_protocol_id']]
    
    #'portfolio_item_list_3_detail_supply_token_list_2_amount',
    #'portfolio_item_list_3_detail_supply_token_list_2_optimized_symbol',
    #'portfolio_item_list_3_detail_supply_token_list_2_protocol_id',
    
    #portfolio_item_list_0 - Borrow
    #'portfolio_item_list_0_detail_description',
    
    #'portfolio_item_list_0_detail_borrow_token_list_0_amount',
    #'portfolio_item_list_0_detail_borrow_token_list_0_optimized_symbol',
    #'portfolio_item_list_0_detail_borrow_token_list_0_protocol_id']]
    
    #################################################################
    #Melt supply/borrow token columns into rows
    
    df_1 = pd.melt(df_new,id_vars=[
    'Address',
    'id',
    'name',
    'portfolio_item_list_0_detail_supply_token_list_0_optimized_symbol',
    'portfolio_item_list_0_detail_supply_token_list_0_protocol_id',
    'portfolio_item_list_0_name',
    'portfolio_item_list_0_detail_types_0',
    'portfolio_item_list_0_pool_adapter_id'],
    
    value_vars =['portfolio_item_list_0_detail_supply_token_list_0_amount'])
    
    df_1.columns = ['Address','id','protocolName','Symbol','Protocol_id','Name','Detail_type',
                    'Adapter_id','Token_id','Amount']
    
    df_1['Token_id'] = 'supply' #Token_identifier
    
    #removed id_var = 'portfolio_item_list_0_detail_description',
    #removed column = 'Detail_info'
    
    #################################################################
    #Melt supply/borrow token columns into rows
    
    df_2 = pd.melt(df_new,id_vars=[
    'Address',
    'id',
    'name',
    'portfolio_item_list_0_name',
    'portfolio_item_list_0_detail_supply_token_list_1_optimized_symbol',
    'portfolio_item_list_0_detail_supply_token_list_1_protocol_id'],
    
    value_vars =['portfolio_item_list_0_detail_supply_token_list_1_amount'])
    
    df_2.columns = ['Address','id','protocolName','Name','Symbol','Protocol_id','Token_id','Amount']
    
    df_2['Token_id'] = 'supply' #Token_identifier
    
    #################################################################
    #Melt supply/borrow token columns into rows
    
    df_3 = pd.melt(df_new,id_vars=[
    'Address',
    'id',
    'name',
    'portfolio_item_list_0_name',
    'portfolio_item_list_0_detail_supply_token_list_2_optimized_symbol',
    'portfolio_item_list_0_detail_supply_token_list_2_protocol_id'],
    
    value_vars =['portfolio_item_list_0_detail_supply_token_list_2_amount'])
    
    df_3.columns = ['Address','id','protocolName','Name','Symbol','Protocol_id','Token_id','Amount']
    
    df_3['Token_id'] = 'supply' #Token_identifier
    
    #################################################################
    #Melt supply/borrow token columns into rows
    
    df_4 = pd.melt(df_new,id_vars=[
    'Address',
    'id',
    'name',
    'portfolio_item_list_0_name',
    'portfolio_item_list_0_detail_supply_token_list_3_optimized_symbol',
    'portfolio_item_list_0_detail_supply_token_list_3_protocol_id'],
    
    value_vars =['portfolio_item_list_0_detail_supply_token_list_3_amount'])
    
    df_4.columns = ['Address','id','protocolName','Name','Symbol','Protocol_id','Token_id','Amount']
    
    df_4['Token_id'] = 'supply' #Token_identifier
    
    #################################################################
    
    #Melt supply/borrow token columns into rows
    """
    df_5 = pd.melt(df_new,id_vars=[
    'Address',
    'id',
    'name',
    'portfolio_item_list_0_name',
    'portfolio_item_list_0_detail_supply_token_list_4_optimized_symbol',
    'portfolio_item_list_0_detail_supply_token_list_4_protocol_id'],
    
    value_vars =['portfolio_item_list_0_detail_supply_token_list_4_amount'])
    
    df_5.columns = ['Address','id','protocolName','Name','Symbol','Protocol_id','Token_id','Amount']
    
    df_5['Token_id'] = 'supply' #Token_identifier
    
    #################################################################
    
    #Melt supply/borrow token columns into rows
    
    df_6 = pd.melt(df_new,id_vars=[
    'Address',
    'id',
    'name',
    'portfolio_item_list_0_name',
    'portfolio_item_list_0_detail_supply_token_list_5_optimized_symbol',
    'portfolio_item_list_0_detail_supply_token_list_5_protocol_id'],
    
    value_vars =['portfolio_item_list_0_detail_supply_token_list_5_amount'])
    
    df_6.columns = ['Address','id','protocolName','Name','Symbol','Protocol_id','Token_id','Amount']
    
    df_6['Token_id'] = 'supply' #Token_identifier
    """
    #################################################################
    #Melt supply/borrow token columns into rows
    
    df_7 = pd.melt(df_new,id_vars=[
    'Address',
    'id',
    'name',
    'portfolio_item_list_1_detail_supply_token_list_0_optimized_symbol',
    'portfolio_item_list_1_detail_supply_token_list_0_protocol_id',
    'portfolio_item_list_1_name',
    'portfolio_item_list_1_pool_adapter_id'],
    
    value_vars =['portfolio_item_list_1_detail_supply_token_list_0_amount'])
    
    
    df_7.columns = ['Address','id','protocolName','Symbol','Protocol_id','Name','Adapter_id',
                    'Token_id','Amount']
    
    df_7['Token_id'] = 'supply' #Token_identifier
    
    ################################################################
    
    #Melt supply/borrow token columns into rows
    
    df_8 = pd.melt(df_new,id_vars=[
    'Address',
    'id',
    'name',
    'portfolio_item_list_1_detail_supply_token_list_1_optimized_symbol',
    'portfolio_item_list_1_detail_supply_token_list_1_protocol_id',
    'portfolio_item_list_1_name',
    'portfolio_item_list_1_pool_adapter_id'],
    
    value_vars =['portfolio_item_list_1_detail_supply_token_list_1_amount'])
    
    
    df_8.columns = ['Address','id','protocolName','Symbol','Protocol_id','Name','Adapter_id',
                    'Token_id','Amount']
    
    df_8['Token_id'] = 'supply' #Token_identifier
    
    #################################################################
    
    #Melt supply/borrow token columns into rows
    """
    df_9 = pd.melt(df_new,id_vars=[
    'Address',
    'id',
    'name',
    'portfolio_item_list_1_detail_supply_token_list_2_optimized_symbol',
    'portfolio_item_list_1_detail_supply_token_list_2_protocol_id',
    'portfolio_item_list_1_name',
    'portfolio_item_list_1_pool_adapter_id'],
    
    value_vars =['portfolio_item_list_1_detail_supply_token_list_2_amount'])
    
    
    df_9.columns = ['Address','id','protocolName','Symbol','Protocol_id','Name','Adapter_id',
                    'Token_id','Amount']
    
    df_9['Token_id'] = 'supply' #Token_identifier
    """
    #################################################################
    #Melt supply/borrow token columns into rows
    
    df_10 = pd.melt(df_new,id_vars=[
    'Address',
    'id',
    'name',
    'portfolio_item_list_2_detail_supply_token_list_0_optimized_symbol',
    'portfolio_item_list_2_detail_supply_token_list_0_protocol_id',
    'portfolio_item_list_2_name',
    'portfolio_item_list_2_pool_adapter_id'],
    
    value_vars =['portfolio_item_list_2_detail_supply_token_list_0_amount'])
    
    
    df_10.columns = ['Address','id','protocolName','Symbol','Protocol_id','Name','Adapter_id',
                    'Token_id','Amount']
    
    df_10['Token_id'] = 'supply' #Token_identifier
    
    #################################################################
    #Melt supply/borrow token columns into rows
    
    df_11 = pd.melt(df_new,id_vars=[
    'Address',
    'id',
    'name',
    'portfolio_item_list_2_detail_supply_token_list_1_optimized_symbol',
    'portfolio_item_list_2_detail_supply_token_list_1_protocol_id',
    'portfolio_item_list_2_name',
    'portfolio_item_list_2_pool_adapter_id'],
    
    value_vars =['portfolio_item_list_2_detail_supply_token_list_1_amount'])
    
    
    df_11.columns = ['Address','id','protocolName','Symbol','Protocol_id','Name','Adapter_id',
                    'Token_id','Amount']
    
    df_11['Token_id'] = 'supply' #Token_identifier
    #################################################################
    #Melt supply/borrow token columns into rows
    """
    df_12 = pd.melt(df_new,id_vars=[
    'Address',
    'id',
    'name',
    'portfolio_item_list_2_detail_supply_token_list_2_optimized_symbol',
    'portfolio_item_list_2_detail_supply_token_list_2_protocol_id',
    'portfolio_item_list_2_name',
    'portfolio_item_list_2_pool_adapter_id'],
    
    value_vars =['portfolio_item_list_2_detail_supply_token_list_2_amount'])
    
    
    df_12.columns = ['Address','id','protocolName','Symbol','Protocol_id','Name','Adapter_id',
                    'Token_id','Amount']
    
    df_12['Token_id'] = 'supply' #Token_identifier
    """
    #################################################################
    #Melt supply/borrow token columns into rows
    
    df_13 = pd.melt(df_new,id_vars=[
    'Address',
    'id',
    'name',
    'portfolio_item_list_3_detail_supply_token_list_0_optimized_symbol',
    'portfolio_item_list_3_detail_supply_token_list_0_protocol_id',
    'portfolio_item_list_3_name',
    'portfolio_item_list_3_pool_adapter_id'],
    
    value_vars =['portfolio_item_list_3_detail_supply_token_list_0_amount'])
    
    
    df_13.columns = ['Address','id','protocolName','Symbol','Protocol_id','Name','Adapter_id',
                    'Token_id','Amount']
    
    df_13['Token_id'] = 'supply' #Token_identifier
    #################################################################
    #Melt supply/borrow token columns into rows
    
    df_14 = pd.melt(df_new,id_vars=[
    'Address',
    'id',
    'name',
    'portfolio_item_list_3_detail_supply_token_list_1_optimized_symbol',
    'portfolio_item_list_3_detail_supply_token_list_1_protocol_id',
    'portfolio_item_list_3_name',
    'portfolio_item_list_3_pool_adapter_id'],
    
    value_vars =['portfolio_item_list_3_detail_supply_token_list_1_amount'])
    
    
    df_14.columns = ['Address','id','protocolName','Symbol','Protocol_id','Name','Adapter_id',
                    'Token_id','Amount']
    
    df_14['Token_id'] = 'supply' #Token_identifier
    #################################################################
    #Melt supply/borrow token columns into rows
    """
    df_15 = pd.melt(df_new,id_vars=[
    'Address',
    'id',
    'name',
    'portfolio_item_list_3_detail_supply_token_list_2_optimized_symbol',
    'portfolio_item_list_3_detail_supply_token_list_2_protocol_id',
    'portfolio_item_list_3_name',
    'portfolio_item_list_3_pool_adapter_id'],
    
    value_vars =['portfolio_item_list_3_detail_supply_token_list_2_amount'])
    
    
    df_15.columns = ['Address','id','protocolName','Symbol','Protocol_id','Name','Adapter_id',
                    'Token_id','Amount']
    
    df_15['Token_id'] = 'supply' #Token_identifier
    """
    #################################################################
    #Melt supply/borrow token columns into rows
    """
    df_16 = pd.melt(df_new,id_vars=[
    'Address',
    'id',
    'name',
    'portfolio_item_list_0_name',
    'portfolio_item_list_0_detail_borrow_token_list_0_optimized_symbol',
    'portfolio_item_list_0_detail_borrow_token_list_0_protocol_id'],
    
    value_vars =['portfolio_item_list_0_detail_borrow_token_list_0_amount'])
    
    df_16.columns = ['Address','id','protocolName','Name','Symbol','Protocol_id','Token_id','Amount']
    
    df_16['Token_id'] = 'borrow' #Token_identifier
    """
    ##############################################################
    #Aggregate dataframes and concatenate
    
    df_list = [df_1,df_2,df_3,df_4,df_7,df_8,df_10,df_11,df_13,df_14] #df_5,df_6,df_9,df_12,df_15,df_16
    
    #for df in df_list:
        #change all missing values to match with dataframe values
    
    df_agg = pd.concat(df_list)
    
    global df_last
    #remove rows that have amoun= nan
    df_last = df_agg[df_agg['Amount'].notna()]
    
    df_last['Timestamp'] = pd.to_datetime('now',utc=True)
        
    print(df_last)
