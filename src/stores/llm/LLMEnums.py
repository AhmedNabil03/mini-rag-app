from enums import Enum

class LLMEnum(Enum):
    OPENAI = "openai"
    COHERE = "cohere"

class OpenAIEnums(Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
