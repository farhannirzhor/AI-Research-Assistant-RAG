import ollama

def analyze_research_paper(text):

    try:

        text = text[:3000]

        prompt = f"""
Analyze the following research paper and return the result in exactly this format:

OBJECTIVE:
(what problem is being solved?)

METHODOLOGY:
(how was the research conducted?)

KEY CONTRIBUTIONS:
(main innovations and contributions)

RESULTS:
(main findings and performance)

FUTURE WORK:
(suggested future improvements)

Research Paper:

{text}
"""

        response = ollama.chat(
            model="gemma4:latest",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:
        return f"Analysis Error: {str(e)}"