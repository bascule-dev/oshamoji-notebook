FROM maruware/detectron

RUN apt-get update
RUN apt-get install -y imagemagick

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root"]