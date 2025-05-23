# Exception for hadolint-docker-linter:
# DL3007: using latest is prone to errors if the image will ever update. Pin the version explicitly to a release tag
# hadolint ignore=DL3007
FROM mundialis/actinia:latest AS actinia_test

LABEL authors="Carmen Tawalika,Anika Weinmann"
LABEL maintainer="tawalika@mundialis.de,weinmann@mundialis.de"

ENV ACTINIA_CUSTOM_TEST_CFG=/etc/default/actinia-grassdata-management-plugin-test

# TODO do not set DEFAULT_CONFIG_PATH if this is fixed
ENV DEFAULT_CONFIG_PATH=/etc/default/actinia-grassdata-management-plugin-test

# install things only for tests
# DL3018: Pin versions in apk add
# hadolint ignore=DL3018
RUN apk add --no-cache valkey valkey-cli && \
    pip3 install --no-cache-dir iniconfig==2.0.0 colorlog==6.8.2 pwgen==0.8.2.post0 pytest==8.3.5 pytest-cov==6.0.0

# COPY docker/actinia-grassdata-management-plugin-test/start.sh /src/start.sh

ENTRYPOINT ["/bin/sh"]
CMD ["/src/start.sh"]

# add data for tests
RUN wget --quiet https://grass.osgeo.org/sampledata/north_carolina/nc_spm_08_micro.zip && \
  unzip nc_spm_08_micro.zip && \
  rm -f nc_spm_08_micro.zip && \
  mv nc_spm_08_micro /actinia_core/grassdb/nc_spm_08
RUN grass -e -c 'EPSG:4326' /actinia_core/grassdb/latlong_wgs84
RUN wget --quiet https://grass.osgeo.org/sampledata/north_carolina/nc_spm_mapset_modis2015_2016_lst_grass8.zip && \
  unzip nc_spm_mapset_modis2015_2016_lst_grass8.zip && \
  rm -f nc_spm_mapset_modis2015_2016_lst_grass8.zip && \
  mv  modis_lst /actinia_core/grassdb/nc_spm_08/modis_lst
RUN chown -R 1001:1001 /actinia_core/grassdb/nc_spm_08/modis_lst && chmod -R g+w /actinia_core/grassdb/nc_spm_08/modis_lst

# copy needed files and configs for test
COPY docker/actinia-grassdata-management-plugin-test/actinia-grassdata-management-plugin-test.cfg /etc/default/actinia
COPY docker/actinia-grassdata-management-plugin-test/actinia-grassdata-management-plugin-test.cfg /etc/default/actinia-grassdata-management-plugin-test
COPY . /src/actinia-grassdata-management-plugin/

WORKDIR /src/actinia-grassdata-management-plugin/
RUN pip3 install --no-cache-dir -e .

# TODO remove when merged to main branch in actinia-core and actinia-api
# This needs to be below actinia-grassdata-management-plugin installation
# as both packages are requirements and would be overwritten again.
RUN pip3 uninstall actinia_core -y
RUN git clone https://github.com/actinia-org/actinia-core.git /src/actinia-core
WORKDIR /src/actinia-core
RUN git checkout develop
RUN pip install --no-cache-dir .
RUN pip3 uninstall actinia_api -y
RUN git clone https://github.com/actinia-org/actinia-api.git /src/actinia-api
WORKDIR /src/actinia-api
RUN git checkout develop
RUN pip install --no-cache-dir .

WORKDIR /src/actinia-grassdata-management-plugin/
RUN chmod a+x tests_with_kvdb.sh && make install

# RUN make test
