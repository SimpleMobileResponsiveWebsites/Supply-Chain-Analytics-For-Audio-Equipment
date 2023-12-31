import streamlit as st
import pandas as pd
import plotly.express as px


# Function to upload CSV file on the first page
def upload_csv_page():
    st.title("Supply Chain Analytics for Audio Equipment - Upload Data")
    st.write("Upload a CSV file with string column headers, and strings, integers, and floats as values.")

    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.success(f"File uploaded successfully. Data has {len(df)} rows.")
            return df
        except Exception as e:
            st.error(f"Error reading CSV file: {e}")
    return None


# Function to display data on the second page
def display_data_page(df):
    st.title("Supply Chain Analytics for Audio Equipment - Display Data")

    if df is not None:
        st.write("## Displaying Data")
        st.write(df)


# Function to create a graph on the third page
def create_graph_page(df):
    st.title("Supply Chain Analytics for Audio Equipment - Create Graph")
    st.write("Select columns for the X-axis and Y-axis to create a graph.")

    x_column = st.selectbox("Select X-axis column", df.columns)
    y_column = st.selectbox("Select Y-axis column", df.columns)

    if st.button("Create Graph"):
        try:
            fig = px.scatter(df, x=x_column, y=y_column, title=f"{x_column} vs {y_column}")
            st.plotly_chart(fig)
        except Exception as e:
            st.error(f"Error creating graph: {e}")


# Main Streamlit application
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Select a page", ["Upload Data", "Display Data", "Create Graph"])

    if page == "Upload Data":
        df = upload_csv_page()
        if df is not None:
            st.session_state.data = df
            st.sidebar.text("Data uploaded successfully.")
    elif page == "Display Data":
        if "data" in st.session_state:
            display_data_page(st.session_state.data)
    elif page == "Create Graph":
        if "data" in st.session_state:
            create_graph_page(st.session_state.data)


if __name__ == "__main__":
    main()
