paper_text = ""

import gradio as gr

from utils.pdf_processor import extract_pdf_text
from utils.summarizer import generate_summary
from utils.research_analyzer import analyze_research_paper
from utils.qa_engine import answer_question


paper_text = ""


def process_pdf(pdf_file):

    global paper_text

    paper_text = extract_pdf_text(pdf_file.name)

    summary = generate_summary(paper_text)

    analysis = analyze_research_paper(paper_text)

    return summary, analysis


def ask_question(question):

    global paper_text

    print("\nQUESTION:")
    print(question)

    print("\nPAPER LENGTH:")
    print(len(paper_text))

    if not paper_text:
        return "Please upload a PDF first."

    answer = answer_question(
        question,
        paper_text
    )

    print("\nANSWER GENERATED:")
    print(answer[:500])

    return answer


with gr.Blocks() as demo:

    gr.Markdown("# AI Research Assistant")

    gr.Markdown(
        """
        Upload a research paper PDF,
        generate summaries,
        extract research insights,
        and ask questions about the paper.
        """
    )

    pdf_input = gr.File(
        label="Upload Research Paper PDF"
    )

    process_button = gr.Button(
        "Process Paper"
    )

    summary_output = gr.Textbox(
        label="Summary",
        lines=10
    )

    analysis_output = gr.Textbox(
        label="Research Analysis",
        lines=15
    )

    process_button.click(
        process_pdf,
        inputs=pdf_input,
        outputs=[
            summary_output,
            analysis_output
        ]
    )

    gr.Markdown("## Chat With Paper")

    question_input = gr.Textbox(
        label="Question"
    )

    ask_button = gr.Button(
        "Ask"
    )

    answer_output = gr.Textbox(
        label="Answer",
        lines=8
    )

    ask_button.click(
        ask_question,
        inputs=question_input,
        outputs=answer_output
    )

demo.launch(
    share=False,
    debug=True
)