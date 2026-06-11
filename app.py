import os

from utils.pdf_processor import extract_pdf_text
from utils.summarizer import generate_summary
from utils.research_analyzer import analyze_research_paper
from utils.qa_engine import answer_question


def main():

    pdf_path = "uploads/research_paper.pdf"

    if not os.path.exists(pdf_path):
        print(f"PDF not found: {pdf_path}")
        return

    print("=" * 50)
    print("READING PDF...")
    print("=" * 50)

    extracted_text = extract_pdf_text(pdf_path)

    print(f"\nTotal Characters Extracted: {len(extracted_text)}")

    # ---------------- SUMMARY ---------------- #

    print("\nGenerating Summary...\n")

    summary = generate_summary(extracted_text)

    print("=" * 50)
    print("RESEARCH PAPER SUMMARY")
    print("=" * 50)

    print(summary)

    # ---------------- ANALYSIS ---------------- #

    print("\nGenerating Research Analysis...\n")

    analysis = analyze_research_paper(extracted_text)

    print("=" * 50)
    print("RESEARCH PAPER ANALYSIS")
    print("=" * 50)

    print(analysis)

    # ---------------- CHAT WITH PDF ---------------- #

    print("\n")
    print("=" * 50)
    print("CHAT WITH RESEARCH PAPER")
    print("=" * 50)

    while True:

        question = input(
            "\nAsk a question (or type 'exit'): "
        )

        if question.lower() == "exit":
            break

        print("\nSearching paper...\n")

        answer = answer_question(
            question,
            extracted_text
        )

        print("\nANSWER:")
        print(answer)

    # ---------------- END ---------------- #

    print("\n")
    print("=" * 50)
    print("AI RESEARCH ASSISTANT COMPLETED")
    print("=" * 50)


if __name__ == "__main__":
    main()