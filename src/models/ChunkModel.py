from .BaseDataModel import BaseDataModel
from .db_schemas import DataChunkDBSchema
from .enums.DataBaseEnum import DataBaseEnum
from bson.objectid import ObjectId
from pymongo import InsertOne

class ChunkModel(BaseDataModel):
    
    def __init__(self, db_client):
        super().__init__(db_client)
        self.collection = self.db_client[DataBaseEnum.COLLECTION_CHUNK_NAME.value]
    
    def create_chunk(self, chunk: DataChunkDBSchema):
        result = self.collection.insert_one(chunk.dict(by_alias=True, exclude_unset=True))
        chunk._id = result.inserted_id
        
        return chunk
    
    def get_chunk(self, chunk_id: str):
        record = self.collection.find_one({"_id": ObjectId(chunk_id)})

        if record is None:
            return None
        
        return DataChunkDBSchema(**record)
    
    async def insert_many_chunks(self, chunks: list, batch_size: int=100):
        for i in range(0, len(chunks), batch_size):
            batch = chunks[i:i+batch_size]

            operations = [
                InsertOne(chunk.dict(by_alias=True, exclude_unset=True))
                for chunk in batch
            ]

            await self.collection.bulk_write(operations)
        
        return len(chunks)
    
    async def delete_chunks_by_project_id(self, project_id: str):
        result = await self.collection.delete_many({"chunk_project_id": ObjectId(project_id)})
        
        return result.deleted_count
    