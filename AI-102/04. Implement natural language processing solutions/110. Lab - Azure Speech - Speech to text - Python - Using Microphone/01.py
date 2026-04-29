import azure.cognitiveservices.speech as speechsdk

endpoint="https://aiservice4000.cognitiveservices.azure.com/"
key=""

config=speechsdk.SpeechConfig(subscription=key,endpoint=endpoint)

output_file="transcribed.txt"
config.speech_recognition_language="en-US"

audio_input = speechsdk.audio.AudioConfig(use_default_microphone=True)
txt_generator = speechsdk.SpeechRecognizer(speech_config=config,audio_config=audio_input)

result=txt_generator.recognize_once_async().get()
if result.reason== speechsdk.ResultReason.RecognizedSpeech:
    print("Text generated successfully")
else:
    print("Generating text failed")

with open(output_file, "w", encoding="utf-8") as file:
    file.write(result.text)
