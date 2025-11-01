# 1️⃣ Base image
FROM python:3.10-slim

# 2️⃣ Set working directory inside container
WORKDIR /app

# 3️⃣ Install system dependencies for ffmpeg (required by Whisper)
RUN apt-get update && apt-get install -y ffmpeg

# 4️⃣ Copy your project files into the container
COPY . /app

# 5️⃣ Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 6️⃣ Expose Streamlit port
EXPOSE 8501

# 7️⃣ Set environment variables to avoid Streamlit warnings
ENV PYTHONUNBUFFERED=1 \
    STREAMLIT_SERVER_PORT=8501 \
    STREAMLIT_SERVER_ADDRESS=0.0.0.0 \
    STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# 8️⃣ Default command to run Streamlit app
CMD ["streamlit", "run", "app/ui.py"]
