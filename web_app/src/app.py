
import gradio as gr
import requests


def predict(question):
    data = {"prompt": question}	
    print("Testing....")
    res=requests.post("http://myservice.sm-llm-demo.internal/v1/models/model:predict", json=data)
    print(res.json())
    return res.json()

examples = [
    ["Who is Lionel Messi"],
    ["Explain quantum physics"],
    ["What is the capital of France and Germany"],
]
logo_html = '<div style="text-align: center;"><img src="file/falcon.jpeg" alt="Logo" style="height: 100px;"></div>'

demo = gr.Interface(
    predict, 
    [ gr.Textbox(label="Enter prompt:", value="Who is Lionel Messi?"),
      
    ],
    "text",
    examples=examples,
    title= "My KnowledgeBot" +logo_html
    )

demo.launch(server_name="0.0.0.0", server_port=7860)