from openai import OpenAI
import yt_dlp
import os

os.environ["OPENAI_API_KEY"] = ""#OpenAI API Key
client = OpenAI()

# YouTube 비디오에서 오디오 다운로드
def download_audio_from_youtube(url, output_path='audio'):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': output_path,
        'quiet': True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return output_path + ".mp3"
    except Exception as e:
        print(f"An error occurred: {e}")
    return None

# OpenAI의 Whisper를 사용하여 오디오 텍스트 변환
def transcribe_audio(file_path):
    try:
        with open(file_path, 'rb') as audio_file:
            transcription = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )
        return transcription.text
    except openai.error.InvalidRequestError as e:
        print(f"Invalid request error: {e}")
    except openai.error.APIError as e:
        print(f"API error: {e}")
    except openai.error.OpenAIError as e:
        print(f"OpenAI error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None

def get_youtube_transcription(youtube_url, save_path="transcription.txt"):
    audio_path = download_audio_from_youtube(youtube_url)
    if audio_path:
        transcription = transcribe_audio(audio_path)
        if transcription:
            #print(transcription)
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            with open(save_path, "w", encoding="utf-8") as file:
                file.write(transcription)
        else:
            print("Transcription failed.")
        os.remove(audio_path)  # 변환 후 오디오 파일 삭제

        return transcription
    else:
        print("Audio download failed.")


youtube_url = ""#youtube url
save_path = 'youtube/script.txt'
#유튜브 비디오에서 텍스트 추출
text = get_youtube_transcription(youtube_url, save_path)



from llama_index.llms.openai import OpenAI
from llama_index.core import Settings

Settings.llm = OpenAI(model="gpt-4-turbo")

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
from llama_index.embeddings.openai import OpenAIEmbedding
import chromadb



# create client and a new collection
chroma_client = chromadb.EphemeralClient() #on memory
chroma_collection = chroma_client.create_collection("youtube_summary") # 1번만 실행합니다!

from llama_index.core.node_parser import SentenceSplitter
import requests

# define embedding function
embed_model = OpenAIEmbedding(
    model="text-embedding-3-small",
)

# load documents
documents = SimpleDirectoryReader("youtube/").load_data()

# set up ChromaVectorStore and load in data
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context, embed_model=embed_model
)
# Query Data
query_engine = query_engine = index.as_query_engine()

prompt = f"""
#script.txt 파일을 읽고 내용을 한글로 요약하려고해 아래 모든 내용들은 한글로 작성해줘
제목을 만든 뒤
핵심적인 주제를 먼저 서술해주고
상세 내용을 설명해줘

형태는 아래와 같아 각 항목들 사이에는 1줄씩 띄워줘
제목 :

주제 :

상세 내용 :
"""

response = query_engine.query(prompt)

response_text = response.response
response_text += f'\n\n링크 : {youtube_url}'

print(response_text)


url = ""#agit webhook url

payload = {
    "text": response_text
}

response = requests.post(url, json=payload)

print(response.text)
