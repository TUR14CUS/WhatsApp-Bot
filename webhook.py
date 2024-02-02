# webhook.py
from flask import Blueprint, request
from twilio.twiml.messaging_response import MessagingResponse
from main import process_message

webhook = Blueprint("webhook", __name__)

@webhook.route('/webhook', methods=['POST'])
def handle_whatsapp_webhook():
    incoming_msg = request.values.get('Body', '')
    response_msg = process_message(incoming_msg)

    resp = MessagingResponse()
    resp.message(response_msg)

    return str(resp)
