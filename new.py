import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly
from streamlit_option_menu import option_menu
import warnings
warnings.filterwarnings('ignore')


st.markdown("""
<style>
    /* Main background gradient */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-attachment: fixed;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #2c3e50 0%, #3498db 100%);
    }
    
    /* Custom title styling */
    .main-title {
    font-size: 3rem;
    font-weight: 700;
    text-align: center;
    color: #ffffff;                /* solid white */
    -webkit-text-fill-color: #ffffff;
    margin-bottom: 2rem;
    text-shadow: 0 6px 18px rgba(0,0,0,0.35), 0 2px 6px rgba(102, 126, 234, 0.25);
    animation: titleGlow 2s ease-in-out infinite alternate;
    }
            
    /* Add a glowing animation to the title */
    @keyframes titleGlow {
        from {
            filter: drop-shadow(0 0 5px rgba(231, 76, 60, 0.5));
        }
        to {
            filter: drop-shadow(0 0 15px rgba(231, 76, 60, 0.8));
        }
    }        
    
    /* Section headers */
    .section-header {
        font-size: 2rem;
        font-weight: 600;
        color: #2c3e50;
        margin: 1.5rem 0;
        padding: 1rem;
        background: rgba(255, 255, 255, 0.9);
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border-left: 5px solid #3498db;
    }
    
    /* Content cards */
    .content-card {
        background: rgba(255, 255, 255, 0.95);    
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        margin: 1rem 0;
    }
    
    /* Info boxes */
    .info-box {
        background: linear-gradient(135deg, #74b9ff 0%, #0984e3 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(116, 185, 255, 0.3);
    }
    
    .warning-box {
        background: linear-gradient(135deg, #fdcb6e 0%, #e17055 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(253, 203, 110, 0.3);
    }
    
    .success-box {
        background: linear-gradient(135deg, #00b894 0%, #00a085 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(0, 184, 148, 0.3);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }
    
    /* Update the selectbox styling */
    .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.9) !important;
        border-radius: 10px !important;
        border: 2px solid #3498db !important;
        color: #2c3e50 !important;  /* Dark text color for better contrast */
    }

    /* Update the dropdown options */
    .stSelectbox [role="listbox"] {
        background: white !important;
        color: #2c3e50 !important;
    }

    /* Update the multiselect styling */
    .stMultiSelect > div > div {
        background: rgba(255, 255, 255, 0.9) !important;
        border-radius: 10px !important;
        border: 2px solid #3498db !important;
        color: #2c3e50 !important;  /* Dark text color */
    }

    /* Multiselect dropdown options */
    .stMultiSelect [role="listbox"] {
        background: white !important;
        color: #2c3e50 !important;
    }

    /* Selected items in multiselect */
    .stMultiSelect [data-baseweb="tag"] {
        background: #3498db !important;
        color: white !important;
    }

    /* Slider labels */
    .stSlider label {
        color: white !important;
    }

    /* Radio button labels */
    .stRadio label {
        color: white !important;
    }

    /* Checkbox labels */
    .stCheckbox label {
        color: white !important;
    }

    /* Date input labels */
    .stDateInput label {
        color: white !important;
    }

    /* Number input labels */
    .stNumberInput label {
        color: white !important;
    }

    /* Text input labels */
    .stTextInput label {
        color: white !important;
    }

    /* Text area labels */
    .stTextArea label {
        color: white !important;
    }
    
    /* Plot containers */
    .plot-container {
        background: rgba(255, 255, 255, 0.95);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
    }
    
    /* Statistics cards */
    .stat-card {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin: 1rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
        color: #2c3e50;
        margin-bottom: 0.5rem;
    }
    
    .stat-label {
        font-size: 1rem;
        color: #5a6c7d;
        font-weight: 500;
    }
    
    /* Animated elements */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .animated-content {
        animation: fadeInUp 0.8s ease-out;
    }
    
    /* Sidebar menu styling */
    .css-1544g2n {
        padding-top: 2rem;
    }
    
    /* Custom text styling */
    .highlight-text {
        background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 600;
    }
    
    /* Footer styling */
    .footer {
        background: rgba(44, 62, 80, 0.9);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin-top: 3rem;
    }
</style>
""", unsafe_allow_html=True)


