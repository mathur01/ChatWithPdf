# Description: This file contains the main code for extacting and asking questions from each different file from the pdf files.
# Created on: 20th August 2024
# By: Dr Nirbhay Mathur (PhD)
# Contact: +91-9799030791

import os
import questionnaire 
import shutil
#from app_new_lamma3 import model
from app_new_v1 import model
#from main_merge import model

path1 = "Path from where files need to be extracted"
path_to_copy = "Path where files need to be copied"
address_file = []
sponsor = []
deal = []
rental_appraisal=[]
prop_insurance = []
promissory_note=[]
settlement= []
flood=[]
prop_detail=[]
prop_tax=[]

## Code to locate the specific folders
for i in os.listdir(path1):
    folder = os.path.join(path1,i)
    print(folder)
    for j in os.listdir(folder):
        sub_folder = os.path.join(folder,j)
        print('subfolder')
        print(sub_folder)
        if 'flood_certificate' in '\t'.join(os.listdir(sub_folder)).lower():
            print('yes flood_certificate found')
            flood.append(sub_folder)
        if 'appraisal' in '\t'.join(os.listdir(sub_folder)).lower():
            print('yes appraisal found')
            rental_appraisal.append(sub_folder)    
        if 'sponsor_application' in '\t'.join(os.listdir(sub_folder)).lower():
            print('yes sponsor_application found')
            sponsor.append(sub_folder)
        if 'deal' in j.lower():
            print('yes deal found')
            deal.append(sub_folder)
        if 'detail' in '\t'.join(os.listdir(sub_folder)).lower():
            print('yes property detail found')
            prop_detail.append(sub_folder)
        if 'insurance' in '\t'.join(os.listdir(sub_folder)).lower():
            print('yes property insurance found')
            prop_insurance.append(sub_folder)
        if 'loan_package' in '\t'.join(os.listdir(sub_folder)).lower():
            print('yes loan package found')
            promissory_note.append(sub_folder)
        if 'loan_package' in '\t'.join(os.listdir(sub_folder)).lower():
            print('yes settlement package found')
            settlement.append(sub_folder)
        if 'tax' in '\t'.join(os.listdir(sub_folder)).lower():
            print('yes tax package found')
            prop_tax.append(sub_folder)
            


print("name path",sponsor)
print("address path",address_file)
print("rental apraisal",rental_appraisal)
print("deal address",deal)
print("Propert Insurance",prop_insurance )
print("Loan Package",promissory_note )
print("Settlement Statement",settlement )
print("Flood Certificate",flood )
print("property detail",prop_detail)
print("property tax",prop_tax)

# # for flood certificate 
for i in flood:
    
    for j in os.listdir(i):
        
        if 'flood_certificate' in j.lower():   
              
            source = os.path.join(i, j)
            dest = os.path.join(path_to_copy, j)
            shutil.copy(source, dest)
            print('file copied')
            # print('data copied')
            queries = questionnaire.flood()     
            print('queries')
            # print(queries)
            ques, ans = model(queries)
            print('model run complete')
        shutil.rmtree(path_to_copy)
        os.mkdir(path_to_copy)





# for sponsor application
# for i in sponsor:
#     #print("In for loop")
#     for j in os.listdir(i):
#         #print("Above sponser")
#         if 'sponsor_application' in j.lower():   
#             #print("after sponser")  
#             source = os.path.join(i, j)
#             dest = os.path.join(path_to_copy, j)
#             shutil.copy(source, dest)
#             print('file copied')
#             # print('data copied')
#             queries = questionnaire.sponsor()     
#             print('queries')
#             # print(queries)
#             ques, ans = model(queries)
#             print('model run complete')
#         shutil.rmtree(path_to_copy)
#         os.mkdir(path_to_copy)

# for rental appraisal  #rental30_appraisal
# for i in rental_appraisal:
#     #print("In for loop")
#     for j in os.listdir(i):
#         #print("Above sponser")
#         if 'appraisal' in j.lower():     
            
