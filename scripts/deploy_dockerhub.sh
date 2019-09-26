#!/bin/sh
docker login -u $DOCKER_USER -p $DOCKER_PASS
if [ "$TRAVIS_BRANCH" = "master" ]; then
    TAG="latest"
else
    TAG="$TRAVIS_BRANCH"
fi
docker build -f Dockerfile -t $TRAVIS_REPO_SLUG:$TAG .
#docker tag $TRAVIS_REPO_SLUG:$TAG $DOCKER_USER/$TRAVIS_REPO_SLUG
docker push $DOCKER_USER/$TRAVIS_REPO_SLUG:${TAG}