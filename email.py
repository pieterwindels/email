import streamlit as st
import smtplib

test = False

if test:
        
    st.header('I want full access to the app!')
    
    user_email = st.text_input("Email")
    
    #st.text_input('your email address', key='body')
    #st.button("Send email", on_click= email, args=(st.session_state.body))
    
    if st.button("Send new Email"):
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
        
    st.write(st.session_state.body)