#             source = os.path.join(i, j)
#             dest = os.path.join(path_to_copy, j)
#             shutil.copy(source, dest)
#             print('file copied')
#             # print('data copied')
#             queries = questionnaire.appraisal()     
#             print('queries')
#             # print(queries)
#             ques, ans = model(queries)
#             print('model run complete')
#         shutil.rmtree(path_to_copy)
#         os.mkdir(path_to_copy)


# for property detail
# for i in prop_detail:
    
#     for j in os.listdir(i):
        
#         if 'detail' in j.lower():     
            
#             source = os.path.join(i, j)
#             dest = os.path.join(path_to_copy, j)
#             shutil.copy(source, dest)
#             print('file copied')
#             # print('data copied')
#             queries = questionnaire.prop_detail()     
#             print('queries')
#             # print(queries)
#             ques, ans = model(queries)
#             print('model run complete')
#         shutil.rmtree(path_to_copy)
#         os.mkdir(path_to_copy)





#for property Insuarance
# for i in prop_insurance:
#     #print("In for loop")
#     for j in os.listdir(i):
#         #print("Above sponser")
#         if 'insurance' in j.lower():   
            
#             source = os.path.join(i, j)
#             dest = os.path.join(path_to_copy, j)
#             shutil.copy(source, dest)
#             print('file copied')
#             # print('data copied')
#             queries = questionnaire.prop_insurance()     
#             print('queries')
#             # print(queries)
#             ques, ans = model(queries)
#             print('model run complete')
#             print('Model run complete')
#             print('Questions:', ques)
#             print('Answers:', ans)
#         shutil.rmtree(path_to_copy)
#         os.mkdir(path_to_copy)


#for property Tax
for i in prop_tax:
    
    for j in os.listdir(i):
        
        if 'tax' in j.lower():   
              
            source = os.path.join(i, j)
            dest = os.path.join(path_to_copy, j)
            shutil.copy(source, dest)
            print('file copied')
            # print('data copied')
            queries = questionnaire.prop_tax()     
            print('queries', queries)
            # print(queries)
            ques, ans = model(queries)
            print('model run complete')
        shutil.rmtree(path_to_copy)
        os.mkdir(path_to_copy)



# for sponsor/ flood certificate application
# for i in address_file:
    
#     for j in os.listdir(i):
        
#         if 'sponsor_application' in j.lower():   
              
#             source = os.path.join(i, j)
#             dest = os.path.join(path_to_copy, j)
#             shutil.copy(source, dest)
#             print('file copied')
#             # print('data copied')
#             queries = questionnaire.sponsor()     
#             print('queries')
#             # print(queries)
#             ques, ans = model(queries)
#             print('model run complete')
#         shutil.rmtree(path_to_copy)
#         os.mkdir(path_to_copy)

# for PROMISSORY_NOTE
# for i in promissory_note:
#     #print("In for loop")
#     for j in os.listdir(i):
#         #print("Above sponser")
#         if 'loan_package' in j.lower():   
            
#             source = os.path.join(i, j)
#             dest = os.path.join(path_to_copy, j)
#             shutil.copy(source, dest)
#             print('file copied')
#             # print('data copied')
#             queries = questionnaire.promissory_note()     
#             print('queries')
#             # print(queries)
#             ques, ans = model(queries)
#             print('model run complete')
#         shutil.rmtree(path_to_copy)
#         os.mkdir(path_to_copy)

# for SETTLEMENT STATEMENT

# for i in settlement:
#     #print("In for loop")
#     for j in os.listdir(i):
#         #print("Above sponser")
#         if 'settlement_statement' in j.lower():   
            
#             source = os.path.join(i, j)
#             dest = os.path.join(path_to_copy, j)
#             shutil.copy(source, dest)
#             print('file copied')
#             # print('data copied')
#             queries = questionnaire.settlement()     
#             print('queries')
#             # print(queries)
#             ques, ans = model(queries)
#             print('model run complete')
#         shutil.rmtree(path_to_copy)
#         os.mkdir(path_to_copy)