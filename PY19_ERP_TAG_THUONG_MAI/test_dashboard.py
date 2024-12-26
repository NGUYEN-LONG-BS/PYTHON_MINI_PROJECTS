import plotly.express as px

# Dữ liệu bản đồ mẫu (world)
fig = px.choropleth(locations=["Vietnam", "United States", "India"], 
                    locationmode="country names", 
                    color=[100, 200, 300],  # Giá trị màu đại diện
                    title="Bản đồ quốc gia")
fig.show()
