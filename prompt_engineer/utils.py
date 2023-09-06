import os

from jinja2 import Template


def generate_prompt(prompt_name: str, text: str, query: str) -> str:
    """Generates a prompt for the Luminous API using a Jinja template.

    Args:
        prompt_name (str): The name of the file containing the Jinja template.
        text (str): The text to be inserted into the template.
        query (str): The query to be inserted into the template.

    Returns:
        str: The generated prompt.

    Raises:
        FileNotFoundError: If the specified prompt file cannot be found.
    """
    try:
        with open(os.path.join("prompts", prompt_name)) as f:
            prompt = Template(f.read())
    except FileNotFoundError:
        raise FileNotFoundError(f"Prompt file '{prompt_name}' not found.")

    # replace the value text with jinja
    # Render the template with your variable
    prompt_text = prompt.render(text=text, query=query)

    return prompt_text


def initialize_wandb():
    # TODO: necessary or where should init go.
    pass


def metrics():
    # TODO: implement metric package including: acc, prec, rec, f1, levensthein.
    pass

