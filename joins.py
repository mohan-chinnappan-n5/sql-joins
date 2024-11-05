import streamlit as st
import pandas as pd

# Sidebar to show details about different types of joins with Venn diagrams
st.sidebar.title("Join Types Explained")

join_types = {
    "Inner Join": {
        "description": "Returns only the rows with matching values in both tables.",
        "venn_image": "img/SQL_Join_-_07_A_Inner_Join_B.svg"
    },
    "Left Outer Join": {
        "description": "Returns all rows from the left table, and the matched rows from the right table. Rows in the left table without a match will show None.",
        "venn_image": "img/SQL_Join_-_01_A_Left_Join_B.svg"
    },
    "Right Outer Join": {
        "description": "Returns all rows from the right table, and the matched rows from the left table. Rows in the right table without a match will show None.",
        "venn_image": "img/SQL_Join_-_03_A_Right_Join_B.svg"
    },
    "Full Outer Join": {
        "description": "Returns all rows when there is a match in either table. Non-matching rows will show None.",
        "venn_image": "img/SQL_Join_-_05b_A_Full_Join_B.svg"
    }
}

for join_type, info in join_types.items():
    st.sidebar.subheader(join_type)
    st.sidebar.write(info["description"])
    st.sidebar.image(info["venn_image"], use_column_width=True)

# Main app title
st.title("CSV - SQL Joins ")

# File upload
st.header("Upload CSV Files")
csv1 = st.file_uploader("Upload First CSV File", type=["csv"])
csv2 = st.file_uploader("Upload Second CSV File", type=["csv"])

# Check if both files are uploaded
if csv1 and csv2:
    # Read the CSV files into DataFrames
    df1 = pd.read_csv(csv1)
    df2 = pd.read_csv(csv2)

    # Display uploaded files
    st.subheader("First CSV Preview")
    st.write(df1.head())

    st.subheader("Second CSV Preview")
    st.write(df2.head())

    # Select join type
    join_type = st.selectbox("Select Join Type", ["Inner Join", "Left Outer Join", "Right Outer Join", "Full Outer Join"])

    # Choose columns to join on
    join_column1 = st.selectbox("Select join column from the first CSV", df1.columns)
    join_column2 = st.selectbox("Select join column from the second CSV", df2.columns)

    # Perform join based on selected join type
    if st.button("Perform Join"):
        if join_type == "Inner Join":
            result = pd.merge(df1, df2, how="inner", left_on=join_column1, right_on=join_column2)
        elif join_type == "Left Outer Join":
            result = pd.merge(df1, df2, how="left", left_on=join_column1, right_on=join_column2)
        elif join_type == "Right Outer Join":
            result = pd.merge(df1, df2, how="right", left_on=join_column1, right_on=join_column2)
        elif join_type == "Full Outer Join":
            result = pd.merge(df1, df2, how="outer", left_on=join_column1, right_on=join_column2)

        # Display the join result
        st.subheader("Join Result")
        st.write(result)

        # Option to download the joined data as a CSV
        csv = result.to_csv(index=False).encode("utf-8")
        st.download_button(
            "Download Joined CSV",
            data=csv,
            file_name="joined_data.csv",
            mime="text/csv"
        )
else:
    st.info("Please upload two CSV files to proceed.")