import streamlit as st
import smtplib

if 'something' not in st.session_state:
    st.session_state.something = ''

def submit():
        st.session_state.something = st.session_state.widget
        #st.session_state.widget = ''
        try:
            # Set up the SMTP server and login to your email account
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            #server.starttls()
            server.login("devpwindels@gmail.com", "eskuahufhdrwiwzb")
        
            # Create the email message
            message = "Subject: New Email from Streamlit App\n\n" + "Email: " + st.session_state.widget
        
            # Send the email
            server.sendmail("devpwindels@gmail.com", "immo2smart@gmail.com", message)
        
            # Close the SMTP server connection
            server.quit()
        
            # Display a success message to the user
            st.success("Email sent successfully!")
        except Exception as e:
            # Display an error message if there is an issue sending the email
            st.error("Email could not be sent. Please try again later.")

        st.session_state.widget = ''
        
st.header('I want full access to the app!')

#st.text_input("Email", key='body')
st.text_input('Something', key='widget', on_change=submit)



