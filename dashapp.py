import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import numpy as np

class UserEngagementDashboard:
    def __init__(self):
        # Seed for reproducibility
        np.random.seed(42)
        self.data = self.generate_sample_data()
    
    def generate_sample_data(self):
        """Generate synthetic user engagement data"""
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        
        registrations = [1200, 1500, 1800, 2100, 2400, 2700]
        active_users = [800, 1100, 1400, 1700, 2000, 2300]
        churned_users = [400, 400, 400, 400, 500, 600]
        
        return {
            'registrations': pd.DataFrame({
                'Month': months,
                'Users': registrations
            }),
            'user_activity': pd.DataFrame({
                'Month': months,
                'Active': active_users,
                'Churned': churned_users
            }),
            'user_segments': {
                'New Users': 40,
                'Active Users': 35,
                'Inactive Users': 25
            }
        }
    
    def calculate_engagement_metrics(self):
        """Compute key engagement statistics"""
        total_registrations = self.data['registrations']['Users'].sum()
        avg_monthly_registrations = self.data['registrations']['Users'].mean()
        churn_rate = (self.data['user_activity']['Churned'].sum() / 
                      self.data['user_activity']['Active'].sum() * 100)
        
        return {
            'Total Registrations': total_registrations,
            'Avg Monthly Registrations': round(avg_monthly_registrations, 2),
            'Churn Rate (%)': round(churn_rate, 2)
        }
    
    def render_dashboard(self):
        """Create Streamlit dashboard interface"""
        st.title('User Engagement Dashboard')
        
        # Sidebar for metric selection
        metric = st.sidebar.selectbox(
            'Select Visualization',
            ['User Registrations', 'User Activity', 'User Segments']
        )
        
        # Visualizations based on selection
        if metric == 'User Registrations':
            fig = px.bar(
                self.data['registrations'], 
                x='Month', 
                y='Users', 
                title='Monthly User Registrations'
            )
            st.plotly_chart(fig)
        
        elif metric == 'User Activity':
            fig = px.line(
                self.data['user_activity'], 
                x='Month', 
                y=['Active', 'Churned'], 
                title='User Activity Trends'
            )
            st.plotly_chart(fig)
        
        elif metric == 'User Segments':
            fig = px.pie(
                values=list(self.data['user_segments'].values()),
                names=list(self.data['user_segments'].keys()),
                title='User Segment Distribution'
            )
            st.plotly_chart(fig)
        
        # Display engagement metrics
        st.subheader('Engagement Metrics')
        metrics = self.calculate_engagement_metrics()
        for metric, value in metrics.items():
            st.metric(label=metric, value=value)

def main():
    dashboard = UserEngagementDashboard()
    dashboard.render_dashboard()

if __name__ == '__main__':
    main()