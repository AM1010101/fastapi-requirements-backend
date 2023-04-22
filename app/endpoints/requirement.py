from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
import psycopg2
from psycopg2.extras import RealDictCursor

router = APIRouter()

# Define the data model
class Requirement(BaseModel):
    id: str
    title: str
    description: str
    status: str
    priority: str
    created_by: str
    created_at: str
    updated_at: str
    assigned_to: str

# Define a function to connect to the PostgreSQL database
def get_db_conn():
    conn = psycopg2.connect(
        host="your_host",
        database="your_database",
        user="your_username",
        password="your_password"
    )
    return conn

# Define the API endpoints
@router.post("/requirements")
async def create_requirement(requirement: Requirement):
    conn = get_db_conn()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(
        "INSERT INTO requirements (id, title, description, status, priority, created_by, created_at, updated_at, assigned_to) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (requirement.id, requirement.title, requirement.description, requirement.status, requirement.priority, requirement.created_by, requirement.created_at, requirement.updated_at, requirement.assigned_to)
    )
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Requirement created successfully"}

@router.get("/requirements")
async def get_requirements():
    conn = get_db_conn()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM requirements")
    requirements = cur.fetchall()
    cur.close()
    conn.close()
    return requirements

@router.get("/requirements/{requirement_id}")
async def get_requirement(requirement_id: str):
    conn = get_db_conn()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM requirements WHERE id = %s", (requirement_id,))
    requirement = cur.fetchone()
    cur.close()
    conn.close()
    if requirement is None:
        raise HTTPException(status_code=404, detail="Requirement not found")
    return requirement

@router.put("/requirements/{requirement_id}")
async def update_requirement(requirement_id: str, requirement: Requirement):
    conn = get_db_conn()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("UPDATE requirements SET title = %s, description = %s, status = %s, priority = %s, created_by = %s, created_at = %s, updated_at = %s, assigned_to = %s WHERE id = %s",
                (requirement.title, requirement.description, requirement.status, requirement.priority, requirement.created_by, requirement.created_at, requirement.updated_at, requirement.assigned_to, requirement_id))
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Requirement updated successfully"}

@router.delete("/requirements/{requirement_id}")
async def delete_requirement(requirement_id: str):
    conn = get_db_conn()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("DELETE FROM requirements WHERE id = %s", (requirement_id,))
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Requirement deleted successfully"}
