FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y libgomp1

# Set up user and working dir
RUN useradd -m -u 1000 user
USER user
WORKDIR /home/user/app

# Copy project files
COPY --chown=user . .

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit port
EXPOSE 7860

# Run Streamlit app
CMD ["python", "-m", "streamlit", "run", "app.py", "--server.port=7860", "--server.enableCORS=false"]

