import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-002",
  prompt="“Disorder, alas, is the natural order of things in the universe.” So says K.C. Cole in her Arrow of Time. How does Golding confirm or refute this assertion? In short, how do things fall apart (Jack) or remain together (Ralph)? Your task here is to take a stand on entropy with LotF as your key source.  \n\nIn the end, which ultimately prevails? Is collapse the natural state of the universe? What might Golding be saying to us about us?  \n\n ",
  temperature=0,
  max_tokens=60,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
