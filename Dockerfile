FROM jupyter/scipy-notebook:notebook-6.4.0

ARG NB_USER=jovyan
ARG NB_UID=1000
ENV USER ${NB_USER}
ENV NB_UID ${NB_UID}
ENV HOME /home/${NB_USER}

USER root

RUN wget -O - https://raw.githubusercontent.com/metacall/install/master/install.sh | sh

# Explicitly include the files in the .dockerignore
COPY . ${HOME}

RUN pip install -r requirements.txt \
    && python3 setup.py install \
    && python3 -m metacall_jupyter.install \
    && metacall npm install

RUN chown -R ${NB_UID} ${HOME}

USER ${NB_USER}
EXPOSE 8888
CMD ["python3", "-m", "metacall_jupyter.launcher"]
