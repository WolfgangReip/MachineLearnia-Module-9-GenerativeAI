import os 
from prompts import PROMPT_SUMMARIZE
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

def summarize(conversation: str) -> str:
    prompt_template = PROMPT_SUMMARIZE
    prompt = PromptTemplate(template=prompt_template, input_variables=["text"])
    
    print("OSGETVENV", os.getenv("OPENAI_MODEL"))
    
    llm = ChatOpenAI(
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        model=os.getenv("OPENAI_MODEL"),
        temperature=0.2,         
    )
    
    chain = prompt | llm | StrOutputParser()
    
    return chain.invoke(conversation)



def call_model(state: State, conversation: str) -> dict:
    llm = ChatOpenAI(
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        model=os.getenv("OPENAI_MODEL"),
        temperature=0.2,         
    )
    history = state.get("history", "")
    if history:
        system_message = f"Summarize of the conversation earlier: {history}"
        messages = [SystemMessage(content=system_message)] + state["messages"] 
    else:
        system_messages = System_PROMPT.format(conversation = conversation_summary)
        messages = [SystemMessage(content=system_message)] + state["messages"]

    response = llm.invoke(messages)
    return {"messages": response}