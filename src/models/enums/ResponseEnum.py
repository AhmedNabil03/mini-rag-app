from enum import Enum

class ResponseSignal(Enum):
    
    FILE_VALIDATION_SUCCESS = "File validation successful"
    FILE_TYPE_NOT_ALLOWED = "File type not allowed"
    FILE_SIZE_EXCEEDS_LIMIT = "File size exceeds limit"
    FILE_UPLOADED_SUCCESSFULLY = "File uploaded successfully"
    FILE_UPLOADED_FAILED = "File upload failed"
    PROCESSING_SUCCESS = "Processing successful"
    PROCESSING_FAILED = "Processing failed"
    NO_FILES_TO_PROCESS = "No files to process"
    NO_FILE_TO_PROCESS = "No file with this id to process"
    PROJECT_NOT_FOUND = "Project not found"
    INSERT_INTO_VECTORDB_ERROR = "Insert into vectordb error"
    INSERT_INTO_VECTORDB_SUCCESS = "Insert into vectordb success"
    VECTORDB_COLLECTION_RETRIEVED = "VectorDB collection retrieved successfully"
    VECTORDB_SEARCH_SUCCESS = "VectorDB search success"
    VECTORDB_SEARCH_ERROR = "Error while searching VectorDB collection"
    RAG_ANSWER_SUCCESS = "RAG answer success"
    RAG_ANSWER_ERROR = "RAG answer error"
