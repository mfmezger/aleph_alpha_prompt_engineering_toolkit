import wandb
from datetime import datetime
from langchain.callbacks.manager import CallbackManager
from utils import generate_prompt
from loguru import logger
from langchain import PromptTemplate, LLMChain
from langchain.callbacks import WandbCallbackHandler, StdOutCallbackHandler
from langchain.llms import AlephAlpha
from dotenv import load_dotenv
import os



load_dotenv()
os.environ["LANGCHAIN_WANDB_TRACING"] = "true"
os.environ["WANDB_PROJECT"] = "llm_course"
ALEPH_ALPHA_API_KEY = os.getenv("ALEPH_ALPHA_API_KEY")



# session_group = datetime.now().strftime("%m.%d.%Y_%H.%M.%S")
# wandb_callback = WandbCallbackHandler(
#     group=f"minimal_{session_group}",
#     job_type="inference",
#     project="llm_course",
#     name="llm",
#     tags=["test"],
# )
# manager = CallbackManager([StdOutCallbackHandler(), wandb_callback])
# logger.info("SUCCESS: Initalized Callback Manager.")

llm = AlephAlpha(temperature=0.7, verbose=True, model="luminous-extended", maximum_tokens=20, stop_sequences=["###"], aleph_alpha_api_key=ALEPH_ALPHA_API_KEY,) # callback_manager=manager, 


prompt_list  = ["What is  the  meaning  of  life?", "What  is the biological meaning of life?"]

prompt_template = "{question}"
prompt = PromptTemplate(
    input_variables=["question"], template=prompt_template
            )
answer_list = []
llm_chain = LLMChain(prompt=prompt, llm=llm)

for p in prompt_list:
    answer_list.append(llm_chain.run(p))

print(answer_list)