st.markdown('<div class="main-title">🔍 Crime Data Analysis Dashboard</div>', unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### 📊 Navigation")
    opt = option_menu(
        "Main Menu",
        ["🏠 Home", "📈 Crime Analysis", "ℹ️ About"],
        icons=["house-fill", "graph-up", "info-circle-fill"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "white", "font-size": "18px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "color": "white"},
            "nav-link-selected": {"background-color": "#3498db"},
        }
    )

if opt == "🏠 Home":
    # Hero section
    st.markdown('<div class="animated-content">', unsafe_allow_html=True)
    
    
    st.markdown("""
    <div class="content-card">
        <h1 style="text-align: center; color: #2c3e50; margin-bottom: 1rem;">
            Welcome to Crime Data Analysis Platform
        </h1>
        <p style="text-align: center; font-size: 1.2rem; color: #5a6c7d;">
            Empowering data-driven decisions for safer communities
        </p>
    </div>
    """, unsafe_allow_html=True)
    
   
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">📊</div>
            <div class="stat-label">Interactive<br>Visualizations</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">🗺️</div>
            <div class="stat-label">Geographic<br>Analysis</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">📈</div>
            <div class="stat-label">Trend<br>Analysis</div>
        </div>
        """, unsafe_allow_html=True)
    
    
    st.markdown("""
    <div class="section-header">
        🎯 Project Introduction
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <h3>🚀 Mission</h3>
        <p>This project focuses on analyzing crime data to understand patterns, trends, and insights that can help in 
        enhancing public safety and informing policy decisions. Using data-driven methods, we examine various aspects 
        of crime, such as frequency, types, affected locations, and trends over time.</p>
    </div>
    """, unsafe_allow_html=True)
    
    
    st.markdown("""
    <div class="section-header">
        🎯 Project Objectives
    </div>
    """, unsafe_allow_html=True)
    
    objectives = [
        "🔍 Explore and analyze historical crime data to identify key insights",
        "🗺️ Understand crime hotspots and geographic patterns",
        "📊 Predict potential areas of crime occurrences",
        "📈 Develop comprehensive visualizations for trend analysis",
        "🏛️ Support law enforcement and policy decision-making"
    ]
    
    for obj in objectives:
        st.markdown(f"""
        <div class="success-box">
            <p style="margin: 0; font-size: 1.1rem;">{obj}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

elif opt == "📈 Crime Analysis":
    st.markdown('<div class="animated-content">', unsafe_allow_html=True)
    
    
    st.markdown("""
    <div class="section-header">
        🔍 Select Crime Type for Analysis
    </div>
    """, unsafe_allow_html=True)
    
    crime_options = ["Rape", "Frauds", "Kidnapping", "Custodial Death", 'Murders']
    
    with st.sidebar:
        st.markdown("### 🎛️ Analysis Controls")
        crime_type = st.selectbox("🔍 Types of Crime", options=crime_options)
    
    dataframes = {
        "Rape": pd.read_csv("20_Victims_of_rape.csv"),
        "Frauds": pd.read_csv('10_Property_stolen_and_recovered.csv'),
        "Kidnapping": pd.read_csv('39_Specific_purpose_of_kidnapping_and_abduction.csv'),
        "Custodial Death": pd.read_csv('40_05_Custodial_death_others.csv'),
        "Murders": pd.read_csv('32_Murder_victim_age_sex.csv')
    }
    
    if crime_type in dataframes:
        df = dataframes[crime_type]
        
        if crime_type == "Rape":
            with st.sidebar:
                st.markdown("### 📈 Analysis Options")
                selected_option = option_menu(
                    "India Crime Data",
                    ["See Dataset", "Cases Reported Yearly", "Cases Reported in States",
                    "Victim's Between 10-14", "Rape Cases of Different Age Groups (Bar Chart)",
                    "Incest and Other Rapes", "Rape Cases of Different Age Groups (Pie Chart)",
                    "Multiple States"],
                    icons=["table", "calendar", "bar-chart", "person-bounding-box", "bar-chart", "bar-chart", "pie-chart", "map"],
                    menu_icon="cast",
                    default_index=0,
                    styles={
                        "container": {"padding": "0!important", "background-color": "transparent"},
                        "icon": {"color": "white", "font-size": "14px"}, 
                        "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "color": "white"},
                        "nav-link-selected": {"background-color": "#e74c3c"},
                    }
                )

            st.markdown("""
            <div class="section-header">
                📊 Rape Crime Analysis
            </div>
            """, unsafe_allow_html=True)

            if selected_option == "See Dataset":
                st.dataframe(df, use_container_width=True)

            elif selected_option == "Cases Reported Yearly":
                yearly_cases = df.groupby("Year")["Rape_Cases_Reported"].sum().reset_index()
                fig = px.line(yearly_cases, x='Year', y='Rape_Cases_Reported', markers=True,
                            title='Rape Cases Reported Yearly (2001-2012)',
                            labels={'Year': 'Year', 'Rape_Cases_Reported': 'Rape Cases Reported'})
                fig.update_traces(mode='lines+markers')
                fig.update_layout(xaxis_title='Year', yaxis_title='Rape Cases Reported', xaxis_tickangle=-45)
                st.plotly_chart(fig, use_container_width=True)

            elif selected_option == "Cases Reported in States":
                fig = px.bar(df, x="Area_Name", y="Rape_Cases_Reported", color="Rape_Cases_Reported",
                            color_continuous_scale='viridis',
                            title='Rape Cases Reported in States',
                            labels={'Area_Name': 'Area Name', 'Rape_Cases_Reported': 'Rape Cases Reported'})
                fig.update_layout(xaxis_title='Area Name', yaxis_title='Rape Cases Reported', xaxis_tickangle=-90)
                st.plotly_chart(fig, use_container_width=True)

            elif selected_option == "Victim's Between 10-14":
                fig = px.bar(df, x="Area_Name", y="Victims_Between_10-14_Yrs", color="Victims_Between_10-14_Yrs",
                            color_continuous_scale='viridis',
                            title="Victims Between 10-14 Years Old in Different Areas",
                            labels={'Area_Name': 'Area Name', 'Victims_Between_10-14_Yrs': 'Victims Between 10-14 Yrs'})
                fig.update_layout(xaxis_title='Area Name', yaxis_title='Victims Between 10-14 Yrs', xaxis_tickangle=-90)
                st.plotly_chart(fig, use_container_width=True)

            elif selected_option == "Rape Cases of Different Age Groups (Bar Chart)":
                age_group_data = df[['Victims_Upto_10_Yrs', 'Victims_Between_10-14_Yrs',
                                    'Victims_Between_14-18_Yrs', 'Victims_Between_18-30_Yrs',
                                    'Victims_Between_30-50_Yrs', 'Victims_Above_50_Yrs']].sum().reset_index()
                age_group_data.columns = ['Age_Group', 'Total_Victims']

                fig = px.bar(age_group_data, x='Age_Group', y='Total_Victims', color='Total_Victims',
                            color_continuous_scale='viridis',
                            title='Distribution of Victims by Age Group (2001-2012)',
                            labels={'Age_Group': 'Age Group', 'Total_Victims': 'Total Victims'})
                fig.update_layout(xaxis_title='Age Group', yaxis_title='Total Victims', xaxis_tickangle=-45)
                st.plotly_chart(fig, use_container_width=True)

            elif selected_option == "Incest and Other Rapes":
                incest_rape_victims = df[df['Subgroup'] == 'Victims of Incest Rape']
                other_rape_victims = df[df['Subgroup'] == 'Victims of Other Rape']

                incest_rape_agg = incest_rape_victims.groupby('Year')['Victims_of_Rape_Total'].sum().reset_index()
                other_rape_agg = other_rape_victims.groupby('Year')['Victims_of_Rape_Total'].sum().reset_index()

                comparison_data = incest_rape_agg.merge(other_rape_agg, on='Year', suffixes=('_Incest', '_Other'))

                fig = px.line(comparison_data, x='Year', y=['Victims_of_Rape_Total_Incest', 'Victims_of_Rape_Total_Other'],
                            labels={'value': 'Total Victims', 'variable': 'Type of Rape'},
                            title='Comparison of Incest and Other Rape Cases (2001-2012)',
                            color_discrete_map={'Victims_of_Rape_Total_Incest': 'red', 'Victims_of_Rape_Total_Other': 'green'})
                fig.update_layout(xaxis_title='Year', yaxis_title='Total Victims', xaxis_tickangle=-45)
                st.plotly_chart(fig, use_container_width=True)

            elif selected_option == "Rape Cases of Different Age Groups (Pie Chart)":
                age_group_data = df[['Victims_Upto_10_Yrs', 'Victims_Between_10-14_Yrs',
                                    'Victims_Between_14-18_Yrs', 'Victims_Between_18-30_Yrs',
                                    'Victims_Between_30-50_Yrs', 'Victims_Above_50_Yrs']].sum()

                fig = px.pie(values=age_group_data, names=age_group_data.index,
                            title='Pie Chart: Distribution of Victims by Age Group (2001-2012)',
                            labels={'index': 'Age Group', 'value': 'Total Victims'})
                st.plotly_chart(fig, use_container_width=True)

            elif selected_option == "Multiple States":
                with st.sidebar:
                    selected_states = st.multiselect(
                        "🗺️ Select states",
                        options=df['Area_Name'].unique(),
                        default=["Delhi", "Punjab", "West Bengal"]
                    )

                multi_state_data = df[df['Area_Name'].isin(selected_states) & (df['Subgroup'] == 'Total Rape Victims')]

                fig = px.line(multi_state_data, x='Year', y='Victims_of_Rape_Total', color='Area_Name',
                            title='Year vs Total Rape Victims in Selected States',
                            labels={'Year': 'Year', 'Victims_of_Rape_Total': 'Total Rape Victims'})
                fig.update_layout(xaxis_title='Year', yaxis_title='Total Rape Victims', xaxis_tickangle=-45)
                st.plotly_chart(fig, use_container_width=True)

        elif crime_type == "Frauds":
            df = df.dropna()
            numeric_df = df.select_dtypes(include=['float64', 'int64'])
            corr_matrix = numeric_df.corr()
            
            with st.sidebar:
                st.markdown("### 📈 Analysis Options")
                selected_option = option_menu(
                    "Property Theft and Recovery Data",
                    ["See Dataset", "Subgroups and Groups", "Property Stolen and Recovered Over the Years",
                    "Bar Plot for Stolen and Recovered Property by States", "Pie Chart for Total Property Stolen and Recovered",
                    "Scatter Plot for Stolen vs Recovered Property", "Heatmap for Correlation",
                    "Boxplot for Distribution of Stolen and Recovered Property Values"],
                    icons=["table", "geo-alt", "line-chart", "bar-chart", "pie-chart", "scatter", "heatmap", "bar-chart"],
                    menu_icon="cast",
                    default_index=0,
                    styles={
                        "container": {"padding": "0!important", "background-color": "transparent"},
                        "icon": {"color": "white", "font-size": "14px"}, 
                        "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "color": "white"},
                        "nav-link-selected": {"background-color": "#f39c12"},
                    }
                )

            st.markdown("""
            <div class="section-header">
                💰 Property Theft & Recovery Analysis
            </div>
            """, unsafe_allow_html=True)

            if selected_option == "See Dataset":
                st.dataframe(df, use_container_width=True)

            elif selected_option == "Property Stolen and Recovered Over the Years":
                fig = px.line(df, x='Year', y=['Value_of_Property_Stolen', 'Value_of_Property_Recovered'],
                            labels={'value': 'Value (in crores)', 'variable': 'Property Type'},
                            title='Property Stolen and Recovered Over the Years',
                            color_discrete_map={'Value_of_Property_Stolen': 'blue', 'Value_of_Property_Recovered': 'green'})
                fig.update_layout(xaxis_title='Year', yaxis_title='Value (in crores)', xaxis_tickangle=-45)
                st.plotly_chart(fig, use_container_width=True)

            elif selected_option == "Subgroups and Groups":
                st.title("Property Stolen by Subgroup Over Time")
                with st.sidebar:
                    subgroups = df['Sub_Group_Name'].unique()
                    selected_subgroup = st.selectbox(
                        "Select Subgroup",
                        options=subgroups,
                        index=0
                    )
                    selected_states = st.multiselect(
                        "Select States",
                        options=df['Area_Name'].unique(),
                        default=["Delhi", "Punjab", "West Bengal"]
                    )
                    
                filtered_data = df[(df['Area_Name'].isin(selected_states)) & (df['Sub_Group_Name'] == selected_subgroup)]
                st.write(filtered_data)
                fig = px.line(
                    filtered_data,
                    x='Year',
                    y='Value_of_Property_Stolen',
                    color='Area_Name',
                    markers=True,
                    title=f'Property Stolen in Selected States for Subgroup: {selected_subgroup} Over Time',
                    labels={'Year': 'Year', 'Value_of_Property_Stolen': 'Value of Property Stolen (Rs. in Crore)', 'Area_Name': 'Area Name'},
                    line_shape='linear'
                )
                fig.update_layout(
                    xaxis_title='Year',
                    yaxis_title='Value of Property Stolen (Rs. in Crore)',
                    xaxis_tickangle=-45,
                    legend_title='Area Name'
                )
                st.plotly_chart(fig, use_container_width=True)

            elif selected_option == "Bar Plot for Stolen and Recovered Property by States":
                fig = px.bar(df, x='Area_Name', y=['Value_of_Property_Stolen', 'Value_of_Property_Recovered'],
                            labels={'value': 'Value (in crores)', 'Area_Name': 'State'},
                            title='Property Stolen and Recovered by States',
                            color_discrete_map={'Value_of_Property_Stolen': 'red', 'Value_of_Property_Recovered': 'green'})
                fig.update_layout(xaxis_title='State', yaxis_title='Value (in crores)', xaxis_tickangle=-90)
                st.plotly_chart(fig, use_container_width=True)

            elif selected_option == "Pie Chart for Total Property Stolen and Recovered":
                total_stolen = df['Value_of_Property_Stolen'].sum()
                total_recovered = df['Value_of_Property_Recovered'].sum()

                fig = px.pie(values=[total_stolen, total_recovered], names=['Total Stolen', 'Total Recovered'],
                            title='Pie Chart: Total Property Stolen vs Recovered',
                            labels={'names': 'Property Type', 'values': 'Value (in crores)'})
                st.plotly_chart(fig, use_container_width=True)

            elif selected_option == "Scatter Plot for Stolen vs Recovered Property":
                with st.sidebar:
                    selected_areas = st.multiselect('Select Area(s)', df['Area_Name'].unique(), default=df['Area_Name'][:5])
                    
                if selected_areas:
                    filtered_df = df[df['Area_Name'].isin(selected_areas)]
                else:
                    filtered_df = df
                    
                fig = px.scatter(
                    filtered_df,
                    x='Value_of_Property_Stolen',
                    y='Value_of_Property_Recovered',
                    color='Area_Name',
                    title='Scatter Plot for Stolen vs Recovered Property',
                    labels={'Value_of_Property_Stolen': 'Value of Property Stolen (in Crores)', 'Value_of_Property_Recovered': 'Value of Property Recovered (in Crores)'},
                    color_discrete_sequence=px.colors.qualitative.Plotly,
                    hover_name='Area_Name',
                    size_max=20,
                    log_x=True,
                    log_y=True,
                )
                st.plotly_chart(fig, use_container_width=True)

            elif selected_option == "Heatmap for Correlation":
                fig = px.imshow(corr_matrix, text_auto=True, color_continuous_scale='viridis',
                                title='Heatmap of Correlation Matrix',
                                labels={'x': 'Features', 'y': 'Features'})
                st.plotly_chart(fig, use_container_width=True)

            elif selected_option == "Boxplot for Distribution of Stolen and Recovered Property Values":
                fig = px.box(df.melt(id_vars='Year', value_vars=['Value_of_Property_Stolen', 'Value_of_Property_Recovered']),
                            x='variable', y='value', log_y=True,
                            title='Boxplot for Distribution of Stolen and Recovered Property Values',
                            labels={'variable': 'Property Type', 'value': 'Value (in crores)'})
                st.plotly_chart(fig, use_container_width=True)

        elif crime_type == "Kidnapping":
            df = dataframes["Kidnapping"]
            df.rename(columns={
                "K_A_Female_10_15_Years": "Female 10-15 Years",
                "K_A_Female_15_18_Years": "Female 15-18 Years",
                "K_A_Female_18_30_Years": "Female 18-30 Years",
                "K_A_Female_30_50_Years": "Female 30-50 Years",
                "K_A_Female_Above_50_Years": "Female Above 50 Years",
                "K_A_Female_Total": "Female Total",
                "K_A_Female_Upto_10_Years": "Female Upto 10 Years",
                "K_A_Grand_Total": "Grand Total",
                "K_A_Male_10_15_Years": "Male 10-15 Years",
                "K_A_Male_15_18_Years": "Male 15-18 Years",
                "K_A_Male_18_30_Years": "Male 18-30 Years",
                "K_A_Male_30_50_Years": "Male 30-50 Years",
                "K_A_Male_Above_50_Years": "Male Above 50 Years",
                "K_A_Male_Total": "Male Total",
                "K_A_Male_Upto_10_Years": "Male Upto 10 Years"
            }, inplace=True)
            
            with st.sidebar:
                st.markdown("### 📈 Analysis Options")
                selected_option = option_menu(
                    "Kidnapping and Abduction Data",
                    ["See Dataset", "Kidnapping Cases Reported Yearly", "Kidnapping Cases in States",
                    "Specific Purpose of Kidnapping and Abduction", "Trend of Kidnapping Over the Years", "Custom Column Analysis"],
                    icons=["table", "calendar", "person-bounding-box", "bar-chart", "pie-chart", "bar-chart"],
                    menu_icon="cast",
                    default_index=0,
                    styles={
                        "container": {"padding": "0!important", "background-color": "transparent"},
                        "icon": {"color": "white", "font-size": "14px"}, 
                        "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "color": "white"},
                        "nav-link-selected": {"background-color": "#9b59b6"},
                    }
                )

            st.markdown("""
            <div class="section-header">
                🎭 Kidnapping & Abduction Analysis
            </div>
            """, unsafe_allow_html=True)

            if selected_option == "See Dataset":
                st.dataframe(df, use_container_width=True)

            elif selected_option == "Kidnapping Cases Reported Yearly":
                yearly_cases = df.groupby("Year")["K_A_Cases_Reported"].sum().reset_index()
                fig = px.line(
                    yearly_cases,
                    x='Year',
                    y='K_A_Cases_Reported',
                    markers=True,
                    title='Kidnapping Cases Reported Yearly (2001-2012)',
                    labels={'K_A_Cases_Reported': 'Kidnapping Cases Reported'}
                )
                fig.update_traces(line=dict(color='blue'))
                fig.update_layout(
                    xaxis_title='Year',
                    yaxis_title='Kidnapping Cases Reported',
                    xaxis_tickangle=-45,
                    template='plotly_white'
                )
                st.plotly_chart(fig, use_container_width=True)

            elif selected_option == "Kidnapping Cases in States":
                fig = px.bar(
                    df,
                    x="Area_Name",
                    y="K_A_Cases_Reported",
                    title='Kidnapping Cases Reported in States',
                    labels={'Area_Name': 'Area Name', 'K_A_Cases_Reported': 'Kidnapping Cases Reported'},
                    color='K_A_Cases_Reported',
                )
                fig.update_layout(
                    xaxis_title='Area Name',
                    yaxis_title='Kidnapping Cases Reported',
                    xaxis_tickangle=-90,
                )
                st.plotly_chart(fig, use_container_width=True)

            elif selected_option == "Specific Purpose of Kidnapping and Abduction":
                purpose_data = df.groupby("Sub_Group_Name")["K_A_Cases_Reported"].sum().reset_index()
                fig = px.bar(
                    purpose_data,
                    x="Sub_Group_Name",
                    y="K_A_Cases_Reported",
                    title='Specific Purpose of Kidnapping and Abduction',
                    labels={'Sub_Group_Name': 'Purpose', 'K_A_Cases_Reported': 'Cases Reported'},
                    color='K_A_Cases_Reported',
                    color_continuous_scale='viridis'
                )
                fig.update_layout(
                    xaxis_title='Purpose',
                    yaxis_title='Cases Reported',
                    xaxis_tickangle=-90,
                    template='plotly_white'
                )
                st.plotly_chart(fig, use_container_width=True)

            elif selected_option == "Trend of Kidnapping Over the Years":
                with st.sidebar:
                    subgroups = df['Sub_Group_Name'].unique()
                    selected_subgroup = st.selectbox(
                        "Select Subgroup",
                        options=subgroups,
                        index=0
                    )
                    selected_states = st.multiselect(
                        "Select States",
                        options=df['Area_Name'].unique(),
                        default=["Delhi", "Punjab", "West Bengal"]
                    )
                    
                filtered_data = df[(df['Area_Name'].isin(selected_states)) & (df['Sub_Group_Name'] == selected_subgroup)]
                fig = px.line(
                    filtered_data,
                    x='Year',
                    y='K_A_Cases_Reported',
                    color='Area_Name',
                    markers=True,
                    title=f'Kidnapping Cases in Selected States for Subgroup: {selected_subgroup} Over Time',
                    labels={'Year': 'Year', 'K_A_Cases_Reported': 'Cases Reported', 'Area_Name': 'Area Name'},
                    line_shape='linear'
                )
                fig.update_layout(
                    xaxis_title='Year',
                    yaxis_title='Cases Reported',
                    xaxis_tickangle=-45,
                    legend_title='Area Name'
                )
                st.plotly_chart(fig, use_container_width=True)

            elif selected_option == "Custom Column Analysis":
                with st.sidebar:
                    columns = [
                        "Female 10-15 Years", "Female 15-18 Years", "Female 18-30 Years",
                        "Female 30-50 Years", "Female Above 50 Years", "Female Total",
                        "Female Upto 10 Years", "Grand Total", "Male 10-15 Years",
                        "Male 15-18 Years", "Male 18-30 Years", "Male 30-50 Years",
                        "Male Above 50 Years", "Male Total", "Male Upto 10 Years"
                    ]
                    selected_columns = st.multiselect(
                        "Select Columns",
                        options=columns,
                        default=["Female 10-15 Years", "Female 15-18 Years"]
                    )

                if selected_columns:
                    column_data = df[selected_columns].sum().reset_index()
                    column_data.columns = ['Column', 'Total']

                    fig = px.bar(
                        column_data,
                        x='Column',
                        y='Total',
                        title='Total Kidnapping Cases by Selected Columns',
                        labels={'Column': 'Columns', 'Total': 'Total Cases'},
                        color='Total',
                        color_continuous_scale='viridis'
                    )
                    fig.update_layout(
                        xaxis_title='Columns',
                        yaxis_title='Total Cases',
                        xaxis_tickangle=-45,
                        template='plotly_white'
                    )
                    st.plotly_chart(fig, use_container_width=True)

        elif crime_type == "Custodial Death":
            df = dataframes["Custodial Death"]
            df.fillna(0, inplace=True)
            df['Total_Deaths'] = df.iloc[:, 4:].sum(axis=1)
            
            with st.sidebar:
                st.markdown("### 📈 Analysis Options")
                selected_option = option_menu(
                    "Custodial Death Data",
                    ["See Dataset", "Trend of Custodial Deaths Over the Years", "Custodial Deaths by State",
                    "Causes of Custodial Deaths", "Yearly Distribution of Causes of Death", "Top States with the Highest Custodial Deaths"],
                    icons=["table", "line-chart", "bar-chart", "pie-chart", "area-chart", "bar-chart"],
                    menu_icon="cast",
                    default_index=0,
                    styles={
                        "container": {"padding": "0!important", "background-color": "transparent"},
                        "icon": {"color": "white", "font-size": "14px"}, 
                        "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "color": "white"},
                        "nav-link-selected": {"background-color": "#34495e"},
                    }
                )
            
            st.markdown("""
            <div class="section-header">
                ⚰️ Custodial Death Analysis
            </div>
            """, unsafe_allow_html=True)

            if selected_option == "See Dataset":
                st.dataframe(df, use_container_width=True)

            elif selected_option == "Trend of Custodial Deaths Over the Years":
                trend_df = df.groupby('Year')['Total_Deaths'].sum().reset_index()
                fig_trend = px.line(trend_df, x='Year', y='Total_Deaths', 
                                  title='Trend of Custodial Deaths Over the Years',
                                  markers=True)
                fig_trend.update_traces(line=dict(color='red'))
                st.plotly_chart(fig_trend, use_container_width=True)

            elif selected_option == "Custodial Deaths by State":
                state_df = df.groupby('Area_Name')['Total_Deaths'].sum().reset_index()
                fig_state = px.bar(state_df, x='Area_Name', y='Total_Deaths', 
                                 title='Custodial Deaths by State', 
                                 labels={'Area_Name': 'State', 'Total_Deaths': 'Total Deaths'},
                                 height=600)
                fig_state.update_layout(xaxis={'categoryorder':'total descending'})
                st.plotly_chart(fig_state, use_container_width=True)

            elif selected_option == "Causes of Custodial Deaths":
                cause_df = df.melt(id_vars=['Area_Name', 'Year'], 
                                 value_vars=['CD_Accidents', 'CD_By_Mob_AttackRiots', 'CD_By_other_Criminals', 
                                           'CD_By_Suicide', 'CD_IllnessNatural_Death', 'CD_While_Escaping_from_Custody'],
                                 var_name='Cause', value_name='Deaths')
                cause_df = cause_df.groupby('Cause')['Deaths'].sum().reset_index()
                fig_cause = px.pie(cause_df, values='Deaths', names='Cause', 
                                 title='Causes of Custodial Deaths')
                st.plotly_chart(fig_cause, use_container_width=True)

            elif selected_option == "Yearly Distribution of Causes of Death":
                yearly_cause_df = df.melt(id_vars=['Year'], 
                                        value_vars=['CD_Accidents', 'CD_By_Mob_AttackRiots', 'CD_By_other_Criminals', 
                                                  'CD_By_Suicide', 'CD_IllnessNatural_Death', 'CD_While_Escaping_from_Custody'],
                                        var_name='Cause', value_name='Deaths')
                yearly_cause_df = yearly_cause_df.groupby(['Year', 'Cause'])['Deaths'].sum().reset_index()
                fig_yearly_cause = px.area(yearly_cause_df, x='Year', y='Deaths', color='Cause', 
                                         title='Yearly Distribution of Causes of Death')
                st.plotly_chart(fig_yearly_cause, use_container_width=True)

            elif selected_option == "Top States with the Highest Custodial Deaths":
                state_df = df.groupby('Area_Name')['Total_Deaths'].sum().reset_index()
                top_states_df = state_df.sort_values(by='Total_Deaths', ascending=False).head(10)
                fig_top_states = px.bar(top_states_df, x='Area_Name', y='Total_Deaths', 
                                      title='Top States with the Highest Custodial Deaths', 
                                      labels={'Area_Name': 'State', 'Total_Deaths': 'Total Deaths'})
                st.plotly_chart(fig_top_states, use_container_width=True)

        elif crime_type == "Murders":
            df = dataframes["Murders"]
            df.fillna(0, inplace=True)
            
            with st.sidebar:
                st.markdown("### 📈 Analysis Options")
                selected_option = option_menu(
                    "Murder Data",
                    ["See Dataset", "Total Number of Victims by Area for a Specific Year", 
                    "Pie Chart: Distribution of Victims by Age Group for a Specific Area and Year", 
                    "Trends of Total Victims Over the Years for a Specific Area"],
                    icons=["table", "bar-chart", "pie-chart", "line-chart"],
                    menu_icon="cast",
                    default_index=0,
                    styles={
                        "container": {"padding": "0!important", "background-color": "transparent"},
                        "icon": {"color": "white", "font-size": "14px"}, 
                        "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "color": "white"},
                        "nav-link-selected": {"background-color": "#c0392b"},
                    }
                )

            st.markdown("""
            <div class="section-header">
                🔪 Murder Crime Analysis
            </div>
            """, unsafe_allow_html=True)

            if selected_option == "See Dataset":
                st.dataframe(df, use_container_width=True)

            elif selected_option == "Total Number of Victims by Area for a Specific Year":
                with st.sidebar:
                    year = st.slider("Select Year", min_value=df['Year'].min(), max_value=df['Year'].max(), value=df['Year'].min())
                    
                data_year = df[df['Year'] == year]
                
                fig_bar = px.bar(data_year, x='Area_Name', y='Victims_Total', 
                               title=f'Total Number of Victims by Area ({year})',
                               labels={'Victims_Total': 'Total Victims', 'Area_Name': 'Area'},
                               color='Victims_Total', 
                               color_continuous_scale='Viridis')
                fig_bar.update_layout(xaxis={'categoryorder':'total descending'})
                st.plotly_chart(fig_bar, use_container_width=True)

            elif selected_option == "Pie Chart: Distribution of Victims by Age Group for a Specific Area and Year":
                with st.sidebar:
                    area = st.selectbox("Select Area", options=df['Area_Name'].unique(), index=0)
                    year = st.slider("Select Year", min_value=df['Year'].min(), max_value=df['Year'].max(), value=df['Year'].min())
                    
                data_area_year = df[(df['Area_Name'] == area) & (df['Year'] == year)]
                
                age_groups = ['Victims_Above_50_Yrs', 'Victims_Upto_10_15_Yrs', 'Victims_Upto_10_Yrs',
                            'Victims_Upto_15_18_Yrs', 'Victims_Upto_18_30_Yrs', 'Victims_Upto_30_50_Yrs']
                age_group_labels = ['Above 50 Yrs', '10-15 Yrs', 'Up to 10 Yrs', '15-18 Yrs', '18-30 Yrs', '30-50 Yrs']
                age_group_values = data_area_year[age_groups].sum().values

                fig_pie = px.pie(names=age_group_labels, values=age_group_values,
                               title=f'Distribution of Victims by Age Group ({area}, {year})')
                st.plotly_chart(fig_pie, use_container_width=True)

            elif selected_option == "Trends of Total Victims Over the Years for a Specific Area":
                with st.sidebar:
                    area = st.selectbox("Select Area", options=df['Area_Name'].unique(), index=0)
                    
                data_area = df[df['Area_Name'] == area]
                
                fig_line = px.line(data_area, x='Year', y='Victims_Total', markers=True,
                                 title=f'Trends of Total Victims Over the Years for {area}',
                                 labels={'Victims_Total': 'Total Victims', 'Year': 'Year'})
                fig_line.update_traces(line=dict(color='blue'))
                fig_line.update_layout(xaxis_title='Year', yaxis_title='Total Victims', xaxis_tickangle=-45)
                st.plotly_chart(fig_line, use_container_width=True)

elif opt == "ℹ️ About":
    st.markdown('<div class="animated-content">', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="section-header">
        ℹ️ About the Crime Data Analysis Project
    </div>
    """, unsafe_allow_html=True)

    # Project Background
    st.markdown("""
    <div class="info-box">
        <h3>🌟 Project Background</h3>
        <p>Crime data analysis is essential for understanding the nature of criminal activities in various regions. By examining 
        historical crime data, we can uncover trends, patterns, and insights that may be hidden in raw data. This project aims 
        to apply data science and machine learning techniques to make meaningful interpretations of crime data.</p>
    </div>
    """, unsafe_allow_html=True)

    # Methodology
    st.markdown("""
    <div class="warning-box">
        <h3>🔬 Methodology</h3>
        <p>In this project, we follow a structured methodology:</p>
        <ul>
            <li><strong>Data Collection:</strong> Gathering crime data from reliable sources</li>
            <li><strong>Data Preprocessing:</strong> Cleaning and preparing the data</li>
            <li><strong>Exploratory Data Analysis (EDA):</strong> Using statistical techniques</li>
            <li><strong>Predictive Modeling:</strong> Building models to predict patterns</li>
            <li><strong>Visualization and Reporting:</strong> Creating dashboards and reports</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # Data Sources
    st.markdown("""
    <div class="success-box">
        <h3>📊 Data Sources</h3>
        <p>The data used in this project has been sourced from credible and publicly available resources, including:</p>
        <ul>
            <li><strong>Local Law Enforcement Agencies:</strong> Historical crime reports</li>
            <li><strong>Open Data Portals:</strong> Government open data portals</li>
            <li><strong>Other Sources:</strong> Relevant datasets for comprehensive analysis</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <div class="footer">
        <h3>🎯 Our Mission</h3>
        <p>To provide insights that can support law enforcement agencies, policymakers, and community organizations 
        in understanding crime patterns and implementing effective strategies for crime prevention and public safety.</p>
        <hr style="border-color: rgba(255,255,255,0.3);">
        <p><em>Building safer communities through data-driven insights</em></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)