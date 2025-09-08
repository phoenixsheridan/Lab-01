import streamlit as st

st.title("BuzzFeed-Style Quiz")
st.write("Just a couple questions regarding things that interest me. If you get at least 4/5, then we maybe can be friends.")

score = 0  # Keep track of correct answers

# --- Question 1: Multi-select ---
st.header("Question 1")
st.write("What are the 5 pieces of Exodia required to win a game of Yu-Gi-Oh?")

exodia_choices = [
    "Left leg of the forbidden one",
    "Right leg of the forbidden one",
    "Left arm of the forbidden one",
    "Right arm of the forbidden one",
    "Exodia the forbidden one",
    "Head of the forbidden one",
    "Torso of the forbidden one"
]

selected = st.multiselect(
    "Select all that apply:",
    exodia_choices
)  #NEW

correct_exodia = exodia_choices[:5]  # first five are correct
if set(selected) == set(correct_exodia):
    score += 1
    st.success("Correct. You have assembled Exodia.")
else:
    st.error("Not quite. try again.")

st.image("images/exodia.png", caption="The Unstoppable Exodia")  #NEW


# --- Question 2: Number input ---
st.header("Question 2")
blue_eyes = st.number_input(
    "How many stars/levels does the Blue-Eyes White Dragon have?",
    min_value=1, max_value=12, step=1
)  #NEW

if blue_eyes == 8:
    score += 1
    st.success("Correct. Blue-Eyes has 8 stars. ")
elif blue_eyes != 0:
    st.error("Nope, that's not right.")

st.image("images/bewd.png", caption="The Legendary Blue Eyes White Dragon")


# --- Question 3: Multiple choice ---
st.header("Question 3")
boss = st.radio(
    "Who is the true final boss of *Bloodborne*?",
    ["Father Gascoigne", "Gehrman", "Moon Presence", "Amygdala", "Cleric Beast"]
)

if boss == "Moon Presence":
    score += 1
    st.success("Correct. The Moon Presence awaits at the end 🌙")
else:
    st.error("Wrong boss.")


# --- Question 4: Number input ---
st.header("Question 4")
shadow_bosses = st.number_input(
    "How many bosses in *Shadow of the Erdtree* are remembrance bosses? (42 bosses total)",
    min_value=0, max_value=42, step=1
)

if shadow_bosses == 10:
    score += 1
    st.success("Correct. 10 remembrance bosses.")
elif shadow_bosses != 0:
    st.error("Nope, that’s not right.")

st.image("images/scadutree.png", caption="Scadutree Avatar, one of the SOTE remembrance bosses.")


# --- Question 5: Multiple choice ---
st.header("Question 5")
halting = st.selectbox(
    "When was the Halting Problem first given a proper name?",
    [1921, 1932, 1939, 1945, 1952, 1966]
)

if halting == 1952:
    score += 1
    st.success("Correct. 1952 📜")
else:
    st.error("Nope, that’s not the right year.")


# --- Final Results ---
st.write("---")
st.subheader("Your Final Score:")
st.metric("Score", f"{score}/5")  #NEW

if score == 5:
    st.balloons()  #NEW
