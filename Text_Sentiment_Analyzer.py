import streamlit as st
from textblob import TextBlob

# Initialize NLTK TextBlob sentiment analysis tool
st.title("Sentiment Analysis")

# User input
user_input = st.text_area("Enter text for sentiment analysis:")
predict_button = st.button("Predict")

if predict_button and user_input:
    # Perform sentiment analysis using TextBlob
    blob = TextBlob(user_input)
    sentiment_score = blob.sentiment.polarity
    sentiment_subjectivity = blob.sentiment.subjectivity

    # Determine sentiment label based on polarity score
    if sentiment_score > 0:
        sentiment_label = "Positive"
    elif sentiment_score < 0:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"

    # Display results
    st.subheader("Sentiment Analysis Results:")
    st.write(sentiment_label)
    #st.write(f"Polarity Score: {sentiment_score}")
    #st.write(f"Subjectivity Score: {sentiment_subjectivity}")
elif predict_button:
    st.write("Please enter text for sentiment analysis.")

