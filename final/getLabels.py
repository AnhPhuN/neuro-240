# screenshot to json

"""
This code sample shows Prebuilt Layout operations with the Azure Form Recognizer client library. 
The async versions of the samples require Python 3.6 or later.

To learn more, please visit the documentation - Quickstart: Form Recognizer Python client library SDKs
https://docs.microsoft.com/en-us/azure/applied-ai-services/form-recognizer/quickstarts/try-v3-python-sdk
"""

from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
import json
import pickle
"""
Remember to remove the key from your code when you're done, and never post it publicly. For production, use
secure methods to store and access your credentials. For more information, see 
https://docs.microsoft.com/en-us/azure/cognitive-services/cognitive-services-security?tabs=command-line%2Ccsharp#environment-variables-and-application-configuration
"""
endpoint = "https://form-recog-test-neuro.cognitiveservices.azure.com/"
key = "10c992231e3f4c8a8b464e40a99ab772"

def callAPI(imgPath):
    document_analysis_client = DocumentAnalysisClient(
        endpoint=endpoint, credential=AzureKeyCredential(key)
    )

    with open(imgPath, "rb") as image:
        poller = document_analysis_client.begin_analyze_document("prebuilt-layout", image)

    result = poller.result()
    json_string = json.dumps(result, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    return json_string

if __name__ == "__main__":
    for i in range(16, 40):
        print("doing number ", i)
        imgPath = "data/screenshots/" + str(i) + ".png"
        json_string = callAPI(imgPath)

        with open("data/rawLabels/" + str(i) + ".json", "w") as file:
            file.write(json_string)


