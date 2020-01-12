Manage team GSuite signatures
=============================

Managing signatures by hand could be a realy headacke. 
Try to use python script to automate this process. 

Requirements
------------
-   [Python 3.6+](https://www.python.org/) 
`pip install -r requirements.txt`
-   google-api-python-client
-   oauth2client
-   httplib2
-   pystache

Prepare and run
-------
1.  API key (simple way)
-   Create a project on [Google APIs](https://console.developers.google.com/start/api?id=gmail&credential=client_key) 
-	Create a JSON file with key - *service_account_key.json* and put it in directory with script
-   [Enable G Suite Domain-wide Delegation](https://developers.google.com/admin-sdk/reports/v1/guides/delegation)
-   [In *Client name* – past your Unique ID, In *One or more API Scopes* – past this (coma separated):](https://admin.google.com/AdminHome?chromeless=1#OGX:ManageOauthClients)
https://www.googleapis.com/auth/gmail.settings.basic,https://www.googleapis.com/auth/ggmai.settings.sharing
-   Authorize
2.  Change template.mustache file according to your needs. It will be passted in each signature
3.  Fill *Team Information - Email-Signatures.csv* with information about your team
4. `python change_domain_signatures.py`