# Exception for hadolint-docker-linter:
# DL3007: using latest is prone to errors if the image will ever update. Pin the version explicitly to a release tag
# hadolint ignore=DL3007
FROM mundialis/actinia:latest

# pwgen is needed for the tests
RUN pip3 install --no-cache-dir pwgen==0.8.2.post0

COPY docker/actinia.cfg /etc/default/actinia
COPY src /src/actinia-grassdata-management-plugin/src/
COPY setup.cfg /src/actinia-grassdata-management-plugin/
COPY setup.py /src/actinia-grassdata-management-plugin/
COPY requirements.txt /src/actinia-grassdata-management-plugin/

RUN pip3 install --no-cache-dir -r /src/actinia-grassdata-management-plugin/requirements.txt && \
    pip3 uninstall actinia-grassdata-management-plugin.wsgi -y
# SETUPTOOLS_SCM_PRETEND_VERSION is only needed if in the plugin folder is no
# .git folder
ENV SETUPTOOLS_SCM_PRETEND_VERSION=0.0

WORKDIR /src/actinia-grassdata-management-plugin
RUN pip3 install --no-cache-dir -e .

WORKDIR /src/actinia_core
