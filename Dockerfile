FROM ${RUNTIME_DOCKER_REPO:-artifactory.marketamerica.com:8443/internalsystems/centos/centos7-atomic-s2i-runtime-pytato:python36-latest}

# THIS RUNTIME DOCKERFILE SHOULD ONLY BE USED AS A REFERENCE.
# THE ORIGINAL FILE IS IN THE PYTATOBASE REPOSITORY AND IS REVIEWED BY THE FOLLOWING TEAMS:
#  - Internal Systems
#  - Release
#  - Middleware Architecture


ARG DEFAULT_MSA_VERSION
ARG DEFAULT_MSA_COMMIT
ARG MSA_VERSION=${DEFAULT_MSA_VERSION:-1.0.0.0}
ARG MSA_COMMIT=${DEFAULT_MSA_COMMIT:-da39a3ee5e6b4b0d3255bfef95601890afd80709}

LABEL com.marketamerica.msa.app=${APP_NAME} \
	com.marketamerica.msa.version=${MSA_VERSION} \
    com.marketamerica.msa.commit=${MSA_COMMIT}

RUN echo "runtime version: ${RUNTIME_VERSION}" && \
    mkdir -p /tmp/src

COPY . /tmp/src/

RUN /usr/libexec/s2i/assemble-runtime

HEALTHCHECK --interval=10m --timeout=3s \
    CMD curl -f http://localhost:8080/${APP_NAME}-micro/heartbeat || exit 1

ENTRYPOINT ["/bin/bash","-c","/usr/libexec/s2i/run"]