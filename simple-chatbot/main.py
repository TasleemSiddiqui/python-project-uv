import chainlit as cl


@cl.on_message
async def simple_chat(message: cl.Message):
    respone = f"you said: \n {message.content}"
    
    
    
    await cl.Message(content=respone).send()
    