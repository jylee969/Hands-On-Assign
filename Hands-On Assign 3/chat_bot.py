# John Lee
# MSCS 633
# Hands On Assign 3: Create a Simple Q&A Chatbot with Python

# This program creates a chatbot where a basic interaction between a user and bot takes place
# provided that the user starts the conversation with the user's input

from django.core.management.base import BaseCommand
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# This class initializes and runs the ChatterBot terminal interface 
class Command(BaseCommand):
    # Provides a description when running --help
    help = 'Chatbot implementation by John Lee '

    # This function provides the main logic for the command. It runs automatically when the command is called.  
    def handle(self, *args, **options):
        # Initializes the Bot
        chatbot = ChatBot('SuperBot')
        
        # Set up the Trainer for the purpose of teaching the bot from the English language files
        trainer = ChatterBotCorpusTrainer(chatbot)
        
        # Train the bot on basic greetings
        trainer.train("chatterbot.corpus.english.greetings")

        # Show a success message in the terminal once the bot is ready for user's input
        self.stdout.write(self.style.SUCCESS('System online. I am ready to chat!'))

        # The chat loop between user and the bot
        while True:
            user_input = input("user: ")
            
            # Check if the user wants to quit
            if user_input.lower() == 'exit':
                self.stdout.write(self.style.SUCCESS("Have a nice day!"))
                break
            
            # Get and print the response from the bot
            response = chatbot.get_response(user_input)
            print(f"bot: {response}")