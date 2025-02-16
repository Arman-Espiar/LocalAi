import streamlit as st
import chatbot_constants as constants
import chatbot_functions as functions

functions.add_online_groq_models()
functions.set_page_config()
functions.initial_session_state()

with st.sidebar:
    st.subheader(body=constants.SETTINGS,divider="rainbow")

    st.session_state.temperature = st.slider(label=constants.SET_TEMPERATURE,min_value=0.0,max_value=1.0,value=0.8,step=0.1)
    st.session_state.type_of_model = st.selectbox(
        constants.SELECT_TYPE_OF_MODEL,
        (constants.TYPE_OF_MODEL),
    )

    if st.session_state.type_of_model == constants.TYPE_OF_MODEL[0]:
        st.session_state.model_name = st.radio(
            index=0,
            options=constants.LOCAL_MODELS,
            label=constants.SELECT_YOUR_MODEL,
        ).strip()
    else:
        st.session_state.model_name = st.radio(
            index=0,
            options=constants.GROQ_MODELS,
            label=constants.SELECT_YOUR_MODEL,
        ).strip()


    st.write(constants.SELECTED_MODEL,st.session_state.model_name)
    st.divider()

    st.markdown(body=constants.ABOUT,unsafe_allow_html=True)
    
    
st.header(body=constants.PAGE_HEADER)
if not st.session_state.model_name:
    st.error(body=constants.ERROR_YOU_DID_NOT_SPECIFY_MODEL_NAME)

if st.session_state.model_name:
    user_prompt :str|None = st.chat_input(
        placeholder=constants.USER_PROMPT_PLACEHOLDER,
    )
    if user_prompt:
        user_prompt=user_prompt.strip()
    if user_prompt:
        st.session_state.messages.append({"role":"user","content":user_prompt})
        if st.session_state.type_of_model == constants.TYPE_OF_MODEL[1]: #online groq models
            assistant_answer = functions.chat_completion_groq(messages=st.session_state.messages,model_name=st.session_state.model_name,temperature=st.session_state.temperature)
        else:
            assistant_answer = functions.chat_completion_local(messages=st.session_state.messages,model_name=st.session_state.model_name,temperature=st.session_state.temperature)
        st.session_state.messages.append({"role":"assistant","content":assistant_answer})

    for index, message in enumerate(st.session_state.messages):
        if message["role"] == "user":
            with st.chat_message(name=constants.USER):
                st.write(message["content"])
        elif message["role"] == "assistant":
            with st.chat_message(name=constants.AI):
                st.write(message["content"])