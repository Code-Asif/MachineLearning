import openai
# Set your OpenAI API key
openai.api_key = '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'

# Make a request to the OpenAI API using the Completion.create method
response = openai.completions.create(
    model="text-davinci-002",  # You can choose a different engine
    prompt="What is the meaning of life?",
    max_tokens=150  # Adjust the maximum number of tokens in the response
)

# Get the generated text from the response
generated_text = response['choices'][0]['text']

# Now you can use `generated_text` on your website
print(generated_text)
