import streamlit as st
from agent import process_bug
from excel_reader import read_bug_file

st.set_page_config(
    page_title="AI Bug Triage",
    page_icon="🐞",
    layout="wide"
)

st.title("🐞 AI Bug Triage Dashboard")
st.caption("AI-Powered QA Bug Triage & Test Management Platform")

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Dashboard",
        "Bug Analysis",
        "Test Cases",
        "Regression Tests"
    ]
)

if "result" not in st.session_state:
    st.session_state.result = None


if page == "Dashboard":

    st.header("📊 Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("AI Bug Triage", "Active")
    col2.metric("Duplicate Detection", "Enabled")
    col3.metric("Test Generation", "Enabled")
    col4.metric("Regression Testing", "Enabled")

    st.divider()

    st.subheader("🐞 Bug Triage Workflow")

    st.write("""
    Excel / CSV Bug Report
            ↓
    Bug Extraction
            ↓
    AI Bug Analysis
            ↓
    Severity / Priority / Component
            ↓
    Duplicate Detection
            ↓
    Test Case Generation
            ↓
    Regression Test Generation
            ↓
    Pytest Automation
            ↓
    Allure Reporting
            ↓
    GitHub Actions CI/CD
    """)


elif page == "Bug Analysis":

    st.header("🐞 Analyze Bug")

    input_type = st.radio(
        "Input Type",
        ["Text", "Excel / CSV"],
        horizontal=True
    )

    title = ""
    description = ""

    if input_type == "Text":

        title = st.text_input("Bug Title")

        description = st.text_area(
            "Bug Description",
            height=200
        )

        if st.button("🔍 Analyze Bug"):

            if not title or not description:
                st.warning("Enter bug title and description")

            else:
                result = process_bug(
                    title,
                    description
                )

                st.session_state.result = result

                st.success("Bug analyzed successfully")

    else:

        uploaded_file = st.file_uploader(
            "Upload Bug Report",
            type=["xlsx", "csv"]
        )

        if uploaded_file:

            try:

                df = read_bug_file(uploaded_file)

                st.subheader("📋 Uploaded Bug Report")

                st.dataframe(
                    df,
                    use_container_width=True
                )

                st.divider()

                st.subheader("Select Bug")

                row_number = st.selectbox(
                    "Select bug row",
                    range(len(df))
                )

                selected_bug = df.iloc[row_number]

                st.write("### Selected Bug")

                st.write(selected_bug.to_dict())

                columns = df.columns.tolist()

                title_column = st.selectbox(
                    "Bug Title Column",
                    columns
                )

                description_column = st.selectbox(
                    "Bug Description Column",
                    columns
                )

                title = str(
                    selected_bug[title_column]
                )

                description = str(
                    selected_bug[description_column]
                )

                st.text_input(
                    "Bug Title",
                    value=title,
                    disabled=True
                )

                st.text_area(
                    "Bug Description",
                    value=description,
                    height=150,
                    disabled=True
                )

                if st.button("🔍 Analyze Selected Bug"):

                    if not title or not description:

                        st.warning(
                            "Selected bug has missing information"
                        )

                    else:

                        result = process_bug(
                            title,
                            description
                        )

                        st.session_state.result = result

                        st.success(
                            "Bug analyzed successfully"
                        )

            except Exception as e:

                st.error(
                    f"Unable to read file: {e}"
                )

    result = st.session_state.result

    if result:

        st.divider()

        st.subheader("📊 Bug Analysis")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Severity",
            result["severity"]
        )

        col2.metric(
            "Priority",
            result["priority"]
        )

        col3.metric(
            "Component",
            result["component"]
        )

        st.divider()

        st.subheader("🔎 Duplicate Detection")

        if result["duplicate"]:

            st.warning(
                f"Possible duplicate: "
                f"{result['duplicate']['id']}"
            )

            st.write(
                "Similarity:",
                result["duplicate_score"]
            )

            st.write(
                "**Existing Bug:**",
                result["duplicate"]["title"]
            )

        else:

            st.success(
                "No duplicate bug detected"
            )


elif page == "Test Cases":

    st.header("🧪 Generated Test Cases")

    result = st.session_state.result

    if not result:

        st.info("Analyze a bug first")

    else:

        for test in result["test_cases"]:

            with st.expander(
                f"{test['id']} - {test['title']}"
            ):

                st.write("### Steps")

                for step in test["steps"]:
                    st.write(f"- {step}")

                st.write("### Expected Result")

                st.write(test["expected"])


elif page == "Regression Tests":

    st.header("🔄 Regression Test Scenarios")

    result = st.session_state.result

    if not result:

        st.info("Analyze a bug first")

    else:

        st.write(
            "These tests should be executed after "
            "the reported bug is fixed."
        )

        st.divider()

        for i, test in enumerate(
            result["regression_tests"],
            1
        ):

            st.checkbox(
                test,
                key=f"regression_{i}"
            )