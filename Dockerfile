FROM python:3.9-slim-buster
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN groupadd -r jupyter -g 1000 \
    && useradd -u 1000 -r -g jupyter -m -d /opt/jupyter -s /sbin/nologin -c "jupyter user" jupyter \
    && chmod 755 /opt/jupyter \
    && apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && curl -sL https://raw.githubusercontent.com/metacall/install/master/install.sh | sh \
    && apt-get --purge remove -y curl \
    && apt-get clean autoclean \
    && apt-get autoremove -y \
    && rm -rf /var/lib/{apt,dpkg,cache,log}/

WORKDIR /opt/jupyter

COPY --chown=1000:1000 . /opt/jupyter/

RUN python3 -m pip install --upgrade pip \
    && pip install -r requirements.txt \
    && python3 setup.py install \
    && python3 -m metacall_jupyter.install \
    && metacall npm install

USER jupyter
EXPOSE 8888
CMD ["python3", "-m", "metacall_jupyter.launcher"]
