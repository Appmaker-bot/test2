# Command Metadata
name = "hello"
description = "A simple command that greets the user."

def run(ui_element, args):
    if args:
        return f"Hello, {args}! Welcome to ForgeOS."
    return "Hello! I am ForgeOS. How can I help you today?"
