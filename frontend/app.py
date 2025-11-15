import streamlit as st
import add_update_ui
import analytics_category_ui
import analytics_month_ui

st.title('EXPENSE MANAGEMENT SYSTEM')

tab1,tab2,tab3 = st.tabs(['Add/Update','Analytics by Category','Analytics by Month'])

with tab1:
    add_update_ui.add_update_tab()

with tab2:
    analytics_category_ui.analytics_by_category_tab()

with tab3:
    analytics_month_ui.analytics_by_month_tab()