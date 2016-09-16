FROM python:3.4.5-alpine
ADD src /var/src
RUN cd /var/src
RUN pip install pytest
CMD ["python3 ./main.py"]
