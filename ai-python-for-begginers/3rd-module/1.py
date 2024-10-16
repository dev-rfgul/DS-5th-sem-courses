from helper_functions import get_llm_response
from IPython.display import display, Markdow


# Write a list of ingredients
ingredients = ['chicken', 'broccoli', 'rice']

# Write the prompt
prompt = f"""
    Create a short recipe that uses the following ingredients:
    {ingredients}
"""

# Get the response from the LLM
response = get_llm_response(prompt)

# Print the LLM response
print(response)