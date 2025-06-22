from ..utils.utils import llm
from langchain_core.prompts import PromptTemplate
from fastapi import APIRouter
from pydantic import BaseModel
from ..vectorstore.about import about_retriever
from ..prompts.about_prompt import about_prompt as prompt

router = APIRouter()

class QueryRequest(BaseModel):
    question: str
    
def get_llm_response(question) -> str:
    docs = about_retriever.invoke(question)
    prompt_template = PromptTemplate.from_template(prompt)
    chain = prompt_template | llm
    context = "\n".join(doc.page_content for doc in docs)
    
    llm_answer = chain.invoke({
            "context": context,
            "question": question
        })
    return llm_answer.content.strip()

    
@router.post("/ask")
def ask_question(request: QueryRequest):
    try:
        if request.question is None or request.question.strip() == "":
            return {"error": "Question is required."}
        result = get_llm_response(request.question)
        return {"answer": result }
    except Exception as e:
        print(f"Error processing question: {e}")
        return {"error": "An error occurred while processing your question."}
