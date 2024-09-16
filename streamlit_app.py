import arxiv.org

# Define search query for AI and finance-related papers
search = arxiv.Search(
    query="AI finance",
    max_results=10,
    sort_by=arxiv.SortCriterion.SubmittedDate
)

# Fetch papers
papers = []
for result in search.results():
    papers.append({
        'title': result.title,
        'summary': result.summary,
        'published': result.published,
        'url': result.entry_id
    })

# Display fetched papers
for paper in papers:
    print(f"Title: {paper['title']}")
    print(f"Summary: {paper['summary']}")
    print(f"Published on: {paper['published']}")
    print(f"Link: {paper['url']}\n")
from transformers import pipeline

# Load summarization pipeline
summarizer = pipeline("summarization")

# Summarize each paper's abstract
for paper in papers:
    summary = summarizer(paper['summary'], max_length=50, min_length=25, do_sample=False)
    paper['short_summary'] = summary[0]['summary_text']

    print(f"Short Summary for '{paper['title']}': {paper['short_summary']}\n")

import streamlit as st

import datetime  # Import datetime module

# Define min_date and max_date using datetime.date
min_date = datetime.date(2000, 1, 1)  # Minimum date for the slider (January 1, 2000)
max_date = datetime.date(2024, 12, 31)  # Maximum date for the slider (December 31, 2024)

# Create a date range slider in Streamlit
date_filter = st.slider("Select a date range", value=(min_date, max_date))

# Display papers in a user-friendly format
st.title('AI and Finance Research Monitor')

# Display filtered papers
for paper in papers:
    st.header(paper['title'])
    st.write(f"Published on: {paper['published']}")
    st.write(f"Summary: {paper['short_summary']}")
    st.markdown(f"[Read Full Paper]({paper['url']})")
    
if st.button('Share with John or Sally'):
    st.write("Link shared with John or Sally.")
