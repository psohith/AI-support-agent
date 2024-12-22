

# Set the API key for authentication
# palm.configure(api_key="AIzaSyBo2HlMw0AvGEeV8dS6gjoa3bsO7MGMGi0")
# AIzaSyCftV3xQcMVD039e8wS4qm25xI44umig5k


from vertexai.generative_models import GenerativeModel

# Initialize the model with the new flash-2.0 version
model = GenerativeModel("gemini-2.0-flash-001")
# model=GenerativeModel("gemini-1.5-flash-001")


text = '''
Install Testsigma Recorder Extension: Chrome
With Testsigma's Chrome extension, users can quickly record test steps by capturing user interactions, such as clicking buttons, entering text, navigating through pages, etc. The extension will also help users create elements interacting with the application during testing. This article explains how to install Testsigma's Chrome extension.
Steps to Install Chrome Extension
Go to
Testsigma Recorder
Click on
Add to Chrome
.
On the permission prompt, click on
Add extension
.
On successful installation, the following message will appear:
Here’s a GIF demonstrating how to add Testsigma's Chrome extension.
For more information on creating test steps using recorder, refer to
recording test steps
.
Record Steps in Incognito Mode
You can record steps in incognito mode by enabling the ""Allow in Incognito"" option in the Testsigma manage extension. This feature lets you record steps privately without storing browsing history or cookies. Follow the steps below to enable the “Allow in Incognito” option in the Testsigma extension in Chrome browser.
Extension Settings for Incognito Mode
1. Open the Testsigma Extension:
Right-click the Testsigma Extension icon in the browser toolbar.
2. Access Extension Settings:
From the extension menu, select
Manage extension
.
3. Enable Allow in Incognito:
Toggle on
Allow in Incognito
option.
Here’s a GIF demonstrating how to enable the
Allow in Incognito
option and record steps in Incognito.
'''

# Generate a summary
response = model.generate_content(f"Summarize the following text:\n\n{text}")

# Print the summary
print("Summary:", response.text)


