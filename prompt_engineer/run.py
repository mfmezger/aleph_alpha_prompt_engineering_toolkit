import wandb
from datetime import datetime
from langchain.callbacks.base import CallbackManager
from utils import generate_prompt
from loguru import logger
from langchain import PromptTemplate, LLMChain
from langchain.callbacks import WandbCallbackHandler, StdOutCallbackHandler
from langchain.llms import AlephAlpha
from dotenv import load_dotenv
import os



load_dotenv()
os.environ["LANGCHAIN_WANDB_TRACING"] = "true"
os.environ["WANDB_PROJECT"] = "langchain-test"



session_group = datetime.now().strftime("%m.%d.%Y_%H.%M.%S")
wandb_callback = WandbCallbackHandler(
    group=f"minimal_{session_group}",
    job_type="inference",
    project="langchain-test",
    name="llm",
    tags=["test"],
)
manager = CallbackManager([StdOutCallbackHandler(), wandb_callback])
logger.info("SUCCESS: Initalized Callback Manager.")

llm = AlephAlpha(temperature=0, callback_manager=manager, verbose=True, model="luminous-extended", maximum_tokens=20, stop_sequences=["###"], aleph_alpha_api_key=ALEPH_ALPHA_API_KEY,)


# TODO: research if langchain way better than jinja2 way.
# load the prompts depends on mode 

# single prompt

# multi propt evaluation


llm_chain = LLMChain(prompt=prompt, llm=llm)
answer = llm_chain.run("What is?")

# iterate over the questions
# for question in questions:
    # answer = llm_chain.run(question)

# TODO: is it necessary to log the prompt?
# TODO: it is necessary to commit the final run?
