"""The one place the app talks to an AI model.

Always call it as:

    from plantbox import ai
    reply = ai.ask_llm(prompt)

No real model is set up yet, so on your machine ask_llm returns a demo reply. Set the
environment variable PLANTBOX_AI=fail to make it raise RuntimeError instead, like a real
model that is down: every feature that uses AI needs a fixed fallback text for that.
Darbni's tests replace ask_llm with a fake model.
"""

import os


def ask_llm(prompt: str) -> str:
    if os.environ.get("PLANTBOX_AI") == "fail":
        raise RuntimeError("The AI is down (PLANTBOX_AI=fail)")
    return "[Demo AI reply] Try the Grower plan."
