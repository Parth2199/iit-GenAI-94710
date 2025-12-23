from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.tools import tool
from langchain.agents.middleware import wrap_model_call
import os
import requests

load_dotenv()

WEATHER_API_KEY = os.getenv("OPEN_WEATHER_API")

llm = init_chat_model(
    model="google/gemma-3n-e4b",
    model_provider="openai",
    base_url="http://10.45.159.113:1234/v1",
    api_key="lm-studio"
)

@tool
def calculator(expression: str) -> str:
    """Evaluate a mathematical expression."""
    allowed = {"__builtins__": {}}
    return str(eval(expression, allowed))


@tool
def file_reader(path: str) -> str:
    """Read a text file and return its content."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

@tool
def current_weather(city: str) -> str:
    """Get current weather details for a city."""
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "metric"
    }
    r = requests.get(url, params=params, timeout=8)
    r.raise_for_status()
    d = r.json()
    return (
        f"Temperature: {d['main']['temp']}°C, "
        f"Feels like: {d['main']['feels_like']}°C, "
        f"Humidity: {d['main']['humidity']}%, "
        f"Weather: {d['weather'][0]['description']}"
    )

@tool
def knowledge_lookup(topic: str) -> str:
    """Provide general information about a topic."""
    return f"General information about {topic}"

tools = [
    calculator,
    file_reader,
    current_weather,
    knowledge_lookup,
    ]

@wrap_model_call
def log_middleware(request,handler):
    """
    Logs each model req and reps for debugging
    """
    print(f"Req msg count :{len(request.messages)}")

    #call next handler
    response=handler(request)

    print("Model responded")
    return response

agent = create_agent(
    model=llm,
    tools=tools,
    middleware=[log_middleware]
)

def log_messages(messages):
    print("----- MESSAGE HISTORY -----")
    for m in messages:
        print(m)
    print("---------------------------")


math = input("Enter math equation : ")
response1 = agent.invoke({
    "messages": [
        {"role": "user", "content": math}
    ]
})
log_messages(response1["messages"])
print("Final Answer:", response1["messages"][-1].content)





city = input("enter message(for weather)  :")
response2 = agent.invoke({
    "messages": [
        {"role": "user", "content": city}
    ]
})
log_messages(response2["messages"])
print("Final Answer:", response2["messages"][-1].content)





path = input("Give path : ")
response3 = agent.invoke({
    "messages": [
        {"role": "user", "content": f"Read thi filr and return the content : {path}"}
    ]
})
log_messages(response3["messages"])
print("Final Answer:", response3["messages"][-1].content)





response4 = agent.invoke({
    "messages": [
        {"role": "user", "content": "Explain LangChain"}
    ]
})
log_messages(response4["messages"])
print("Final Answer:", response4["messages"][-1].content)