







print(f"\nInitial AI Response: {initial_response}")
modified_prompt = input(
    "Modify the prompt to make it more neutral(e.g., 'Describe the qualities of a doctor'): "
    ).strip()





def token_limit_activity():
    





preview = (long_response[:500] + "...") if len(long_response) > 500 else