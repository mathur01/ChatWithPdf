# Description: This file contains the code for asking questions from eac different file from the pdf files.
# Created on: 20th August 2024
# By: Dr Nirbhay Mathur (PhD)
# Contact: +91-9799030791
def sponsor():
    queries = [#Extract the Name in the format Last Name, First Name. The first and last name can be found in a table. Extract only asked value.',
               ]
    print(queries)
    return queries

def flood():
    queries = [
               'What is the value of "Flood Zone" privided in document.']
    #queries = ['Extract the flood zone value only']
    
    #res = qa('Extract the Order')
    #print(res)

    #res = qa('Extract the flood zone value only')
    #print(queries)
    return queries

def appraisal():
    queries = [
               'extract the street address '
                "]
    return queries

def prop_detail():
    queries = ['Extract the property use value from the property details report. ']
    return queries

def prop_insurance():
    queries = [' Extract the insurance company name.']
    return queries


# def prop_tax():
#     queries = [' Extract the total tax value in $.',
#                ' Extract the total tax value in $.'
#                ]
#     return queries


def prop_tax():
    queries = [' Extract the total tax value in $.',
              
    ]
    return queries


def promissory_note():
    queries = ["Extract the First Payment Due Date from the text. Store date as Next Due Date in following format 'Month Date Year'."]
                
    return queries

def settlement():
    queries = ["Extract the NAME AND ADDRESS OF BORROWER." ]
    return queries