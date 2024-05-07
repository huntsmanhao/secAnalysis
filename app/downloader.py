from sec_edgar_downloader import Downloader

def download_10k_filings(ticker, start_date="1995-01-01", end_date="2023-12-31"):
    """
    Downloads 10-K filings for a given ticker symbol and date range from the SEC website.

    Args:
        ticker (str): The ticker symbol of the company.
        start_date (str): The start date for downloading filings in YYYY-MM-DD format (default is "1995-01-01").
        end_date (str): The end date for downloading filings in YYYY-MM-DD format (default is "2023-12-31").

    Returns:
        None
    """
    # Initialize SEC downloader
    dl = Downloader("Steven", "stevenhao2020@gmail.com")

    # Download 10-K filings for the specified date range
    try:
        dl.get("10-K", ticker, after=start_date, before=end_date)
        print(f"Downloaded {ticker} 10-K filings from {start_date} to {end_date}")
    except Exception as e:
        print(f"Error downloading {ticker} 10-K filings: {e}")
