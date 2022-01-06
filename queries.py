import authentication
import numpy as np

def get_names(service, sheet_id):
    query = "B1:C1"
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=sheet_id,
                                    range=query).execute()
    values = result.get('values', [])
    return values[0]

def get_total_score(service, sheet_id):
    query = "B2:C2"
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=sheet_id,
                                    range=query).execute()
    values = result.get('values', [])
    return values[0]

def get_champions(service, sheet_id):
    query = "A1:A200"
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=sheet_id,
                                    range=query).execute()
    values = result.get('values', [])
    champs = list(filter(lambda x: len(x) == 1, values))
    champs = np.array([x[0] for x in champs])
    return champs

def get_champion_score(service, sheet_id, row):
    query = f"B{row}:C{row}"
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=sheet_id,
                                    range=query).execute()
    values = result.get('values', [])
    return values

def increment(service, sheet_id, cell):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=sheet_id,
                                    range=cell).execute()
    value = result.get('values', [])
    val = 0
    if len(value) == 1 and len(value[0]) == 1:
        val = int(value[0][0])
    new_val = val + 1
    result = sheet.values().update(spreadsheetId=sheet_id,
                                    range=cell, valueInputOption="RAW" ,body={"values":[[new_val]]}).execute()
    return
    
