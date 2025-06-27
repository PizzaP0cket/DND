import pychrome
import json
import time

# Import the JS code for prompting as a string
with open("prompt.js", "r", encoding="utf-8") as js_file:
    prompt_script_template = js_file.read()


# Import the JS code for response a string
with open("response.js", "r", encoding="utf-8") as js_file:
    response_script = js_file.read()


# Connect to Chrome
# Get a list of open tabs (Tab objects)
# Find the ChatGPT tab (you can refine this)
browser = pychrome.Browser(url="http://localhost:9222")
tabs = browser.list_tab()
chatgpt_tab = next(tab for tab in tabs if "chatgpt.com" in tab._kwargs.get("url"))
chatgpt_tab.start()  # start tab event


# Sending prompt to CHAT_GPT in Chrome Browser
def send_prompt(prompt_text):
    print(f"\n📝 Sending prompt!")
    clean_prompt = json.dumps(prompt_text)  # Cleaned up prompt
    prompt_script = prompt_script_template.replace("Your prompt here", clean_prompt)
    chatgpt_tab.call_method("Runtime.evaluate", expression=prompt_script)
    time.sleep(3)  # 3 for slow internet


# Get response from CHAT_GPT in Chrome Browser
def wait_for_response():
    print("⏳ Waiting for ChatGPT response to finish...")
    result = chatgpt_tab.call_method(
        "Runtime.evaluate", expression=response_script, awaitPromise=True
    )
    return result.get("result", {}).get("value", "")
