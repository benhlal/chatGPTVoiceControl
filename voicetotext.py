import speech_recognition as sr
import requests
import json

# Function to convert speech to text
def speech_to_text():
    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()

    # Reading Microphone as source
    # listening the speech and store in audio_text variable
    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
        print("Time over, thanks")

    # recoginize_() method will throw a request error if the API is unreachable
    try:
        # using google speech recognition
        text = r.recognize_google(audio_text)
        print("You said: " + text)
    except:
        print("Sorry, I did not get that")
    return text

# Function to call GPT-3 API
def generate_text(prompt):
    # Replace YOUR_API_KEY with your actual API key
  #  api_key = ""

   # api_key = ""
    api_key =  ""
 
    headers = {'Content-Type': 'application/json',
               'Authorization': f"Bearer {api_key}"}
    endpoint = "https://api.openai.com/v1/engines/davinci/completions"

    # The prompt that you want to pass to GPT-3
    data = {
        "prompt": prompt,
          "max_tokens": 30000,
    }

    # Making the API call
    response = requests.post(endpoint, json=data, headers=headers)

    print("RAW RESPONSE ==> ",response.content)
    # Parsing the response
    response_json = json.loads(response.text)

    print("AFTER PARSING  RESPONSE ==> ",response)
    generated_text = response_json["choices"][0]["text"]
    print(generated_text)

# main function
if __name__ == "__main__":
    prompt = speech_to_text()
    generate_text(prompt)
