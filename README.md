# 10-K Filings Analysis Tool

This tool automates the process of downloading SEC 10-K filings for public firms, analyzing the text data, and providing insights through a simple web interface.

![Steven Hao 10-K Filings Analysis](https://github.com/huntsmanhao/secAnalysis/assets/144931059/2051ce4b-f3c6-43ce-9e7b-90e317fa32f0)
Note: Sometimes running on a slow local machine may cause long runtimes of up to 5 minutes. Above is a screenshot of an example output if this occurs.
Due to disk space limitation, the deployment wasn't successful to pythonanywhere free version. Here is a link to the demo video: https://youtu.be/-yPof_U6Xr4

## Requirements

### Task 1.1: Download Data from the SEC-EDGAR
- Select 2-3 companies or tickers of your choice.
- Download a 10-K filing for each year from the SEC website for the period 1995 through 2023 for the selected companies.
- Use a script or program to automate the download process. You can utilize the `sec-edgar-downloader` package in Python or similar alternatives.

### Task 1.2: Text Analysis
- Utilize LLM (Large Language Model) inference API to extract insights from the 10-K filings.
- Generate visualizations based on the extracted insights.
- Provide a brief explanation of the significance of the insights for users.

### Task 2: Construct and Deploy Simple App
- Build a simple web app that takes a company ticker as input and displays visualizations based on the analysis of 10-K filings.
- Choose any technology stack for the app development.
- Deploy the app on a platform or record a demo if deployment is not feasible.

## Solution Overview

The solution is implemented using Django, a high-level Python web framework. Below is an overview of the components:

### Views.py
- Contains the logic for rendering the home page and analyzing 10-K filings.
- Utilizes the `sec_edgar_downloader` module to download filings and performs text analysis using LLM.

### Downloader.py
- Module responsible for downloading 10-K filings using the `sec-edgar-downloader` package.

### home.html
- HTML template for the home page of the web app.
- Allows users to select a company and year for analysis and displays the generated text.

## Technology Stack
- **Framework**: Django
- **Backend**: Python
- **Text Analysis**: Transformers library for LLM inference
- **Frontend**: HTML with Bootstrap for styling

## Deployment
The app can be deployed on any web hosting platform supporting Django applications. I have deployed this app on pythonanywhere. It is available at the url: https://stevenhao.pythonanywhere.com/
Due to disk space limitation, the deployment wasn't successful to pythonanywhere free version. Here is a link to the demo video: https://youtu.be/-yPof_U6Xr4

## Rationale
- **Django**: Chosen for its simplicity, scalability, and robustness in building web applications.
- **Transformers Library**: Utilized for its powerful NLP capabilities, enabling efficient text analysis.
- **Bootstrap**: Used for quick and responsive UI development.

- The rationale for the insight is as follows: Users would care about this insight because it provides valuable information on the company's performance and strategic direction, enabling them to make informed decisions regarding investments, partnerships, or other business activities.

## How to Run
1. Due to disk space limitation, the deployment wasn't successful to pythonanywhere free version. Here is a link to the demo video: https://youtu.be/-yPof_U6Xr4

OR

1. Clone the repository.
2. Install dependencies (`pip install -r requirements.txt`).
3. Run the Django server (`python manage.py runserver`).
4. Access the web app in your browser (`http://localhost:8000`).

## Contributors
- [Steven Hao]
shao44@gatech.edu

Feel free to contribute to the project by submitting pull requests or reporting issues.

