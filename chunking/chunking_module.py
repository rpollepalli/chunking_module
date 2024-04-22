

from langchain.text_splitter import RecursiveCharacterTextSplitter
import time
from chunker import Chunker
from typing import Any,List, Optional, Dict,Literal
from langchain_core.embeddings import Embeddings
from langchain_experimental.text_splitter import SemanticChunker
from langchain_core.documents import Document
 
class TextChunker(Chunker):
    
    
    def __init__(
        self,
        chunk_size: int = 600,
        chunk_overlap: int = 200,
        separators: Optional[List[str]] = None,
    ) -> None:
        self._chunk_size = chunk_size
        self._chunk_overlap = chunk_overlap
        self._separators = separators
        

    def chunk_text(self,  text,) -> List[str]:
        return self._chunk_text(self._chunk_size,self._chunk_overlap,text,self._separators)
        
        
    def _chunk_text(self,chunk_size, chunk_overlap,text: str,separators: Optional[List[str]] = None,)-> list[str]:
        start_time = time.perf_counter
        print(f"\t\t\tStarted the chunking the text ")
        # Initialize the text splitter with custom parameters
        splitter = RecursiveCharacterTextSplitter(
            # Set custom chunk size
            chunk_size = chunk_size,
            chunk_overlap  = chunk_overlap,
            # Use length of the text as the size measure
            length_function = len,
            # Use only "\n\n" as the separator
            separators = separators

        )       
        # Create the chunk    
        final_texts= splitter.split_text(text)
        end_time = time.perf_counter
        
        print(f"\t\t\tEnded the chunking the text ")
        return final_texts
    
   
    
            
    # class SemanticTextChunker(Chunker,SemanticChunker):
       
        
    #     def __init__(
    #         self,
    #         embeddings: Embeddings,
    #         buffer_size: int = 1,
    #         add_start_index: bool = False,
    #         breakpoint_type:str ="",
    #         breakpoint_threshold_amount: Optional[float] = None,
    #         number_of_chunks: Optional[int] = None,
    #     ):        
    #         self._embeddings = embeddings
    #         self._buffer_size = buffer_size
    #         self._breakpoint_threshold_type = super.BreakpointThresholdType=breakpoint_type
    #         self._number_of_chunks = number_of_chunks
    #         if breakpoint_threshold_amount is None:
    #             self._breakpoint_threshold_amount = super.BREAKPOINT_DEFAULTS[
    #                 self._breakpoint_threshold_type 
    #             ]
    #         else:
    #             self._breakpoint_threshold_amount = breakpoint_threshold_amount
            
        
    # def chunk_text(self,  text,) -> List[Document]:
    #     return self._chunk_text(self._embeddings,self._buffer_size,text,self._separators)
        