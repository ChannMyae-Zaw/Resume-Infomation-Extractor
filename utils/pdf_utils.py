from langchain_community.document_loaders import PyPDFLoader

def extract_text_from_pdf(path: str) -> str:
    loader = PyPDFLoader(path)
    pages = loader.load()
    return pages[0].page_content if pages else ""
