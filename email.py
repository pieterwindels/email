import streamlit as st
import smtplib


st.header('I want full access to the app!')

st.text_input("Email", key='body')

#st.text_input('your email address', key='body')
#st.button("Send email")

if st.button("Send new Email"):

        st.write('1')

        if st.session_state.body is None:
                st.error("Please enter your email address to request full access to the app.")

        else:
                st.write(st.session_state.body)
                try:
                    # Set up the SMTP server and login to your email account
                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                    #server.starttls()
                    server.login("devpwindels@gmail.com", "eskuahufhdrwiwzb")
                
                    # Create the email message
                    message = "Subject: New Email from Streamlit App\n\n" + "Email: " + user_email
                
                    # Send the email
                    server.sendmail("devpwindels@gmail.com", "immo2smart@gmail.com", message)
                
                    # Close the SMTP server connection
                    server.quit()
                
                    # Display a success message to the user
                    st.success("Email sent successfully!")
                except Exception as e:
                    # Display an error message if there is an issue sending the email
                    st.error("Email could not be sent. Please try again later.")

