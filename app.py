#streamlit
import streamlit as st

st.set_page_config(page_title= "Growth Mindset Challenge", page_icon="🙋")
st.title("Growth Mindset Challenge: web app with streamlit" )

st.header("Welcome to Elevate Journey ⬆️")
st.write("a path of learning, self-improvement, and limitless possibilities. Keep moving forward, embrace the process, and unlock your full potential! 🚀🌱")

#quote section
st.header("Growth Mindset Daily 🌱✨")
st.write("Growth is a journey—embrace challenges, learn daily, and keep evolving.")

st.header("What's Your Challenge Today? 🛠️")
user_input = st.text_input("Describe a challenge you're facing:")


#condition
if user_input:
    st.success(f"🛠️You're facing: {user_input}. keep pushing forward towards your goal!✨")
else:
    st.warning("Tell us about your challenge to get started!")

#reflexing
st.header("Growth Reflections 🌱💡")
reflection = st.text_area("write your reflections here")

if reflection:
    st.success(f"🌟📝Reflections of Growth: {reflection}")
else:
    st.info("Struggles to Strength 💪")


#achievement
st.header("Small Wins, Big Impact 💪🎯")
achievement = st.text_input("Your Victory Board 🏅✨")


if achievement:
    st.success(f"🎉Amazing! You Did It!🚀: {achievement}")
else:
    st.info("✨Big or small, Every Win Counts! Share one now 🏆") 


#footer
st.write("- - -")
st.write("Every step forward, big or small, brings you closer to greatness. Keep pushing, keep believing—your journey is unstoppable!🔥")
st.write("**© Created By Ali Abbas**")
