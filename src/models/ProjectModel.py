from .BaseDataModel import BaseDataModel
from .db_schemas import ProjectDBSchema
from .enums.DataBaseEnum import DataBaseEnum
from pymongo import InsertOne
from typing import List

class ProjectModel(BaseDataModel):
    
    def __init__(self, db_client: object):
        
        super().__init__(db_client)
        self.collection = self.db_client[DataBaseEnum.COLLECTION_PROJECT_NAME.value]

    async def create_project(self, project: ProjectDBSchema):
        
        result = await self.collection.insert_one(project.dict(exclude={"_id"}))
        project._id = result.inserted_id
        
        return project
        
    async def get_project_or_create_one(self, project_id: str):
        
        record = await self.collection.find_one(
            {"project_id": project_id}
            )
        
        if record is None:
            new_project = ProjectDBSchema(project_id=project_id)
            created_project = await self.create_project(new_project)
            
            return created_project
        
        return ProjectDBSchema(**record)
    
    async def get_all_projects(self, page: int = 1, page_size: int = 10):
        
        total_documents = await self.collection.count_documents({})
        total_pages = total_documents // page_size + (1 if total_documents % page_size > 0 else 0)

        cursor = self.collection.find().skip((page - 1) * page_size).limit(page_size)
        projects = []
        async for document in cursor:
            projects.append(ProjectDBSchema(**document))
            
        return projects, total_pages
