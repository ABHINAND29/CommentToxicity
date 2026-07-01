import streamlit as st
import pandas as pd
import joblib
import numpy as np
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


LR_pipeline = joblib.load('toxicity_pipeline.pkl')


st.header("🛡 Toxicity Detector")

comment = st.text_area(

"Enter a comment"

)

if st.button("Analyze"):

    prediction = LR_pipeline.predict(
        [comment]
    )

    result = pd.DataFrame(

        prediction,

        columns=[

        'toxic',

        'severe_toxic',

        'obscene',

        'threat',

        'insult',

        'identity_hate'

        ]

    )

    st.dataframe(result)

uploaded = st.file_uploader(

"Upload CSV",

type='csv'

)

if uploaded:

    new_df = pd.read_csv(uploaded)

    pred = LR_pipeline.predict(

        new_df['text']

    )

    pred_df = pd.DataFrame(

        pred,

        columns=[

        'toxic',

        'severe_toxic',

        'obscene',

        'threat',

        'insult',

        'identity_hate'

        ]

    )

    final = pd.concat(

        [new_df,pred_df],

        axis=1

    )

    st.dataframe(final)

    csv = final.to_csv(

        index=False

        )

    st.download_button(

    "Download Predictions",

    csv,

    "toxicity_predictions.csv",

    "text/csv"

    )

# st.header("📊 Data Insights")

# st.write("Dataset Shape")
# st.write(df.shape)

# st.write("First Five Records")
# st.dataframe(df.head())

# st.write("Missing Values")
# st.dataframe(df.isnull().sum())

# st.write("Label Distribution")

# toxicity_counts = df[
# [
# 'toxic',
# 'severe_toxic',
# 'obscene',
# 'threat',
# 'insult',
# 'identity_hate'
# ]
# ].sum()

# st.bar_chart(toxicity_counts)\


# st.header("📈 Model Performance")

# c1,c2,c3 = st.columns(3)

# c1.metric(
# "Accuracy",
# f"{accuracy:.2%}"
# )

# c2.metric(
# "ROC-AUC",
# f"{roc_auc:.2f}"
# )

# c3.metric(
# "F1 Score",
# f"{f1:.2f}"
# )