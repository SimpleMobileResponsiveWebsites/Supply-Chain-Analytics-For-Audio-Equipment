import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import io
from PIL import Image

# Function to upload CSV file on the first page
def upload_csv_page():
    st.title("Supply Chain Analytics For Audio Equipment - Upload Data")
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
    st.title("Supply Chain Analytics For Audio Equipment - Display Data")

    if df is not None:
        st.write("## Displaying Data")
        st.write(df)

# Function to create a 3D scatter plot on a separate page
def create_3d_scatter_plot_page(df):
    st.title("3D Scatter Plot")
    st.write("Select columns for the X-axis, Y-axis, and Z-axis to create a 3D scatter plot.")

    x_column = st.selectbox("Select X-axis column", df.columns)
    y_column = st.selectbox("Select Y-axis column", df.columns)
    z_column = st.selectbox("Select Z-axis column", df.columns)

    if st.button("Create 3D Scatter Plot"):
        try:
            fig = px.scatter_3d(df, x=x_column, y=y_column, z=z_column, color=z_column,
                                 title=f"{x_column} vs {y_column} vs {z_column}")
            st.plotly_chart(fig)

            # Export and download the 3D scatter plot as a PDF
            export_3d_scatter_plot_to_pdf(fig, "3d_scatter_plot.pdf")
        except Exception as e:
            st.error(f"Error creating 3D scatter plot: {e}")

# Function to export and download a Plotly figure as a screenshot and save it to PDF
def export_3d_scatter_plot_to_pdf(fig, pdf_filename):
    st.write(f"Exporting 3D Scatter Plot to PDF: {pdf_filename}")

    # Create a screenshot of the plot
    img_data = fig.to_image(format="png")
    img = Image.open(io.BytesIO(img_data))

    # Save the screenshot as a PDF
    img.save(pdf_filename, "PDF")

    # Provide download link
    st.success(f"3D Scatter Plot exported to PDF successfully. [Download PDF](./{pdf_filename})")

# Function to create a histogram on a separate page
def create_histogram_page(df):
    st.title("Histogram")
    st.write("Select a column to create a histogram.")

    column = st.selectbox("Select a column", df.columns)

    if st.button("Create Histogram"):
        try:
            fig = px.histogram(df, x=column, title=f"Histogram of {column}")
            st.plotly_chart(fig)

            # Export and download the histogram as a PDF
            export_histogram_to_pdf(fig, "histogram.pdf")
        except Exception as e:
            st.error(f"Error creating histogram: {e}")

# Function to export and download a Plotly figure as a screenshot and save it to PDF
def export_histogram_to_pdf(fig, pdf_filename):
    st.write(f"Exporting Histogram to PDF: {pdf_filename}")

    # Create a screenshot of the plot
    img_data = fig.to_image(format="png")
    img = Image.open(io.BytesIO(img_data))

    # Save the screenshot as a PDF
    img.save(pdf_filename, "PDF")

    # Provide download link
    st.success(f"Histogram exported to PDF successfully. [Download PDF](./{pdf_filename})")

# Function to create a box plot on a separate page
def create_box_plot_page(df):
    st.title("Box Plot")
    st.write("Select columns for the X-axis and Y-axis to create a box plot.")

    x_column = st.selectbox("Select X-axis column", df.columns)
    y_column = st.selectbox("Select Y-axis column", df.columns)

    if st.button("Create Box Plot"):
        try:
            fig = px.box(df, x=x_column, y=y_column, title=f"Box Plot of {y_column} by {x_column}")
            st.plotly_chart(fig)

            # Export and download the box plot as a PDF
            export_box_plot_to_pdf(fig, "box_plot.pdf")
        except Exception as e:
            st.error(f"Error creating box plot: {e}")

# Function to export and download a Plotly figure as a screenshot and save it to PDF
def export_box_plot_to_pdf(fig, pdf_filename):
    st.write(f"Exporting Box Plot to PDF: {pdf_filename}")

    # Create a screenshot of the plot
    img_data = fig.to_image(format="png")
    img = Image.open(io.BytesIO(img_data))

    # Save the screenshot as a PDF
    img.save(pdf_filename, "PDF")

    # Provide download link
    st.success(f"Box Plot exported to PDF successfully. [Download PDF](./{pdf_filename})")

# Main Streamlit application
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Select a page", ["Upload Data", "Display Data", "3D Scatter Plot", "Histogram", "Box Plot"])

    if page == "Upload Data":
        df = upload_csv_page()
        if df is not None:
            st.session_state.data = df
            st.sidebar.text("Data uploaded successfully.")
    elif page == "Display Data":
        if "data" in st.session_state:
            display_data_page(st.session_state.data)
    elif page == "3D Scatter Plot":
        if "data" in st.session_state:
            create_3d_scatter_plot_page(st.session_state.data)
    elif page == "Histogram":
        if "data" in st.session_state:
            create_histogram_page(st.session_state.data)
    elif page == "Box Plot":
        if "data" in st.session_state:
            create_box_plot_page(st.session_state.data)

if __name__ == "__main__":
    main()
