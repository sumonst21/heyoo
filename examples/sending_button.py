from os import getenv
from heyoo import WhatsApp
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    messenger = WhatsApp(token=getenv("TOKEN"),phone_number_id=getenv("PHONE_NUMBER_ID"))

    response = messenger.send_button(
        recipient_id=getenv("TEST_NUMBER")
        button={
            "header": "Header Testing",
            "body": "Body Testing",
            "footer": "Footer Testing",
            "action": {
                "button": "Button Testing",
                "sections": [
                    {
                        "title": "Some Action",
                        "rows": [
                            {"id": "row 1", "title": "Getter", "description": ""},
                            {
                                "id": "row 2",
                                "title": "Setter",
                                "description": "",
                            },
                        ],
                    }
                ],
            },
        },
    )
