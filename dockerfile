FROM  python:slim
ENV TOKEN = '6388506183:AAEm7b4bG4_7mC1m6YiaszBRqm5D26mYQws'


COPY . .
RUN pip install -r req.txt
CMD python bot.py
