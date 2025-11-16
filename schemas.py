"""
Database Schemas for the Plumber website

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- Lead -> "lead" collection
- Message -> "message" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Lead(BaseModel):
    """
    Leads collected from contact/quote forms
    Collection: "lead"
    """
    name: str = Field(..., description="Full name of the client")
    email: EmailStr = Field(..., description="Client email address")
    phone: Optional[str] = Field(None, description="Client phone number")
    service: Optional[str] = Field(None, description="Requested service (e.g., leak repair, installation)")
    message: Optional[str] = Field(None, description="Additional details provided by the client")
    preferred_time: Optional[str] = Field(None, description="Preferred time for contact or intervention")
    source: str = Field("website", description="Source of the lead")

class Message(BaseModel):
    """
    General messages from the contact form
    Collection: "message"
    """
    name: str = Field(..., description="Full name of the sender")
    email: EmailStr = Field(..., description="Sender email address")
    phone: Optional[str] = Field(None, description="Sender phone number")
    subject: Optional[str] = Field(None, description="Message subject")
    body: str = Field(..., description="Message content")
