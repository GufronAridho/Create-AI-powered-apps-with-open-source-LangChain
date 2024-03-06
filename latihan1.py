import gradio as gr
from langchain_openai import ChatOpenAI

openai_api_key = "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"

# Define the model
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    openai_api_key=openai_api_key
)

def generateAnswer(question: str) -> str:
    prompt = f"Question: {question} please provide step by step Answer:"
    response = llm.invoke(prompt).content
    return response

inputs = [
    gr.Textbox(label="question"),
]

output = gr.Textbox(label="Template")

gr.Interface(fn=generateAnswer, inputs=inputs, outputs=output).launch(share=True)
