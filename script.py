from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline, set_seed,BlenderbotTokenizerFast, BlenderbotForConditionalGeneration
from huggingface_hub import login
from decouple import config

#Login to HuggingFace
# try:
#     login(config('HF_TOKEN'))
# except Exception as e:
#     print(f"Une erreur s'est produite : {e}")


# models_dict = {
#   "LLAMA-2" : "meta-llama/Llama-2-7b-chat-hf",
#   "GPT2" : "gpt2-large",
#   "BlenderBot" : "facebook/blenderbot-400M-distill",
#   "Wizard" : "TheBloke/Wizard-Vicuna-7B-Uncensored-GPTQ",
#   "GPT-neo" : "EleutherAI/gpt-neo-2.7B"
# }

model_name = "facebook/blenderbot-400M-distill"

#Tokenizer
tokenizer = BlenderbotTokenizerFast.from_pretrained(model_name)

# Model
model = BlenderbotForConditionalGeneration.from_pretrained(model_name)

# Run the chatbot
while True:
  query = input("\nUser: ")
  if query == "exit":
    break
  if query.strip() == "":
    continue

  # Générer une réponse en prenant en compte tout l'historique
  inputs = tokenizer([query], return_tensors="pt", max_length=1024, padding='longest')
  reply_ids = model.generate(**inputs)

  # Décoder la réponse
  bot_output = tokenizer.decode(reply_ids[0], skip_special_tokens=True)

  # afficher la réponse
  print(f"Bot: {bot_output}")
