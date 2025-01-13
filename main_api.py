from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI

# Initialize FastAPI app
app = FastAPI()

# Define the input schema
class ChatRequest(BaseModel):
    assignment: str
    question: str

# Initialize the OpenAI client
client = OpenAI(
    api_key="sk-ZHBoHGDDtUW9UlFvdYyfMldgGJdHJPwc4s18bUN249BmyXDq",
    base_url="https://api.opentyphoon.ai/v1"
)

@app.post("/chat/")
async def generate_response(request: ChatRequest):
    """
    Endpoint to handle OpenAI chat completion requests.
    Takes 'assignment' and 'question' as input and returns the model's response.
    """
    try:
        # Call the OpenAI API
        chat_completion = client.chat.completions.create(
            model="typhoon-v1.5x-70b-instruct",
            messages=[
                {
                    "role": "system",
                    "content": request.assignment  # Assignment string
                },
                {
                    "role": "user",
                    "content": request.question  # Question string
                }
            ]
        )
        print(chat_completion.choices[0].message.content)
        # Extract and return the response
        return {
            "response": chat_completion.choices[0].message.content
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
