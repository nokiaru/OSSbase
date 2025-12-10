import streamlit as st 

import plotly.express as px 

  

st.set_page_config(page_title="Orwellian Surveillance Scale (OSS)", layout="centered") 

  

st.title("Orwellian Surveillance Scale (OSS) – Prototype") 

  

st.write( 

    "This tool lets you score a surveillance system on several dimensions and " 

    "produces an overall *Orwellian surveillance* index from 0 to 100." 

    "This tool lets you score a surveillance system across key dimensions " 

    "and produces an overall Orwellian surveillance index from 0 to 100." 

) 

  

# --- Define core dimensions and short descriptions --- 

# --- Core dimensions and descriptions --- 

DIMENSIONS = { 

    "Visibility / Monitoring": "How constantly and pervasively are people observed or tracked?", 

    "Predictive Control": "To what extent is data used to predict and pre-empt behaviour?", 

    "Self-Censorship": "Do people change or limit what they say or do because they feel watched?", 

    "Datafication": "How fully are people reduced to data points, profiles or risk scores?", 

    "Trust in State / Institutions": "How much power over data and surveillance is given to state or major institutions?", 

    "Resignation / Normalisation": "Do people feel that surveillance is inevitable and unchangeable?", 

    "Self-Censorship": "Do people change what they say or do because they feel watched?",

    "Datafication": "How fully are people reduced to data points or algorithmic profiles?", 

    "Trust in State / Institutions": "How much power over data is given to institutions?", 

    "Resignation / Normalisation": "Do people feel surveillance is inevitable and unchangeable?" 

} 

  

# Optional theoretical weights – you can tweak these later 

# --- Weights (you can tweak these later based on theory) --- 

WEIGHTS = { 

    "Visibility / Monitoring": 1.2, 

    "Predictive Control": 1.3, 

@@ -28,17 +30,15 @@ 

    "Resignation / Normalisation": 0.9 

} 

  

MAX_SCORE_PER_DIM = 4 # 0–4 Likert scale 

MAX_SCORE = 4 # 0–4 Likert 

  

# --- Form UI --- 

with st.form("oss_form"): 

    st.subheader("1. System being assessed") 

    system_name = st.text_input("Name or short description of the system/technology") 

    system_name = st.text_input("System or technology being assessed") 

    location = st.text_input("Country / location (optional)") 

     

    st.markdown("### 2. Rate each dimension from 0 to 4") 

    st.markdown( 

        "**0 = Not present · 1 = Very weak · 2 = Moderate · 3 = Strong · 4 = Extreme / totalising**" 

    ) 

  

    st.markdown("### Rate each dimension from 0 to 4") 

    st.caption("0 = Not present · 1 = Very weak · 2 = Moderate · 3 = Strong · 4 = Extreme / totalising") 

  

    scores = {} 

    for dim, desc in DIMENSIONS.items(): 

@@ -54,29 +54,29 @@ 

  

    submitted = st.form_submit_button("Calculate OSS score") 

  

# --- Logic after submit --- 

if submitted: 

    # --- Calculate weighted score --- 

    weighted_sum = 0 

    max_weighted_sum = 0 

  

    for dim, score in scores.items(): 

        w = WEIGHTS[dim] 

        weighted_sum += score * w 

        max_weighted_sum += MAX_SCORE_PER_DIM * w 

        max_weighted_sum += MAX_SCORE * w 

  

    if max_weighted_sum > 0: 

        oss_index = round((weighted_sum / max_weighted_sum) * 100, 1) 

        oss_score = round((weighted_sum / max_weighted_sum) * 100, 1) 

    else: 

        oss_index = 0.0 

        oss_score = 0.0 

  

    # --- Classify the level of Orwellian surveillance --- 

    if oss_index <= 25: 

    # Classification bands 

    if oss_score <= 25: 

        category = "Low surveillance" 

        explanation = "Surveillance is present but limited in scope or intensity." 

    elif oss_index <= 50: 

    elif oss_score <= 50: 

        category = "Moderate surveillance" 

        explanation = "Surveillance is significant but not yet fully structuring everyday life." 

    elif oss_index <= 75: 

    elif oss_score <= 75: 

        category = "High behavioural adaptation" 

        explanation = "Surveillance is strong and likely shaping behaviour, choices and self-expression." 

    else: 

@@ -86,21 +86,33 @@ 

            "for chilling effects and systemic control." 

        ) 

  

    st.subheader("Results") 

    st.subheader("OSS Result") 

    if system_name: 

        st.write(f"**System assessed:** {system_name}") 

        st.write("**System:**", system_name) 

    if location: 

        st.write(f"**Location:** {location}") 

        st.write("**Location:**", location) 

  

    st.metric("OSS Index (0–100)", oss_index) 

    st.metric("OSS Score (0–100)", oss_score) 

    st.write(f"**Category:** {category}") 

    st.write(explanation) 

  

    st.subheader("Dimension breakdown") 

    for dim, score in scores.items(): 

        st.write(f"- **{dim}**: {score} / 4 (weight {WEIGHTS[dim]})") 

    # --- Radar chart of dimension scores --- 

    st.subheader("Dimension Profile") 

  

    categories = list(DIMENSIONS.keys()) 

    values = [scores[dim] for dim in categories] 

  

    # Close the loop for radar 

    categories_loop = categories + [categories[0]] 

    values_loop = values + [values[0]] 

  

    fig = px.line_polar( 

        r=values_loop, 

        theta=categories_loop, 

        line_close=True, 

        range_r=[0, 4], 

        title="OSS Dimension Radar", 

    ) 

    fig.update_traces(fill="toself") 

  

    st.info( 

        "This is an early prototype of the OSS. In your dissertation, you can explain the " 

        "theoretical basis of each dimension and how the weights and thresholds were chosen." 

    ) 

    st.plotly_chart(fig, use_container_width=True) 
