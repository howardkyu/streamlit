import streamlit as st
import altair as alt
import pandas as pd

# Setting the title and page layout
st.title("Mario's Rockstar Dream")
st.write("Welcome to Mario's world at Windoio!")

# Biographical information about Mike
mike_bio = """
**Name**: Mike
**Occupation**: Software Engineer
**Hobbies**: Guitar playing, Video games
"""

# Displaying Mike's biographical information
st.markdown("## Mike's Biography")
st.markdown(mike_bio)

# Slider for Mario's rockstar skills
st.markdown("## Mario's Rockstar Skills")
rockstar_skill = st.slider("How awesome is Mario as a rockstar?", min_value=1, max_value=10, value=5)

# Mario's dream as a rockstar
st.markdown("## Mario's Rockstar Dream")
st.write("Mario works at Windoio, but his true passion lies in becoming a rockstar! He dreams of rocking the stage and becoming a music legend.")

# Altair bar chart
st.markdown("## Mario's Musical Journey")
music_genre_data = {
    'Genre': ['Rock', 'Pop', 'Hip Hop', 'Jazz', 'Metal'],
    'Popularity': [7, 8, 6, 4, 9]
}

genre_chart = alt.Chart(pd.DataFrame(music_genre_data)).mark_bar().encode(
    x='Genre',
    y='Popularity',
    color=alt.Color('Popularity', scale=alt.Scale(scheme='blues')),
    tooltip=['Genre', 'Popularity']
).properties(
    width=500,
    height=300
).interactive()

st.altair_chart(genre_chart)

# Altair line chart
st.markdown("## Mario's Music Progress")
music_progress_data = {
    'Year': [2018, 2019, 2020, 2021, 2022],
    'Songs Created': [5, 8, 12, 15, 10],
    'Concerts Played': [2, 4, 6, 8, 5]
}

line_chart = alt.Chart(pd.DataFrame(music_progress_data)).mark_line().encode(
    x='Year',
    y='value',
    color=alt.Color('variable', scale=alt.Scale(scheme='set1')),
    tooltip=['Year', 'value']
).properties(
    width=500,
    height=300
).interactive()

st.altair_chart(line_chart)

# Conclusion
st.markdown("## Conclusion")
if rockstar_skill >= 8:
    st.write("With his incredible rockstar skills, Mario is destined to conquer the music world!")
elif rockstar_skill >= 5:
    st.write("Mario's rockstar skills are solid. With some practice, he can achieve his dream of becoming a rockstar!")
else:
    st.write("Mario has a long way to go in his rockstar journey, but with dedication and passion, anything is possible!")

st.write("Thank you for joining us in Mario's world at Windoio! Keep on rocking!")
