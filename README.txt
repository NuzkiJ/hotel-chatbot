HOTEL Booking CHATBOT 

PROJECT OVERVIEW:
This chatbot is developed for Grand Ceylonara Berlin (ficational) and allows users to book and track hotel reservations through a conversational interface. 
This system is built using Dialogflow and Flask.

DIALOGFLOW AGENT:
The chatbot agent is provided as a ZIP file (GrandCeylonaraBerlinBot) included in this submission.

🔗 Live Webhook: https://hotel-chatbot-ajzz.onrender.com/webhook
🔗 GitHub: https://github.com/NuzkiJ/hotel-chatbot
🔗 Demo Video: https://drive.google.com/file/d/1k_1FKGm4Ty3skbJFNSq3rdHu-sFeecdx/view?usp=sharing  


Key Features:
Natural language booking system
Real-time reservation storage
Booking ID generation
Booking tracking system
Deployed backend using Render

IMPORT STEPS:

1. Open Dialogflow (https://dialogflow.cloud.google.com/)
2. Click on the Settings (gear icon)
3. Navigate to "Export and Import"
4. Select "Import from ZIP"
5. Upload the file: GrandCeylonaraBerlinBot
6. Confirm import

TESTING THE CHATBOT:

Booking Flow:

1. Type "book"
2. Provide required details (name, guests, room type, dates, etc.)
3. Confirm the booking when prompted
4. A Booking ID will be generated

Tracking Flow:

1. Type "track"
2. Enter the Booking ID
3. Booking details will be displayed

WEBHOOK:
The chatbot is connected to a deployed webhook service:
https://hotel-chatbot-ajzz.onrender.com/webhook

TECHNOLOGIES USED:

* Dialogflow ES (NLP and conversation management)
* Python (backend logic)
* Flask (webhook framework)
* SQLite (database)
* Render (deployment)


The repository contains the webhook implementation and supporting files used in this project.
Nuzki Jiffry
