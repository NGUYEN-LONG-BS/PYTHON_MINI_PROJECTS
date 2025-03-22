from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

def plot_line_chart(df):
    x_values = df.iloc[:, 0]
    y_values = df.iloc[:, 1].astype(float)
    
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values, marker='o', linestyle='-', color='b')
    
    ax.set_xlabel("Trục X")
    ax.set_ylabel("Trục Y")
    ax.set_title("Biểu đồ Line Chart từ Excel")
    
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    
    return plot_url

@app.route('/mychart', methods=['GET', 'POST'])
def mychart():
    plot_url = None
    df_html = None
    
    if request.method == 'POST':
        file = request.files['file']
        if file:
            df = pd.read_excel(file)
            if len(df.columns) >= 2:
                plot_url = plot_line_chart(df)
                df_html = df.to_html(classes='table table-striped', index=False)
    
    return render_template('mychart.html', plot_url=plot_url, df_html=df_html)

if __name__ == '__main__':
    app.run(debug=True)
