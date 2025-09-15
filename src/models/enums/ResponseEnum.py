from enum import Enum

class ResponseSignal(Enum):
    
    FILE_VALIDATION_SUCCESS = "File validation successful"
    FILE_TYPE_NOT_ALLOWED = "File type not allowed"
    FILE_SIZE_EXCEEDS_LIMIT = "File size exceeds limit"
    FILE_UPLOADED_SUCCESSFULLY = "File uploaded successfully"
    FILE_UPLOADED_FAILED = "File upload failed"
    PROCESSING_SUCCESS = "Processing successful"
    PROCESSING_FAILED = "Processing failed"
    
