from pydantic import BaseModel, Field

# Define the document schema using Pydantic
class EmailSchema(BaseModel):
    recipient_name: str = Field(default_factory=str, description="Name of the dummy recipient")
    recipient_email: str = Field(default_factory=str, description="Email address of the dummy recipient")
    subject: str = Field(default_factory=str, description="Subject for the email")
    body: str = Field(default_factory=str, description="Body of the email along with salutation following above instruction")
    product_url: str = Field(default_factory=str, description="Generated synthetic product URL")
