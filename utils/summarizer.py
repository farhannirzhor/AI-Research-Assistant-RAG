import ollama


def generate_summary(text):

    try:

        text = text[:3000]

        response = ollama.chat(
            model="gemma4:latest",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an expert research assistant. "
                        "Generate a concise summary of the research paper."
                    )
                },
                {
                    "role": "user",
                    "content": f"Summarize this research paper:\n\n{text}"
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:
        return f"Summary Error: {str(e)}"