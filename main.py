import streamlit as st
from streamlit_jina import jina

st.set_page_config(page_title="Searching Statistics Terms",)

endpoint = "https://stats.libretexts.org/Bookshelves/Introductory_Statistics/Book%3A_Introductory_Statistics_(Shafer_and_Zhang)/01%3A_Introduction_to_Statistics/1.01%3A_Basic_Definitions_and_Concepts"

st.title("Searching LibreTexts for Statistics Terms")
# st.markdown("You can run our [Wikipedia search example](https://github.com/jina-ai/examples/tree/master/wikipedia-sentences) to test out this search")

jina.text_search(endpoint=endpoint)