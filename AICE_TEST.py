import streamlit as st
import google.generativeai as palm

# Configure the AI API
palm.configure(api_key="AIzaSyBHFH2xfKgxvIxEJL7EVyXIg64a3JmKQkI")

def main():
    st.title("Arjun's AI Code Explainer")

    # Input code
    input_code = st.text_area("Enter the code to be explained:", height=200)

    if st.button("Explain Code"):
        if input_code:
            # Generate explanation
            prompt = f"Detect the language of code and Explain the following code snippet in a concise way:\n\n{input_code}"
            response = palm.generate_text(prompt=prompt)

            # Display the explanation
            st.subheader("Code Explanation:")
            st.write(response.result)  # Display the explanation

if __name__ == "__main__":
    main()
