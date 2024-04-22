from langchain.document_loaders import PyPDFLoader
from chunking_module import TextChunker

def test_chunking():
    file_path = "./chunking/Jacksonville_FL.pdf"
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    documents_content = '\n'.join(doc.page_content for doc in documents)
    _chunker = TextChunker(600, 50,  separators = ['\n','\n\n'])
    chunks = _chunker.chunk_text(documents_content)
    print(len(chunks))
    



if __name__ == "__main__":
    test_chunking()