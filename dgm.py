import streamlit as st

# navigation
# https://getemoji.com/
pg = st.navigation(
    {   
        "DGM":
        [
            st.Page("page/home/home.py", title="Home", icon="💻"),
        ],
        "Project" : 
        [
            st.Page("page/benchmark/benchmark.py", title="Benchmark", icon="🐳"),
        ],
        "Infrastructure" : 
        [
            st.Page("page/cpfs/cpfs.py", title="Setting", icon="🍄"),
        ]
    },
    expanded=True,
    position="sidebar"
)

pg.run()