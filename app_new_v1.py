# Description: This file contains the code for the LLM load locally which is used to extract the information from the pdf files.
# Created on: 20th August 2024
# By: Dr Nirbhay Mathur (PhD)
# Contact: +91-9799030791

from langchain.chains import ConversationalRetrievalChain
from langchain.chains import RetrievalQA
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import CTransformers
from langchain.text_splitter import RecursiveCharacterTextSplitter
#from langchain.vectorstores import FAISS
from langchain_community.vectorstores import FAISS
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
import transformers
import torch
import warnings
from sentence_transformers import models
import pandas as pd
import re
warnings.filterwarnings("ignore")

import time
start = time.time()

def model(llm1):
    # Load the pdf files from the path
    loader = DirectoryLoader('Extracted/', glob="*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()
    print('Document loaded')

    # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    text_chunks = text_splitter.split_documents(documents)
    print('Text splitted')

    # Create embeddings (ensure using GPU)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2",
                                       model_kwargs={'device': "cuda" if torch.cuda.is_available() else "cpu"})
    print('Embedding creation done')

    # Create vector store
    vector_store = FAISS.from_documents(text_chunks, embeddings)
    print('Vector store created')

    # Initialize LLM
    llm = CTransformers(model="llama-2-13b-chat.Q8_0.gguf", model_type="llama",
                        config={'max_new_tokens': 1024, 'temperature': 0.01, 'context_length': 2000})  #max-1024, length:4096
    print('LLM setup done')

    # Define the prompt
    B_INST, E_INST = "[INST]", "[/INST]"
    B_SYS, E_SYS = "<<SYS>>\n", "\n<</SYS>>\n\n"
    DEFAULT_SYSTEM_PROMPT = '''
    <s>
    [INST]
    <<SYS>>
    You are a virtual assistant given the important task of taking a set of given {context} and using that context and only 
    that context tp answer a query in an intelligent manner. Try your hardest to find the answer within the context. 
    Do not under any circumstances use any outside knowledge not found in the documents. If the answer isn't within the documents, respond with 'Not found'
    </SYS>

    Text - Extract Property Address, City , State, County Legal Description, property type 
    JSON:
    [/INST]

    {{'City': ' ', 'County':' '  , 'Property Type': ' '}}

    [INST]
    Text - Extract total amount, manufacturing date from the text -- the part was manufactured on
    03/08/2002 and total cost was $30000.
    JSON:
    [/INST]

    {{'total amount': '$30000', 'manufacturing date': '03/08/2002'}}
    <s>

    [INST]
    Text - <question>{question}</question>
    JSON:
    [/INST]
    '''

    SYSTEM_PROMPT = B_SYS + DEFAULT_SYSTEM_PROMPT + E_SYS

    template = B_INST + SYSTEM_PROMPT + E_INST

    prompt = PromptTemplate(template=template, input_variables=["context", "question"])

   # Define the chain with updated API
    qa = RetrievalQA.from_llm(
        llm=llm,
        retriever=vector_store.as_retriever(search_kwargs={"k": 1}), #2
        prompt=prompt)
    print('QA chain setup done')

    print("Total setup time:", time.time() - start)

    # Process queries
    ques = []
    ans = []
    for query in llm1:
        print('Processing query:', query)
        res = qa(query)
        ques.append(query)
        a = res['result']
        print('result',a)
        a = a[re.search(':', a).start()+1:re.search('}', a).end()-1]
        print('refined',a)
        ans.append(a)

        df = pd.DataFrame()
        df['Question'] = ques
        df['Answer'] = a
        df.to_csv(r'Output.csv',index = False)

        
    
    return ques, ans

    #df = pd.DataFrame()
    #df['Question'] = ques
    #df['Answer'] = ans
    #df.to_csv(r'Loan_Aggrement.csv',index = False)
 
