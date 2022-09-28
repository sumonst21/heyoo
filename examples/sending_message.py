from os import getenv
from heyoo import WhatsApp
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()

    messenger = WhatsApp(token=getenv("TOKEN"), phone_number_id=getenv("PHONE_NUMBER_ID"))

    response = messenger.send_message(
        message="https://compliance.normalsys.com/",
        recipient_id=getenv("TEST_NUMBER"),
    )

    print(response)
