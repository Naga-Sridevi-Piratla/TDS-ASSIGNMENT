import streamlit as st

def find_largest(num1, num2, num3):
    return max(num1, num2, num3)

def main():
    st.title("Find the largest number")
    st.write("Enter three numbers below:")
    num1 = st.number_input("Number 1", value=0)
    num2 = st.number_input("Number 2", value=0)
    num3 = st.number_input("Number 3", value=0)

    if st.button("Find largest"):
        largest = find_largest(num1, num2, num3)
        st.write("The largest number is:", largest)

if __name__ == "__main__":
    main()
