from pytubefix import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.messages import TextMessage, ToolCallRequestEvent, ToolCallExecutionEvent
from autogen_core import CancellationToken
from autogen_agentchat.base._chat_agent import Response
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()

async def GetvideoTranscript(url: str)-> str:
    """Gets the url of a video and returns th title, description and transcript."""
    ytt_api = YouTubeTranscriptApi()
    yt = YouTube(url)
    title = yt.title
    description = yt.description
    video_id = url.split('v=')[1].split('&')[0]
    transcript = ytt_api.fetch(video_id)
    transcript_text = ' '.join([item.text for item in transcript])

    res = f'Title: {title}\n\nDescription: {description}\n\nTranscript: {transcript_text}'
    return res

async def GetVideoTranscriptWithTimeStamps(url: str) -> str:
    """Gets the url of a video and returns th title, description and transcript with timestamps"""
    ytt_api = YouTubeTranscriptApi()
    yt = YouTube(url)
    title = yt.title
    description = yt.description
    video_id = url.split('v=')[1].split('&')[0]
    transcript = ytt_api.fetch(video_id)
    res = f'Title: {title}\n\nDescription: {description}\n\nTranscript with timestamp: {transcript}'
    return res   



def ConfigAgent():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not found in your environment")
    
    model = OpenAIChatCompletionClient(
        model = 'o3-mini',
        api_key = api_key
    )
    agent = AssistantAgent(
        name='YouTube_video_Proxy',
        system_message=(
            "You are a helful assistant. You will get the video url of a YouTube video and "
            "the user will ask question about the video. You can use the tools to answer "
            "the user's questions. If the answer to that question is not in the video, "
            "you should say that you don't know the answer."
            "If the question is asking when a particular event is happening, you should use 'GetVideoTranscriptWithTimeStamps' tool,"
            "otherwise, you should use 'GetvideoTranscript' tool."
            "When you are reporting a time in the video, you should use the format 'at 01:25' or 'at 1:25:15'."
        ),
        tools=[GetvideoTranscript, GetVideoTranscriptWithTimeStamps],
        reflect_on_tool_use=True,
        model_client = model,
    )
    return agent

async def AskAgent(agent, url, query):    
    
    task = f'this is the url of the video {url}. {query}' 

    async for msg in agent.on_messages_stream([TextMessage(source='user', content = task)],cancellation_token=CancellationToken()):
        if isinstance(msg, Response):
            print(message:=msg.chat_message.content)
            yield message
        else:
            print(message:=msg.to_text)
            yield msg

async def main(url, query):
    agent = ConfigAgent()
    await AskAgent(agent, url, query)



if __name__ == '__main__':
    url = 'https://www.youtube.com/watch?v=9_PepvnqIfU&t=5s'
    #query = 'Share a brief description of the video.'
    query = 'Does he mention Lionel Messi?'
    res = asyncio.run(main(url, query))

