print("=" * 50)
print("AI CUSTOMER SUPPORT CHATBOT")
print("=" * 50)
print("Type 'exit' to end the conversation.\n")

while True:

    user = input("You: ").lower()

    if user == "exit":
        print("Bot: Thank you for contacting us. Have a great day! 😊")
        break

    elif "hello" in user or "hi" in user:
        print("Bot: Hello! Welcome to Customer Support. How can I help you?")

    elif "price" in user or "cost" in user:
        print("Bot: Our plans start from ₹499 per month.")

    elif "refund" in user:
        print("Bot: Refunds are processed within 5-7 business days.")

    elif "delivery" in user:
        print("Bot: Delivery usually takes 3-5 working days.")

    elif "contact" in user:
        print("Bot: You can contact us at support@example.com")

    elif "help" in user:
        print("Bot: I can assist with pricing, refunds, delivery, and contact information.")

    else:
        print("Bot: Sorry, I didn't understand that. Please try another question.")