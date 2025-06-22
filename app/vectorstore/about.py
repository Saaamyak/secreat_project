import os
from langchain_astradb import AstraDBVectorStore
from ..utils.utils import embeddings

vector_persona_store = AstraDBVectorStore(
    collection_name="Sam_G",
    embedding=embeddings,
    api_endpoint=os.environ["ASTRA_DB_ABOUT_API_ENDPOINT"],
    token=os.environ["ASTRA_DB_APPLICATION_TOKEN"],
)

about_retriever = vector_persona_store.as_retriever(search_kwargs={"k": 2})