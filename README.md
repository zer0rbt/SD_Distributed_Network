# Stable Diffusion Distributed Network

**Version:** v0.1

**ATTENTION:** *WORK IN PROGRESS*

## What is it?

Distributed computations network, dedicated to allowing faster image generation speed. It also contains features like a distributed database. This project is created as part of the "Distributed Computations" course at SPbU.

## Build

`docker build -t deps -f ./Dockerfile .`

`docker build -t stablediffusion ./stablediffusion/.`

`docker build -t upscaler ./upscalers/.`

`docker build -t database ./database/.`

## Usage

`docker run --name database1 -v ./:/workspace/cache --env-file ./.env -p 5003:5003 --rm database`

`docker run --name up1 -v ./:/workspace/cache --env-file ./.env --network host --rm upscaler`

## TODO LIST

### First Priority (minimum required version)

- [x] Image generator (v0.1)
- [x] Image upscaler (v0.1)
- [x] Image storage (v0.1)
- [x] Server (v0.0.1)

### Second priority (optimal version)

- [ ] Message Broker (To Do)
- [ ] Logger (To Do)
- [ ] Log Storage (To Do)

### Third priority (minimum required final version)

- [ ] Load Balancer (To Do)

### Fourth priority (optimal final version)

- [ ] OpenVPN clusters (To Do)
- [ ] Config storage (To Do)

## Contributors

- **zer0rbt** - idea & code
- **v113v** - architecture & code (we hope so :^])
