from django.shortcuts import render, redirect
import os
import logging

from app.downloader import download_10k_filings
import re
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def home(request):
    """
    Renders the home page.

    Args:
        request: HTTP request object.

    Returns:
        Rendered home page HTML template.
    """
    return render(request, 'home.html')

def analyze_filings(request):
    """
    Analyzes 10-K filings for a selected company and year.

    Args:
        request: HTTP request object.

    Returns:
        Rendered home page HTML template with generated text.
    """
    if request.method == 'POST':
        # Get the selected company and year from the form
        company = request.POST.get('company')
        year = request.POST.get('year')

        # Download 10-K filings for the selected company and year
        download_10k_filings(company, start_date=f"{year}-01-01", end_date=f"{year}-12-31")

        # Process downloaded filings
        filings_dir = os.path.abspath(os.path.join(os.getcwd(), "sec-edgar-filings", company, "10-K"))
        if os.path.exists(filings_dir):
            logger.info(f"Found 10-K directory for {company}.")

            # Concatenate text data from all filings
            all_text_data = ""
            for root, dirs, files in os.walk(filings_dir):
                for file in files:
                    if file.endswith(".txt"):
                        file_path = os.path.join(root, file)
                        with open(file_path, 'r') as f:
                            text_data = f.read()
                        all_text_data += text_data

            # Extract relevant sections for summary
            summary_text = extract_summary(all_text_data)

            torch.set_default_device("cuda")

            model = AutoModelForCausalLM.from_pretrained("microsoft/phi-2", torch_dtype="auto", trust_remote_code=True)
            tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-2", trust_remote_code=True)

            prompt = ("Imagine you are an industry analyst discussing the future prospects of {company} in {year}. "
                      "What key insights would you highlight about the company's performance and strategic direction?")

            # Set max_length based on the length of summary_text
            max_length = min(len(summary_text) + 400, 1000)  # Adjust 400 as needed

            inputs = tokenizer(prompt.format(passage=summary_text, company=company, year=year), return_tensors="pt", return_attention_mask=False)

            outputs = model.generate(**inputs, max_length=max_length)
            text = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]

            # Pass the generated text to the template
            context = {
                'company': company,
                'text': text
            }
        else:
            logger.error(f"No 10-K directory found for {company}.")
            # Initialize an empty context dictionary if no directory is found
            context = {}

        # Redirect to the home page or any other page as needed
        return render(request, 'home.html', context)

    else:
        # If the request method is not POST, redirect to the home page
        return redirect('home')

def extract_summary(text):
    """
    Extracts a summary from 10-K filing text.

    Args:
        text: Text data from 10-K filings.

    Returns:
        Summary text extracted from the filings.
    """
    # Extract relevant sections for summary
    summary_text = ""
    # Define regex patterns for common section headers in 10-K filings
    section_patterns = [
        r"item\s+1\.\s+business(.+?)item\s+2\.",
        r"item\s+1a\.\s+risk factors(.+?)item\s+1b\.",
        r"item\s+7\.\s+management\s+discussion\s+and\s+analysis(.+?)item\s+8\.",
        r"item\s+8\.\s+financial\s+statements(.+?)item\s+9\.",
        r"item\s+9\.\s+changes\s+in\s+and\s+disagreements\s+with\s+accountants(.+?)item\s+9a\."
    ]
    for pattern in section_patterns:
        match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
        if match:
            summary_text += match.group(1) + "\n\n"

    return summary_text