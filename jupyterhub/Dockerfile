#FROM  jupyter/base-notebook:hub-1.0.0
#COPY ./secrets /data
#COPY hosts /etc
#RUN pip install jupyterhub==1.0.0

#ARG JUPYTERHUB_VERSION=0.9.2
#ARG JUPYTERHUB_VERSION=1.0.0
#FROM jupyterhub/jupyterhub:${JUPYTERHUB_VERSION}

FROM jupyterhub/jupyterhub:1.0.0


#ADD . /tmp/dockerspawner

#RUN pip install --no-cache /tmp/dockerspawner

#RUN pip install --no-cache jupyterhub-dummyauthenticator

RUN pip install dockerspawner jupyterhub-dummyauthenticator


ADD jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py
