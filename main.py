import streamlit as st
import streamlit as st
from finance_functions import simple_interest, compound_interest, compound_value, present_value
from expression_evaluator import evaluate_expression


st.markdown(
    """
    <h1 style='text-align: right; color: orange;'>
    Calculator 💸
    </h1>
    """,
    unsafe_allow_html=True
)

st.sidebar.title("Calculators 🏦")

calculator = st.sidebar.selectbox(
    "Choose Calculator",
    ["Financial", "Simple", "Scientific", "Statistical"]
)

if calculator == "Simple":

    st.title("Simple Calculator 🧮")

    expression = st.text_input("Enter Expression", "2 + 3 * 5")

    if st.button("Calculate", key="simple_calc"):

        if expression.strip() == "":
            st.warning("Please enter a mathematical expression")

        else:
            try:
                result = evaluate_expression(expression)
                st.success(f"Result: {result}")

            except ZeroDivisionError:
                st.warning("Result is undefined (division by zero)")

            except TypeError:
                st.error("Invalid mathematical expression")

            except Exception:
                st.error("Something went wrong while evaluating the expression")


if calculator == "Financial":

    st.title("Financial Calculator")

    select = st.selectbox(
        "What do you want to know?",
        ["Simple Interest", "Compound Interest", "Present Value", "Future Value"]
    )

    if select == "Simple Interest":

        p = st.number_input("Principal", key="si_p")
        r = st.number_input("Rate (%)", key="si_r")
        t = st.number_input("Time (years)", key="si_t")

        if st.button("Calculate", key="si_button"):
            result = simple_interest(p, r, t)
            st.success(f"Simple Interest = {result}")

    elif select == "Present Value":

        fv = st.number_input("Future Value", key="pv_fv")
        r = st.number_input("Rate (%)", key="pv_r")
        n = st.number_input("Time (years)", key="pv_n")

        if st.button("Calculate", key="pv_button"):
            result = present_value(fv, r, n)
            st.success(f"Present Value = {result}")

    elif select == "Compound Interest":

        pv = st.number_input("Principal", key="ci_pv")
        r = st.number_input("Rate (%)", key="ci_r")
        n = st.number_input("Time (years)", key="ci_n")

        if st.button("Calculate", key="ci_button"):
            result = compound_interest(pv, r, n)
            st.success(f"Compound Interest = {result}")

    elif select == "Future Value":

        pv = st.number_input("Present Value", key="fv_pv")
        r = st.number_input("Rate (%)", key="fv_r")
        n = st.number_input("Time (years)", key="fv_n")

        if st.button("Calculate", key="fv_button"):
            result = compound_value(pv, r, n)
            st.success(f"Future Value = {result}")
            
if calculator == "Statistical":

    st.title("Statistical Calculator")

    select = st.selectbox(
        "What do you want to know?",
        ["Mean", "Median", "Mode", "Standard Deviation"]
    )
