# GPTCustomerAssistant

## Demonstration
https://github.com/weibb123/GPTCustomerAssistant/assets/84426364/86f23290-6642-42e0-9dbd-2f11fe2b8cd1

## Key Accomplishment: 
Utilizing Large Language Model to design a new way for customers to shop online.

## Table of Contents

  - [Business problem](#business-problem)
  - [Data source](#data-source)
  - [Methods](#methods)
  - [Tech Stack](#tech-stack)
  - [Lessons learned and recommendation](#lessons-learned-and-recommendation)
  - [Limitation and what can be improved](#limitation-and-what-can-be-improved)
  - Evaluation(#Evaluation)
  - [Reference](#reference)


## Business Problem

This web app allows users to ask question about available products that are being sell and efficiently learn about the available products without human intervene.

## Data Source
Electronic products that are made up or from online search. Each product in store as JSON format.

## Methods

- OPENAI API
- PROMPT ENGINEERING
- DIALOG MANAGEMENT(CHAT HISTORY)
- MODEL DEPLOYMENT

## Tech Stack

- Python/LangChain (Main coding)
- OPENAI API (Leveraging Large Language Model)
- STREAMLIT (UI for the system)

## Lessons learned and recommendation
The difficult part of building this web app is to include chat history in the system. I learned that OPENAI CHATGPT API does not have the components to store chat history. Thankfully, Langchain has the ability to add memory in LLM Chains. Now, the difficult part is to learn more about streamlit(frontend for the chatbot) and store user's input inside langchain's llm chain. I believe that chat history is an essential component especially chatbot with conversational capabilities. The times that you might not need chat history but nice to have is when building a question answering chatbot mainly information retreival.


## Limitation and what can be improved
So far this chatbot support limited categories.

Suppose the allowed products or categories expand, because OPENAI's API only support limited number of tokens, it is impossible to feed in the original size to the large language model since it exceeds maximum token limits.

One possible solution:

Given user's input, perform a similarity search through the data and check if user's sentence match any allowed products or categories in the data. \
Either ML model with some sort of distance metric or use GPT's great ability to understand context to do similarity search but at a cost of API call.

## Evaluation

Although this webapp does not include evaluation.., one can certainly use different evaluation methods to evaluate success.\
BLEU score: comparing human response and GPT response\
OPENAI API Check: Check whether GPT response contains harmful content\
Human validation: Check if GPT reponse match with what human will typically response.

## Reference
https://python.langchain.com/docs/modules/memory/how_to/adding_memory

https://docs.streamlit.io/library/api-reference/session-state












