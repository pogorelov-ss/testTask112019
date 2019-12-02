# problem with docker on fedora 31 switch to the podman and podman-compose

`podman-compose -f docker/postgersql.yaml up`

clean all containers

`podman pod stop $(podman pod ps -q)` then `podman pod prune`
